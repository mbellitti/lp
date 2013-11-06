# Scrive i numeri di Catalan minori di un miliardo
Cn = 1
n = 0

while Cn < 1e9:
	print(int(Cn))
	Cn *= (4*n + 2)/(n+2)
	n += 1

