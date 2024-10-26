#!/bin/bash

# Activate the virtual environment
source "/Users/songye03/Desktop/me/.venv/bin/activate"

# Run the Python script
python "/Users/songye03/Desktop/me/_site/travelmap.py"

# Navigate to the project directory
cd "/Users/songye03/Desktop/me"

# Add changes to Git, commit, and push
git add .
git commit -m "update travelmap"
git push
