#Importaciones

from turtle import Turtle, Screen

#Inicio

print('Bienvenido al programa de creación de un círculo')

#variables

valorx= int(input('Dame el valor de X: '))
valory= int(input('Dame el valor de Y: '))
radio= int(input('Dame el radio: '))

#Setup

pantalla= Screen()
pantalla.setup( 400, 300)
pantalla.screensize(1000, 1000)
tortuga= Turtle()

#Colocación del circulo

tortuga.penup()
tortuga.goto(valorx, valory)
tortuga.pendown()
tortuga.write('({0},{1})'.format(valorx, valory))

#Dibujo del radio

tortuga.forward(radio)
tortuga.penup()
tortuga.backward(radio/2)
tortuga.write('radio= ' + str(radio))
tortuga.forward(radio/2)

#Dibujo círculo

tortuga.pendown()
tortuga.left(90)
tortuga.circle(radio)

#salida

pantalla.exitonclick()

