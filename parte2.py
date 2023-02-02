resultado = 0
pontos = 0

arq = open("input.txt", "r")
input = arq.readlines()
arq.close()

alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = 0
y = 0
while t < len(input):
    ###################
    print ("")
    print("Vez: ", y)
    i1 = input[t].strip()
    i2 = input[t+1].strip()
    i3 = input[t+2].strip()
    
    print("bolsas: ", i1, i2, i3)
    ###################
    ###################
    a = 0
    while a < len(alfa):
        k = alfa[a].strip()
        b = 0
        while b < len(i1):
            l = i1[b].strip()
            if l == k:
               c = 0
               while c < len(i2):
                   j = i2[c].strip()
                   if j == l:
                       d = 0
                       while d < len(i3):
                           h = i3[d].strip()
                           if h == j:
                               same = h
                           
                           d = d + 1
                   c = c + 1        
            b = b+1
        a = a + 1
        
    print ("")   
    print ("Repetição: ", same)
    ###################
    ###################
    e = 0
    while e < len(alfa):
        if same == alfa[e].strip():
            pontos = e + 1
        e = e + 1
    ###################    
    ###################       
    print ("")   
    print ("Ponto: ", pontos)
    
    resultado = resultado + pontos 
    ###################
    y = y + 1
    t = t + 3
    ###################
    
    
    print("")
    print("Resultado: ", resultado)