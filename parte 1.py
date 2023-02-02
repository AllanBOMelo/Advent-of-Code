
resultado = 0
soma = 0
a = 1

cont = open("input.txt", 'r')
lista = cont.readlines()
cont.close()


while a < len(lista):

    teste = str(lista[a].strip())
    
    if teste == "":
        if soma > resultado:
            resultado = soma
            soma = 0
        else:
            soma = 0
    else:
        cal = int(lista[a].strip())
        soma = soma + cal
    
    a = a + 1
    #

print (resultado)
#while a < 2263:
    
    #.strip()
      
          
          
          
          
        


