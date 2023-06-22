import os 
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


# @dataclass
# class Data_Ingestion_Config:
#     train_path=os.path.join("artifacts","train.csv")
#     test_path=os.path.join("artifacts","test.csv")
#     raw_path=os.path.join("artifacts","raw.csv")

class Data_Ingestion:
    def __init__(self):
        self.train_path=os.path.join("artifacts","train.csv")
        self.test_path=os.path.join("artifacts","test.csv")
        self.raw_path=os.path.join("artifacts","raw.csv")

    def Intiate_Data_Ingestion(self):
        logging.info("Data Ingestion started")
        try:
            df=pd.read_csv(os.path.join("notebooks/data","credit_data.csv"))
            os.makedirs(os.path.dirname(self.raw_path),exist_ok=True)
            df.to_csv(self.raw_path,index=False)
            logging.info("Raw data saved and train test split started")
            
            train_set,test_set=train_test_split(df,random_state=42,test_size=0.25)
            logging.info("train test split done ")
            train_set.to_csv(self.train_path)
            test_set.to_csv(self.test_path)

            logging.info("data ingestion done ")

            return( 
                self.train_path,
                self.test_path
            )
        except Exception as e:
            logging.info("Exception occured during Data Ingestion")
            raise CustomException(e,sys)









