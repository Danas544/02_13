names = ["Tomass","Danielius","Jonass","Petras","Antanas"]
benras = []

for name in names:
    if len(name) > 5:
        #print(f' Pirmas {name}')
        benras.append(name)
print(f'Pirmas: {benras}')



print([name for name in names if len(name)>5])


names_com = [names_com for names_com in names if len(names_com) > 5]
print(f'Antras: {names_com}')


dicts = {key:vardas for key , vardas in enumerate(names,start=1)}
print(dicts)