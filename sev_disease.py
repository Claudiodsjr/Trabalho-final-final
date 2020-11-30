#!/usr/bin/env python3
import math

d =  input("Insira o código da doença (cultura): ")
a1 = int(input("Para banana, insira o número de folhas doentes da classe 1: "))
a2 = int(input("Para banana, insira o número de folhas doentes da classe 2: "))
a3 = int(input("Para banana, insira o número de folhas doentes da classe 3: "))
a4 = int(input("Para banana, insira o número de folhas doentes da classe 4: "))
x = int(input("Para as demais culturas, insira o número de folhas doentes: "))
y = int(input("Para qualquer cultura escolhida, insira o número total de folhas: "))

if isinstance(d, str) == True and isinstance(a1, int) == True and isinstance(a2, int) == True and isinstance(a3, int) == True and isinstance(a4, int) == True and isinstance(x, int) == True and isinstance(y, int) == True:
	print("Os parâmetros foram inseridos corretamente")
	if d == 'Banana':
		severity = ((0.05*a1) + (0.15*a2) + (0.35*a3) + (0.5*a4))/y
		sev = severity*100
		print('Confirmação: A cultura digitada foi {}, equivalente a doença mancha foliar da bananeira. {} equivale ao número de folhas doentes de escala 1. {} equivale ao número de folhas doentes de escala 2. {} equivale ao número de folhas doentes de escala 3. {} equivale ao número de folhas doentes de escala 4. {} equivale ao número total de folhas sintomáticas.'.format(d, a1, a2, a3, a4, y))
		print('A severidade estimada da doença é {}'.format(round(sev, 2)))
	elif d == 'Milho':
		incidence = (x/y)
		severity = (-0.00942 + 0.0167 + incidence)
		sev = severity*100
		print('Confirmação: A cultura digitada foi {}, equivalente a ferrugem comum do milho doce. {} equivale ao número de folhas doentes. {} equivale ao número de folhas total'.format(d, x, y))
		print('A severidade estimada da doença é {}.'.format(round(sev, 2)))
	elif d == 'Cacau':
		incidence = (x/y)
		severity = ((1.1625*incidence) + 0.4392)
		sev = severity*100
		print('Confirmação: A cultura digitada foi {}, equivalente a gomose do cacaueiro. {} equivale ao número de folhas doentes. {} equivale ao número de folhas total'.format(d, x, y))
		print('A severidade estimada da doença é {}.'.format(round(sev, 2)))
	elif d == 'Café':
		incidence = (x/y)
		severity = (0.001 - (0.01076*incidence) + (0.008376*(incidence**2)))*-1
		sev = severity*100
		print('Confirmação: A cultura digitada foi {}, equivalente a ferrugem do café. {} equivale ao número de folhas doentes. {} equivale ao número de folhas total'.format(d, x, y))
		print('A severidade estimada da doença é {}.'.format(round(sev, 5)))
	else:
		print('O código de doença inserido foi {}, que não condiz com nenhum dos disponíveis. Os códigos disponíveis são: Banana para mancha foliar da bananeira|Cacau para a gomose do cacaueiro.|Café para a ferrugem do cafeeiro.|Milho para a ferrugem comum do milho doce.'.format(d))
else:
	print("Os parâmetros não foram inseridos corretamente. Os códigos disponíveis são: Banana para mancha foliar da bananeira; Cacau para a gomose do cacaueiro; Café para a ferrugem do cafeeiro; Milho para a ferrugem comum do milho doce. Os números inseridos devem ser inteiros e seguir as recomendações disponibilizadas previamente.")

