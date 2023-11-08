def print_staircase_triangle(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

print_staircase_triangle(5)