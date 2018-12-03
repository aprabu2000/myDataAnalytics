import urllib
from urllib.parse import urlparse
import os
import time
import re

def is_four_digit_year(values):
    new_values = [v for v in values if v and str(v) != 'nan']
    if float(len(new_values))/len(values) > .5 and all([len(str(v)) is 4 and str(v)[0] in ['1','2'] for v in new_values]):
        return True

    return False
