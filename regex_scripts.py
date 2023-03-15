import re

emails = '''
yash4success@gmail.com
120CH0007@nitrkl.ac.in
random@work.net

'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
names = '''
Mr. Yash
Mr. Yasg
Mr Yashi
Mr. Yashu
'''

#pattern = re.compile(r'[a-zA-Z0-9.-+_]+@[a-zA-Z-0-9]+\.(com|net|ac.in)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#matches = pattern.finditer(emails)
matches = pattern.finditer(urls)

for match in matches :
    print(match.group(3))


sentence = 'Start a sentence and then bring it to an end'
patterns = re.compile(r'sentence')
matches1 = patterns.search(sentence)
print(matches1)