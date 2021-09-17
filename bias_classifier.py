from typing import Tuple, List
from sklearn.metrics import classification_report

class BiasClassifier:
    def __init__():
        self._model = None
        pass
    
    def fit(self, train_file_path: str):
        """Train a classifier model after reading and extracting features from 
        train_file_path.

        Args:
            train_file_path: String path to the training data as a json, you 
            may assume instances have labels.

        Returns:
            A tuple of list of document id and prediction label and 
        """
        # TODO write code to extract features from train_file_path and 
        # train the model
        return self._model
    
    def eval(self, test_file_path: str) -> Tuple[List[Dict[str, float]], classification_report]:
        """Evaluates the test data given in test_file_path after reading and
         extracting features.

        Args:
            test_file_path: String path to the test data, you may assume 
            instances have labels.

        Returns:
            A tuple of list of document id and prediction label and 
            evaluation summary in the form of sklearn classification_report.
        """
        # TODO write code to extract features from test_file_path and 
        # test the model
        pass


    def predict(self, test_file_path: str) -> List[Dict[str, float]]:
        """Evaluates the test data given in test_file_path after reading and
         extracting features.

        Args:
            test_file_path: String path to the test data, the instances do not 
            have labels.

        Returns:
            A list of document id and prediction label.
        """
        # TODO write code to extract features from test_file_path and 
        # predict the labels for the model.
        pass
