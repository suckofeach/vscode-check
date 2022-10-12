print("welcome")

agr = input("wanna play? ")

if agr.lower() != "y":
    quit()

print('ok')
list = []

answer = input('u gay ')

if answer.lower() == 'no u':
    print('nice')
    list.append(True)
else:
    print('wrong')
    list.append(False)

answer = input('u gay 2 ')

if answer.lower() == 'no u':
    print('nice')
    list.append(True)
else:
    print('wrong')
    list.append(False)

answer = input('u gay 3 ')

if answer.lower() == 'no u':
    print('nice')
    list.append(True)
else:
    print('wrong')
    list.append(False)

score = 0
for i in list:
    if i == True:
        score += 1

print('u got %s coreects' %score)
