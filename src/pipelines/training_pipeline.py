import pandas as pd
import os
import sys

from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import Data_Ingestion

if __name__=='__main__':
    obj=Data_Ingestion()
    train_data_path,test_data_path = obj.Intiate_Data_Ingestion()
    print(train_data_path,test_data_path)
