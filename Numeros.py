# -*- coding: utf-8 -*-
_author_ = 'ji.bernal27 oa.fajardo'


class Numeros:
    def mmne(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif not "," in cadena:
            return [float(cadena), float(cadena), float(cadena), float(cadena)]
        else:
            numeroosPar=[float(i) for i in cadena.split(",")]
            return [len(numeroosPar), min(numeroosPar), max(numeroosPar), 1.5]
