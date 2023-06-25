import re
regex=re.compile('saa|sss')
print(regex.findall('saa sss bbb saa sss sccsaa'))