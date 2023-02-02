ponto = 0
resultado = 0
 
arq = open("input.txt", "r")
input = arq.readlines()
arq.close()
 
q = 0
while q < len(input):
    print("=================================================")
    print("Vez: ", q)
    #Dividir elfos
    dupla = input[q].strip()
    elfos = dupla.split(',')
    elfo1 = elfos[0].strip()
    elfo2 = elfos[1].strip()
    ###########################
    #Dividir seções
    sec1 = elfo1.split('-')
    sec2 = elfo2.split('-')
    ###########################
    print("Dupla:", dupla)
    print("Elfo 1: ", elfo1)
    print("Elfo 2: ", elfo2)
   
    print()

    ls1 = []
    for i in range(int(sec1[0]), int(sec1[1])+1):
        ls1.append(i)
        
    ls2 = []
    for i in range(int(sec2[0]), int(sec2[1])+1):
        ls2.append(i)  
    
    a = 0
    p = int(sec1[0].strip())
    o = int(sec1[1].strip())
    i = int(sec2[0].strip())
    u = int(sec2[1].strip())
    
    
    if ls1 == ls2:
        print("São iguais, então sim")
        resultado = resultado + 1
    
    else:   
        while a < len(ls2):
            if p == ls2[a]:
                b = 0
                while b < len(ls2):
                    if o == ls2[b]:
                        print("1 no 2")
                        print(sec1[1], ls2[b]) 
                        resultado = resultado + 1        
                    b = b + 1
            a = a + 1
    
        c = 0
    
     
        while c < len(ls1):
            if i == ls1[c]:
                d = 0
                while d < len(ls1):
                    if u == ls1[d]:
                        print("2 no 1")
                        print(sec2[1], ls1[d]) 
                        resultado = resultado + 1         
                    d = d + 1
            c = c + 1
        
       
        
    q = q + 1
    
    print("result: ", resultado)