#!/usr/bin/env python3
"""
🏎️ AlphaWolf Ferrari Mode - Full Memory Lane Activation
For Dementia/Alzheimer's patients - preserving human existence
"""

import os
from pathlib import Path

print("🏎️ STARTING ALPHAWOLF IN FERRARI MODE...")
print("=" * 60)

# Check Memory Lane
memory_lane_path = Path("data/memory_lane")
if memory_lane_path.exists():
    print("\n✅ Memory Lane structure exists")
    
    # Check index
    index_file = memory_lane_path / "memory_lane_index.json"
    if index_file.exists():
        import json
        with open(index_file) as f:
            index = json.load(f)
        
        print(f"\n🧠 Memory Lane Status:")
        print(f"   Albums: {index.get('total_albums', 0)}")
        print(f"   Timeline Events: {index.get('total_events', 0)}")
        print(f"   Music Memories: {index.get('total_music', 0)}")
        print(f"   Life Stories: {index.get('total_stories', 0)}")
        print(f"   Last Updated: {index.get('last_updated', 'Unknown')}")
    else:
        print("   ⚠️  Memory Lane not initialized - run FIX_MEMORY_LANE.py")
else:
    print("\n❌ Memory Lane directory missing!")
    print("   Run: python3 FIX_MEMORY_LANE.py")

# Check Ferrari brain
try:
    from simple_memory_mesh import SimpleMemoryMesh
    memory = SimpleMemoryMesh(memory_dir="./alphawolf_memory")
    stats = memory.get_stats()
    print(f"\n🏎️ Ferrari Brain:")
    print(f"   Episodic: {stats.get('episodic_memory_count', 0)}")
    print(f"   Working: {stats.get('working_memory_count', 0)}")
    print("   ✅ Memory system operational!")
except Exception as e:
    print(f"\n⚠️  Ferrari brain: {e}")

print("\n✅ AlphaWolf is ready!")
print("\nMemory Lane preserves human existence for dementia patients.")
print("Start the app: python3 app.py")
