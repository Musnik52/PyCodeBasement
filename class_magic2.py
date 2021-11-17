import shelve

she = shelve.open('accounts.db')
print([she[f'{i}'] for i in she ])
i = input ('Enter id 1-4: ')
acc1 = she[f'{i}']
print(acc1)
she.close()