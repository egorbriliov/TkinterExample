import tkinter
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
        Creates widgets that helps users to choose
        """
        # Creating label without initialization variable
        Label(self,
              text="Select your favorite movie genres"
              ).grid(
            row=1,
            column=0,
            sticky=W
        )
        # Creating flags without initialization variable
        self.likes_comedy: BooleanVar = BooleanVar() # Unic type
        Checkbutton(
            self,
            text="Comedy",
            variable=self.likes_comedy,
            command=self.update_text
        ).grid(
            row=2,
            column=0,
            sticky=W
        )
        self.likes_drama: BooleanVar = BooleanVar()
        Checkbutton(
            self,
            text="Drama",
            variable=self.likes_drama,
            command=self.update_text,
        ).grid(
            row=3,
            column=0,
            sticky=W
        )
        self.likes_romance: BooleanVar = BooleanVar()
        Checkbutton(
            self,
            text="Romance",
            variable=self.likes_romance,
            command=self.update_text,
        ).grid(
            row=4,
            column=0,
            sticky=W
        )
        self.result_txt: Text = Text(self,
                                     width=40,
                                     height=5,
                                     wrap=WORD)
        self.result_txt.grid(
            row=5,
            column=0,
            columnspan=3
        )


    def update_text(self) -> None:
        """
        Updates the text field when the user selects their favorite genres.
        :return: None
        """
        text: str = "Favorite movie genres:"
        if self.likes_comedy.get():
            text += "\nComedy"
        if self.likes_drama.get():
            text += "\nDrama"
        if self.likes_romance.get():
            text += "\nRomance"

        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, text)


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
