import turtle as t

t.setup (500,500)
t.shape("turtle")
t.color("red")
#   def rectangulo (px, py, ancho, alto)
# t.seth donde apuntara despues de moverse (0 es derecha)(90 es arriba)(180 es izquierda) (360 es abajo)
# t.circle dibuja un circulo
def izquierda():
    t.seth(180)
    t.forward(50)

def derecha():
    t.seth(0)
    t.forward(50)

def arriba():
    t.seth(90)
    t.forward(50)

def abajo():
    t.seth(270)
    t.forward(50)

# enlazar funciones con una tecla

t.onkey(arriba, "w")
t.onkey(abajo, "s")
t.onkey(derecha, "d")
t.onkey(izquierda, "a")

# hacemos que la tortuga este atenta

t.listen()


t.done()
t.bye()