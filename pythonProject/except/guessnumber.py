import random,sys
def continuee(flag):
    if flag.lower()=='n':
        sys.exit()

while True:
    guess = ''

    while guess not in ('big', 'little'):
        guess = input("输入 your guess ,big or litte\n")

    if guess == 'big':
        guessnum = 1
    else:
        guessnum = 0

    toss = random.randint(0, 1)
    if toss == guessnum:
        print('you achieve win')
        flag = input('要继续吗 y/n\n')
        continuee(flag)
    else:
        print('你失败了')