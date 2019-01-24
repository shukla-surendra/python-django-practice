my_global_var = "GLOBAL_DATA_121"
def local_function():
    first_number = 10
    second_number = 20
    print(first_number, second_number)
    print("Locals", locals())
local_function()
print(globals())


# Python3 program to demonstrate global() function 
  
# global variable 
a = 5
  
def func(): 
    c = 10
    d = c + a 
      
    # Calling globals() 
    globals()['a'] = d 
    print(d, a) 
      
# Driver Code     
func()

# Python3 program to demonstrate global() function 
  
# global variable 
name = 'gautam'
  
print('Before modification:', name) 
  
# Calling global() 
globals()['name'] = 'gautam karakoti'
print('After modification:', name) 