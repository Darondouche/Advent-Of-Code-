#Calories Counting
#Compter le nombre de calories totales par elfes
#Les comparer et trouver celui qui en porte le +
#Retourner ce montant 

#j'ouvre le file input en lecture depuis mon script
with open('puzzle_input', 'r') as f:
    puzzle_input = f.read()

#je sépare les données par ligne
lists = puzzle_input.splitlines()

results = []
elves = []

#je parcours toute ma liste pour trier les données
for item in lists:
    if item == '':
        #...sauf quand je trouve un espace, alors j'initie un new tableau
        results.append(elves)
        elves = []
    else:
        #je pousse les num dans un tableau...
        elves.append(item)

#print(results)
sum_food = []
all_food = 0

#pour chaque elf dans mon tableau de résultats
for elf in results:
    all_food = 0
    #pour chaque aliment chez un elf 
    for i in elf:
        #je fais la somme de tous les aliments d'un elf
        all_food = all_food + int(i) 
    #je pousse la somme dans un tableau qui contient toutes les sommes
    sum_food.append(all_food)

print(sum_food)

#je compare toutes les sommes de nourriture et je ressors la plus grande
max_food = 0
for food in sum_food:
    if food > max_food:
        max_food = food 

print (max_food)
    