import re
from typing import Text

# 1

# MATCH TEXT cat. ✔
# MATCH TEXT 896. ✔
# MATCH TEXT ?=+. ✔
# SKIP TEXT abc1  ✖

strings="cat. 896. ?=+. abc1"
patt = re.compile(r".+\.")
ex_1 = patt.findall(strings)
print(ex_1)
