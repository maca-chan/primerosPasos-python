# -*- coding: utf-8 -*-

from time import sleep


def temporizador(segundos):
	sleep(segundos)
	print("Ya han pasado " + str(segundos) + " segundos")


temporizador(5)