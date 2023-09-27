"""
What do assertions check ?:

-Invariants are Invariant
-Assumptions:
  -Preconditions
  -Postconditions

Ex:
-This argument is not None
-Return value is str
"""

"""
What do assertions Good For:

-Debugging:
  -Ensure New Bugs are not added

-Documenting
-Testing

"""

"""
When Not To Use Assertions:

-Data Processing
-Data Validation
-Not an error handling. Ultima purpose of assertions is not to handle errors in
production but notify you during development, so you can fix them

OJO:
-In Python, assert is a statement NOT a function

#Split in two lines if neccesary and DO NOT USE Parenthesis

number = 42

assert number > 0 and isinstance(number,int), \
  f'number greater than 0 expected, got: {number}'

"""

def get_response(server, ports=(443, 80)):
    assert len(ports) > 0, f"ports expected a non-empty tuple, got{ports}"
    for port in ports:
        if server.connect(port):
            return server.get()
    return None

