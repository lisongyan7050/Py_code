import os

slef=""
PartyA=""
with open('self.txt', encoding='utf-8') as file_obj:
    slef = file_obj.read().strip()

with open('PartyA.txt', encoding='utf-8') as file_obj:
    PartyA = file_obj.read().strip()

self=slef.splitlines()
PartyA=PartyA.splitlines()

for name in self:
    if name not in PartyA:
        with open('result.txt','a+') as f:
            f.writelines(name+'\n')



