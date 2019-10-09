estados = input("").split(" ")
alfabeto = input("").split(" ")
numeroTransicoes = int(input())

OCD = {}
for i in range(0, numeroTransicoes):#preenchimento da estrutura dict, a qual implementa uma hashable
    t = input("").split(" ")
    if(t[0] in OCD):#tratamento de possiveis colisoes
        OCD[t[0]].update({t[1]:t[2]})
    else:
        OCD[t[0]] = {t[1] : t[2]}

estadoInicial = input()
estadosFinais = input("").split(" ")

listaFinal = {}
for i in estadosFinais:
    listaFinal.update({i:""})#hashable com os estados finais, como nao havera multiplos estados finais identicos, nao havera colisoes, o que garante a complexidade O(1)

palavras = input("").split(" ")

for palavra in palavras:#for para percorrer as palavras fornecidas como entrada
    estadoFinal = estadoInicial#Atribuição inicial para comecar a iteracao sobre cada palavra
    for ch in palavra:# for esta iterando ate o tamanho de cada palavra, sendo w o tamanho da palavra, complexidade torna-se O(w)
        try:
            aux = OCD[estadoFinal]#A estrutura dict implementa uma hashable, a busca por indice possui complexidade O(1)
            try:#desta forma, para evitar o aumento da complexidade devido a colisoes, aux passa a ser uma hashable auxiliar, sendo a busca por indice na hashable O(1)
                estadoFinal = aux[ch]#Novamente fazendo uma nova busca por indice na hashable, mantem a complexidade O(1)
            except KeyError:#Caso o indice nao exista na hashable, estado final passa a ser um estado de erro
                estadoFinal = 'erro'#string referente ao estado de erro
        except KeyError:#Except referente a busca no indice mais externo, caso a nao exista o estado, estado final passa a ser um estado de erro 
                estadoFinal = 'erro'
        if(estadoFinal == 'erro'):
            break
    if(estadoFinal in listaFinal):#Novamente um dict, nesta hashtable nao ha possibilidade de colisoes, assim a complexidade se garante O(1)
        result = 'S'
    else:
        result = 'N'
    print(result)