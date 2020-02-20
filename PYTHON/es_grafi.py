nodi = input("inserisci il numero di nodi")

m = [[]]
provvisorio = []

for i in range(int(nodi)):
    arco = input(f"a quali altri nodi è collegato il nodo {i}")
    archi = arco.split(",")
    for k in range(int(nodi)):
        if (archi[k] == nodi[k]):
            provvisorio.append(1)
        else: 
            provvisorio.append(0)
    m.append(provvisorio)

print(m)