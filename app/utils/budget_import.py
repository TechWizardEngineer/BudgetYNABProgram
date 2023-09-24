import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)

import root

# Processing files
import re
import chardet

#Make a table with files info by date


class YnabImportProgram():
  """
  :Date: 08-06-2022
  :Version: 0.1
  :Author: Camila Martinez <kamynz16@gmail.com>
  """

  def __init__(self, path_data: str,
               path_export: str):
    self.path_data = path_data
    self.path_export = path_export

  def get_list_files(self) -> List[str]:
    files = os.listdir(self.path_data)
    return(files)

  def get_encoding(self, filepath_complete: str) -> str:
    with open(filepath_complete, 'rb') as file:
      var_encoding = chardet.detect(file.read())['encoding']
      print(f'INFO: The encoding of file for correct importation is {var_encoding}')
    return(var_encoding)

  def process_encoding_by_file(self) -> Dict[str,str]:
    dict_encoding_by_file = {}
    files = self.get_list_files()
    for filename in files:
      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]
      if (match1 and match2=="txt"):
        filepath_complete=str(self.path_data+"/"+filename)
        #Use get_encoding function and filling dictionary
        dict_encoding_by_file[filename] = self.get_encoding(filepath_complete)
    return(dict_encoding_by_file)

  def rename_df_columns(self, dfcopy: pd.DataFrame) -> pd.DataFrame:

    dfcopy = dfcopy.rename(columns={'FECHA':'Date','OFICINA':'Oficina',
                              'REFERENCIA':'Referencia','DESCRIPCIÓN':'Memo','VALOR':'Amount'})

    list_desire_columns=['Date','Oficina','Referencia','Memo','Amount']
    dfcopy_transform = dfcopy[list_desire_columns]
    mssg=f'PROCESS: Executing info() function'
    print(mssg)
    #print(dfcopy_transform.info())

    return(dfcopy_transform)

  def export_key_csv(self, dfcopy_transform: pd.DataFrame,
                     filename: str, ext: str) -> str:

    max_name, min_name = str(dfcopy_transform['Date'].max().date()), str(dfcopy_transform['Date'].min().date())
    print(f'INFO: File is in range {min_name} to {max_name}')
    date_range_to_export = min_name+"_to_"+max_name
    filename_to_export = filename.split(".txt")[0]+"_pfile_"+date_range_to_export

    if(ext == ".xlsx"):
      filepath_to_export_excel = self.path_export+filename_to_export+".xlsx"
      sheet_name="_pfile_"+date_range_to_export
      print(f'INFO: Exported file is in: {filepath_to_export_excel}')
      dfcopy_transform.to_excel(filepath_to_export_excel,
                                sheet_name=sheet_name,
                                index=False)

    if(ext == ".csv"):
      filepath_to_export_csv = self.path_export+filename_to_export+".csv"
      print(f'INFO: Exported file is in: {filepath_to_export_csv}')
      dfcopy_transform.to_csv(filepath_to_export_csv,
                              index=False,
                              index_label=False)

    return(filename_to_export)


  def process_structure_change(self) -> Dict[str, str]:
    dict_transform = {}
    files = self.get_list_files()
    print(files)

    for filename in files:
      print(filename)

      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]

      if match1 and match2=="txt":
        print("INFO: Has condition 1 and assumes file is tabulated")

        filepath = str(self.path_data+"/"+filename)
        try:
          mssg=f"File has been reading, OK"
          df = pd.read_csv(filepath,sep="\t",encoding="ISO-8859-1",parse_dates=["FECHA"])
        except:
          mssg=f"EXCEPTION: There is a problem with the reading of the file. It can be the encoding"
          print(mssg)
        #first changing the name of corresponding columns
        dfcopy = df.copy()
        dfcopy_transform = self.rename_df_columns(dfcopy)

        #Getting range date from excel to put in export file as .csv for import in YNAB
        filename_to_export = self.export_key_csv(dfcopy_transform,filename,".csv")

        dict_transform[filename] = filename_to_export

    return(dict_transform)

# Running for api of FastApi, you have to comment main

# Running locally from YnabImportProgram Class
if __name__ == "__main__":
  print(root.DIR_DATA)
  print(root.DIR_DATA_RAW)
  budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
  budget_obj.process_structure_change()


