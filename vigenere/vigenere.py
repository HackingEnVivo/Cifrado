#!/usr/bin/env python
#-*- coding: utf-8 -*-

abc = 'abcdefghijklmnopqrstuvwxyz'

def cifrar(cadena, clave):
	text_cifrar = ''

	i = 0
	for letra in cadena:
		suma = abc.find(letra) + abc.find(clave[i % len(clave)])
		modulo = int(suma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1
	return text_cifrar

def descifrar(cadena, clave):
	text_cifrar = ''

	i = 0
	for letra in cadena:
		suma = abc.find(letra) - abc.find(clave[i % len(clave)])
		modulo = int(suma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1

	return text_cifrar

def main():
	c = str(raw_input('cadena a cifrar: ')).lower()
	clave = str(raw_input('Clave: ')).lower()
	print cifrar(c,clave)
	c = str(raw_input('cadena a descifrar: ')).lower()
	clave = str(raw_input('clave: ')).lower()
	print descifrar(c,clave)
if __name__ == '__main__':
	main()
