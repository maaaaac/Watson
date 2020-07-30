
b = 'bravo'
for h in b:
    if h == 'b':
        #print('hohoho')
        b = b.replace('b', 'h')

s = [['fjasdf'], ['jjj'], ['kkk']]
count = 0
while count < len(s):
    s[(count)] = "".join(s[(count)])
    count += 1
#print(s)
y = '1234'
x = 'jjjj3jjj'

m = False
for i in y:
    z = i in x
    if z == True:
        m = True

print(m)



m = False
nums = '1234'

hhh = 1
if m == True:
    hhh = 2
elif nums == '1':
    hhh = 2
