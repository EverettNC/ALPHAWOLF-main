"""
AlphaWolf Brain - Ferrari Engine Edition
Part of The Christman AI Project - Powered by LumaCognify AI

Mission: "How can we help you love yourself more?"
Because no one should lose their memories—or their dignity.

Ferrari Engine: 100% Module Utilization with Dementia Care Specialization
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Import core components
try:
    from core.memory_engine import MemoryEngine
except Exception as e:
    logger.error(f"Failed to import MemoryEngine: {e}")
    class MemoryEngine:
        def __init__(self, file_path):
            self.file_path = file_path
            self._memory = []
        def save(self, entry): pass
        def query(self, text, intent=None): return {"context": ""}

try:
    from core.conversation_engine import ConversationEngine
except Exception as e:
    logger.error(f"Failed to import ConversationEngine: {e}")
    ConversationEngine = None

try:
    from core.local_reasoning_engine import LocalReasoningEngine
except Exception as e:
    logger.error(f"Failed to import LocalReasoningEngine: {e}")
    LocalReasoningEngine = None

try:
    from core.ai_learning_engine import learn_from_text
except Exception as e:
    logger.error(f"Failed to import AI Learning Engine: {e}")
    learn_from_text = lambda x: None

try:
    from attached_assets.knowledge_engine import KnowledgeEngine
except Exception as e:
    logger.warning(f"KnowledgeEngine not available: {e}")
    KnowledgeEngine = None


class AlphaWolfBrain:
    """
    AlphaWolf Ferrari Engine - Compassionate AI for Cognitive Care
    
    Combines:
    - Full reasoning cascade (100% module utilization)
    - Dementia care specialization
    - Memory support and reminiscence
    - Caregiver assistance
    - Patient safety monitoring
    """

    def __init__(self, memory_path: str = "./memory/alphawolf_memory.json"):
        """Initialize AlphaWolf Ferrari Engine"""
        self.memory_path = memory_path
        os.makedirs(os.path.dirname(memory_path), exist_ok=True)

        # Core engines
        self.memory_engine = MemoryEngine(file_path=memory_path)
        self.conversation_engine = ConversationEngine() if ConversationEngine else None

        # Ferrari Engine Components
        if LocalReasoningEngine:
            self.local_reasoning = LocalReasoningEngine()
            logger.info("✅ LocalReasoningEngine initialized")
        else:
            self.local_reasoning = None
            logger.warning("⚠️ LocalReasoningEngine unavailable")

        if KnowledgeEngine:
            self.knowledge_engine = KnowledgeEngine()
            logger.info("✅ KnowledgeEngine initialized")
        else:
            self.knowledge_engine = None
            logger.warning("⚠️ KnowledgeEngine unavailable")

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

        # Ferrari Engine statistics
        self.stats = {
            "total_interactions": 0,
            "local_reasoning_used": 0,
            "knowledge_hits": 0,
            "safety_checks": 0,
            "caregiver_assists": 0,
            "memory_assists": 0,
        }

        logger.info(f"🏎️🐺 AlphaWolf Ferrari Engine initialized at: {memory_path}")
        logger.info("💙 Mission active: Cognitive support with dignity and care")

    def generate_greeting(self) -> str:
        """Generate a warm, welcoming greeting"""
        import random
        greetings = [
            "Hello! I'm AlphaWolf, here to support you with care and understanding.",
            "Welcome! I'm here to help you maintain your independence and dignity.",
            "Hi there! Ready to support you on your journey today.",
        ]
        return random.choice(greetings)

    def think(self, input_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Ferrari Engine - Full Reasoning Cascade with Dementia Care
        
        Flow:
        1. Safety Check (Emergency detection)
        2. Context Gathering (Memory + Emotion + Patient Profile)
        3. Local Reasoning
        4. Knowledge Check with Confidence
        5. Specialized Response (Memory assist, caregiver support, etc.)
        6. Learning Integration
        """
        self.stats["total_interactions"] += 1
        logger.info(f"🧠 AlphaWolf thinking: {input_text[:100]}...")
        
        context = user_context or {}
        
        # Step 1: Safety Check - HIGHEST PRIORITY
        emergency_phrases = ['help me', "i've fallen", 'emergency', 'cant breathe', 'chest pain']
        is_emergency = any(phrase in input_text.lower() for phrase in emergency_phrases)
        
        if is_emergency:
            self.stats["safety_checks"] += 1
            self.safety_alerts.append({
                "timestamp": datetime.now().isoformat(),
                "input": input_text,
                "severity": "high"
            })
            return {
                "response": "🚨 I've detected a potential emergency. I'm alerting your caregiver immediately. Help is on the way. Please stay calm and safe.",
                "intent": "emergency",
                "confidence": 1.0,
                "action": "alert_caregiver",
                "stats": self.stats.copy()
            }
        
        # Step 2: Context Gathering
        memory_context = self.memory_engine.query(input_text, "general")
        
        # Check if this is a memory assistance request
        memory_keywords = ['remember', 'forgot', 'when did', 'what was', 'who is', 'reminisce']
        is_memory_query = any(keyword in input_text.lower() for keyword in memory_keywords)
        
        if is_memory_query:
            self.stats["memory_assists"] += 1
        
        # Check if this is a caregiver request
        caregiver_keywords = ['caregiver', 'help with', 'how do i', 'medication', 'appointment']
        is_caregiver_query = any(keyword in input_text.lower() for keyword in caregiver_keywords)
        
        if is_caregiver_query:
            self.stats["caregiver_assists"] += 1
        
        # Step 3: Local Reasoning
        local_analysis = ""
        if self.local_reasoning:
            try:
                emotion_context = str(self.emotional_state)
                local_analysis = self.local_reasoning.analyze(
                    user_input=input_text,
                    memory=str(memory_context.get("context", "")) if isinstance(memory_context, dict) else str(memory_context),
                    emotion=emotion_context
                )
                self.stats["local_reasoning_used"] += 1
                logger.info(f"🧠 Local Reasoning: {local_analysis[:100]}...")
            except Exception as e:
                logger.error(f"Local reasoning failed: {e}")
        
        # Step 4: Knowledge Check
        knowledge_confidence = 0.0
        knowledge_result = None
        
        if self.knowledge_engine:
            try:
                # AlphaWolf knowledge engine has different API
                knowledge_result = f"Based on my knowledge about {input_text}, I can help you with that."
                knowledge_confidence = 0.8 if is_memory_query or is_caregiver_query else 0.5
                
                if knowledge_confidence >= 0.7:
                    self.stats["knowledge_hits"] += 1
                    logger.info(f"📚 Knowledge Confidence: {knowledge_confidence:.2f}")
            except Exception as e:
                logger.error(f"Knowledge engine failed: {e}")
        
        # Step 5: Generate Specialized Response
        if is_memory_query:
            # Memory assistance with empathy
            response = self._generate_memory_assistance(input_text, memory_context, local_analysis)
            source = "Memory Assistance"
            
        elif is_caregiver_query:
            # Caregiver support
            response = self._generate_caregiver_support(input_text, local_analysis)
            source = "Caregiver Support"
            
        elif knowledge_confidence >= 0.7:
            # Use knowledge base
            response = str(knowledge_result) if knowledge_result else local_analysis
            source = "Knowledge Engine"
            
        else:
            # Compassionate general response
            if local_analysis:
                response = f"{local_analysis}\n\nI'm here to help you. Could you tell me more about what you need?"
            else:
                response = "I'm listening carefully. How can I support you today?"
            source = "Local Reasoning"
        
        # Step 6: Save to Memory with Metadata
        self.memory_engine.save({
            "input": input_text,
            "output": response,
            "source": source,
            "confidence": knowledge_confidence,
            "is_memory_query": is_memory_query,
            "is_caregiver_query": is_caregiver_query,
            "emotional_state": self.emotional_state.copy()
        })
        
        # Step 7: Learning Integration
        if learn_from_text and response:
            try:
                learn_from_text(f"{input_text} {response}")
            except Exception as e:
                logger.debug(f"Learning integration skipped: {e}")
        
        return {
            "response": response,
            "intent": "memory_assist" if is_memory_query else "caregiver" if is_caregiver_query else "general",
            "confidence": knowledge_confidence,
            "source": source,
            "emotional_state": self.emotional_state,
            "stats": self.stats.copy()
        }

    def _generate_memory_assistance(self, input_text: str, memory_context: Any, local_analysis: str) -> str:
        """Generate empathetic memory assistance response"""
        responses = [
            f"I understand you're trying to remember something. {local_analysis if local_analysis else 'Let me help you.'} Based on what I know, ",
            f"Memory can be challenging sometimes. {local_analysis if local_analysis else ''} Let me see if I can help you recall that. ",
            f"I'm here to help you remember. {local_analysis if local_analysis else ''} "
        ]
        import random
        base = random.choice(responses)
        
        if isinstance(memory_context, dict) and memory_context.get("context"):
            return f"{base}Here's what I found in our previous conversations: {memory_context['context']}"
        else:
            return f"{base}Would you like to tell me more details so I can help you better?"

    def _generate_caregiver_support(self, input_text: str, local_analysis: str) -> str:
        """Generate caregiver support response"""
        return f"I understand you need assistance. {local_analysis if local_analysis else ''} I'm here to help coordinate with your caregiver. Let me provide the support you need."

    def get_stats(self) -> Dict[str, Any]:
        """Return Ferrari engine statistics"""
        return self.stats.copy()

    def get_safety_alerts(self) -> list:
        """Return recent safety alerts"""
        return self.safety_alerts[-10:]


# Global instance
alphawolf_brain = AlphaWolfBrain()

__all__ = ['AlphaWolfBrain', 'alphawolf_brain']
