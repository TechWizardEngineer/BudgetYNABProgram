import os
import sys
import root
from utils.budget_import import YnabImportProgram
from typing import List, Dict

import pytest

@pytest.fixture
def budget_import():
  return YnabImportProgram(root.DIR_DATA_RAW_TEST,root.DIR_DATA_ANALYTICS_TEST)

def test_constructor():
  budget_import = YnabImportProgram(path_data=root.DIR_DATA_RAW_TEST,
                                 path_export=root.DIR_DATA_ANALYTICS_TEST)

  #asserting instance
  assert isinstance(budget_import,YnabImportProgram)

  #asserting correct path
  assert budget_import._path_data==root.DIR_DATA_RAW_TEST,f'path_data=={root.DIR_DATA_RAW_TEST} expected, got: {budget_import._path_data}'
  assert budget_import._path_export==root.DIR_DATA_ANALYTICS_TEST,f'path_data=={root.DIR_DATA_ANALYTICS_TEST} expected, got: {budget_import._path_export}'

def test_get_list_files(budget_import):
  set_files = budget_import.get_list_files()
  #print(f'\nMaking isintance(f,str) asserts in loop')
  for f in set_files:
    #print(f)
    assert isinstance(f,str), f'f must be instance of "str" expected, got: {type(f)}'

  assert set_files == ['640-212335-18_92.txt','640-212335-18_343.txt',
                       '640-212335-18_630.txt','640-212335-18_901.txt',
                       '640-212335-18_525.txt','640-212335-18_280.txt']

  assert len(set_files)==6, f'len(set_files)==6 expected, got: {len(set_files)}'

def test_get_encoding(budget_import):
  file_path_encoding = budget_import._path_data+'640-212335-18_92.txt'
  encoding = budget_import.get_encoding(file_path_encoding)

  assert encoding == "ISO-8859-1", f'enconding == "ISO-8859-1" expected, got {encoding}'

