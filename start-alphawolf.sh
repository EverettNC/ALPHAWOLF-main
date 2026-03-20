#!/bin/bash

# 🐺 AlphaWolf - The Christman AI Project
# Launcher script for AlphaWolf AI ecosystem

echo "🐺 Starting AlphaWolf AI - Neurodivergent Support Platform"
echo "Part of The Christman AI Project"
echo ""

# Navigate to AlphaWolf directory
cd "/Users/EverettN/ALPHAWOLF-main"

# Load environment variables
if [ -f .env ]; then
    echo "✅ Loading environment configuration..."
    export $(cat .env | xargs)
else
    echo "⚠️  .env file not found - using default settings"
fi

# Check Python dependencies
echo "🔍 Checking dependencies..."
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 available"
else
    echo "❌ Python 3 not found - please install Python"
    exit 1
fi

# Start AlphaWolf
echo "🚀 Launching AlphaWolf on port 8000..."
echo "🌐 Access at: http://localhost:8000"
echo ""

# Start the Flask application
python3 main.py