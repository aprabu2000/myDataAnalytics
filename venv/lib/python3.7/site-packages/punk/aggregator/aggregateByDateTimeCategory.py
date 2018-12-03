import pandas as pd
from typing import List, NamedTuple

from .timeseries import agg_by_category_by_date
from primitive_interfaces.base import PrimitiveBase

class AggregateByDateTimeCategory(PrimitiveBase[pd.DataFrame, List[str]]):
    __author__ = 'distil'

    def __init__(self):
        pass

    def get_params(self) -> dict:
        return {}

    def set_params(self, params: dict) -> None:
        self.params = params

    def get_call_metadata(self) -> {}: 
        return {}

    def fit(self):
        pass

    def produce(self, inputs: pd.DataFrame, values: List[str] = [], groupby : List[str] = [],
                datetime=None, intervals=None, aggregation=None):
        return agg_by_category_by_date(inputs, datetime, values, groupby, interval=intervals, 
                            agg=aggregation)
