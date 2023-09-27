"""
The goal of Assertions in Debugging

--Informing Developers of Unrecoverables Errors
--Not for Expected Errors
--Uncovering Programmer's Errors
--Useful During Development, Not Production

Comands to run to disable assertions of production code:

python -O
python --OO

If you are using bpython to check stuff, use:
bpython -O

#Assertions are different to Error Handling
    -To make a stable code, you should add:

    if():
        raise Error

"""

#circle_improved.py
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # This is good to use since this variable is key
    # Preconditions: radius SHOULD NOT BE negative
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("positive radius expected")
        self._radius = value

    def area(self):
        return math.pi * self.radius ** 2

    def correct_radius(self, correction_coefficient):
        self.radius *= correction_coefficient
