import numpy as np
import pandas as pd
from datetime import datetime

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    if type(string) == datetime:
        return str(string)
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def date_from_timestamp(d):
    try:
        return datetime.fromtimestamp(int(d))
    except:
        return None


def header_cleaner(string):
    header = strip_non_ascii(string)
    header = header.replace('\n','').replace('\t','').replace('\r','')
    return header


def number_cleaner(x,force=False):
    try:
        x_str = str(x).strip()
    except:
        return np.nan

    if x_str == str('nan'):
        if force:
            return 0.0
        else:
            return np.nan

    x_str = ''.join([c for c in str(x) if c == '.' or c.isdigit() or c == '-' or c == 'e'])
    if not x_str:
        if force:
            return 0.0
        else:
            return np.nan

    try:
        return float(x_str) 
    except:
        return np.nan


def string_cleaner(x):
    if isinstance(x, str):
        return x
    else:
        return str(x)
