from tkinter import *

class Application(Frame):
    """
    GUI-application with widgets that help of which the user will enter the initial data and receive a ready-made story
    """
    def __init__(self, master: Tk):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates widgets with that help of which the user will enter the initial data and receive a ready-made story
        """
        # Labels
        Label(self,
              text="Enter your data to create a cool story"
              ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=W
        )

        # Entry fields
        Label(self,
              text="Name of the user:"
              ).grid(
            row=1,
            column=0,
            sticky=W
        )
        self.person_ent: Entry = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self,
              text="Noun in plural:"
              ).grid(
            row=2,
            column=0,
            sticky=W
        )
        self.noun_ent: Entry = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Verb in infinitive:"
              ).grid(
            row=3,
            column=0,
            sticky=W
        )
        self.verb_ent: Entry = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        # Check buttons
        Label(self,
              text="Adjective(-s): "
              ).grid(row=4, column=0, sticky=W)
        self.is_itchy: BooleanVar = BooleanVar()
        Checkbutton(self,
                    text="is itchy",
                    variable=self.is_itchy
                    ).grid(row=4, column=1, sticky=W)

        self.is_joyous: BooleanVar = BooleanVar()
        Checkbutton(self,
                    text="is joyous",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)

        self.is_electric: BooleanVar = BooleanVar()
        Checkbutton(self,
                    text="is electric",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)

        # Body part
        Label(self,
              text="Body part:"
              ).grid(row=5, column=3, sticky=W)
        self.body_part: StringVar = StringVar()
        self.body_part.set(None)
        body_parts: list[str] = ["navel", "big toe", "medulla"]
        for index, part in enumerate(body_parts):
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part,
                        ).grid(
                row=5, column=index+1, sticky=W
            )

        # Button to send
        Button(self,
               text="Get answer",
               command=self.tell_story
        ).grid(row=6, column=0, sticky=W)
        self.story_txt: Text = Text(self, width=75, height=75, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self) -> None:
        """
        Sends the answer into text field
        :return: None
        """
        # get values from the GUI
        person: str = self.person_ent.get()
        noun: str = self.noun_ent.get()
        verb: str = self.verb_ent.get()

        adjectives: str = ""
        if self.is_itchy.get():
            adjectives += "itchy"
        if self.is_joyous.get():
            adjectives += "joyous"
        if self.is_electric.get():
            adjectives += "electric"

        body_part: str = self.body_part.get()

        story: str = (f"The famous {person} traveler had already completely despaired of completing the work of his "
                      f"life - the search for the lost city, in which, according to legend, lived {noun.title()}. "
                      f"But one day {noun}, and {person} having come face to face. A powerful, {adjectives} incomparable "
                      f"feeling seized the soul of the traveler. After so many years of searching, the goal was finally "
                      f"achieved. {person.title()} felt a tear roll down his {body_part}. And then suddenly {noun} went on the"
                      f" attack, and {person} was instantly devoured by them. Moral of the story? If you plan to {verb},"
                      f" you must do it with caution.")

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


def root() -> Tk:
    """
    Creating root
    :return: Tk
    """
    root: Tk = Tk()
    root.title("Long-liver")
    root.geometry("650x650")
    return root

def main():
    r: Tk = root()

    # Creating your own object based on Frame with widgets
    app: Application = Application(r)

    r.mainloop()

if __name__ == "__main__":
    main()
