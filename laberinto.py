# Por: Carlos Mario Duque Mejía y Claudia Patricia Ordóñez Enríquez

import turtle
import time
import sys
from collections import deque
#-----------------------------------------------
#declaración instancias de turtle para el laberinto.
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#34495E")
        self.hideturtle()
        self.penup()
        self.speed(0)

class Color(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.hideturtle()
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.hideturtle()
        self.penup()
        self.speed(0)

class Texto(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed(0)
#-------------------------------------------
#Creación del laberinto.
maze = Maze()
wall_color= Color()
player=Player()
texto_general=Texto()

walls = []
path = []
visited = set()
frontier = deque()
solution = {}   
fin_x,fin_y=0,0
#S -> start
#E -> exit
#X -> wall.
lab = [
"XXXXXXXXXXXXXXXXXXXXXXX",
"X               X     X",
"XS XXXXX XXXX  XXXXX  X",
"X          X          X",
"X  XXX XXX  XXXXX  XXXX",
"X  X     X     X  X   X",
"X  X X X X  X  X  X   X",
"X  X  X  X  X      X  X",
"X  X    X  XXXXXX  X  X",
"X  X        X      X  X",
"X  XXXX  X  XXXXXXXEX X",
"X     X  X     X      X",
"X XX  X  X  XXXXX XXXXX",
"X  X  X               X",
"X  X   XXX  XXXXX  X  X",
"X  X  X     X      X  X",
"X  X    XX XX  X  X  XX",
"XXXXXXXXXXXXXXXXXXXXXXX",


]

contadorPlayer=0
contadorIA=0
nivel=1

#-------------------------------------------
#creación de la ventana con turtle
def principal(ventana):
    ventana.clear()
    ventana.setup(600,600)
    ventana.bgcolor("Black")
    ventana.bgpic("files/maze_image1.gif")
    texto=turtle.Turtle()
    texto.hideturtle()
    texto.penup()
    texto.goto(-290,200)
    texto.color('white')
    style =('Courier', 20, 'italic', 'bold')
    texto.write('Laberinto de Inteligencia Artificial', font=style, move=True)
    makeButton(80,-150,-200,"Jugar")
    makeButton(175,50,-200,"Hacerlo con IA")
    texto_general.goto(-290,150)
    global nivel
    nivel=1
    cambiarNivel()
    texto_general.write('Nivel actual: 1', font=('Courier', 12, 'italic', 'bold'), move=True)
    makeButton(200,-50, 150,"Cambiar nivel")
    

    turtle.onscreenclick(buttonsMainViewClick,1)
    turtle.listen()

#definición de botones con turtle
def makeButton(tam,x,y,msg):
    penButtons= turtle.Turtle()
    penButtons.hideturtle()
    penButtons.fillcolor("white")
    penButtons.penup()
    penButtons.goto(x,y)
    penButtons.pendown()

    penButtons.begin_fill()
    for i in range(2):
        penButtons.forward(tam)
        penButtons.left(90)
        penButtons.forward(30)
        penButtons.left(90)

    penButtons.end_fill()
    penButtons.penup()
    penButtons.goto(x+6,y+7)
    penButtons.write(msg, font=["Courier",15,"bold"])

def cambiarNivel():
        global lab
        if nivel==1:
            lab = [
            "XXXXXXXXXXXXXXXXXXXXXXX",
            "X               X     X",
            "XS XXXXX XXXX  XXXXX  X",
            "X          X          X",
            "X  XXX XXX  XXXXX  XXXX",
            "X  X     X     X  X   X",
            "X  X X X X  X  X  X   X",
            "X  X  X  X  X      X  X",
            "X  X    X  XXXXXX  X  X",
            "X  X        X      X  X",
            "X  XXXX  X  XXXXXXXEX X",
            "X     X  X     X      X",
            "X XX  X  X  XXXXX XXXXX",
            "X  X  X               X",
            "X  X   XXX  XXXXX  X  X",
            "X  X  X     X      X  X",
            "X  X    XX XX  X  X  XX",
            "XXXXXXXXXXXXXXXXXXXXXXX",
            ]
        elif nivel == 2:
            lab = [
            "XXXXXXXXXXXXXXXXXXXXXXX",
            "X          XXXXXXXXX  E",
            "X XXXX XX            XX",
            "X XXXX XXXXXXXXXXXXX XX",
            "X             XXXXXX XX",
            "XXXXXXXXX XXX XXXXXX XX",
            "XXXXXXXXX XXX X      XX",
            "X         XXXXXXXXXXXXX",
            "X XXXXXXXXX          XX",
            "X X         XX  X XXXXX",
            "X XXXXXXXXXXXX  XXXXXXX",
            "X    X XXXX        XXXX",
            "XXXX        XXXXXX XXXX",
            "XXXX XXXXXX XX     XXXX",
            "X           XX XXXXXXXX",
            "X XXXXXXXXX XX      XXX",
            "X         X XXXXXXXXXXX",
            "XXXXXXXXXXXSXXXXXXXXXXX",
            ]
        else:
            lab = [
            "XXXXXXXXXXXXXXXXXXXXXXX",
            "X  X            X     X",
            "X  XXXXX XXXX  XXXXX  X",
            "X          X          X",
            "X  XXX XXX XXXXXX  XXXX",
            "X  X     X  X  X  X   X",
            "X  X     X  X  X  X   X",
            "X  X  XXXX  X      X  X",
            "X  X    X  XXXXXX  X  X",
            "X          SX      X  X",
            "X  XXXXXXX  XXXX XXXX X",
            "X     X  X            X",
            "X XX  X  XXXXXXXX XXXXX",
            "X  X  X               X",
            "X  X  XXXX  XXXXX  X  X",
            "X  XXXX     X      X  X",
            "XE      XXXXX  X  XX  X",
            "XXXXXXXXXXXXXXXXXXXXXXX",
            ]


#Evento para los botones de la primera pantalla
def buttonsMainViewClick(x,y):
    #Botón para jugar
    if x> -150 and x< -70 and y> -200 and y< -170:
        wn.clear()
        wn.bgcolor("black")
        inicializar_laberinto(lab)
        inicializar_controles(start_x,start_y,end_x,end_y)
        texto=turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-290,260)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        texto.write('Encuentra el camino: ', font=style, move=True)
        texto.color("orange")
        texto.shape('square')
        texto.goto(-280, 220)
        texto.stamp()
        texto.color("red")
        texto.goto(-280, 250)
        texto.stamp()
        texto.color("purple")
        texto.shape('circle')
        texto.goto(30, 250)
        texto.stamp()

        texto.goto(-260,240)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        texto.write(': Entrada. ', font=style, move=True)

        texto.goto(-260,210)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        texto.write(': Salida.', font=style, move=True)

        texto.goto(50,240)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        texto.write(': Jugador.', font=style, move=True)

    #Resolver con IA
    if x> 40 and x< 190 and y> -200 and y< -170:
        wn.clear()
        wn.bgcolor("black")
        inicializar_laberinto(lab)
        makeButton(110,-50,210,"Resolver")
        
        turtle.onscreenclick(buttonsMazeClick,1)
        turtle.listen()

    #cambiar nivel
    if x> -50 and x< 150 and y> 150 and y< 180:
        global nivel
        texto_general.goto(-290,150)
        style =('Courier', 12 , 'italic', 'bold')
        
        if nivel==1:
            nivel=2
            texto_general.clear()
            texto_general.write('Nivel actual: 2', font=style, move=True)
            cambiarNivel()
        elif nivel==2:
            nivel=3
            texto_general.clear()
            texto_general.write('Nivel actual: 3', font=style, move=True)
            cambiarNivel()
        else:
            nivel=1
            texto_general.clear()
            texto_general.write('Nivel actual: 1', font=style, move=True)
            cambiarNivel()
    
        
#Evento para los botones de la segunda pantalla
def buttonsMazeClick(x,y):
    if x> -50 and x< 60 and y> 210 and y< 240:
        #------------------------------------------
        #Usando el algoritmo Breath first search para encontrar la ruta mas corta.
        turtle.onscreenclick(None)
        buscar(start_x,start_y)
        camino_mas_corto(end_x, end_y)
        texto= turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-250,260)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        msg='El camino mas corto es de '+ str(contadorIA) +" movimientos"
        texto.write(msg, font=style, move=True)
        makeButton(110,-50,210,"Volver")
        turtle.onscreenclick(volverI)

#Función para salir del programa.
def volverI(x,y):
    if x> -50 and x< 60 and y> 210 and y< 240:
        principal(wn)

def volver(x,y):
    if x> -200 and x< -90 and y> -180 and y< -150:
        principal(wn)


def inicializar_laberinto(lab):
    global start_x, start_y, end_x, end_y
    walls.clear()
    path.clear()
    visited.clear()
    frontier.clear()
    solution.clear()
    
    for y in range(len(lab)):
        for x in range(len(lab[y])):
            letra = lab[y][x]
            screen_x = -270 + (x * 24)
            screen_y = 180 - (y * 24)
            if letra == "X":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if letra == " " or letra == "E":
                path.append((screen_x, screen_y))

            if letra == "E":
                wall_color.color("orange")
                wall_color.goto(screen_x, screen_y)
                end_x, end_y = screen_x,screen_y
                wall_color.stamp()

            if letra == "S":
                start_x, start_y = screen_x, screen_y
                wall_color.color("red")
                wall_color.goto(screen_x, screen_y)
                wall_color.stamp()


def up():
    x,y=(player.position()[0]),(player.position()[1]+24)
    if (x,y) in path:
        player.clear()
        player.goto(x,y)
        player.stamp()
        global contadorPlayer
        contadorPlayer+=1
    if (x,y) == (fin_x,fin_y):
        time.sleep(0.5)
        wn.clear()
        wn.bgcolor("Black")
        wn.setup(500,500)
        wn.bgpic("files/di.gif")
        texto= turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-200,200)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        msg='Bien!, lo hiciste en '+ str(contadorPlayer) +" movimientos"
        texto.write(msg, font=style, move=True)
        makeButton(110,-200,-180,"Volver")
        turtle.onscreenclick(volver)


def left():
    x,y=(player.position()[0]-24),(player.position()[1])
    if (x,y) in path:
        player.clear()
        player.goto(x,y)
        player.stamp()
        global contadorPlayer
        contadorPlayer+=1
    if (x,y) == (fin_x,fin_y):
        time.sleep(0.5)
        wn.clear()
        wn.bgcolor("Black")
        wn.setup(500,500)
        wn.bgpic("files/di.gif")
        texto= turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-200,200)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        msg='Bien!, lo hiciste en '+ str(contadorPlayer) +" movimientos"
        texto.write(msg, font=style, move=True)
        makeButton(110,-200,-180,"Volver")
        turtle.onscreenclick(volver)


def right():
    x,y=(player.position()[0]+24),(player.position()[1])
    if (x,y) in path:
        player.clear()
        player.goto(x,y)
        player.stamp()
        global contadorPlayer
        contadorPlayer+=1
    if (x,y) == (fin_x,fin_y):
        time.sleep(0.5)
        wn.clear()
        wn.bgcolor("Black")
        wn.setup(500,500)
        wn.bgpic("files/di.gif")
        texto= turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-200,200)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        msg='Bien!, lo hiciste en '+ str(contadorPlayer) +" movimientos"
        texto.write(msg, font=style, move=True)
        makeButton(110,-200,-180,"Volver")
        turtle.onscreenclick(volver)


def down():
    x,y=(player.position()[0]),(player.position()[1]-24)
    if (x,y) in path:
        player.clear()
        player.goto(x,y)
        player.stamp()
        global contadorPlayer
        contadorPlayer+=1
    if (x,y) == (fin_x,fin_y):
        time.sleep(0.5)
        wn.clear()
        wn.bgcolor("Black")
        wn.setup(500,500)
        wn.bgpic("files/di.gif")
        texto= turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(-200,200)
        texto.color('white')
        style =('Courier', 15 , 'italic', 'bold')
        msg='Bien!, lo hiciste en '+ str(contadorPlayer) +" movimientos"
        texto.write(msg, font=style, move=True)
        makeButton(110,-200,-180,"Volver")
        turtle.onscreenclick(volver)

#Keyboard Binds
def inicializar_controles(x,y,e_x,e_y):
    global fin_x,fin_y, contadorPlayer
    contadorPlayer=0
    fin_x=e_x
    fin_y=e_y
    player.goto(x,y)
    player.color("purple")
    player.stamp()
    wn.listen()
    wn.onkeypress(up,"Up")
    wn.onkeypress(left,"Left")
    wn.onkeypress(right,"Right")
    wn.onkeypress(down,"Down")

def buscar(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:
        time.sleep(0)
        x, y = frontier.popleft()

        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            wall_color.color("purple")
            wall_color.goto(cell)
            wall_color.stamp()
            frontier.append(cell)
            visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            wall_color.color("purple")
            wall_color.goto(cell)
            wall_color.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            wall_color.color("purple")
            wall_color.goto(cell)
            wall_color.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            wall_color.color("blue")
            wall_color.goto(cell)
            wall_color.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        wall_color.color("blue")
        wall_color.goto(x,y)
        wall_color.stamp()

def camino_mas_corto(x, y):
    global contadorIA
    contadorIA=0
    wall_color.color('chartreuse')
    wall_color.goto(x, y)
    wall_color.stamp()

    while (x, y) != (start_x, start_y):
        wall_color.goto(solution[x, y])
        wall_color.stamp()
        contadorIA+=1
        x, y = solution[x, y]



wn = turtle.Screen()
wn.setup(600,600) 
wn.bgcolor("Black")
wn.title("Parcial 1-Laberinto Inteligencia Artificial.")

principal(wn)
#-------------------------------------------
#ejecutando indefinidamente la app.
turtle.done()