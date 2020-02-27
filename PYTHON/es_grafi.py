def user2Adj():
    nodi = int(input("inserisci il numero di nodi"))
    m = []

    for i in range(0,nodi):
        arco = [int(n) for n in input(f"a quali altri nodi è collegato il nodo {i}:").split(",")]
        colonne = [0 for n in range (0,nodi)]
        for k in arco:
            if (k != -1):
                colonne.append(1)
        m.append(colonne)
    return m   

def adj2Dict(m):
    dictionary = {}

    for n in len(m):
        m[n] = dictionary[n]


def dict2Adj(d):

#fare anche per non orientati pesati
#fare disegno del grafo con networkX


def main():
    matrix = []
    matrix = user2Adj()

if __name__ == "main":
    main()