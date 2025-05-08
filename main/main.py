times= []
partida = []
time = []

vencedor = 'Vencedor!'
perdedor = 'Perdedor...'
empate = 'Empatados!'

# responsável por pedir o nome dos times, armazenar num vetor e printar eles
for i in range(4):
    nome = input(f'Insira o nome do {i+1}° time: ')
    times.append(nome)
print(f'Os times que vão jogar são: {times}')

pontos = [0] * len(times)


# organiza os times nas respectivas partidas
for i in range(4):
    time1 = times[i]
    for j in range(i+1,4):
        time2 = times[j]
        partida = [time1, time2]
        print(f'Partida: {time1} vs {time2}')
        
        # atribui gols para cada time
        gols = []
        for a in range(2):
            golsTime = int(input(f'Quantos gols o time {partida[a]} fez? '))
            gols.append(golsTime)
        print(f'Resultado: {partida[0]} {gols[0]} x {gols[1]} {partida[1]}')
        
        # determina o resultado da partida
        if gols[0] > gols[1]:
            print(f'{partida[0]} {vencedor} ')
            print(f'{partida[1]} {perdedor} \n')
            pontos[times.index(partida[0])] += 3 #index procura o primeiro valor encontrado que seja igual ao argumento
            
        elif gols[0] < gols[1]:
            print(f'{partida[1]} {vencedor} ')
            print(f'{partida[0]} {perdedor} \n')
            pontos[times.index(partida[1])] += 3
            
        else:
            print(f'{partida[0]} e {partida[1]} {empate} \n')
            pontos[times.index(partida[0])] += 1
            pontos[times.index(partida[1])] += 1
            
# junta os times e a respectiva pontuação em pares,     
ranking = list(zip(times, pontos)) # zip empacota os elementos respectivos, e list transforma o objeto de zip em uma lista de tuplas

# ordena os times com base no valor dos pontos em ordem decrescente
ranking.sort(key=lambda x: x[1], reverse=True) #sort ordena os elementos em ordem crescente, lambda define x[1] como base

# printa o ranking dos times
print("Ranking Final:")
for i, (time, pontuacao) in enumerate(ranking, start=1): #enumerate obtem tanto a posição quanto o conteudo da lista
    print(f'{i}º lugar: {time} - {pontuacao} pontos')

            