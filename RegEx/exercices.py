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


# [cmf] -> it will only find the words starting from c, m, f. can, man and fan will match here
