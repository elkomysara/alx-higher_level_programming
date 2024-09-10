import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPython.so')

# Define argument types for the C function
lib.print_python_string.argtypes = [ctypes.py_object]

# Test with various strings
s = "The spoon does not exist"
lib.print_python_string(s)

s = "ложка не существует"
lib.print_python_string(s)

s = "La cuillère n'existe pas"
lib.print_python_string(s)

s = "勺子不存在"
lib.print_python_string(s)

s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)

s = "スプーンは存在しない"
lib.print_python_string(s)

# Test with invalid string object (byte string)
s = b"The spoon does not exist"
lib.print_python_string(s)
