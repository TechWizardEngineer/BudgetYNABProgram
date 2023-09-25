import sys
import root
from utils.budget_import import YnabImportProgram
from typing import List, Dict

import pytest

#key vars for class
#test_path_data=root.DIR_DATA_RAW_TEST
#test_path_export=root.DIR_DATA_ANALYTICS_TEST

@pytest.fixture
def budget_import():
  return YnabImportProgram(root.DIR_DATA_RAW_TEST,root.DIR_DATA_ANALYTICS_TEST)

def test_constructor():
  budget_import = YnabImportProgram(path_data=root.DIR_DATA_RAW_TEST,
                                 path_export=root.DIR_DATA_ANALYTICS_TEST)

  #asserting instance
  assert isinstance(budget_import,YnabImportProgram)

  #asserting correct path
  assert budget_import._path_data==root.DIR_DATA_RAW_TEST
  assert budget_import._path_export==root.DIR_DATA_ANALYTICS_TEST

def test_get_list_files(budget_import):
  list_files = budget_import.get_list_files()
  print(f'\nMaking asserts in loop')
  for f in list_files:
    assert isinstance(f,str)
