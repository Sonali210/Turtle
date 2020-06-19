import turtle
turtle.speed(0)
turtle.bgcolor("Green")
turtle.shape("arrow")
turtle.pensize("2")
n=150
dist=2
for _ in range(n):
  if _ < 100:
    turtle.color("Brown")
    dist += 2
  else:
    turtle.color("Yellow")
    turtle.stamp()
    dist += 2
  turtle.fd(dist)
  turtle.left(137.5)
