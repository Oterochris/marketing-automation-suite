# This file enables pytest to find the package
import sys
from pathlib import Path

root = Path(__file__).parent
sys.path.insert(0, str(root))