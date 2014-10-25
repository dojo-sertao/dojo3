'''
Problema de Caixa Eletronico

Descricao:
Retornar o menor numero de notas, notas possiveis: 10, 20, 50, 100.

'''

import unittest
from caixa import Caixa


class TesteCaixaEletronico(unittest.TestCase):

	def test_de_30_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(30), {10:1, 20:1, 50:0, 100:0});

	def test_de_40_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(40), {10:0, 20:2, 50:0, 100:0});

	def test_de_200_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(200), {10:0, 20:0, 50:0, 100:2});

	def test_de_250_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(250), {10:0, 20:0, 50:1, 100:2});

	def test_de_180_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(180), {10:1, 20:1, 50:1, 100:1});

	def test_de_15_conto(self):
		objCaixa = Caixa()
		self.assertEquals(objCaixa.sacar(15), {10:1, 20:0, 50:0, 100:0});
		
unittest.main()