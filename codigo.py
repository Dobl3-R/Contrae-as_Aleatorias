# Contrae-as_Aleatorias
#Genera contraseñas completamente aleatorias con python, la extension de lo largo de la contraseña se cambia en la variable "largo"

import random
letras_minusculas = "abcdefghijklmnñopqrstuvwxyz"
letras_mayusuclas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numero ="1234567890"
caracteres = "!#$%&/()=?¡]*_:;"

todo = letras_mayusuclas + letras_minusculas + numero + caracteres
largo = 10
contraseña = "".join(random.sample(todo,largo))

print("La contraseña aleatoria es: ", contraseña)
