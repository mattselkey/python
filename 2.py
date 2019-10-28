# 
# Example file for variables
#
f=0
print(f)

# Declare a variable and initialize it
f="abc"
print(f)


# # re-declaring the variable works
print("this is a string" + str(123))

# # ERROR: variables of different types cannot be combined
# # print("this is a string" + 123)

# Global vs. local variables in functions
p=0
def someFunction():
    global p
    p="def"
    print(p)

someFunction()
print(p)