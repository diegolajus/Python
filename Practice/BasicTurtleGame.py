import turtle as t

t.setup (500,500)
t.shape("turtle")
t.color("red")




#   def rectangulo (px, py, ancho, alto)
# t.seth donde apuntara despues de moverse (0 es derecha)(90 es arriba)(180 es izquierda) (360 es abajo)
# t.circle dibuja un circulo

def ordenar():

    orden = t.textinput("Cómo se juega",
                        "Movimientos: a s w d - Salir: e")
    if orden == "d":    t.seth(0)
    elif orden == "w": t.seth(90)
    elif orden == "a":  t.seth(180)
    elif orden == "s":  t.seth(270)
    elif orden == "e":  t.bye()
    else: return              
    
    
    t.forward(50)


while True:
    ordenar()

t.done()
t.bye()