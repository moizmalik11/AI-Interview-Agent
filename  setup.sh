#!/bin/bash

# Step 1: Check Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Please install Python 3 first."
    exit
fi

echo "✅ Python3 found: $(python3 --version)"

# Step 2: Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Step 3: Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Step 4: Install requirements
if [ -f "requirements.txt" ]; then
    echo "📥 Installing packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found. Skipping package install."
fi

# Step 5: Deactivate venv
echo "🛑 Deactivating virtual environment..."
deactivate

# Step 6: Instructions
echo ""
echo "✅ Setup complete!"
echo "👉 To run the app:"
echo "   source venv/bin/activate"
echo "   python app.py"
