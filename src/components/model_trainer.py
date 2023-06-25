import os, sys
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj
from src.utils import model_evaluation

from dataclasses import dataclass


@ dataclass
class modeltrainerconfig:
    train_model_path=os.path.join("artifacts","model.pkl")


class model_trainer:
    def __init__(self):
        self.model_trainer_config=modeltrainerconfig()
    
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("splitting independent and dependent variables from train test")

            X_train,y_train,X_test,y_test= (train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])
        
            models={
                "Logistic_Regression":LogisticRegression(),
                "Random_Forest":RandomForestClassifier(),
                "XG_Boost":xgb.XGBClassifier(),
                "Decision_Tree":DecisionTreeClassifier(),   
                "KNN":KNeighborsClassifier()
                }

            model_report:dict=model_evaluation(X_train,X_test,y_train,y_test,models)
            print("n/===============================================================")
            logging.info(f"Model report : {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            print(f"Best model name: {best_model_name} and Best model score is {best_model_score}")


            save_obj(
                file_path=self.model_trainer_config.train_model_path,
                obj=best_model

            )

     

        except Exception as e:
            logging.info("error occured during model trainer")
            raise CustomException(e,sys)








