def draw_triangle(height):
    for i in range(height):
        if i == len(range(height)) - 1:
            print(" " * (height - i - 1) + "/" + "_" * (2 * i) + "\\")
        else:
            print(" " * (height - i - 1) + "/" + " " * (2 * i) + "\\")
draw_triangle(5)