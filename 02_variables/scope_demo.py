# Write a Python program that demonstrates the use of:
# global
# nonlocal
# Modify a global counter and an enclosing function variable inside nested functions.
# Observe how the values change across multiple function calls.


# global counter.
counter = 6 

def outer_func():
    # enclosing variable.
    num = 6  

    def inner_func():
        # access global variable.
        global counter
        # access enclosing variable.  
        nonlocal num  

        counter += 2  # update global counter.
        num += 4  # update enclosing variable.

        print(f"counter = {counter}, num = {num}")  # display values.
    # return nested function.
    return inner_func  

# create first closure.
f1 = outer_func()  
f1()  # first call.
f1()  # second call

# create second closure.
f2 = outer_func()  
f2()  # first call of second closure.
f2()  # second call of second closure.