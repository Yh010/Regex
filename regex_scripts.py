import re

emails = '''
yash4success@gmail.com
120CH0007@nitrkl.ac.in
random@work.net

'''

pattern = re.compile(r'[a-zA-Z0-9.-+_]+@[a-zA-Z-0-9]+\.(com|net|ac.in)')
matches = pattern.finditer(emails)

for match in matches :
    print(match)