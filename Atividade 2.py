#Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas,
#empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e
#cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de
#pontos perdidos e o percentual de aproveitamento da equipe

time = input('digite o nome do seu time:')
quant_jogos = int(input(f'{time} jogou: '))
vitoria = int(input(f'{time} ganhou: '))
empate = int(input(f'{time} empatou: '))
derrota = int(input(f'{time} perdeu: '))

vitoria_total = vitoria * 3
vitoria_100 = quant_jogos * 3
empate_total = empate * 1
derrota_total = derrota * 3
pontos_ganhos = vitoria_total + empate_total
percentual = pontos_ganhos/vitoria_100 * 100

print(f'{time} ganhou:{pontos_ganhos} e perdeu:{derrota_total}')
print(f'{time} teve um percentual de: {percentual}')
