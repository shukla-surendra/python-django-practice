'''
startswith
endswith
split
join
'''

text = "Python is easy to learn."
result = text.startswith('is easy')
# returns False
print(result)
result = text.startswith('Python is ')
# returns True
print(result)
result = text.startswith('Python is easy to learn.')
# returns True
print(result)
result = text.endswith('to learn.')
print("Ends with", result)
# split/join
exploded_list = text.split(" ") # return list
print(exploded_list)
joined_string = " ".join(exploded_list)
print(joined_string)
