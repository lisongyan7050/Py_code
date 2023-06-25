import re,pyperclip
"""疯狂填词  在动词名词形容词的地方填上 设定的单词"""
# adjective=input("输入一个 形容词")
# noun=input("输入一个 名词")
# verb=input("输入一个 动词")
# noun2=input("输入第二个 名词")

toReplList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
text=pyperclip.paste()
for toReplItem in toReplList:
    repl=input("输入你要替换的单词"+toReplItem)
    regex=re.compile(toReplItem)
    text=regex.sub(repl,text)

print(text)

# adjective_regex=re.compile('ADJECTIVE|adjective')
# noun_regex=re.compile('NOUN|noun')
# verb_regex=re.compile('VERB|verb')
# text=pyperclip.paste()
# text=adjective_regex.sub(adjective,text)
# print(text)