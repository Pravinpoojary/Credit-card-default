from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
import os,sys
import pickle

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import save_obj

@dataclass
class Data_transformation_config:
    preprocessor_path = os.path.join("artifacts","preprocessor.pkl")

class Data_transformation():
    def __init__(self):
        self.data_preprocessor_path=Data_transformation_config()

    def get_preprocessor_obj(self):

        try:
            logging.info("data preprocessing started")
            col=['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE',
                  'AGE', 'PAY_0', 'PAY_2','PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
                  'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
                  'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']


            Num_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy="median")),
                ('Scaler',StandardScaler())
                ])

            preprocessor=ColumnTransformer([
                ("num_pipeline",Num_pipeline,col)
                ])
            
            return preprocessor
        
        except Exception as e:
            logging.info("error during data preprocessing")
            raise CustomException(e,sys)
        
        
    def initiate_data_tranformation(self,train_path,test_path):
        logging.info("data tranformation intiated")

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("train test data loaded")
            logging.info(f"train data set head : \n {train_df.head().to_string()}")
            logging.info(f"test data set head : \n {test_df.head().to_string()}")
            logging.info("preprocessing object created")

            preprocessing_obj =self.get_preprocessor_obj()

            # dividing dependent independent data
            x_train_df=train_df.drop(['default payment next month'],axis=1)
            y_train_df=train_df['default payment next month']

            x_test_df=test_df.drop(['default payment next month'],axis=1)
            y_test_df=test_df['default payment next month']

            x_train_df_arr = preprocessing_obj.fit_transform(x_train_df)
            x_test_df_arr = preprocessing_obj.transform(x_test_df)

            train_arr=np.c_[x_train_df_arr,y_train_df]
            test_arr=np.c_[x_test_df_arr,y_test_df]

            logging.info("preprocessing done")
            save_obj(
                file_path=self.data_preprocessor_path.preprocessor_path,
                obj=preprocessing_obj
            )
            

            return (
                train_arr,test_arr,self.data_preprocessor_path.preprocessor_path

            )
            
                
        except Exception as e:
            logging.info("error occured during tranformation")
            raise CustomException(e,sys)
        



    





