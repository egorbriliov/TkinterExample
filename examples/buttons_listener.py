from dataclasses import Field
from tkinter import *

class Application(Frame):
    """
    GUI-application with three buttons
    """

    def __init__(self, master: Tk):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates buttons, text boxes and text areas
        """

        # Creates Label
        self.inst_lbl: Label = Label(self, text="Enter the password")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        # Creates Label
        self.pw_lbl: Label = Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        # Creates Input field
        self.pw_ent: Entry = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # Creates Button for send answers
        self.submit_bttn: Button = Button(self, text="Find out the secret", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        # Creates Text field for program answer
        self.secret_txt: Text = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self) -> str:
        """
        Depending on the answer entered sends different answers
        :return: str
        """
        # Getting field answer
        contents: str = self.pw_ent.get()

        # Comparison of answers
        if contents == "secret":
            message: str = "To live to be 100, you first have to live to be 99, and then be VERY careful."
        else:
            message: str = "Password incorrect"

        # Clearing text field
        self.secret_txt.delete(0.0, END)
        # Inserting program answer into field
        self.secret_txt.insert(0.0, message)




def root() -> Tk:
    """
    Creating root
    :return: Tk
    """
    root: Tk = Tk()
    root.title("Long-liver")
    root.geometry("300x150")
    return root

def main():
    r: Tk = root()

    # Creating your own object based on Frame with widgets
    app: Application = Application(r)

    r.mainloop()

if __name__ == "__main__":
    main()
