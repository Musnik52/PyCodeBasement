x = ['world of coding','penny','python','bar','hello']
for i, word in enumerate(x):
    if len(word) < 4: break
    print(word.capitalize())