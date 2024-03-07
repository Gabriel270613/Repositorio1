#Este es el juego de la bola 8 de 1946
import random

pregunta = input("pregunta algo de si o no : ")

respuesta_random = random.randint(1, 9)

if respuesta_random == 1:
  print('si-definitivamente')
elif respuesta_random == 2:
  print('Sin duda.')
elif respuesta_random == 3:
  print('Respuesta confusa, intenta otra vez.')
elif respuesta_random == 4:
  print('Pregunta de nuevo más tarde.')
elif respuesta_random == 5:
  print('Mejor no decirte ahora.')
elif respuesta_random == 6:
  print('Mis fuentes dicen que no.')
elif respuesta_random == 7:
  print('Las perspectivas no son tan buenas.')
elif respuesta_random == 8:
  print('Muy dudoso.')
else :
  print('no lose.... Tu dimelo.......jajajaja')