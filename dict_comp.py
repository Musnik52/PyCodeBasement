print ({i: i**2 for i in range(1,11)})

print({i: len(i) for i in ['I', 'Love', 'Python', 'Today']})

x = {'Jack': 38, 'John': 33, 'Michael': 48, 'Guido': 57}
print({i: j for i, j in x.items() if j%2==0})
print({i: 'below 40' if j<40 else 'above_equals_40' for i, j in x.items()})