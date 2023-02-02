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
    
    
    p = int(sec1[0].strip())
    o = int(sec1[1].strip())
    i = int(sec2[0].strip())
    u = int(sec2[1].strip())
    
    
    if p in ls2:
        print("sim")
        resultado = resultado + 1
    else:
        if o in ls2:
            print("Sim") 
            resultado = resultado + 1   
        else:
            if i in ls1:
                print("SSim")
                resultado = resultado + 1
            else:
                if u in ls1:
                    print("SSiim")
                    resultado = resultado + 1
                else:
                    print("não")
        
    q = q + 1
    
    print("result: ", resultado)