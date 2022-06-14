from test_functions import *
from ReferenceManual import *
from config import *

if __name__ == '__main__':
      print_reference_manual(MAJOR_COLORS, MINOR_COLORS)
      test_number_to_pair(4, 'White', 'Brown')
      test_number_to_pair(5, 'White', 'Slate')
      test_pair_to_number('Black', 'Orange', 12)
      test_pair_to_number('Violet', 'Slate', 25)
      test_pair_to_number('Red', 'Orange', 7)
      print('Done :)')
