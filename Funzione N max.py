def max(n1, n2, n3, nmax):
    if n1 > n2 and n1 > n3:
        nmax = n1
    else:
        if n2 > n1 and n2 > n3:
            nmax = n2
        else:
            nmax = n3
    
    return nmax

# Main
print("Inserisci il primo numero")
n1 = int(input())
print("Inserisci il secondo numero")
n2 = int(input())
print("Inserisci il terzo numero")
n3 = int(input())
max(n1, n2, n3)
print("Il numero massimo é" + str(nmax))
