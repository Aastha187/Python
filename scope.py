
x=20
def outer_function(x):
    print(f"value of x in outer function {x}")
    x=30
    print(f"value of x in outer function after modification {x}")
    def inner_function():
        x=40
        print(x)
    inner_function()
outer_function(x)
	
print(x)
print(f"value of x in global scope before function execution {x}")
