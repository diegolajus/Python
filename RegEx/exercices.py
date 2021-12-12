import re
from typing import Text

# 1

# MATCH TEXT cat. ✔
# MATCH TEXT 896. ✔
# MATCH TEXT ?=+. ✔
# SKIP TEXT abc1  ✖

ex1="cat. 896. ?=+. abc1"
patt = re.compile(r".+\.")
ex_1 = patt.findall(ex1)
print(ex_1)

# 2

# MATCH TEXT can ✔
# MATCH TEXT man ✔
# MATCH TEXT fan ✔
# SKIP TEXT dan  ✖
# SKIP TEXT ran  ✖
# SKIP TEXT pan  ✖

ex2="can man fan dan ran pan"
patt = re.compile(r"[cmf]an")
ex_2 = patt.findall(ex2)
print(ex_2)

# 3

# MATCH TEXT hot ✔
# MATCH TEXT dog ✔
# SKIP TEXT bog  ✖

ex3="hot dog bog"
patt = re.compile(r"[hd]")
ex_3 = patt.findall(ex3)
print(ex_3)

# 4

# MATCH TEXT 	wazzzzup 	 ✓
# MATCH TEXT 	wazzzup 	 ✓
# MATCH TEXT 	wazup 		 ✓

ex4="wazup wazzzup wazzzzup"
patt = re.compile(r"waz{1,4}up")
ex_4 = patt.findall(ex4)
print(ex_4)

# 5

# MATCH TEXT 	1. abc 		✓
# MATCH TEXT 	2. abc 		✓
# MATCH TEXT 	3. abc 		✓
# SKIP TEXT 	4.abc       ✖

ex5="1. abc 2. abc 3. abc 4.abc"
patt = re.compile(r"\d\.\s+abc")
ex_5 = patt.findall(ex5)
print(ex_5)

# 6 Write a Python program that matches a string that has an a followed by one or more b's.

def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("aBc"))


# 6 Write a Python program that matches a string that has an a followed by zero or more b's.

def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("aBc"))

