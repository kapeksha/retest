#20.

import re
pattern=r'\b\d{3}\b'
text="123 4567 890 12 3456"
result=re.findall(pattern,text)
print(result)

Ans: ['123', '890']