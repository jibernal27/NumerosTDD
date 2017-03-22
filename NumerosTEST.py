# -*- coding: utf-8 -*-
from unittest import TestCase

from  Numeros import Numeros


class NumerosTEST(TestCase):
    def test_NumeroElementos(self):
        self.assertEqual(Numeros().mmne("")[0], 0, "Número de elementos")

    def test_Minimo(self):
        self.assertEqual(Numeros().mmne("")[1], 0, "Mínimo")

    def test_Maximo(self):
        self.assertEqual(Numeros().mmne("")[2], 0, "Máximo")

    def test_Promedio(self):
        self.assertEqual(Numeros().mmne("")[3], 0, "Promedio")

    def test_NumeroElementos1(self):
        self.assertEqual(Numeros().mmne("1")[0], 1, "Número de elementos")

    def test_Minimo1(self):
        self.assertEqual(Numeros().mmne("1")[1], 1, "Mínimo")

    def test_Maximo1(self):
        self.assertEqual(Numeros().mmne("1")[2], 1, "Máximo")

    def test_Promedio1(self):
        self.assertEqual(Numeros().mmne("1")[3], 1, "Promedio")

    def test_NumeroElementos2(self):
        self.assertEqual(Numeros().mmne("1,2")[0], 2, "Número de elementos")

    def test_Minimo2(self):
        self.assertEqual(Numeros().mmne("1,2")[1], 1, "Mínimo")

    def test_Maximo2(self):
        self.assertEqual(Numeros().mmne("1,2")[2], 2, "Máximo")

    def test_Promedio2(self):
        self.assertEqual(Numeros().mmne("1,2")[3], 1.5, "Promedio")

    def test_NumeroElementosn(self):
        self.assertEqual(Numeros().mmne("1,2,3,5")[0], 4, "Número de elementos")

    def test_Minimon(self):
        self.assertEqual(Numeros().mmne("10,2,3,5")[1], 2, "Mínimo")

    def test_Maximon(self):
        self.assertEqual(Numeros().mmne("10,2,3,5")[2], 10, "Máximo")

    def test_Promedion(self):
        self.assertEqual(Numeros().mmne("10,2,3,5")[3], 5, "Promedio")
