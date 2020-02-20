import random
nameList = ["Mario Rossi", "John Doe", "Tizio Caio"]

for num, student in enumerate(nameList):
    print(f"{num} - {student}")

print("viene interrogato oggi ohhhhhhhhhhhh... " + nameList[(random.randint(0,len(nameList)-1))] + "!!!")
