y = i = n = a = 0
while i < 10:
    v = int(input(f'1-Yes\n2-No\n3-Abstain\n4-Veto\nCountry #{i+1} Cast your vote: '))
    if v > 4: continue
    elif v == 4:
        print(f' Country number {i+1} voted Veto')
        break
    elif v == 1: y += 1
    elif v == 2: n += 1
    elif v == 3: a += 1
    i += 1
if i == 10: print(f'Yes: {y}, No: {n}, Abstain: {a}')