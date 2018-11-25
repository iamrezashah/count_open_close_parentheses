t = '()(())((())())()'
opening_list = []
closing_list = []
if len(t) % 2 == 0:
    for i in range(len(t)):
        if t[i] == '(':
            opening_list.append(i+1)
        else:
            closing_list.append(i+1)
else:
    print('Error !')


pairs = []
z = 2 * int(len(t)/2)

for diff in range(1, z, 2):
    if len(pairs) != 0:
        for n in pairs:
            ni = n[0]
            nj = n[1]
            if ni in opening_list and nj in closing_list:
                opening_list.remove(ni)
                closing_list.remove(nj)

    if len(opening_list) != 0:
        for i in opening_list:
            for j in closing_list:
                print(i, j)
                x = j - i
                if x == diff:
                    pairs.append([i, j])
                    break
            print('--- end of j')
        print('=== end of i')


print(pairs)
