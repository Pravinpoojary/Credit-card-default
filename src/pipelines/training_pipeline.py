import pandas as pd
import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.components.data_tranformation import Data_transformation
from src.components.model_trainer import model_trainer


from src.components.data_ingestion import Data_Ingestion

if __name__=='__main__':
    obj=Data_Ingestion()
    train_data_path,test_data_path = obj.Intiate_Data_Ingestion()
    print(train_data_path,test_data_path)
    data_transformation=Data_transformation()
    train_arr,test_arr,obj_path=data_transformation.initiate_data_tranformation(train_path=train_data_path,test_path=test_data_path)

    Model_trainer=model_trainer()
    
    Model_trainer.initiate_model_training(train_arr,test_arr)

