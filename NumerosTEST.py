# -*- coding: utf-8 -*-
from unittest import TestCase

from  Numeros import Numeros
class NumerosTEST(TestCase):
    def test_NumeroElementos(self):
        self.assertEqual(Numeros().mmne(""), 0, "Número de elementos")
    def test_Minimo(self):
        self.assertEqual(Numeros().mmne("")[1], 0, "mínimo")