def fun(a, b):
    i = 1
    div_list = [ ]
    while i <= b:
        if a%i==0:
            if b%i==0:
                div_list.append(i)
        i += 1
    return div_list

a = int(input('please enter the small num'))
b = int(input('please enter the big num'))
print(f'The Deviders Are: {fun(a, b)}')