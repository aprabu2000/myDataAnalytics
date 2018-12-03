from typing import List, Tuple
import logging
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.feature_selection import RFE
from sklearn.preprocessing import normalize
import pandas as pd

class RFFeatures():
    def rank_features(self, inputs: pd.DataFrame, targets: pd.DataFrame, problem_type='classification') -> pd.DataFrame:
        """ Rank features using Random Forest classifier and the recursive feature elimination

        """
        try:

            X = normalize( \
                                inputs.apply(pd.to_numeric, errors='coerce') \
                                .applymap(lambda x: 0.0 if np.isnan(x) else x) \
                                .values, axis=0)
            y = targets.iloc[:,0].values
            original_columns = list(inputs)
            print(original_columns)

            if problem_type == 'classification':
                predictor = RandomForestClassifier()
            else:
                predictor = RandomForestRegressor()

            rfe = RFE(predictor, n_features_to_select=1)
            rfe = rfe.fit(X, y)
            
            best_features = [original_columns[i-1] for i in rfe.ranking_]

        except:
            logging.exception("Failed")
            # If any error occurs, just return indices in original order
            # In the future we should consider a better error handling strategy
            best_features = [i for i in range(inputs.shape[1])]

        return best_features


if __name__ == '__main__':
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': [2.0, 3.0, 2.0]})
    inputs = pd.DataFrame(np.random.rand(10000,10))
    inputs[1] = inputs[1].apply(lambda x: x * 10.0)
    inputs[5] = inputs[5].apply(lambda x: 'blarg')
    targets = pd.DataFrame(random.choices([True, False], k=10000))
    f = RFFeatures()
    print(f.rank_features(inputs, targets))
