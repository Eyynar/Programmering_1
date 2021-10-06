def circ_rectangle(l, h):
    circ = 2*l+2*h
    print(f"The circumference of the rectangle is {circ}")


length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

circ_rectangle(length, width)
