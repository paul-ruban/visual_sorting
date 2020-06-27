from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.quick_sort import quick_sort
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from tkinter import Tk, Frame, Button, Radiobutton, Scale, Label, StringVar, IntVar, BOTH, BOTTOM, HORIZONTAL, font
from random import shuffle

"""dictionary containing sorting algorithms, their complexity 
and the generators that yield values along the sorting process"""
sort_dict = {
        'selection_sort' : { 'title' : r'Selection Sort ($O(n^2)$)', 'generator' : lambda data: selection_sort(data)},
        'insertion_sort' : { 'title' : r'Insertion Sort ($O(n^2)$)', 'generator' : lambda data: insertion_sort(data)},
        'bubble_sort' : { 'title' : r'Bubble Sort ($O(n^2)$)', 'generator' : lambda data:bubble_sort(data)},
        'merge_sort' : { 'title' : r'Merge Sort ($O(n log(n))$)', 'generator' : lambda data: merge_sort(data, 0, len(data))},
        'heap_sort' : { 'title' : r'Heap Sort ($O(n log(n))$)', 'generator' : lambda data: heap_sort(data)},
        'quick_sort' : { 'title' : r'Quick Sort ($O(n log(n))$)', 'generator' : lambda data: quick_sort(data, 0, len(data) - 1)},
    }

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.sort_size = IntVar()
        self.sort_type = StringVar(None, 'selection_sort')
        self.init_window()

    def init_window(self):
        def_font = font.nametofont("TkDefaultFont")
        def_font.configure(size=16)
        self.master.option_add('*Font', def_font)
        self.master.resizable(0, 0)
        self.master.geometry("360x480")
        self.master.title('Visual Sorting')
        self.pack(fill=BOTH, expand=0)
        Label(self, text='Number of elements to be sorted:', width=50).pack(anchor='n')
        Scale(self, from_=2, to=100, variable=self.sort_size, orient=HORIZONTAL, length=300, width=30 ).pack(anchor='n')
        Label(self, text='Sorting algorithm:', width=50).pack(anchor='n')
        radio_group = Frame(self, highlightbackground="black", highlightthickness=1)
        for v,k in sort_dict.items():
            Radiobutton(radio_group, text=k.get('title').rsplit('(')[0], variable=self.sort_type, value=v).pack(anchor='w')
        radio_group.pack(anchor='c')
        Button(self, text='START', width=15, command=self.start_sorting).pack(side=BOTTOM)

    def start_sorting(self):
        sort(self.sort_size.get(), self.sort_type.get())

def sort(n = 10, algorithm = 'selection_sort'):

    data = [i for i in range(n, 0, -1)]
    shuffle(data)

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
             frames=sort_type.get('generator')(data),
             blit=True,
             interval=1,
             repeat=False)
    plt.show()

def main():
    root = Tk()
    app = GUI(master=root)
    root.mainloop()

main()