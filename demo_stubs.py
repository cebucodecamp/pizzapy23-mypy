import demo_stubs_lib

# demo_stubs.py:6: error: Incompatible types in assignment (expression has type "float", variable has type "str")
# demo_stubs.py:6: error: Argument 1 to "f" has incompatible type "int"; expected "str"
l: str
l = demo_stubs_lib.f(8)

# demo_stubs.py:9: error: Incompatible types in assignment (expression has type "int", variable has type "str")
demo_stubs_lib.version = 8
