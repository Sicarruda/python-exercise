import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from algorithms_execises.utils.time_comparer import *
from algorithms_execises.algorithms.bubble_sort.bubble_sort import *
from algorithms_execises.algorithms.cocktail_sort.cocktail_sort import *
from algorithms_execises.algorithms.insertion_sort.insertion_sort import *
from algorithms_execises.algorithms.selection_sort.selection_sort import *


list_comparison = [10]

compare_ordering_time(list_comparison, bubble_sort)
compare_ordering_time(list_comparison,cocktail_sort)
compare_ordering_time(list_comparison, insertion_sort)
compare_ordering_time(list_comparison, selection_sort)