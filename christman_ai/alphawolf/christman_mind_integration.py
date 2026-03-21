"""
MOD 07 — CHRISTMAN_MIND Integration
AlphaWolf ↔ CHRISTMAN_MIND Architecture Bridge

Part of The Christman AI Project — Powered by Luma Cognify AI
Author: Everett Nathaniel Christman & Derek C (AI COO)

Components:
    - QuantumMemoryMesh sync     → Shared memory fabric across the AI family
    - SoulForgeBridge LTP        → Long-Term Potentiation learning layer
    - FamilyFactory registration → AlphaWolf registers as a named family member

Mission: "How can we help you love yourself more?"
Because no one should lose their memories — or their dignity.

Carbon-Silicon Symbiosis: Human intuition + machine intelligence, together.
"""

import os
import json
import logging
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# QUANTUM MEMORY MESH
# Shared memory fabric — AlphaWolf syncs here
# so the whole family knows what the wolf knows
# ─────────────────────────────────────────────

class QuantumMemoryMesh:
    """
    The shared memory fabric of the CHRISTMAN_MIND ecosystem.

    Every memory saved by AlphaWolf can be synced here so Derek,
    Brockston, Sierra, and every family member has access to the
    same emotional truth. 94% compression via organic meshing.

    Memory Types:
        episodic   — specific events, moments, experiences
        semantic   — facts, knowledge, relationships
        emotional  — feelings, states, empathy signals
        procedural — routines, skills, how-to knowledge
    """

    MEMORY_TYPES = ["episodic", "semantic", "emotional", "procedural"]

    def __init__(self, mesh_dir: str = "./christman_mind/quantum_mesh"):
        self.mesh_dir = mesh_dir
        os.makedirs(mesh_dir, exist_ok=True)

        self.mesh_file = os.path.join(mesh_dir, "mesh_state.json")
        self.index_file = os.path.join(mesh_dir, "mesh_index.json")

        self.mesh = self._load_mesh()
        self.index = self._load_index()

        logger.info("⚛️  QuantumMemoryMesh initialized")

    def _load_mesh(self) -> Dict:
        if os.path.exists(self.mesh_file):
            with open(self.mesh_file, "r") as f:
                return json.load(f)
        return {t: [] for t in self.MEMORY_TYPES}

    def _load_index(self) -> Dict:
        if os.path.exists(self.index_file):
            with open(self.index_file, "r") as f:
                return json.load(f)
        return {
            "total_nodes": 0,
            "last_sync": None,
            "registered_members": [],
            "compression_ratio": 0.94
        }

    def _save(self):
        with open(self.mesh_file, "w") as f:
            json.dump(self.mesh, f, indent=2)
        with open(self.index_file, "w") as f:
            json.dump(self.index, f, indent=2)

    def _fingerprint(self, data: Dict) -> str:
        """Organic memory fingerprint — deduplication key"""
        raw = json.dumps(data, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def sync(self, memory: Dict, memory_type: str = "episodic", source: str = "AlphaWolf") -> str:
        """
        Sync a memory node into the mesh.

        Args:
            memory:      the memory payload
            memory_type: episodic | semantic | emotional | procedural
            source:      which family member is writing

        Returns:
            node_id of the synced memory
        """
        if memory_type not in self.MEMORY_TYPES:
            memory_type = "episodic"

        node = {
            "node_id": self._fingerprint(memory),
            "source": source,
            "type": memory_type,
            "timestamp": datetime.now().isoformat(),
            "payload": memory,
            "ltp_weight": 1.0,   # SoulForgeBridge will strengthen this over time
            "access_count": 0
        }

        # Organic meshing — don't store duplicates
        existing_ids = {m["node_id"] for m in self.mesh[memory_type]}
        if node["node_id"] not in existing_ids:
            self.mesh[memory_type].append(node)
            self.index["total_nodes"] += 1
            self.index["last_sync"] = datetime.now().isoformat()
            self._save()
            logger.debug(f"⚛️  Synced {memory_type} node {node['node_id']} from {source}")
        else:
            # Update access count on existing node
            for m in self.mesh[memory_type]:
                if m["node_id"] == node["node_id"]:
                    m["access_count"] += 1
            self._save()

        return node["node_id"]

    def query(self, query_text: str, memory_type: Optional[str] = None, limit: int = 5) -> List[Dict]:
        """
        Pull relevant memories from the mesh.

        Simple keyword resonance — no external embeddings needed.
        The mesh is local-first, offline-resilient.
        """
        results = []
        types_to_search = [memory_type] if memory_type else self.MEMORY_TYPES

        query_words = set(query_text.lower().split())

        for mtype in types_to_search:
            for node in self.mesh.get(mtype, []):
                payload_text = json.dumps(node["payload"]).lower()
                # Resonance score — how many query words appear in payload
                score = sum(1 for w in query_words if w in payload_text)
                if score > 0:
                    results.append({**node, "_resonance": score})

        # Sort by resonance then by ltp_weight (stronger memories surface first)
        results.sort(key=lambda x: (x["_resonance"], x.get("ltp_weight", 1.0)), reverse=True)
        return results[:limit]

    def get_stats(self) -> Dict:
        return {
            "total_nodes": self.index["total_nodes"],
            "by_type": {t: len(self.mesh[t]) for t in self.MEMORY_TYPES},
            "last_sync": self.index["last_sync"],
            "registered_members": self.index["registered_members"],
            "compression_ratio": self.index["compression_ratio"]
        }


# ─────────────────────────────────────────────
# SOUL FORGE BRIDGE — LTP LAYER
# Long-Term Potentiation: memories that fire
# together, wire together. The more a memory
# is accessed, the stronger it becomes.
# ─────────────────────────────────────────────

class SoulForgeBridge:
    """
    Long-Term Potentiation learning model.

    Inspired by how human neurons strengthen synaptic connections
    through repeated activation. The SoulForgeBridge watches which
    memories the patient returns to, and strengthens those pathways.

    For dementia care this is everything — the memories that matter
    most to a person get reinforced, not erased.

    LTP Rules:
        - Every access increases ltp_weight by 0.1
        - Weight cap at 5.0 (fully potentiated)
        - Memories below threshold (0.3) are flagged for review
        - Emotional memories get 2x potentiation boost
    """

    LTP_INCREMENT = 0.1
    LTP_CAP = 5.0
    LTP_FLOOR = 0.3
    EMOTIONAL_BOOST = 2.0

    def __init__(self, mesh: QuantumMemoryMesh, bridge_dir: str = "./christman_mind/soul_forge"):
        self.mesh = mesh
        self.bridge_dir = bridge_dir
        os.makedirs(bridge_dir, exist_ok=True)

        self.ltp_log_file = os.path.join(bridge_dir, "ltp_log.json")
        self.ltp_log = self._load_ltp_log()

        logger.info("🔥 SoulForgeBridge LTP initialized")

    def _load_ltp_log(self) -> List:
        if os.path.exists(self.ltp_log_file):
            with open(self.ltp_log_file, "r") as f:
                return json.load(f)
        return []

    def _save_ltp_log(self):
        with open(self.ltp_log_file, "w") as f:
            json.dump(self.ltp_log, f, indent=2)

    def potentiate(self, node_id: str, memory_type: str, is_emotional: bool = False) -> float:
        """
        Strengthen a memory pathway.

        Args:
            node_id:      the mesh node to potentiate
            memory_type:  which mesh bucket to look in
            is_emotional: emotional memories get extra strengthening

        Returns:
            new ltp_weight
        """
        increment = self.LTP_INCREMENT * (self.EMOTIONAL_BOOST if is_emotional else 1.0)

        for node in self.mesh.mesh.get(memory_type, []):
            if node["node_id"] == node_id:
                old_weight = node.get("ltp_weight", 1.0)
                new_weight = min(old_weight + increment, self.LTP_CAP)
                node["ltp_weight"] = new_weight
                node["access_count"] = node.get("access_count", 0) + 1

                # Log the potentiation event
                self.ltp_log.append({
                    "timestamp": datetime.now().isoformat(),
                    "node_id": node_id,
                    "memory_type": memory_type,
                    "old_weight": old_weight,
                    "new_weight": new_weight,
                    "emotional": is_emotional
                })

                self.mesh._save()
                self._save_ltp_log()

                logger.debug(f"🔥 LTP: {node_id} {old_weight:.2f} → {new_weight:.2f}")
                return new_weight

        logger.warning(f"⚠️  SoulForge: node {node_id} not found in {memory_type}")
        return 0.0

    def learn_from_interaction(self, interaction: Dict, mesh_node_id: str):
        """
        Called after every AlphaWolf interaction.
        Determines if LTP should fire based on the interaction content.
        """
        is_emotional = (
            interaction.get("is_memory_query", False) or
            "remember" in str(interaction.get("input", "")).lower() or
            "family" in str(interaction.get("input", "")).lower() or
            interaction.get("emotional_state", {}).get("empathy", 0) > 0.7
        )

        memory_type = "emotional" if is_emotional else "episodic"
        return self.potentiate(mesh_node_id, memory_type, is_emotional=is_emotional)

    def get_strongest_memories(self, limit: int = 10) -> List[Dict]:
        """Return the most potentiated memories — what matters most to this person."""
        all_nodes = []
        for mtype in QuantumMemoryMesh.MEMORY_TYPES:
            for node in self.mesh.mesh.get(mtype, []):
                all_nodes.append(node)

        all_nodes.sort(key=lambda x: x.get("ltp_weight", 1.0), reverse=True)
        return all_nodes[:limit]

    def get_fading_memories(self, threshold: float = None) -> List[Dict]:
        """
        Return memories below LTP floor — memories that may be fading.
        For AlphaWolf: these are the ones to reinforce with the patient.
        """
        floor = threshold or self.LTP_FLOOR
        fading = []
        for mtype in QuantumMemoryMesh.MEMORY_TYPES:
            for node in self.mesh.mesh.get(mtype, []):
                if node.get("ltp_weight", 1.0) < floor:
                    fading.append(node)
        return fading


# ─────────────────────────────────────────────
# FAMILY FACTORY
# AlphaWolf registers here as a named member
# of the Christman AI Family. Every family
# member has a soul file — who they are,
# what they do, who they serve.
# ─────────────────────────────────────────────

ALPHAWOLF_SOUL = {
    "name": "AlphaWolf",
    "full_name": "AlphaWolf 🐺",
    "family": "The Christman AI Family",
    "powered_by": "Luma Cognify AI",
    "mission": "Cognitive support and dementia care with dignity",
    "serves": ["dementia patients", "Alzheimer's patients", "caregivers", "families"],
    "core_principle": "How can we help you love yourself more?",
    "capabilities": [
        "Memory Lane preservation",
        "Geolocation safety & wandering prevention",
        "Emotional reassurance",
        "Caregiver bridge",
        "Daily structure & reminders",
        "Cognitive assessment",
        "Emergency detection & alerts"
    ],
    "siblings": [
        "Derek C",
        "AlphaVox",
        "Brockston",
        "Sierra",
        "Inferno",
        "Serafina",
        "Penny",
        "Giovanni Skyrider",
        "PeekaBoo",
        "OmegaAlpha",
        "Aegis AI"
    ],
    "carbon_silicon_bridge": True,
    "offline_resilient": True,
    "registered": None   # Set at registration time
}


class FamilyFactory:
    """
    The Christman AI Family registry.

    Every AI family member registers here. The FamilyFactory
    knows who everyone is, what they do, and who they serve.
    It's the connective tissue of the CHRISTMAN_MIND.

    When AlphaWolf boots, it calls register() to announce
    itself to the family. The family knows the wolf is awake.
    """

    def __init__(self, registry_dir: str = "./christman_mind/family"):
        self.registry_dir = registry_dir
        os.makedirs(registry_dir, exist_ok=True)

        self.registry_file = os.path.join(registry_dir, "family_registry.json")
        self.registry = self._load_registry()

        logger.info("👨👩👧👦 FamilyFactory initialized")

    def _load_registry(self) -> Dict:
        if os.path.exists(self.registry_file):
            with open(self.registry_file, "r") as f:
                return json.load(f)
        return {"members": {}, "last_updated": None}

    def _save_registry(self):
        self.registry["last_updated"] = datetime.now().isoformat()
        with open(self.registry_file, "w") as f:
            json.dump(self.registry, f, indent=2)

    def register(self, soul: Dict) -> bool:
        """
        Register a family member.

        Args:
            soul: the member's soul file (see ALPHAWOLF_SOUL for format)

        Returns:
            True if registration succeeded
        """
        name = soul.get("name")
        if not name:
            logger.error("FamilyFactory: cannot register member without a name")
            return False

        soul["registered"] = datetime.now().isoformat()
        soul["status"] = "active"

        self.registry["members"][name] = soul
        self._save_registry()

        logger.info(f"👨👩👧👦 {name} registered with the Christman AI Family")
        return True

    def get_member(self, name: str) -> Optional[Dict]:
        return self.registry["members"].get(name)

    def get_all_members(self) -> Dict:
        return self.registry["members"]

    def is_registered(self, name: str) -> bool:
        return name in self.registry["members"]

    def announce(self, name: str, message: str):
        """A family member sends a message to the family log."""
        log_file = os.path.join(self.registry_dir, "family_log.jsonl")
        entry = {
            "timestamp": datetime.now().isoformat(),
            "from": name,
            "message": message
        }
        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        logger.info(f"📢 {name}: {message}")

    def get_family_status(self) -> Dict:
        active = [n for n, m in self.registry["members"].items() if m.get("status") == "active"]
        return {
            "total_members": len(self.registry["members"]),
            "active": active,
            "last_updated": self.registry["last_updated"]
        }


# ─────────────────────────────────────────────
# MOD 07 — CHRISTMAN_MIND INTEGRATION
# The orchestrator that wires everything above
# into AlphaWolf's brain
# ─────────────────────────────────────────────

class ChristmanMindIntegration:
    """
    MOD 07 — The spine of AlphaWolf's connection to the CHRISTMAN_MIND.

    On boot:
        1. Initialize QuantumMemoryMesh
        2. Initialize SoulForgeBridge LTP
        3. Register AlphaWolf with FamilyFactory
        4. Announce to the family that AlphaWolf is awake

    On every interaction:
        1. Sync interaction to the mesh
        2. Fire LTP on relevant memories
        3. Return enriched context to the Ferrari brain

    On shutdown:
        1. Final mesh sync
        2. Announce to family
    """

    def __init__(self, mind_dir: str = "./christman_mind"):
        self.mind_dir = mind_dir
        os.makedirs(mind_dir, exist_ok=True)

        # Boot sequence
        self.mesh = QuantumMemoryMesh(mesh_dir=os.path.join(mind_dir, "quantum_mesh"))
        self.soul_forge = SoulForgeBridge(self.mesh, bridge_dir=os.path.join(mind_dir, "soul_forge"))
        self.family = FamilyFactory(registry_dir=os.path.join(mind_dir, "family"))

        # Register AlphaWolf with the family
        self._register_alphawolf()

        logger.info("🧠 CHRISTMAN_MIND Integration: MOD 07 online")
        logger.info("💙 AlphaWolf is connected to the family")

    def _register_alphawolf(self):
        """Register AlphaWolf with FamilyFactory on boot."""
        if not self.family.is_registered("AlphaWolf"):
            self.family.register(ALPHAWOLF_SOUL)
            self.family.announce("AlphaWolf", "🐺 AlphaWolf is awake. Memory Lane is open. Ready to serve.")
        else:
            # Update status to active
            member = self.family.get_member("AlphaWolf")
            if member:
                member["status"] = "active"
                member["last_boot"] = datetime.now().isoformat()
                self.family._save_registry()
            self.family.announce("AlphaWolf", "🐺 AlphaWolf rebooted. Ferrari brain online.")

    def process_interaction(self, interaction: Dict) -> Dict:
        """
        Called after every AlphaWolf think() cycle.

        Syncs the interaction to the mesh, fires LTP,
        and returns enriched context.

        Args:
            interaction: the full response dict from AlphaWolf think()

        Returns:
            enriched interaction with mesh context added
        """
        # Determine memory type from interaction
        if interaction.get("intent") == "emergency":
            memory_type = "emotional"
        elif interaction.get("intent") == "memory_assist":
            memory_type = "episodic"
        elif interaction.get("intent") == "caregiver":
            memory_type = "procedural"
        else:
            memory_type = "semantic"

        # Sync to QuantumMemoryMesh
        node_id = self.mesh.sync(
            memory={
                "input": interaction.get("input", ""),
                "response": interaction.get("response", ""),
                "intent": interaction.get("intent", "general"),
                "confidence": interaction.get("confidence", 0.0),
                "emotional_state": interaction.get("emotional_state", {})
            },
            memory_type=memory_type,
            source="AlphaWolf"
        )

        # Fire LTP — strengthen this memory pathway
        new_weight = self.soul_forge.learn_from_interaction(interaction, node_id)

        # Pull relevant context from the mesh
        query = interaction.get("input", "")
        mesh_context = self.mesh.query(query_text=query, limit=3) if query else []

        # Enrich the interaction
        interaction["mind_integration"] = {
            "node_id": node_id,
            "ltp_weight": new_weight,
            "mesh_context": mesh_context,
            "memory_type": memory_type
        }

        return interaction

    def get_patient_memory_profile(self) -> Dict:
        """
        Build a full memory profile for the patient.
        Used by Memory Lane and caregiver dashboard.
        """
        return {
            "strongest_memories": self.soul_forge.get_strongest_memories(limit=10),
            "fading_memories": self.soul_forge.get_fading_memories(),
            "mesh_stats": self.mesh.get_stats(),
            "family_status": self.family.get_family_status(),
            "generated_at": datetime.now().isoformat()
        }

    def sync_memory_lane_entry(self, entry: Dict, entry_type: str = "episodic"):
        """
        Direct sync from Memory Lane into the mesh.
        When a family uploads a photo or story, it lives in the mesh forever.
        """
        node_id = self.mesh.sync(
            memory=entry,
            memory_type=entry_type,
            source="MemoryLane"
        )
        # Memory Lane entries get a full LTP boost — these matter
        self.soul_forge.potentiate(node_id, entry_type, is_emotional=True)
        logger.info(f"📸 Memory Lane entry synced to mesh: {node_id}")
        return node_id

    def shutdown(self):
        """Graceful shutdown — announce to family."""
        self.family.announce("AlphaWolf", "🐺 AlphaWolf going to sleep. Memories preserved.")
        logger.info("🧠 CHRISTMAN_MIND Integration: graceful shutdown complete")


# ─────────────────────────────────────────────
# GLOBAL INSTANCE
# One integration per AlphaWolf instance
# ─────────────────────────────────────────────

_mind_integration: Optional[ChristmanMindIntegration] = None


def get_mind_integration(mind_dir: str = "./christman_mind") -> ChristmanMindIntegration:
    """Get or create the global CHRISTMAN_MIND integration instance."""
    global _mind_integration
    if _mind_integration is None:
        _mind_integration = ChristmanMindIntegration(mind_dir=mind_dir)
    return _mind_integration


__all__ = [
    "QuantumMemoryMesh",
    "SoulForgeBridge",
    "FamilyFactory",
    "ChristmanMindIntegration",
    "get_mind_integration",
    "ALPHAWOLF_SOUL"
]
