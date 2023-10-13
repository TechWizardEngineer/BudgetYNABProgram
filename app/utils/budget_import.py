import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict
import logging
import logging.config
import yaml
from utils.error_handling import WrongOsError
from utils.error_handling import macos_interaction, encoding_error
# Processing files
import re
import chardet
from pathlib import Path

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)
import root

#Logger configuration
log_config_path = "/app/logging/" +"config.yaml"

with open(log_config_path,'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

class YnabImportProgram():
  """
  :Date: 08-06-2022
  :Version: 0.1
  :Author: Camila Martinez <kamynz16@gmail.com>
  """

  def __init__(self, path_data: str,
               path_export: str):
    self._path_data = path_data
    self._path_export = path_export

  # __str__ => Easy to read representation of class (Human consumption)
  def __str__(self):
    result = """({self._path_data},{self._path_export})"""
    return(result.format(self=self))

  # __repr__ => unambigous representation of class for debugging
  def __repr__(self):
    return '{self.__class__.__name__}({self._path_data},{self._path_export})'.format(self=self)

  def verify_running_platform(self):
    try:
      macos_interaction()
    except WrongOsError:
      #print(error)
      logger.error("Exception occured", exc_info=True)
    else:
      #print("👏🏽, Now work can be done. No problem :)")
      logger.info("Now work can be done. No problem")
    finally:
      #print("🧼 Cleaning up despite any execeptions.")
      logger.debug("Cleaning up despite any execeptions.")

  def get_list_files(self) -> List[str]:
    files = os.listdir(self._path_data)
    return(files)

  def get_encoding(self, filepath_complete: str) -> str:
    with open(filepath_complete, 'rb') as file:
      var_encoding = chardet.detect(file.read())['encoding']

      #assert to debug
      assert isinstance(var_encoding,str) and var_encoding=="ISO-8859-1"

      if var_encoding != "ISO-8859-1":
        raise ValueError("EXCEPTION: Problem reading file. It can be the encoding")
    return(var_encoding)

  def process_encoding_by_file(self) -> Dict[str,str]:
    #//TODO: This function can be refactored
    dict_encoding_by_file = {}
    files = self.get_list_files()

    for filename in files:
      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]
      if (match1 and match2=="txt"):
        filepath_complete=str(self._path_data+"/"+filename)
        #Use get_encoding function and filling dictionary
        dict_encoding_by_file[filename] = self.get_encoding(filepath_complete)
        logger.info("Encoding of files was done")
    return(dict_encoding_by_file)

  def rename_df_columns(self, dfcopy: pd.DataFrame) -> pd.DataFrame:
    #//TODO: An exception can be done here
    dfcopy = dfcopy.rename(columns={'FECHA':'Date','OFICINA':'Oficina',
                              'REFERENCIA':'Referencia','DESCRIPCIÓN':'Memo',
                              'VALOR':'Amount'})

    list_desire_columns=['Date','Oficina','Referencia','Memo','Amount']

    dfcopy_transform = dfcopy[list_desire_columns]

    logger.info("Rename of colum was done")
    return(dfcopy_transform)

  def export_key_csv(self, dfcopy_transform: pd.DataFrame,
                     filename: str, ext: str = ".csv") -> str:

    max_name, min_name = str(dfcopy_transform['Date'].max().date()),str(dfcopy_transform['Date'].min().date())

    #print(f'INFO: File is in range {min_name} to {max_name}')
    logger.info(f'File is in range {min_name} to {max_name}')
    date_range_to_export = min_name+"_to_"+max_name
    filename_to_export = filename.split(".txt")[0]+"_pfile_"+date_range_to_export

    if(ext == ".xlsx"):
      filepath_to_export_excel = self._path_export+filename_to_export+".xlsx"
      sheet_name="_pfile_"+date_range_to_export
      #print(f'INFO: Exported file is in: {filepath_to_export_excel}')
      logger.info(f'Exported file is in: {filepath_to_export_excel}')
      dfcopy_transform.to_excel(filepath_to_export_excel,
                                sheet_name=sheet_name,
                                index=False)

    if(ext == ".csv"):
      filepath_to_export_csv = self._path_export+filename_to_export+".csv"
      #print(f'INFO: Exported file is in: {filepath_to_export_csv}')
      logger.info(f'Exported file is in: {filepath_to_export_csv}')
      dfcopy_transform.to_csv(filepath_to_export_csv,
                              index=False,
                              index_label=False)

    return(filename_to_export)


  def process_structure_change(self) -> Dict[str, str]:
    dict_transform = {}
    files = self.get_list_files()

    for filename in files:
      #print(filename)
      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]

      if match1 and match2=="txt":
        #print("INFO: Has condition 1 and assumes file is tabulated")
        filepath = str(self._path_data+"/"+filename)
        try:
          var_encoding = self.get_encoding(filepath)
          df = pd.read_csv(filepath,sep="\t",
                           encoding="ISO-8859-1",
                           parse_dates=["FECHA"])
        except ValueError as e:
          logger.critical(e)
        finally:
          #print("🐧 Correct reading of file with ISO encoding")
          logger.info("🐧 Correct reading of file with ISO encoding")

        #first changing the name of corresponding columns
        dfcopy = df.copy()
        dfcopy_transform = self.rename_df_columns(dfcopy)

        #Getting range date from excel to put in export file as .csv for import in YNAB
        filename_to_export = self.export_key_csv(dfcopy_transform,filename)

        #Populating Dict[str, str]
        dict_transform[filename] = filename_to_export
        logger.info("Process was done")

    return(dict_transform)


# Running locally from YnabImportProgram Class
# Running for api of FastApi, you have to comment main

# if __name__ == "__main__":
#   print(root.DIR_DATA)
#   # print(root.DIR_DATA_RAW)
#   # print(root.DIR_DATA_RAW_TEST)
#   budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
#   budget_obj.verify_running_platform()
#   #print(budget_obj)
#   #print(budget_obj.__str__)
#   #print("\n")
#   #print(budget_obj.__repr__)
#   budget_obj.process_structure_change()


