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
    for n in range(len(m)):
        dictionary[n] = m[n]

    print(dictionary)


def dict2Adj(d):
    matrix = []

    for _, n in d.items():      #_, si utilizza per ignorare la prima parte di ogni elemento, quindi la chiave
        matrix.append(n)
    print(matrix)

#fare anche per non orientati pesati
def user2DictPes():
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

#fare disegno del grafo con networkX


def main():
    matrix = []
    dic = {}
    matrix = user2Adj()
    matrix = dict2Adj(dic)

if __name__ == "main":
    main()