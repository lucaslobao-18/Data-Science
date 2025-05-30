words = ['cat', 'dog', 'elephant']
sem_cachorro = {}

for animal in words:
    if animal != 'dog':
        sem_cachorro[animal] = animal

print('lista com cachorro')

for animal in words:
    print(animal)

print('lista sem cachorro')

for animal in sem_cachorro:
    print(animal)