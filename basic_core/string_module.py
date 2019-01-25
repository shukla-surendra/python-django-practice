import string
from string import Formatter
from string import Template

# module Constants

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'
print(string.punctuation)


# module classes
'''
Formatter

It behaves exactly same as str.format() function.
This class become useful if you want to subclass it and define your own format string syntax.

'''
formatter = Formatter()
print(formatter.format('{website}', website='JournalDev'))
print(formatter.format('{} {website}', 'Welcome to', website='JournalDev'))

# format() behaves in similar manner
print('{} {website}'.format('Welcome to', website='JournalDev'))




t = Template('$name is the $title in $company')
s = t.substitute(name='Surendra', title='Software Engineer', company='Example Corp.')
print(s)
