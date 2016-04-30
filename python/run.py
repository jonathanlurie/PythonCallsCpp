# this can be useful:
# http://starship.python.net/crew/theller/ctypes/tutorial.html

import os

import ctypes

'''
from ctypes import cdll # allow loading a dylib
from ctypes import c_char # type corresponding to C's char
from ctypes import c_char_p # type corresponding to C's char*
from ctypes import c_int # type corresponding to C's int
from ctypes import c_float # type corresponding to C's float
from ctypes import byref # allow calling a c_type by reference
from ctypes import POINTER # allow declaring a pointer (on a c_type) as argument
'''

if __name__ == '__main__':

    # getting the dylib relative path
    dylib_path = os.path.join(os.path.dirname(__file__),  "../cpp/bin/release/mydylib.so")

    # loading the dynamic library into a Python object:
    cpp_dylib = ctypes.cdll.LoadLibrary(dylib_path)


    # FIRST CASE **************************************************************
    # parameter: string (char*)
    # return type: string (const char*)

    # Loading the "greeting" function into a Python object:
    mydylib_greetings = cpp_dylib.greetings

    # defining the argument types
    mydylib_greetings.argtypes = [ctypes.c_char_p]

    # Define the return type of the greetings object
    mydylib_greetings.restype = ctypes.c_char_p


    # Calling "greetings"
    myGreetings = mydylib_greetings("Johnny Bravo")
    print(myGreetings)


    # SECOND CASE *************************************************************
    # parameters: float
    # return type: float

    # Loading the "add" function into a Python object
    mydylib_add = cpp_dylib.add

    # defining the argument types
    mydylib_add.argtypes = [ctypes.c_float, ctypes.c_float]

    # Define the return type of the greetings object
    mydylib_add.restype = ctypes.c_float

    # Calling it
    result = mydylib_add(120.4, 23.9)
    print("result: " + str(result))


    # THIRD CASE **************************************************************

    mydylib_multiply = cpp_dylib.multiply

    # defining the argument types
    mydylib_multiply.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_float)]

    # the result is a pointer on float (in the c++ part)
    # thus, here it must be a c_float (and not a Python regular float)
    resultMultiply = ctypes.c_float()
    mydylib_multiply(1.5, 4.5, ctypes.byref(resultMultiply))
    print(resultMultiply.value)
