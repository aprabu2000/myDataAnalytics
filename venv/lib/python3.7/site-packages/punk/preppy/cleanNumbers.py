import pandas as pd
from .clean_list import clean_numbers

class CleanNumbers():
    def clean_numbers(self, inputs: pd.DataFrame) -> pd.DataFrame:
        return inputs.apply(clean_numbers)
