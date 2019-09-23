
from random import randrange
import os

os.system ("cls") 
nombre = ["Anthony", "Addil", "Yohanna", "Karla"]
temas = ["Preguntas #1 y #2", "Pregunta #3", "Preguntas #4", "Preguntas #5"]
i = 0
j = 0
while i < 4: 
    print("El estudiante " + nombre[i] + " le tocan las " + temas[randrange(4)])
    i += 1