import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)

import root

# Processing files
import re
import chardet

class YnabStatisticsProgram():
  pass
