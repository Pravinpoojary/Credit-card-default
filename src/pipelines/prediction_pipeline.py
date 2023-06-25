import os,sys

import pandas as pd
from src.exception import CustomException
from src.logger import logging
from utils import load_object




class PredictPipeline:
    def __init__():
        pass

    def predict(self,feature):
        
        try:
            preprocessor_path=os.path.join("artificats","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(feature)

            pred=model.predict(data_scaled)

            return pred
        
        except Exception as e:
            logging.info("Error during prediction")
            raise CustomException(e,sys)   
