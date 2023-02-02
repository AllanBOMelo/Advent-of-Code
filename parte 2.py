resul = ""
pont = 0
a = 0
eu = 0

cont = open("input.txt", 'r')
lista = cont.readlines()
cont.close()

while a < len(lista):
    
    partida = str(lista[a].strip())
    
    if partida[0] == "A":   
        #vitoria     
        if partida[2] == "Z":
            eu = eu + 6 + 2
        #empate
        if partida[2] == "Y":
            eu = eu + 3 + 1
        #derrota
        if partida[2] == "X":
            eu = eu + 0 + 3
            
    if partida[0] == "B":   
        #vitoria     
        if partida[2] == "Z":
            eu = eu + 6 + 3
        #empate
        if partida[2] == "Y":
            eu = eu + 3 + 2
        #derrota
        if partida[2] == "X":
            eu = eu + 0 + 1
            
    if partida[0] == "C":   
        #vitoria     
        if partida[2] == "Z":
            eu = eu + 6 + 1
        #empate
        if partida[2] == "Y":
            eu = eu + 3 + 3
        #derrota
        if partida[2] == "X":
            eu = eu + 0 + 2
    
    a = a + 1
    
print (eu)

          
          
          
          
        


