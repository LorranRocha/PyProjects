import os
import turtle
import time
import random

delay = 0.1 
os.system('cls')

# Criar janela
wn = turtle.Screen()
wn.title("Snake by @Lorran")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Desativa atualizações de tela


# Cabeça da cobra
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "parado"

# Comida da cobra
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

segments = []

# Funções

def go_up():
    head.direction = "cima"

def go_down():
    head.direction = "baixo"

def go_left():
    head.direction = "esquerda"

def go_right():
    head.direction = "direita"    



def move():
    if head.direction == "cima":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "baixo":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "esquerda":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "direita":
        x = head.xcor()
        head.setx(x + 20)            

# Entrada do teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")
# Main game loop
while True:
    wn.update()

    #Checa colisão com a borda
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "parado"

        # Esconde segmentos
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpa os segmentos
        segments.clear()    


    # Checa colisão com a comida
    if head.distance(food) < 20:
        # Move a comida para uma posição aleatória
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Adiciona um seguimento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move o fim dos segmentos primeiro em ordem reversa
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()    
        segments[index].goto(x, y)

    # Move segmento 0 para onde está a cabeça
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)   

    move()

    # Checa colisão de cabeça com o corpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

             # Esconde segmentos
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpa os segmentos
            segments.clear() 
    time.sleep(delay)
# Manter loop da janela
wn.mainloop()