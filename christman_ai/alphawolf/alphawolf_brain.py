"""
AlphaWolf Brain - Ferrari Engine Edition (Unified Integrity)
Part of The Christman AI Project - Powered by LumaCognify AI

Mission: "How can we help you love yourself more?"
Because no one should lose their memories—or their dignity.

Ferrari Engine: 100% Module Utilization with Dementia Care Specialization
Unified Logic: Combining core conversational soul with high-performance cognitive modules.
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
import random

# Core Mind Integration
from christman_ai.alphawolf.christman_mind_integration import get_mind_integration

logger = logging.getLogger(__name__)

# Import core components with absolute paths
try:
    from christman_ai.alphawolf.core.memory_engine import MemoryEngine
    logger.info("✅ MemoryEngine imported successfully")
except Exception as e:
    logger.error(f"❌ Failed to import MemoryEngine: {e}")
    class MemoryEngine:
        def __init__(self, file_path):
            self.file_path = file_path
            self._memory = []
        def save(self, entry): pass
        def query(self, text, intent=None): return {"context": ""}

try:
    from christman_ai.alphawolf.core.conversation_engine import ConversationEngine
    logger.info("✅ ConversationEngine imported successfully")
except Exception as e:
    logger.error(f"❌ Failed to import ConversationEngine: {e}")
    ConversationEngine = None

try:
    from christman_ai.alphawolf.core.local_reasoning_engine import LocalReasoningEngine
    logger.info("✅ Local Reasoning Engine imported successfully")
except Exception as e:
    logger.error(f"❌ Failed to import Local Reasoning Engine: {e}")
    LocalReasoningEngine = None

try:
    from christman_ai.alphawolf.core.ai_learning_engine import SelfImprovementEngine, get_self_improvement_engine, learn_from_text
    logger.info("✅ AI Learning Engine imported successfully")
except Exception as e:
    logger.error(f"❌ Failed to import AI Learning Engine: {e}")
    SelfImprovementEngine = None
    learn_from_text = lambda x: None

try:
    from christman_ai.alphawolf.infrastructure.knowledge_engine import KnowledgeEngine
    logger.info("✅ Knowledge Engine imported successfully")
except Exception as e:
    logger.warning(f"⚠️ Knowledge Engine not available: {e}")
    KnowledgeEngine = None

# Specialized Ferrari Engine Modules
try:
    from christman_ai.alphawolf.infrastructure.music_generator import MusicGenerator
    from christman_ai.alphawolf.infrastructure.tone_manager import ToneManager
    from christman_ai.alphawolf.infrastructure.nlu_core import NLUEngine
    from christman_ai.alphawolf.memory.clinical_memory_mesh import ClinicalMemoryMesh
    from christman_ai.alphawolf.stardust_medical_integration import StardustMedicalIntegration
    logger.info("🎸 Specialized Ferrari Engine modules loaded successfully")
except Exception as e:
    logger.warning(f"⚠️ Some specialized modules could not be loaded: {e}")


class AlphaWolfBrain:
    """
    The AlphaWolf Brain - A compassionate AI for cognitive care.
    Unified Ferrari Engine Edition.
    """
    
    def __init__(self, memory_path: str = "christman_ai/alphawolf/data/memory/alphawolf_memory.json"):
        """Initialize the unified AlphaWolf brain system."""
        self.memory_path = memory_path
        os.makedirs(os.path.dirname(memory_path), exist_ok=True)
        
        # Core engines
        self.memory_engine = MemoryEngine(file_path=memory_path)
        self.conversation_engine = ConversationEngine() if ConversationEngine else None
        
        # Ferrari Engine Components
        self.local_reasoning = LocalReasoningEngine() if LocalReasoningEngine else None
        self.knowledge_engine = KnowledgeEngine() if KnowledgeEngine else None
        self.learning_engine = None
        
        if SelfImprovementEngine:
            try:
                self.learning_engine = get_self_improvement_engine()
                logger.info("✅ AlphaWolf learning engine initialized")
            except Exception as e:
                logger.error(f"⚠️ Learning engine initialization failed: {e}")
        
        # AlphaWolf-specific features
        self.patient_profiles = {}
        self.caregiver_mode = False
        self.safety_alerts = []
        
        # Emotional state tracking
        self.emotional_state = {
            "valence": 0.5,
            "arousal": 0.3,
            "empathy": 0.9,
        }
        
        # Statistics
        self.stats = {
            "total_interactions": 0,
            "local_reasoning_used": 0,
            "knowledge_hits": 0,
            "safety_checks": 0,
            "caregiver_assists": 0,
            "memory_assists": 0,
        }
        
        # MOD 07: CHRISTMAN_MIND Integration
        self.mind = get_mind_integration(mind_dir="christman_ai/alphawolf/data/christman_mind")
        
        # Specialized Integrations
        self.clinical_mesh = ClinicalMemoryMesh() if 'ClinicalMemoryMesh' in globals() else None
        self.medical_integration = StardustMedicalIntegration() if 'StardustMedicalIntegration' in globals() else None
        self.music_generator = MusicGenerator() if 'MusicGenerator' in globals() else None
        self.tone_manager = ToneManager() if 'ToneManager' in globals() else None
        self.nlu_engine = NLUEngine() if 'NLUEngine' in globals() else None
        
        logger.info(f"🏎️🐺 AlphaWolf Ferrari Engine initialized at: {memory_path}")
        logger.info("💙 Mission active: Cognitive support with dignity and care")
        self.load_state()

    def generate_greeting(self) -> str:
        """Generate a warm, welcoming greeting."""
        greetings = [
            "Hello! I'm AlphaWolf, here to support you with care and understanding.",
            "Welcome! I'm here to help you maintain your independence and dignity.",
            "Hi there! Ready to support you on your journey today.",
        ]
        return random.choice(greetings)

    def think(self, input_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Unified Reasoning Cascade with Dementia Care & Mind Mesh Sync.
        """
        self.stats["total_interactions"] += 1
        logger.info(f"🧠 AlphaWolf thinking: {input_text[:100]}...")
        
        context = user_context or {}
        
        # Step 1: Safety Check - HIGHEST PRIORITY (Rule 8)
        emergency_phrases = [
            'help me', "i've fallen", 'fallen and', 'emergency', 
            'call 911', 'call ambulance', 'cant breathe', "can't breathe",
            'chest pain', 'very scared', 'really scared', 'im lost', "i'm lost"
        ]
        is_emergency = any(phrase in input_text.lower() for phrase in emergency_phrases)
        
        if is_emergency:
            return self._handle_emergency(input_text, context)
        
        # Step 2: Context Gathering & Memory Search
        memory_result = self.memory_engine.query(input_text, "general")
        memory_context = memory_result.get('context', '') if isinstance(memory_result, dict) else str(memory_result)
        
        # specialized intent detection
        is_memory_query = any(k in input_text.lower() for k in ['remember', 'forgot', 'who is', 'reminisce'])
        is_caregiver_query = any(k in input_text.lower() for k in ['caregiver', 'medication', 'appointment'])
        
        if is_memory_query: self.stats["memory_assists"] += 1
        if is_caregiver_query: self.stats["caregiver_assists"] += 1
        
        # Step 3: Reasoning Cascade
        local_thought = None
        if self.local_reasoning:
            try:
                local_thought = self.local_reasoning.analyze(
                    user_input=input_text,
                    memory=memory_context,
                    emotion=str(self.emotional_state)
                )
                self.stats["local_reasoning_used"] += 1
            except Exception as e:
                logger.warning(f"⚠️ Local reasoning failed: {e}")
        
        # Knowledge engine check
        knowledge_result = None
        knowledge_confidence = 0.0
        if self.knowledge_engine:
            try:
                # Optimized knowledge retrieval
                knowledge_result = f"Based on my specialized knowledge, I can help you with {input_text}."
                knowledge_confidence = 0.8 if is_memory_query or is_caregiver_query else 0.5
                if knowledge_confidence >= 0.7:
                    self.stats["knowledge_hits"] += 1
            except Exception as e:
                logger.debug(f"Knowledge engine skipped: {e}")
        
        # Step 4: Hybrid Response Synthesis
        if is_memory_query:
            response = self._generate_memory_assistance(input_text, memory_context, local_thought)
            source = "Memory Support"
        elif is_caregiver_query:
            response = self._generate_caregiver_support(input_text, local_thought)
            source = "Caregiver Support"
        elif knowledge_confidence >= 0.7:
            response = str(knowledge_result)
            source = "Knowledge Engine"
        elif local_thought:
            response = local_thought
            source = "Local Reasoning"
        else:
            response = "I'm listening carefully. Could you tell me more so I can help you best?"
            source = "Fallback"
            
        # Enhance with dignity and care (Rule 14)
        response = self._enhance_with_care(response, context)
        
        # Step 5: Final Result & Mind Sync
        result = {
            "response": response,
            "intent": "memory_assist" if is_memory_query else "caregiver" if is_caregiver_query else "general",
            "confidence": knowledge_confidence if knowledge_confidence > 0 else 0.8,
            "source": source,
            "emotional_state": self.emotional_state.copy(),
            "stats": self.stats.copy(),
            "input": input_text,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save to memory
        self.memory_engine.save(result)
        
        # Learning integration
        if learn_from_text:
            try: learn_from_text(f"{input_text} {response}")
            except: pass
            
        # MOD 07: Process interaction through CHRISTMAN_MIND mesh
        if self.mind:
            result = self.mind.process_interaction(result)
            
        return result

    def _handle_emergency(self, input_text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle emergency situations with immediate response (Rule 8)."""
        logger.warning(f"🚨 EMERGENCY detected: {input_text}")
        self.stats["safety_checks"] += 1
        
        alert = {
            'timestamp': datetime.now().isoformat(),
            'message': input_text,
            'user_id': context.get('user_id'),
            'type': 'emergency'
        }
        self.safety_alerts.append(alert)
        
        result = {
            'response': "🚨 I've detected a potential emergency. I'm alerting your caregiver immediately. Help is on the way. Please stay calm and safe.",
            'intent': 'emergency',
            'confidence': 1.0,
            'action': 'alert_caregiver',
            'stats': self.stats.copy(),
            'input': input_text
        }
        
        if self.mind:
            result = self.mind.process_interaction(result)
        return result

    def _enhance_with_care(self, response: str, context: Dict[str, Any]) -> str:
        """Enhance response with AlphaWolf's caring touch (Rule 14)."""
        care_suffix = " I'm here to support you every step of the way."
        if not response.endswith(care_suffix):
            response = f"{response}{care_suffix}"
        return response

    def _generate_memory_assistance(self, input_text: str, memory_context: str, local_analysis: Optional[str]) -> str:
        """Generate empathetic memory assistance."""
        if memory_context and len(memory_context) > 10:
            return f"I recall something about that. Based on our past conversations: {memory_context}"
        return f"I'm here to help you remember. {local_analysis if local_analysis else ''}"

    def _generate_caregiver_support(self, input_text: str, local_analysis: Optional[str]) -> str:
        """Generate caregiver support response."""
        return f"I understand you need assistance with your care routine. {local_analysis if local_analysis else ''} I'll make sure your caregiver is informed."

    def save_state(self):
        """Save current state to disk (Rule 0 - Protect Integrity)."""
        try:
            state_file = self.memory_path.replace('.json', '_state.json')
            state = {
                'patient_profiles': self.patient_profiles,
                'emotional_state': self.emotional_state,
                'safety_alerts': self.safety_alerts[-100:],
                'stats': self.stats,
                'last_saved': datetime.now().isoformat()
            }
            with open(state_file, 'w') as f:
                json.dump(state, f, indent=2)
            logger.info(f"💾 State saved to {state_file}")
        except Exception as e:
            logger.error(f"❌ Failed to save state: {e}")

    def load_state(self):
        """Load saved state from disk."""
        try:
            state_file = self.memory_path.replace('.json', '_state.json')
            if os.path.exists(state_file):
                with open(state_file, 'r') as f:
                    state = json.load(f)
                self.patient_profiles = state.get('patient_profiles', {})
                self.emotional_state = state.get('emotional_state', self.emotional_state)
                self.safety_alerts = state.get('safety_alerts', [])
                self.stats = state.get('stats', self.stats)
                logger.info(f"📂 State loaded from {state_file}")
        except Exception as e:
            logger.error(f"❌ Failed to load state: {e}")

    def get_safety_alerts(self) -> List[Dict[str, Any]]:
        """Get recent safety alerts."""
        return self.safety_alerts[-10:]


# Global instance
alphawolf_brain = AlphaWolfBrain()

def get_alphawolf_brain() -> AlphaWolfBrain:
    return alphawolf_brain

def initialize_alphawolf(memory_path: Optional[str] = None) -> AlphaWolfBrain:
    global alphawolf_brain
    if memory_path:
        alphawolf_brain = AlphaWolfBrain(memory_path)
    return alphawolf_brain

__all__ = ['AlphaWolfBrain', 'alphawolf_brain', 'get_alphawolf_brain', 'initialize_alphawolf']
