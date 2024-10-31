from tkinter import *

class Application(Frame):
    """
    GUI-application with three buttons
    """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates three useless buttons
        """
        self.bttn1: Button = Button(self, text="I do nothing")
        self.bttn1.grid()

        self.bttn2: Button = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too")

        self.bttn3: Button = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "And me!"


def root() -> Tk:
    """
    Creating root
    :return: Tk
    """
    root: Tk = Tk()
    root.title("Useless buttons")
    root.geometry("200x200")
    return root

def main():
    r: Tk = root()

    # Creating your own object based on Frame with widgets
    app: Application = Application(r)

    r.mainloop()

if __name__ == "__main__":
    main()
