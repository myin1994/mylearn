import sys
import os
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from core import src
src.run()