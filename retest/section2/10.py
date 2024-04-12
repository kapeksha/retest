#10.Validate password using regular expression:

import re

password = "Abcd12@34"
pattern=r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!#?&]).*$'
expre= re.compile(pattern)
if expre.match(password):
    print("Password is valid.")
else:
    print("Password is invalid.")