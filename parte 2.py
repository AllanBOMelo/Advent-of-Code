
topum = 0 
topdois = 0
toptres = 0 
soma = 0
resultado = 0
a = 1

cont = open("input.txt", 'r')
lista = cont.readlines()
cont.close()


while a < len(lista):
    
    teste = str(lista[a].strip())
    
    
    if teste == "":
  
        if soma > toptres:
            toptres = soma
 
            if toptres > topdois:
                inter = topdois
                topdois = toptres
                toptres = inter
                inter = 0

                if topdois > topum:
                    inter = topum
                    topum = topdois
                    topdois = inter
                    inter = 0          
            soma = 0
        else:
            soma = 0
    else:
        cal = int(lista[a].strip())
        soma = soma + cal
    
    a = a + 1
    
resultado = topum + topdois + toptres
print (resultado)

          
          
          
          
        


