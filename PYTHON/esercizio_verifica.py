import random

def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack, element

class carta(object):
    def __init__(self, seme, numero):
        self.seme = seme
        self.numero = numero
        
    def stampa(self):
        print(f"la carta ha seme {self.seme} con numero {self.numero}")

def mescolaMazzo(Mazzo):
    Mazzetto1 = []
    elemento = []
    elemento1 = []
    elemento2 = []

    coppa = random.randint(0,len(Mazzo)-1)

    for i in range(0,coppa):
        elemento = pop(Mazzo[i])
        push(Mazzetto1, elemento)

    for i in range(0,coppa):
        elemento1 = pop(Mazzetto1)
        push(Mazzetto1, elemento1)

    for i in range(0,len(Mazzo)-coppa):
        elemento2 = pop(Mazzo)
        push(Mazzetto1, elemento2)

Mazzo = []
Semi = ["C","D","P","F"]

for i in range (1,14):
    for s in Semi:
        push(Mazzo, carta(s,i))

mescolaMazzo(Mazzo)

for i in Mazzo:
    i.stampa()


