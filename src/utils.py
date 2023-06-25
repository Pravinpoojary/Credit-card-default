import sys,os,pickle
import numpy as np
import pandas as pd


from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import accuracy_score,precision_score,recall_score


def save_obj(file_path,obj):
    try:
        dir_path= os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("error while saving pickle file")
        raise CustomException(e,sys)
    


def model_evaluation(x_train,x_test,y_train,y_test,models):
    performance={}
    for i in range(len(models)):
        model=list(models.values())[i]
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        score=accuracy_score(y_test,y_pred)*100
        performance[list(models.keys())[i]]=score
        
    return performance


def load_object(pickle_path):
    try:
        with open(pickle_path,"rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info("error uccured during loading pickle file")
        raise CustomException(e,sys)
    


