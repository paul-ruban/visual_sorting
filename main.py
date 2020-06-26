from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.quick_sort import quick_sort
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import random

n = 50
data = [i for i in range(n, 0, -1)]
random.shuffle(data)

sort_dict = {
    'selection_sort' : { 'title' : r'Selection Sort ($O(n^2)$)', 'generator' : selection_sort(data)},
    'insertion_sort' : { 'title' : r'Insertion Sort ($O(n^2)$)', 'generator' : insertion_sort(data)},
    'bubble_sort' : { 'title' : r'Bubble Sort ($O(n^2)$)', 'generator' : bubble_sort(data)},
    'merge_sort' : { 'title' : r'Merge Sort ($O(n log(n))$)', 'generator' : merge_sort(data, 0, len(data))},
    'heap_sort' : { 'title' : r'Heap Sort ($O(n log(n))$)', 'generator' : heap_sort(data)},
    'quick_sort' : { 'title' : r'Quick Sort ($O(n log(n))$)', 'generator' : quick_sort(data, 0, len(data) - 1)},
}

fig, ax = plt.subplots()

sort_type = sort_dict.get('quick_sort')

def init():
    ax.set_title(sort_type.get('title'))
    x_data = [i for i in range(n)]
    y_data = data
    return plt.bar(x_data, y_data, color='r')

def update(data):
    y_data = data
    x_data = [i for i in range(n)]
    return plt.bar(x_data, y_data, color='g')

animation = FuncAnimation(fig=fig,
                     func=update,
                     init_func=init,
                     frames=sort_type.get('generator'),
                     blit=True,
                     interval=1,
                     repeat=False)

plt.show()
