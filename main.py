from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.quick_sort import quick_sort
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from matplotlib.widgets import Button, Slider, RadioButtons
import random

# prompt for input
n = 0
while n <= 0:
    n = int(input('Enter a number of items sorted (n > 0):\n'))

data = [i for i in range(n, 0, -1)]
random.shuffle(data)

sort_dict = {
    's' : { 'title' : r'Selection Sort ($O(n^2)$)', 'generator' : selection_sort(data)},
    'i' : { 'title' : r'Insertion Sort ($O(n^2)$)', 'generator' : insertion_sort(data)},
    'b' : { 'title' : r'Bubble Sort ($O(n^2)$)', 'generator' : bubble_sort(data)},
    'm' : { 'title' : r'Merge Sort ($O(n log(n))$)', 'generator' : merge_sort(data, 0, len(data))},
    'h' : { 'title' : r'Heap Sort ($O(n log(n))$)', 'generator' : heap_sort(data)},
    'q' : { 'title' : r'Quick Sort ($O(n log(n))$)', 'generator' : quick_sort(data, 0, len(data) - 1)},
}

algorithm = 'x'
while algorithm not in sort_dict.keys():
    print('Enter the sorting algorithm.\nUsage:'
          '\nb - bubble sort\nh - heap sort\n'
          'i - insertion sort\nm - merge sort\n'
          'q - quick sort\ns - selection sort\n')
    algorithm = input("Enter the algorithm:\n")

fig, ax= plt.subplots()

fig.canvas.set_window_title('Visual Sorting')
sort_type = sort_dict.get(algorithm)


def init():
    ax.set_title(sort_type.get('title'))
    x_data = [i for i in range(n)]
    y_data = data
    return plt.bar(x_data, y_data)

def update(data):
    y_data = data
    x_data = [i for i in range(n)]
    return plt.bar(x_data, y_data, color='m')

animation = FuncAnimation(fig=fig,
                     func=update,
                     init_func=init,
                     frames=sort_type.get('generator'),
                     blit=True,
                     interval=1,
                     repeat=False)

plt.show()
