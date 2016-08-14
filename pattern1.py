import turtle

def pattern():
	window=turtle.Screen()
	window.bgcolor("pink")

	rach=turtle.Turtle()
	rach.shape("arrow")
	rach.color("red")
	rach.speed(5)

	for i in range(0,36):

		for i in range(0,2):

		
			rach.forward(100)
			rach.left(45)
			rach.forward(100)
			rach.left(135)

		rach.left(10)
			

	window.exitonclick()

pattern()