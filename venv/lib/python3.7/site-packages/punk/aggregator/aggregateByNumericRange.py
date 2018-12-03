import pandas as pd
import numpy as np
from typing import List, NamedTuple

from .numeric import range_groups
from primitive_interfaces.base import PrimitiveBase

Inputs = pd.DataFrame
Outputs = np.ndarray
Params = dict
CallMetadata = dict

class AggregateByNumericRange(PrimitiveBase[Inputs, Outputs, Params]): 
    __author__ = 'distil'
    __metadata__ = {
        "id": "5ab6f38f-d57a-30a7-8919-87d9d02954f6",
        "name": "punk.aggregator.aggregateByNumericRange.AggregateByNumericRange",
        "common_name": "NumericRangeAggregation",
        "description": "Determine the best bins for value counts and perform the aggregation",
        "languages": [
            "python3.6"
        ],
        "library": "punk",
        "version": "1.1.1",
        "source_code": "https://github.com/NewKnowledge/punk/blob/dev/punk/aggregator/aggregateByNumericRange.py",
        "is_class": True,
        "interface_type": "data_cleaning",
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

    def produce(self, inputs: Inputs, values: List[str] = []) -> Outputs:
        return range_groups(inputs, values)