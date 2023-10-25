with open('Государство.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
print ("\t НАЗВАНИЕ \t СТОЛИЦА \t\t ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ \t\t\t\t ПЛОЩАДЬ \n")
for line in lines:
    parts = line.split('; ')
    if len(parts) == 4:
        name, capital, population, area = parts
        population = int(population)
        area = float(area)

        if population > 1000000:
            print(f"\t {name} \t {capital} \t\t\t {population} чел. \t\t\t\t {area} км² \n")
