# -*- coding: utf-8 -*-
_author_ = 'ji.bernal27 oa.fajardo'


class Numeros:
    def mmne(self, cadena):
        if cadena == "":
            return [0]*4
        else:
            numeroosPar = [float(i) for i in cadena.split(",")]
            return [len(numeroosPar), min(numeroosPar), max(numeroosPar), sum(numeroosPar) / float(len(numeroosPar))]
