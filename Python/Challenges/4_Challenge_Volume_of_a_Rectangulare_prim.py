def volume_of_rectangular_prism(l, w, h):
    return l * w * h


length = int(input("Enter the length of rectangular : "))
width = int(input("Enter the width of rectangular : "))
height = int(input("Enter the height of of rectangular : "))

volume = volume_of_rectangular_prism(length, width, height)

print("The volume of the rectangular prism is ", volume, " cubic feet.")
