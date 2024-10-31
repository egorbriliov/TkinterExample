from tkinter import *

class Application(Frame):
    """
    GUI-application with three buttons
    """

    def __init__(self, master: Tk):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates buttons, text boxes and text areas
        """
        # Text
        self.inst_lbl: Label = Label(self, text="Enter the password")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        # Text
        self.pw_lbl: Label = Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        # Input field
        self.pw_entry: Entry = Entry(self)
    def update_count(self):
        """Updates and displays the number of times a button has been pressed"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Click count: " + str(self.bttn_clicks)

def main():
    root: Tk = Tk()
    root.title("Useless buttons")
    root.geometry("200x50")

    app: Application = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
