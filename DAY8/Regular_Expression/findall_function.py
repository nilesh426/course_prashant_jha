import re
mtch = re.findall("[^a-zA-Z0-9]","abcdefghijk5j9gd8$@94&*")
mtch1 = re.findall("[abc]","abcdefghijk5j9gd8$@94&*")
print(mtch)
print(mtch1)