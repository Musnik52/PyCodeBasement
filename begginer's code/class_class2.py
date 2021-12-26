import shelve

she = shelve.open('grades.db')
print([she[f'{i}'] for i in she ])
i = input ('Enter id 1-4: ')
inp = she[f'{i}']
print(inp)
she.close()