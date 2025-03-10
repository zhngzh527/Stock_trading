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
        self.company_name = self.canvas.create_text(
            200,
            30,
            text = "Nvidia",
            font = FONT,
            fill = "#76b900"
        )
        self.price = self.canvas.create_text(
            300,
            100,
            text = "$200.12",
            font = FONT,
            fill = "#76b900"
        )

        self.changed = self.canvas.create_text(
            300,
            150,
            text = "100%",
            font = FONT,
            fill = "#76b900"
        )

        self.symbol = self.canvas.create_text(
            100,
            130,
            text = "😁",
            font = ("Arial",60,"italic"),
            fill = "green"
        )

        self.news_title = self.canvas.create_text(
            200,
            300,
            text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
                   "et dolore magna aliqua.",
            font = FONT,
            width = 380,
            fill = "green"
        )


        self.canvas.pack()


        self.window.mainloop()


app = Ui()