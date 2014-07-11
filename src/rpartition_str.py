#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How to split a string into two looking from the end of the string and
using a string as separator?

¿Como dividir un string en dos buscando desde el final del string y usando
un string como separador?
'''

#create a str
s = 'red lorry, yellow lorry, red lorry, yellow lorry'
print(s)

#generates a tuple containing the part before the separator, the last
#separator itself and the part after the separator.
tupla = s.rpartition(',')
print(tupla)

#If the separator is not found, return a tuple containing the first two are
#empty strings and the last item is the string itself
tupla = s.rpartition('.')
print(tupla)
