import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Image segmentation')
        self.geometry('400x400')
        Segmentation(self).pack()

class Segmentation(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        img_path = Image.open('Segmentation/koala.png')

        img = tk.Label(self, image=img_path)
        label_img = ttk.Label(self, text='Kola image')

        img.grid(row=0, column=0)
        label_img.grid(row=1, column=1)


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()