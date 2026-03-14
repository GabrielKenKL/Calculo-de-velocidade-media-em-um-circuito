#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
print("Cálculo da velocidade média em uma corrida circular:")
print("Indique o número de voltas:")
voltas = int(input())

print("Indique a extensão do círculo em metros:")
extensão = float(input())
extensão = extensão / 1000

distancia_percorrida = voltas * extensão

print("Indique o tempo de duração em minutos:")
tempo = float(input())
tempo = tempo / 60

Vm = distancia_percorrida / tempo

print() #pula linha
print("A velocidade média do atleta foi de:" , Vm , "km/h")
