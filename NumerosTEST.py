# -*- coding: utf-8 -*-
from unittest import TestCase

from  Numeros import Numeros
class NumerosTEST(TestCase):
    def test_NumeroElementos(self):
        self.assertEqual(Numeros().mmne("")[0],0,"Número de elementos")