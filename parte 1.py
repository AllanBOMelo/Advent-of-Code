resultado = 0
ponto = 0

arq = open("input.txt", 'r')
lista = arq.readlines()
arq.close()

#loop geral
a = 0
while a < len(lista):
    mochila = lista[a]
    comp1 = mochila[:len(mochila)//2]
    comp2 = mochila[len(mochila)//2:]
    print(comp1, comp2)
    
    b = 0
    while b < len(comp1):
        i = 0
        while i < len(comp2):
            if comp1[b] is comp2[i]:
               
                letra = comp2[i]
                b = b + 100
                i = i + 100
            else:
                i = i + 1
        b = b + 1

    print(letra)
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    print(letras.index(letra.strip()))
    ponto = 1 + letras.index(letra.strip())
    resultado = resultado + ponto
    a = a + 1
   
print("Resultado", resultado)
print("end")

