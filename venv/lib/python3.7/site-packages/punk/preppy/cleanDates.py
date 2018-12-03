import pandas as pd
from typing import List
from datetime import datetime

from .clean_list import clean_dates

class CleanDates():
    def clean_dates(self, inputs: pd.DataFrame) -> pd.DataFrame:
        return inputs.apply(clean_dates)
