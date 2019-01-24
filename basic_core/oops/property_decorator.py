# Python program to explain property() function.
# In Python, the main purpose of Property() function is to create property of a class. 
  
# Alphabet class 
class Alphabet: 
    def __init__(self, value): 
        self._value = value 
          
    # getting the values 
    def getValue(self): 
        print('Getting value') 
        return self._value 
          
    # setting the values 
    def setValue(self, value): 
        print('Setting value to ' + value) 
        self._value = value 
          
    # deleting the values 
    def delValue(self): 
        print('Deleting value') 
        del self._value 
      
    value = property(getValue, setValue, delValue, ) 
  
# passing the value 
x = Alphabet('GeeksforGeeks') 
print(x.value) 
x.value = 'GfG'
del x.value 
# Python program to explain property() 
# function using decorator 
  
class AlphabetUsingDecorator: 
    def __init__(self, value): 
        self._value = value 
          
    # getting the values     
    @property
    def value(self): 
        print('Getting value') 
        return self._value 
          
    # setting the values     
    @value.setter 
    def value(self, value): 
        print('Setting value to ' + value) 
        self._value = value 
          
    # deleting the values 
    @value.deleter 
    def value(self): 
        print('Deleting value') 
        del self._value 
  
  
# passing the value 
x = AlphabetUsingDecorator('Peter') 
print(x.value)   
x.value = 'Diesel' 
del x.value 