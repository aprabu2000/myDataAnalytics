import numpy as np
import logging
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from datetime import datetime

class PCAFeatures():
    def rank_features(self, inputs: pd.DataFrame) -> pd.DataFrame:
        """ Perform PCA and return a list of the indices of the most important
        features, ordered by contribution to first PCA component
                                                                                
        The matrix M will correspond to the absolute value of the components of 
        the decomposiiton thus giving a matrix where each column corresponds to 
        a principal component and rows are the components that rescale each 
        feature.  
                                                                                
        For example, pca.components_.T could look like this:                        
                                                                                
        array([[ 0.52237162,  0.37231836, -0.72101681, -0.26199559],                
            [-0.26335492,  0.92555649,  0.24203288,  0.12413481],                 
            [ 0.58125401,  0.02109478,  0.14089226,  0.80115427],                 
            [ 0.56561105,  0.06541577,  0.6338014 , -0.52354627]])                
                                                                                
        So the most important feature with respect to the first principal 
        component would be the 3rd feature as this has an absolute value of 
        0.58125401 which is greater than all the entries in that column.                             
                                                                                
                                                                                
        "importance_on1stpc" corresponds to the indices of most important       
        features for the first principal. Component are in ascending order      
        (most important feature 0, least important feature n_features-1).       
                                                                                
        
        Params 
        ------- 
        data : np.ndarray, [n_samples, n_features]
            Training data.
        """

        pca = PCA()

        try:
            pca.fit(normalize( \
                            inputs.apply(pd.to_numeric, errors='coerce') \
                            .applymap(lambda x: 0.0 if np.isnan(x) else x) \
                            .values, axis=0))

            importance_on1stpc= np.argsort( \
                                np.absolute( \
                                pca.components_[0,:]))[::-1]

            scores = [np.absolute(pca.components_[0,i]) for i in importance_on1stpc]
        except:
            logging.exception("Failed")
            # If any error occurs, just return indices in original order
            # In the future we should consider a better error handling strategy
            importance_on1stpc = [i for i in range(inputs.shape[0])]
            scores = [0.0 for i in importance_on1stpc]

        return pd.DataFrame({'features': importance_on1stpc, 'scores': scores})


if __name__ == '__main__':
    f = PCAFeatures()
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': [2.0, 3.0, 2.0]})
    inputs = pd.DataFrame(np.random.rand(1000000,10))
    inputs[1] = inputs[1].apply(lambda x: x * 10.0)
    inputs[5] = inputs[5].apply(lambda x: 'blarg')
    print(f.rank_features(inputs))
