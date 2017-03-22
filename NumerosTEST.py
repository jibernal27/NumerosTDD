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
