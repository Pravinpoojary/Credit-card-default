import logging
import os
from datetime import datetime


log_file_name=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",log_file_name)
os.makedirs(log_path,exist_ok=True)

Log_File_Path = os.path.join(log_path,log_file_name)



logging.basicConfig(
    filename=Log_File_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)