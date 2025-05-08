times= []
partida = []
time = []

# responsável por pedir o nome dos times, armazenar num vetor e printar eles
for i in range(4):
    nome = input(f'Insira o nome do {i+1}° time: ')
    times.append(nome)
print(f'Os times que vão jogar são: {times}')

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
            print(f'{partida[0]} Vencedor! ')
            print(f'{partida[1]} Perdedor... \n')
        elif gols[0] < gols[1]:
            print(f'{partida[1]} Vencedor! ')
            print(f'{partida[0]} Perdedor... \n')
        else:
            print(f'{partida[0]} e {partida[1]} Empatados! \n')