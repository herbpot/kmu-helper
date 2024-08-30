import sys
e = 0
answer = ''
while e != 3:
    num = input()
    if not num.replace('-','').isdigit() or len(num) > 20:
        e += 1
        continue
    for i,v in enumerate(num[:: -1]):
        if i % 3 == 0 and i != 0:
            answer += ','
        answer += v
    print(answer[::-1])
    sys.exit()
print('error')