 ## FINDALL
#### The findall() Function returns a list containing all matches.

```py
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# Output: ['ai', 'ai']

```


## SEARCH
#### The search() Function returns a Match object if there is a match.

```py
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
# Output: The first white-space character is located in position: 3
```

## SPLIT
#### The split() Function returns a list where the string has been split at each match

```py
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
# Output: ['The', 'rain', 'in', 'Spain']

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 
# Output: ['The', 'rain in Spain']
```
