from tkinter import *


def root() -> Tk:
    """
    :return: Tk
    """
    root: Tk = Tk()
    root.title("It's me, mark")
    root.geometry("200x50")
    return root


def main():
    r: Tk = root()

    # Creating Frame
    app: Frame = Frame(r)
    # Frame placement
    app.grid()

    # Creating Label
    label: Label = Label(app, text="It's me mark!")
    # Label placement
    label.grid()

    r.mainloop()

if __name__ == "__main__":
    main()

