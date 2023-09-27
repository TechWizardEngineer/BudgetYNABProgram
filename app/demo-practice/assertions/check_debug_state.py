# demo.py

print(f"{__debug__ = }")
if __debug__:
    print("Running in Normal mode!")
else:
    print("Running in Optimized mode!")
