#!/usr/bin/env python3

arquivo = input("Insira o arquivo 1 contendo os dados da amostragem, no formato .txt: ")
arquivo2 = input("Insira o arquivo 2, onde serão salvas as severidades na mesma ordem do arquivo 1, também em .txt: ")

value = 0
va = 1
value2 = 1
conv_g = []


with open(arquivo, 'r') as f, open(arquivo2, 'w') as g:
	results = [[int(entry) for entry in line.split()] for line in f.readlines()]
	for line in results:
		x = results[value][0]
		y = results[value][1]
		value += 1
		i = x/y
		severity = -0.00942 + 0.0167 + i
		sev = severity*100
		s = round(sev, 2)
		g.write(str(s) + "\n")
		print(f'Para a planta {va} a incidência da doença é {i} e a severidade é {s}')
		va += 1
		conv_g.append(s)
	result = sum(map(int, conv_g))
	print(f'A soma das severidades é {result}')
	mean = result/len(conv_g)
	m = round(mean, 2)
	print(f'A média da severidade no campo é de {m}')
	if mean < 25:
		print(f'Sua severidade média no campo é {m}, não é necessário fazer aplicação para a ferrugem do milho doce.')
	elif 25 < mean < 40:
		print(f'Sua severidade média no campo é {m}, não é necessário aplicar de imediato, mas deve-se acompanhar a situação com maior cautela.')
	else:
		print(f'Sua severidade média no campo é {m}, é recomendado fazer a aplicação para a ferrugem do milho doce.')

print(f'Severidades escritas em {arquivo2}')

