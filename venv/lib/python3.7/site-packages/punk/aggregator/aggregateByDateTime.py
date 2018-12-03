import pandas as pd
import numpy as np
from typing import List, NamedTuple

from .timeseries import agg_by_date
from primitive_interfaces.base import PrimitiveBase

Inputs = pd.DataFrame
Outputs = np.ndarray
Params = dict
CallMetadata = dict

class AggregateByDateTime(PrimitiveBase[Inputs, Outputs, Params]):
    __author__ = 'distil'
    __metadata__ = {
        "id": "0a67edef-d032-37b7-b88c-792f567177e9",
        "name": "punk.aggregator.aggregateByDateTime.AggregateByDateTime",
        "common_name": "DatetimeAggregation",
        "description": "Arbitrary groupby aggregations over intervals of time",
        "languages": [
            "python3.6"
        ],
        "library": "punk",
        "version": "1.1.1",
        "source_code": "https://github.com/NewKnowledge/punk/blob/dev/punk/aggregator/aggregateByDateTime.py",
        "is_class": True,
        "algorithm_type": [                                                         
            "aggregation"                                              
        ],
        "task_type": [
            "data cleaning"                                              
        ],
        "output_type": [
            "features"
        ], 
        "team": "distil",
        "schema_version": 1.0,
        "build": [
            {
                "type": "pip",
                "package": "punk"
            }
        ],
        "compute_resources": {
            "sample_size": [
                1000.0, 
                10.0
            ],
            "sample_unit": [
                "MB"
            ],
            "num_nodes": [
                1
            ],
            "cores_per_node": [
                1
            ],
            "gpus_per_node": [
                0
            ],
            "mem_per_node": [
                1.0
            ],
            "disk_per_node": [
                1.0
            ],
            "mem_per_gpu": [
                0.0
            ],
            "expected_running_time": [
                5.0
            ]
        }
    }


    def __init__(self):
        pass

    def get_params(self) -> Params:
        return {}

    def set_params(self, params: Params) -> None:
        self.params = params

    def get_call_metadata(self) -> CallMetadata:
        return {}

    def fit(self) -> None:
        pass

    def produce(self, inputs: Inputs, datetime: List[str] = None, values: List[str] = [], 
                interval: str = None, aggregation: str = 'mean') -> Outputs:
        return agg_by_date(inputs, datetime, values, interval=interval, agg=aggregation)