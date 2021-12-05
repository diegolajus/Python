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
patt = re.compile(r"[hd]an")
ex_3 = patt.findall(ex3)
print(ex_3)

# 4

# MATCH TEXT ✓
# MATCH TEXT ✓
# SKIP TEXT	✓
# SKIP TEXT	✖
# SKIP TEXT	✖

ex4="hot dog bog"
patt = re.compile(r"^a-z")
ex_4 = patt.findall(ex4)
print(ex_4)




