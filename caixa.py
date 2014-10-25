

class Caixa:

	def sacar(self, valor):
		cedulas = {100: 0, 50: 0, 20: 0, 10: 0}

		resto = valor % 10

		if (resto > 0):
			raise Exception("Passe amanha")

		# temp = valor // 100
		# cedulas[100] = temp

		# resto = valor % 100 

		# if resto > 0:
			
		# 	temp = resto // 50
		# 	cedulas[50] = temp

		# resto = resto % 50

		# if resto > 0:

		# 	temp = resto //20
		# 	cedulas[20] = temp

		# resto = resto % 20

		# if resto > 0:
		# 	temp = resto // 10
		# 	cedulas[10] = temp

		cedulas_ordenadas = list(cedulas.keys())
		cedulas_ordenadas.sort(reverse=True)

		for cedula_vez in cedulas_ordenadas:
			cedulas[cedula_vez] = valor // cedula_vez
			valor = valor % cedula_vez

			if valor == 0:
				print (cedulas.items())
				return cedulas