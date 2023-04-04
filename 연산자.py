from itertools import permutations

N = int(input())
num = list(map(int, input().split(' ')))
operator = ['+', '-', '*', '//']
operator_cnt = list(map(int, input().split(' ')))
op = []
for x, y in zip(operator, operator_cnt):
    op.extend([x]*y)


final = []

for i in set(list(permutations(op, len(op)))):

    value = num[0]
    

    for a, b in zip(num[1:], i):
        if b == '//':
            if value < 0:
                value = -(abs(value)//a)
            else:
                value = value//a
        else:
            value = eval(str(value) + b + str(a))
	
    final.append(value)
    
print(max(final))
print(min(final))