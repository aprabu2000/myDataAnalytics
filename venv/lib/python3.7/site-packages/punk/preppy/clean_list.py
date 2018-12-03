from dateutil.parser import parse
from .utils import is_four_digit_year
from .clean_value import number_cleaner, string_cleaner, date_from_timestamp

import pandas as pd

def clean_dates(values):
    test_values = values[:100]
    if is_four_digit_year(test_values):
        return pd.to_datetime(values,format='%Y',errors='coerce')

    utc = False
    is_int = False
    for val in test_values:
        if not val:
            continue
        try:
            d = val
            if type(d) != datetime:
                d = parse(unicode(val))
            if d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None:
                utc = True
        except:
            try:
                d = date_from_timestamp(val)
                if d.year > 1900 and d.year < datetime.now().year + 5:
                    is_int = True
            except:
                continue

    if is_int:
        return [date_from_timestamp(d) for d in values]
    
    return pd.to_datetime(values, errors='coerce', utc=utc).values


def clean_coordinates(values):
    series = pd.Series(values).str.replace(')','')
    series = series.str.replace('(','')
    return series.values


def clean_numbers(values):
    series = pd.Series(values).apply(number_cleaner)
    return series.values
