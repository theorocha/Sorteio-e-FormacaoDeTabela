import random

#Lendo o arquivo e colocando em uma lista
arquivo = open('Atletas.txt', 'r')
lista_de_atletas = arquivo.readlines()
arquivo.close()

#retirando os "\n" dos termos.
for i in range(len(lista_de_atletas)):
    lista_de_atletas[i] = lista_de_atletas[i].strip("\n")
    
#código de sorteio em si.
qte_de_jogos_normais = 0
qte_de_cabecas_de_chave = 0

qte_de_jogos_normais = int(input("Digite a quantidade de jogos normais:"))
qte_de_cabecas_de_chave = int(input("Digite o número de cabeças de chave: "))


for i in range(qte_de_jogos_normais):
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n                                                           " + str(i+1) + "º jogo:")
    print("                                                           " + lista_de_atletas.pop(random.randint(0,len(lista_de_atletas) -1)) + "  X   " + lista_de_atletas.pop(random.randint(0,len(lista_de_atletas) -1)) + "\n") 
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
       
if(qte_de_cabecas_de_chave == 0):
    print("\n\n\nNão há cabeças de chave.")
else:
    print("\n\n\n                                                         COMEÇANDO AGORA OS CABEÇAS DE CHAVE!!!!!!\n\n\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(qte_de_cabecas_de_chave):
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n                                                           " + str(i+1) + "º cabeça de chave:")
        print("                                                           " + lista_de_atletas.pop(random.randint(0,len(lista_de_atletas) -1)) + "\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------")
    
    



    
    
