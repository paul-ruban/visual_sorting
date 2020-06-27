from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.quick_sort import quick_sort
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from tkinter import Tk, Button, Radiobutton, Entry, StringVar
from random import shuffle

def callback(sv, btn):
    try:
        n = int(sv.get())
    except ValueError:
        btn['state'] = 'disabled'
        return
    btn['state'] = 'normal' if n > 0 and n < 1000 else 'disabled'

def GUI():
    window = Tk("Visual Sorting")
    sv = StringVar()
    start_btn = Button(window, text='START', command=lambda: sort(int(sv.get()), sort_type.get()))
    start_btn['state'] = 'disabled'
    size_entry = Entry(window, width=5, textvariable=sv)
    size_entry.pack(anchor='n')
    sv.trace('w', lambda name, index, mode, sv=sv, btn=start_btn: callback(sv, btn))
    start_btn.bind('<Button-1>', )
    sort_type = StringVar(None, 'selection_sort')
    Radiobutton(window, text='Selection Sort', variable=sort_type, value='selection_sort').pack(anchor='nw')
    Radiobutton(window, text='Insertion Sort', variable=sort_type, value='insertion_sort').pack(anchor='nw')
    Radiobutton(window, text='Bubble Sort', variable=sort_type, value='bubble_sort').pack(anchor='nw')
    Radiobutton(window, text='Merge Sort', variable=sort_type, value='merge_sort').pack(anchor='nw')
    Radiobutton(window, text='Heap Sort', variable=sort_type, value='heap_sort').pack(anchor='nw')
    Radiobutton(window, text='Quick Sort', variable=sort_type, value='quick_sort').pack(anchor='nw')

    start_btn.pack(anchor='s')
    window.mainloop()

def sort(n = 10, algorithm = 'selection_sort'):
    data = [i for i in range(n, 0, -1)]
    shuffle(data)

    sort_dict = {
        'selection_sort' : { 'title' : r'Selection Sort ($O(n^2)$)', 'generator' : selection_sort(data)},
        'insertion_sort' : { 'title' : r'Insertion Sort ($O(n^2)$)', 'generator' : insertion_sort(data)},
        'bubble_sort' : { 'title' : r'Bubble Sort ($O(n^2)$)', 'generator' : bubble_sort(data)},
        'merge_sort' : { 'title' : r'Merge Sort ($O(n log(n))$)', 'generator' : merge_sort(data, 0, len(data))},
        'heap_sort' : { 'title' : r'Heap Sort ($O(n log(n))$)', 'generator' : heap_sort(data)},
        'quick_sort' : { 'title' : r'Quick Sort ($O(n log(n))$)', 'generator' : quick_sort(data, 0, len(data) - 1)},
    }

    fig, ax= plt.subplots()

    fig.canvas.set_window_title(sort_dict.get(algorithm).get('title').rsplit('(')[0])
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

    FuncAnimation(fig=fig,
                 func=update,
                 init_func=init,
                 frames=sort_type.get('generator'),
                 blit=True,
                 interval=1,
                 repeat=False)
    plt.show()

def main():
    GUI()

main()