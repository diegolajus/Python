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
print("Ex1 -->",ex_1)

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
print("Ex2 -->",ex_2)

# 3

# MATCH TEXT hot ✔
# MATCH TEXT dog ✔
# SKIP TEXT bog  ✖

ex3="hot dog bog"
patt = re.compile(r"[hd]")
ex_3 = patt.findall(ex3)
print("Ex3 -->",ex_3)

# 4

# MATCH TEXT 	wazzzzup 	 ✓
# MATCH TEXT 	wazzzup 	 ✓
# MATCH TEXT 	wazup 		 ✓

ex4="wazup wazzzup wazzzzup"
patt = re.compile(r"waz{1,4}up")
ex_4 = patt.findall(ex4)
print("Ex4 -->",ex_4)

# 5

# MATCH TEXT 	1. abc 		✓
# MATCH TEXT 	2. abc 		✓
# MATCH TEXT 	3. abc 		✓
# SKIP TEXT 	4.abc       ✖

ex5="1. abc 2. abc 3. abc 4.abc"
patt = re.compile(r"\d\.\s+abc")
ex_5 = patt.findall(ex5)
print("Ex5 -->",ex_5)


# 6 Write a Python program that matches a string that has an a followed by one or more b's.

def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex6 i) -->",text_match("ab"))
print("Ex6 ii)-->",text_match("abc"))
print("Ex6 iii)-->",text_match("aBc"))


# 7 Write a Python program that matches a string that has an a followed by zero or more b's.

def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex7 i) -->",text_match("ab"))
print("Ex7 ii) -->",text_match("abc"))
print("Ex7 iii) -->",text_match("aBc"))


# 8 Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.

def longest_item(*args):
  return max(args, key = len)
 
print("Ex8 i) -->",longest_item('Red', 'Green', 'Black', 'Orange'))
print("Ex8 ii) -->",longest_item([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print("Ex8 iii) -->",longest_item([1, 2, 3], 'Java'))
print("Ex8 iv) -->",longest_item({10, 100}, 'Python'))


# 9 Write a Python program that matches a string that has an a followed by three 'b'.

def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex9 i) -->",text_match("abbb"))
print("Ex9 ii) -->",text_match("aabbbbbc"))



# 10 Write a Python program that matches a string that has an a followed by two to three 'b'.

def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print("Ex10 i) -->",text_match("ab"))
print("Ex10 ii) -->",text_match("aabbbbbc"))


# 11 Write a Python program that matches a string that has an a followed by two to three 'b'.

def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex11 i) -->",text_match("aab_cbbbc"))
print("Ex11 ii) -->",text_match("aab_Abbbc"))
print("Ex11 iii) -->",text_match("Aaab_abbbc"))

# 12 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print("Ex12 i) -->",text_match("AaBbGg"))
print("Ex12 ii) -->",text_match("Python"))
print("Ex12 iii) -->",text_match("python"))
print("Ex12 iv) -->",text_match("PYTHON"))
print("Ex12 v) -->",text_match("aA"))
print("Ex12 vi) -->",text_match("Aa"))


# 13 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex13 i) -->",text_match("aabbbbd"))
print("Ex13 ii) -->",text_match("aabAbbbc"))
print("Ex13 iii) -->",text_match("accddbbjjjb"))


# 14 Write a Python program that matches a word at the beginning of a string.

def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex14 i) -->",text_match("The quick brown fox jumps over the lazy dog."))
print("Ex14 ii) -->",text_match(" The quick brown fox jumps over the lazy dog."))


# 15 Write a Python program that matches a word at the end of a string, with optional punctuation.

def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex15 i) -->",text_match("The quick brown fox jumps over the lazy dog."))
print("Ex15 ii) -->",text_match("The quick brown fox jumps over the lazy dog. "))


# 16 Write a Python program that matches a word containing 'z'.

def text_match(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex16 i) -->",text_match("The quick brown fox jumps over the lazy dog."))
print("Ex16 ii) -->",text_match("Python Exercises."))



# 17 Write a Python program that matches a word containing 'z', not at the start or end of the word.

def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Ex17 i) -->",text_match("The quick brown fox jumps over the lazy dog."))
print("Ex17 ii) -->",text_match("Python Exercises."))
