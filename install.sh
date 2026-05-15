#!/bin/bash
# ============================================================
# install.sh — Installation script for Linux/Mac
# Nigerian AI Review Generator — Task A
# ============================================================

set -e  # Exit on any error

echo "🇳🇬 Installing Nigerian AI Review Generator..."
echo ""

# Check Python version
echo "✓ Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "  Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ -d "venv" ]; then
    echo "  Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "  Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate
echo "  Virtual environment activated"
echo ""

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "  pip upgraded"
echo ""

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt
echo "  Dependencies installed"
echo ""

# Create .env file
echo "✓ Setting up environment variables..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "  .env file created from .env.example"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your Groq API key:"
    echo "   nano .env"
    echo ""
    echo "   Replace: GROQ_API_KEY=gsk_your_actual_api_key_here_do_not_expose"
    echo "   With:    GROQ_API_KEY=gsk_YOUR_ACTUAL_KEY_HERE"
else
    echo "  .env file already exists"
fi
echo ""

# Verify installation
echo "✓ Verifying installation..."
python3 -c "from agent import run_pipeline; from personas import NIGERIAN_USERS; print('  ✓ All imports successful!')" 2>/dev/null || {
    echo "  ❌ Import verification failed"
    echo "  Make sure you've installed all dependencies"
    exit 1
}
echo ""

echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your Groq API key: nano .env"
echo "2. Run the app: python3 app.py"
echo "3. Open browser: http://127.0.0.1:7860"
echo ""
echo "For help, see SETUP.md or TROUBLESHOOTING.md"
