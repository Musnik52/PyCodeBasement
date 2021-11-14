class person:
    pass

def create_p(id, fname, lname, address, phone):
    inp = person()
    inp.id = id
    inp.fname = fname
    inp.lname = lname
    inp.address = address
    inp.phone = phone
    return inp

muhamad = create_p(321, 'Muhamad', 'Levi', 'Rashi 15', 9723355665 )
print(muhamad.__dict__)
'''
muhamad = person()
muhamad.__dict__['id'] = 321
muhamad.__dict__['fname'] = 'Muhamad'
muhamad.__dict__['lname'] = 'Levi'
muhamad.__dict__['address'] = 'Rashi 15'
muhamad.__dict__['phone'] = 9723355665
print(muhamad.__dict__)
'''


'''
netta = person()
netta.id = 123
netta.fname = 'Netta'
netta.lname = 'Schwartznegger-Lavi'
netta.address = 'Rashi 15'
netta.phone = 97248474473
print(netta.__dict__)

plist = [netta, muhamad]
#pdict = {muhamad.id: muhamad, netta.id: netta}
pdict = {person.id: person for person in plist}
print(pdict[123].__dict__)
'''