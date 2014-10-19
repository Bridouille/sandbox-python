#!/usr/bin/python3.3

from tkinter import *

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width = 768, height = 576, **kwargs)
        self.pack(fill = BOTH)
        self.nb_clic = 0

        self.msg = Label(self, text = "Vous n'avez pas cliqué sur le boutton")
        self.msg.pack()

        self.btn_quit = Button(self, text = "Quitter", command = self.quit)
        self.btn_quit.pack(side = "left")

        self.btn_clic = Button(self, text = "Cliquez ici", bg = "#e84e40", command = self.cliquer)
        self.btn_clic.pack()


    def cliquer(self):
        self.nb_clic += 1
        self.msg["text"] = "Vous avez cliqué {} fois !".format(self.nb_clic)


def main():
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()


if __name__ == "__main__":
    main()
