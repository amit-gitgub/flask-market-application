import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal', s)

print(match.group(0))
