# -*- coding: utf-8 -*-
from unittest import TestCase

from  Numeros import Numeros



class NumerosTEST(TestCase):

    def test_CadenaVacia(self):
        self.assertItemsEqual(Numeros().mmne(""), [0]*4, "Cadena vacia")

    def test_CadenaConUnNumero(self):
        self.assertItemsEqual(Numeros().mmne("1"), [1]*4, "Cadena con un elemento")


    def test_CadenaCon2Elementos(self):
        self.assertItemsEqual(Numeros().mmne("1,2"), [2,1,2,1.5], "Cadena con 2 elementos")


    def test_NumeroElementosn(self):
        self.assertItemsEqual(Numeros().mmne("10,2,3,5"), [4,2,10,5], "Número de elementos")

