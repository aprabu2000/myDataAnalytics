import pandas as pd
from typing import List

class CleanStrings():
    def clean_strings(self, inputs: pd.DataFrame) -> pd.DataFrame:
        return inputs.applymap(str)
