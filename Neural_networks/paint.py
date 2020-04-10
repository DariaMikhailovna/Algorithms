from tkinter import *
from PIL import Image
from mnist import MyNeural
import threading


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.alive = True
        self.canvas = Canvas(self, bg="white")
        self.parent = parent
        self.color = "black"
        self.brush_size = 20
        self.label = None
        self.setup()
        self.predictor = threading.Thread(target=self.run_prediction_loop)
        self.predictor.setDaemon(True)
        self.predictor.start()

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
        clear_btn = Button(self, text="Очистить", width=10, command=lambda: self.canvas.delete("all"))
        clear_btn.grid(row=0, column=0, sticky=W)
        eraser_btn = Button(self, text="Ластик", width=10, command=lambda: self.set_color("white"))
        eraser_btn.grid(row=0, column=1, sticky=W)
        pen_btn = Button(self, text="Перо", width=10, command=lambda: self.set_color("black"))
        pen_btn.grid(row=0, column=2, sticky=W)
        Label(self, text="Предсказание:").grid(row=0, column=3, sticky=W)
        self.label = Label(self, text='Nan')
        self.label.grid(row=0, column=4, sticky=W)

    def set_color(self, new_color):
        self.color = new_color

    def predict(self, neural):
        self.canvas.postscript(file="image" + '.ps', colormode='color')
        img = Image.open("image" + '.ps').resize([28, 28])
        img.save("image" + '.png', 'png')
        prediction = str(neural.go_predict('image.png'))
        self.label.configure(text=prediction)

    def run_prediction_loop(self):
        neural = self.set_neural()
        while True:
            self.predict(neural)

    @staticmethod
    def set_neural():
        neural = MyNeural(150)
        neural.build_model()
        neural.load_model()
        return neural


def main():
    root = Tk()
    root.geometry("500x500+500+300")
    Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()

