from tkinter import *


def root() -> Tk:
    """
    Creating root
    :return: Tk
    """
    root: Tk = Tk()
    root.title("Useless buttons")
    root.geometry("200x200")
    return root

def create_buttons(app: Frame) -> None:
    """
    Creates buttons inside Frame
    :return: None
    """
    # Creates new button | First example to creating
    bttn1: Button = Button(app, text="I do nothing!")
    bttn1.grid()

    # Creates new button | Second example to creating
    bttn2: Button = Button(app)
    bttn2.grid()
    # Changing name after creating | First example
    bttn2.configure(text="Me to!")

    # Creates new button | Third example to creating
    bttn3: Button = Button(app)
    bttn3.grid()
    # Changing name after creating | Second example
    bttn3["text"] = "And me"


def main():
    r: Tk = root()

    app: Frame = Frame(r)
    app.grid()

    # Creates buttons inside Frame
    create_buttons(app=app)

    r.mainloop()

if __name__ == "__main__":
    main()

