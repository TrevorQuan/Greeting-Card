import turtle

#turtle.screen allows you to define your screen size
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#F4EABA")

#dictionary of colors
colors = {
  "SeaGreen": "#00FFD4",
  "Red": "#E50E0E",
  "Blue": "#256DFF",
  "Green": "#53E12D",
  "Purple": "#772EFF"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(colors["SeaGreen"])
artist.speed(2)
artist.penup()
userName = input("What is your name? ")

#(font-family, font-size, font-style)
style = ("Trattatello, fantasy", 30, "normal")
styleTwo = ("Luminari, fantasy", 20, "normal")
styleThree = ("Chalkduster, fantasy", 15, "normal")
styleFace = ("Marker Felt, fantasy", 50, "bold")
styleCredit = ("Impact, fantasy", 10, "italic")
artist.goto(0,210)
artist.color(colors["Red"])
artist.write("--------------------------------------", font = style, align = "center")
artist.goto(0, 175)
artist.color(colors["SeaGreen"])
artist.write("Happy Today!, " + userName + "!", font = style, align = "center")
artist.goto(0,100)
artist.color(colors["Blue"])
artist.write("You are a GREAT teacher! Bye!", font = styleTwo, align = "center")
artist.right(90)
artist.color("Black")
artist.goto(0, -10)
artist.write(": )", font = styleFace, align = "center")
artist.color(colors["Green"])
artist.goto(0, -100)
artist.write("From: Da Epic Turtle!", font = styleThree, align = "center")
artist.goto(0,-125)
artist.color(colors["Purple"])
artist.write("and Trevor too, don't forget, :>", font = styleCredit, align = "center")
artist.goto(0,-210)
artist.color(colors["Red"])
artist.write("--------------------------------------", font = style, align = "center")
artist.color("Green")
artist.goto(0, -220)
artist.right(180)
