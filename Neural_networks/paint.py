from tkinter import *
from PIL import ImageTk, Image
from struct import pack
from PIL import ImageGrab
from mnist import MyNeural


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="white")
        self.parent = parent
        self.color = "black"
        self.brush_size = 25
        self.prediction = 0
        self.setup()

    def draw(self, event):
        self.canvas.create_oval(event.x - self.brush_size,
                                event.y - self.brush_size,
                                event.x + self.brush_size,
                                event.y + self.brush_size,
                                fill=self.color, outline=self.color)

    def setup(self):
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)
        self.canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5,
                         sticky=E + W + S + N)
        self.canvas.bind("<B1-Motion>", self.draw)
        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canvas.delete("all"))
        clear_btn.grid(row=0, column=1, sticky=W)
        clear_btn = Button(self, text="Save", width=10)
        clear_btn.bind('<Button-1>', self.save)
        clear_btn.grid(row=0, column=2, sticky=W)
        Label(self, text="Предсказание:").grid(row=0, column=3, sticky=W)
        Label(self, text=self.prediction).grid(row=0, column=4, sticky=W)

    def save(self, event):
        self.canvas.postscript(file="image" + '.ps', colormode='color')
        img = Image.open("image" + '.ps').resize([28, 28])
        img.save("image" + '.png', 'png')
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image([28, 28], image=img_tk, anchor="center")
        print('Щас предскажу')

    def get_prediction(self):
        self.prediction = 1


def main():
    root = Tk()
    root.geometry("500x500+500+300")
    Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()

