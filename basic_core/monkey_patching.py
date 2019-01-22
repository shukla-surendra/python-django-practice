class MonkeyTest:
   def get_square(self, number):
       return number**2

# monkey patching to get a cube
def get_cube(self, number):
    return number**3
MonkeyTest.get_square = get_cube
object = MonkeyTest()
print(object.get_square(2))