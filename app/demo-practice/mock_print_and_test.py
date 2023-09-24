#defining a mock function for this exercise
def greet(name: str) -> str:
  print("Hello",name)

#from unittes library you can import mock and use patch if necessary
from unittest.mock import patch

@patch('builtins.print')
def test_greet(mock_print):
  #ok, test
  greet('Andres')
  mock_print.assert_called_with('Hello','Andres')

  #calling function for test
  greet('Camila')
  #using mockprint from unnittest module
  mock_print.assert_called_with('Hello','Camila')

  #calling function for test, Not OK
  # greet('CamilaX')
  # #using mockprint from unnittest module
  # mock_print.assert_called_with('Hello','Camila')

  #using this to check test, all the test that were run
  import sys
  #print("Last assert call")
  sys.stdout.write(str(mock_print.call_args)+"\n")
  #print("All assert call")
  sys.stdout.write(str(mock_print.call_args_list)+"\n")

test_greet()
