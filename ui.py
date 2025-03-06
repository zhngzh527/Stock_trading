from tkinter import *

THEME_COLOR = "#010203"
FONT = ("Arial",20,"italic")

class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Stock_trading")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        # self.name_label = Label(text="Nvidia", fg='#76b900', bg=THEME_COLOR)
        # self.name_label.pack()

        self.canvas = Canvas( width=400,height=400,bg=THEME_COLOR,highlightthickness=0)
        self.text = self.canvas.create_text(
            200,
            50,
            text = "Nvidia",
            font = FONT,
            fill = "#76b900"
        )
        self.canvas.pack()


        self.window.mainloop()


app = Ui()