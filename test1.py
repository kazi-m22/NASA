import numpy as np
import pandas as pd
import datetime
import urllib

from bokeh.plotting import *
from bokeh.models import HoverTool
from collections import OrderedDict

query = ("https://data.nasa.gov/resource/fh5h-mx94.json")
raw_data = pd.read_json(query)
print(raw_data)