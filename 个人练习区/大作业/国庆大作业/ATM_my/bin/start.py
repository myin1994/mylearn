import sys
import os
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,base_path)
from core import src

src.run()