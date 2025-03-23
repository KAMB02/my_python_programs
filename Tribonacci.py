print("On cherche a calculé le Tribonacci d'un nombre donné\n")

def Tribonacci(n, memoire={}):
    if n in memoire:
        return memoire[n]
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memoire[n] = Tribonacci(n-1, memoire) + Tribonacci(n-2, memoire) + Tribonacci(n-3, memoire)
        return memoire[n]

n = int(input("entrer la valeur dont vous volez son Tribonacci:"))
print(f"Tribonacci({n})={Tribonacci(n)}")