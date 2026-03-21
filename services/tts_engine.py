import logging
import os
import hashlib
import time
from datetime import datetime

logger = logging.getLogger(__name__)

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")
ELEVENLABS_VOICE_ID = os.environ.get("VOICE_ID", "")

class TTSEngine:
    """Text-to-Speech engine — ElevenLabs primary, gTTS fallback."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cache_dir = os.path.join('static', 'audio', 'tts_cache')
        os.makedirs(self.cache_dir, exist_ok=True)

        self.voices = {
            'female_default': {'language': 'en', 'gender': 'female', 'rate': 1.0, 'pitch': 1.0},
            'male_default':   {'language': 'en', 'gender': 'male',   'rate': 1.0, 'pitch': 1.0},
            'female_slow':    {'language': 'en', 'gender': 'female', 'rate': 0.8, 'pitch': 1.0},
            'male_slow':      {'language': 'en', 'gender': 'male',   'rate': 0.8, 'pitch': 1.0},
        }

        # ElevenLabs
        self.elevenlabs_available = False
        if ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID:
            try:
                from elevenlabs.client import ElevenLabs as EL
                self._el_client = EL(api_key=ELEVENLABS_API_KEY)
                self.elevenlabs_available = True
                self.logger.info("ElevenLabs TTS ready (voice_id=%s)", ELEVENLABS_VOICE_ID)
            except Exception as e:
                self.logger.warning("ElevenLabs init failed: %s", e)

        # gTTS fallback
        self.gtts_available = False
        try:
            from gtts import gTTS  # noqa: F401
            self.gtts_available = True
            self.logger.info("gTTS available as TTS fallback")
        except ImportError:
            self.logger.warning("gTTS not available")

        self.logger.info("TTS Engine initialized (elevenlabs=%s, gtts=%s)",
                         self.elevenlabs_available, self.gtts_available)
    
    def synthesize(self, text, voice_id='female_default', **kwargs):
        """
        Main synthesize method that other parts of your app expect.
        This calls the generate_speech method internally.
        """
        return self.generate_speech(text, voice_id, cache=kwargs.get('cache', True))
    
    def generate_speech(self, text, voice_id='female_default', cache=True):
        """Generate speech — ElevenLabs first, gTTS fallback."""
        if not text or not text.strip():
            return {'success': False, 'error': 'Empty text provided',
                    'timestamp': datetime.utcnow().isoformat()}

        voice = self.voices.get(voice_id, self.voices['female_default'])
        cache_key = hashlib.md5((text + voice_id).encode()).hexdigest()
        cache_path = os.path.join(self.cache_dir, f"{cache_key}.mp3")

        if cache and os.path.exists(cache_path):
            return {'success': True, 'path': cache_path, 'cached': True,
                    'url': '/static/audio/tts_cache/' + os.path.basename(cache_path),
                    'timestamp': datetime.utcnow().isoformat()}

        # --- ElevenLabs ---
        if self.elevenlabs_available:
            try:
                audio = self._el_client.text_to_speech.convert(
                    voice_id=ELEVENLABS_VOICE_ID,
                    text=text,
                    model_id="eleven_monolingual_v1",
                )
                with open(cache_path, 'wb') as f:
                    for chunk in audio:
                        f.write(chunk)
                return {
                    'success': True,
                    'path': cache_path,
                    'cached': False,
                    'voice': 'elevenlabs',
                    'url': '/static/audio/tts_cache/' + os.path.basename(cache_path),
                    'timestamp': datetime.utcnow().isoformat(),
                }
            except Exception as e:
                self.logger.warning("ElevenLabs generation failed, falling back to gTTS: %s", e)

        # --- gTTS fallback ---
        if self.gtts_available:
            try:
                from gtts import gTTS
                tts = gTTS(text=text, lang=voice['language'], slow=(voice['rate'] < 0.9))
                tts.save(cache_path)
                return {
                    'success': True,
                    'path': cache_path,
                    'cached': False,
                    'voice': voice_id,
                    'url': '/static/audio/tts_cache/' + os.path.basename(cache_path),
                    'timestamp': datetime.utcnow().isoformat(),
                }
            except Exception as e:
                self.logger.error("gTTS generation failed: %s", e)
                return {'success': False, 'error': str(e), 'text': text,
                        'timestamp': datetime.utcnow().isoformat()}

        return {'success': False, 'error': 'No TTS engine available', 'text': text,
                'timestamp': datetime.utcnow().isoformat()}
    
    def speak_text(self, text, voice_id='female_default', context=None):
        """
        Generate speech and prepare for playback.
        
        Args:
            text: Text to speak
            voice_id: ID of voice to use
            context: Optional context information for adapting speech
            
        Returns:
            dict: Result with audio information
        """
        try:
            # Adapt text based on context if provided
            if context:
                text = self._adapt_text(text, context)
            
            # Generate speech
            result = self.generate_speech(text, voice_id)
            
            if result['success']:
                result['text'] = text
            
            return result
        except Exception as e:
            self.logger.error(f"Error preparing speech: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'text': text,
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def _adapt_text(self, text, context):
        """Adapt text based on context for better TTS."""
        adapted_text = text
        
        # Extract context information
        audience = context.get('audience', 'patient')
        cognitive_level = context.get('cognitive_level', 'moderate')
        urgency = context.get('urgency', 'normal')
        
        # Add pauses for easier comprehension
        if cognitive_level == 'low':
            # Add pauses after sentences and commas
            adapted_text = adapted_text.replace('. ', '. <break time="1s"/> ')
            adapted_text = adapted_text.replace(', ', ', <break time="0.5s"/> ')
        
        # Emphasize important words for urgent messages
        if urgency == 'high':
            # Simple approach: add emphasis to first sentence
            sentences = adapted_text.split('. ')
            if sentences:
                sentences[0] = f"<emphasis level='strong'>{sentences[0]}</emphasis>"
                adapted_text = '. '.join(sentences)
        
        return adapted_text
    
    def get_available_voices(self):
        """Get list of available voices."""
        return [
            {
                'id': voice_id,
                'name': voice_id.replace('_', ' ').title(),
                'language': voice['language'],
                'gender': voice['gender'],
                'rate': voice['rate'],
                'pitch': voice['pitch']
            }
            for voice_id, voice in self.voices.items()
        ]
    
    def add_custom_voice(self, voice_id, language, gender, rate, pitch):
        """Add a custom voice configuration."""
        try:
            if voice_id in self.voices:
                return {
                    'success': False,
                    'error': f"Voice ID '{voice_id}' already exists"
                }
            
            # Validate parameters
            if rate < 0.5 or rate > 1.5:
                return {
                    'success': False,
                    'error': "Rate must be between 0.5 and 1.5"
                }
                
            if pitch < 0.5 or pitch > 1.5:
                return {
                    'success': False,
                    'error': "Pitch must be between 0.5 and 1.5"
                }
            
            # Add voice
            self.voices[voice_id] = {
                'language': language,
                'gender': gender,
                'rate': rate,
                'pitch': pitch
            }
            
            return {
                'success': True,
                'voice_id': voice_id
            }
        except Exception as e:
            self.logger.error(f"Error adding custom voice: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def cleanup_cache(self, max_age_days=30):
        """Clean up old cache files."""
        try:
            now = time.time()
            count = 0
            
            for filename in os.listdir(self.cache_dir):
                file_path = os.path.join(self.cache_dir, filename)
                
                # Check if file is old enough to delete
                if os.path.isfile(file_path):
                    file_age = now - os.path.getmtime(file_path)
                    if file_age > (max_age_days * 86400):  # Convert days to seconds
                        os.remove(file_path)
                        count += 1
            
            self.logger.info(f"Cleaned up {count} old cache files")
            return {
                'success': True,
                'files_removed': count
            }
        except Exception as e:
            self.logger.error(f"Error cleaning up cache: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }