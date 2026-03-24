import os
import sys

# Get project root path (resilient-api/)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add root path to PYTHONPATH
sys.path.insert(0, ROOT_DIR)