from config import *
from operation_functions import *

def print_reference_manual(major_color, minor_color):
    print ("Reference Manual\n")
    print("Major Color     Minor Color     Pair Number")
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            color_number = get_pair_number_from_color(major_color, minor_color)
            major_color_name, minor_color_name = get_color_from_pair_number(color_number)
            print("{:<15} {:<15} {:<15}".format(major_color_name, minor_color_name, str(color_number)))
