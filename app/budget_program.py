import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime

# Processing files
import re
import chardet

class YnabImportProgram():
  """
  :Date: 08-06-2022
  :Version: 0.1
  :Author: Camila Martinez <kamynz16@gmail.com>
  """

  def __init__(self, filename: str):
    self.path_import_from_bank = data_path + export_from_bank
    self.path_to_export_csv = path_to_export_csv

  def get_list_files(self):
    files = os.listdir(data_path+export_from_bank)
    return(files)

  def get_encoding(self, filepath_complete: str):
    with open(filepath_complete, 'rb') as file:
      var_encoding = chardet.detect(file.read())['encoding']
      print(f'INFO: The encoding of file for correct importation is {var_encoding}')
    return(var_encoding)

  @staticmethod
  def process_encoding_by_file(self):
    dict_encoding_by_file = {}
    files = self.get_list_files()
    for filename in files:
      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]
      if (match1 and match2=="txt"):
        filepath_complete=str(data_path+export_from_bank+"/"+filename)
        #Use get_encoding function and filling dictionary
        dict_encoding_by_file[filename] = self.get_encoding(filepath_complete)
    return(dict_encoding_by_file)

  def rename_df_columns(self, dfcopy: pd.DataFrame):

    dfcopy = dfcopy.rename(columns={'FECHA':'Date','OFICINA':'Oficina',
                              'REFERENCIA':'Referencia','DESCRIPCIÓN':'Memo','VALOR':'Amount'})

    list_desire_columns=['Date','Oficina','Referencia','Memo','Amount']
    dfcopy_transform = dfcopy[list_desire_columns]
    print(f'PROCESS: Executing info() function')
    print(dfcopy.info())

    return(dfcopy_transform)

  def export_key_csv(self, dfcopy_transform: pd.DataFrame, filename: str, ext: str):

    max_name, min_name = str(dfcopy_transform['Date'].max().date()), str(dfcopy_transform['Date'].min().date())
    print(f'INFO: File is in range {min_name} to {max_name}')
    date_range_to_export = min_name+"_to_"+max_name
    filename_to_export = filename.split(".txt")[0]+"_pfile_"+date_range_to_export

    if(ext == ".xlsx"):
      filepath_to_export_excel = data_path+"/ImportTrials_Budget_Program/"+filename_to_export+".xlsx"
      sheet_name="_pfile_"+date_range_to_export
      print(f'INFO: Exported file is in: {filepath_to_export_excel}')
      dfcopy_transform.to_excel(filepath_to_export_excel,sheet_name=sheet_name,index=False)

    if(ext == ".csv"):
      filepath_to_export_csv = data_path+"/ImportTrials_Budget_Program/"+filename_to_export+".csv"
      print(f'INFO: Exported file is in: {filepath_to_export_csv}')
      dfcopy_transform.to_csv(filepath_to_export_csv,index=False,index_label=False)


  def process_structure_change(self):
    files = self.get_list_files()

    for filename in files:
      print(filename)

      match1 = re.search("-",str(filename))
      match2 = filename.split(".")[1]

      if match1 and match2=="txt":
        print("INFO: Has condition 1 and assumes file is tabulated")

        filepath = str(data_path+export_from_bank+"/"+filename)
        try:
          df = pd.read_csv(filepath,sep="\t",encoding="ISO-8859-1",parse_dates=["FECHA"])
          print(df.columns) #checking columns names
          print(df.nunique(axis=0)) #checking values
        except:
          print("EXCEPTION: There is a problem with the reading of the file. It can be the encoding")

        #first changing the name of corresponding columns
        dfcopy = df.copy()
        dfcopy_transform = self.rename_df_columns(dfcopy)

        #Getting range date from excel to put in export file as .csv for import in YNAB
        self.export_key_csv(dfcopy_transform,filename,".csv")

if __name__ == "__main__":

  # Running locally

  base_dir = "/content/gdrive/My Drive/Colab Notebooks/My_projects/Budget_program/"
  data_path = base_dir + "project/data/"
  export_from_bank = "Export_from_Bank"
  path_to_export_csv = "/content/gdrive/My Drive/Colab Notebooks/My_projects/Budget_program/project/data//ImportTrials_Budget_Program/"
  budget_obj = YnabImportProgram(path_to_export_csv)
  dict_encoding_by_file = budget_obj.get_encoding
  budget_obj.process_structure_change()


