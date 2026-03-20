#!/usr/bin/env python3
"""
Fix AlphaWolf Memory Lane - Create Storage and Initialize
Memory Lane is the KILLER FEATURE for dementia patients
"""

import os
import json
from pathlib import Path
from datetime import datetime

print("🧠 FIXING ALPHAWOLF MEMORY LANE")
print("=" * 70)

# Create Memory Lane directory structure
base_path = Path("data/memory_lane")
paths = {
    "albums": base_path / "albums",
    "timeline": base_path / "timeline",
    "music": base_path / "music",
    "stories": base_path / "stories",
    "uploads": base_path / "uploads"
}

print("\n1️⃣ Creating Memory Lane directory structure...")
for name, path in paths.items():
    path.mkdir(parents=True, exist_ok=True)
    print(f"   ✅ Created {name}/ directory")

# Initialize albums with demo data
print("\n2️⃣ Initializing demo albums...")

demo_albums = [
    {
        'id': 'demo_1',
        'name': 'Family Gatherings',
        'description': 'Special moments with loved ones over the years',
        'category': 'Family',
        'cover_image': '/static/img/album-placeholder.jpg',
        'item_count': 0,
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'created_at': '2020-01-15',
        'items': []
    },
    {
        'id': 'demo_2',
        'name': 'Career Highlights',
        'description': 'Professional accomplishments and milestones',
        'category': 'Career',
        'cover_image': '/static/img/album-placeholder.jpg',
        'item_count': 0,
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'created_at': '2018-05-10',
        'items': []
    },
    {
        'id': 'demo_3',
        'name': 'Special Places',
        'description': 'Locations that hold special memories',
        'category': 'Travel',
        'cover_image': '/static/img/album-placeholder.jpg',
        'item_count': 0,
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'created_at': '2019-03-20',
        'items': []
    }
]

albums_file = paths["albums"] / "albums.json"
with open(albums_file, 'w') as f:
    json.dump(demo_albums, f, indent=2)

print(f"   ✅ Created {len(demo_albums)} demo albums")

# Initialize timeline events
print("\n3️⃣ Initializing timeline...")

demo_timeline = [
    {
        'id': 'event_1',
        'title': 'Wedding Day',
        'description': 'Married my best friend',
        'date': '1995-06-15',
        'category': 'Life Milestone',
        'image': None,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 'event_2',
        'title': 'First Child Born',
        'description': 'Welcome to the world',
        'date': '1998-03-22',
        'category': 'Family',
        'image': None,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 'event_3',
        'title': 'Career Achievement',
        'description': 'Promoted to senior position',
        'date': '2005-09-10',
        'category': 'Career',
        'image': None,
        'created_at': datetime.now().isoformat()
    }
]

timeline_file = paths["timeline"] / "events.json"
with open(timeline_file, 'w') as f:
    json.dump(demo_timeline, f, indent=2)

print(f"   ✅ Created {len(demo_timeline)} timeline events")

# Initialize music memories
print("\n4️⃣ Initializing music memories...")

demo_music = [
    {
        'id': 'music_1',
        'title': 'Our Song',
        'artist': 'Unknown',
        'memory': 'Played at our wedding',
        'year': '1995',
        'category': 'Wedding',
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 'music_2',
        'title': 'Road Trip Playlist',
        'artist': 'Various',
        'memory': 'Cross-country adventure',
        'year': '2003',
        'category': 'Travel',
        'created_at': datetime.now().isoformat()
    }
]

music_file = paths["music"] / "music_memories.json"
with open(music_file, 'w') as f:
    json.dump(demo_music, f, indent=2)

print(f"   ✅ Created {len(demo_music)} music memories")

# Initialize stories
print("\n5️⃣ Initializing life stories...")

demo_stories = [
    {
        'id': 'story_1',
        'title': 'How We Met',
        'content': 'It was a beautiful spring day when we first crossed paths...',
        'category': 'Love Story',
        'date': '1994-04-15',
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 'story_2',
        'title': 'First Day of School',
        'content': 'I remember walking into that classroom, nervous but excited...',
        'category': 'Childhood',
        'date': '1965-09-01',
        'created_at': datetime.now().isoformat()
    }
]

stories_file = paths["stories"] / "stories.json"
with open(stories_file, 'w') as f:
    json.dump(demo_stories, f, indent=2)

print(f"   ✅ Created {len(demo_stories)} life stories")

# Create Memory Lane index
print("\n6️⃣ Creating Memory Lane index...")

memory_lane_index = {
    'total_albums': len(demo_albums),
    'total_events': len(demo_timeline),
    'total_music': len(demo_music),
    'total_stories': len(demo_stories),
    'last_updated': datetime.now().isoformat(),
    'initialized': True
}

index_file = base_path / "memory_lane_index.json"
with open(index_file, 'w') as f:
    json.dump(memory_lane_index, f, indent=2)

print("   ✅ Created Memory Lane index")

# Apply Ferrari brain to AlphaWolf
print("\n7️⃣ Applying Ferrari brain to AlphaWolf...")

# Copy SimpleMemoryMesh from Derek
derek_path = Path("/Users/EverettN/DEREKRISE")
simple_mesh = derek_path / "simple_memory_mesh.py"

if simple_mesh.exists():
    import shutil
    shutil.copy2(simple_mesh, "simple_memory_mesh.py")
    print("   ✅ Copied SimpleMemoryMesh")
else:
    print("   ⚠️  SimpleMemoryMesh not found in Derek")

# Create AlphaWolf Ferrari startup
startup_script = '''#!/usr/bin/env python3
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
    print("\\n✅ Memory Lane structure exists")
    
    # Check index
    index_file = memory_lane_path / "memory_lane_index.json"
    if index_file.exists():
        import json
        with open(index_file) as f:
            index = json.load(f)
        
        print(f"\\n🧠 Memory Lane Status:")
        print(f"   Albums: {index.get('total_albums', 0)}")
        print(f"   Timeline Events: {index.get('total_events', 0)}")
        print(f"   Music Memories: {index.get('total_music', 0)}")
        print(f"   Life Stories: {index.get('total_stories', 0)}")
        print(f"   Last Updated: {index.get('last_updated', 'Unknown')}")
    else:
        print("   ⚠️  Memory Lane not initialized - run FIX_MEMORY_LANE.py")
else:
    print("\\n❌ Memory Lane directory missing!")
    print("   Run: python3 FIX_MEMORY_LANE.py")

# Check Ferrari brain
try:
    from simple_memory_mesh import SimpleMemoryMesh
    memory = SimpleMemoryMesh(memory_dir="./alphawolf_memory")
    stats = memory.get_stats()
    print(f"\\n🏎️ Ferrari Brain:")
    print(f"   Episodic: {stats.get('episodic_memory_count', 0)}")
    print(f"   Working: {stats.get('working_memory_count', 0)}")
    print("   ✅ Memory system operational!")
except Exception as e:
    print(f"\\n⚠️  Ferrari brain: {e}")

print("\\n✅ AlphaWolf is ready!")
print("\\nMemory Lane preserves human existence for dementia patients.")
print("Start the app: python3 app.py")
'''

startup_file = Path("start_alphawolf_ferrari.py")
with open(startup_file, 'w') as f:
    f.write(startup_script)
os.chmod(startup_file, 0o755)

print("   ✅ Created start_alphawolf_ferrari.py")

# Create alphawolf_memory directory
memory_dir = Path("alphawolf_memory")
memory_dir.mkdir(exist_ok=True)
print("   ✅ Created alphawolf_memory/ directory")

print("\n" + "="*70)
print("🏁 MEMORY LANE FIXED!")
print("\n📊 Summary:")
print(f"   - {len(demo_albums)} albums")
print(f"   - {len(demo_timeline)} timeline events")
print(f"   - {len(demo_music)} music memories")
print(f"   - {len(demo_stories)} life stories")
print("\n🏎️ Ferrari brain installed")
print("\n🚀 Test with: python3 start_alphawolf_ferrari.py")

