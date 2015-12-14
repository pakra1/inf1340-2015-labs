#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = "Paniz Pakravan"
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""


class NameThatShapeGUI:

    def __init__(self):

        self.main_window = Tkinter.Tk()
        self.main_window.geometry('500x100')


        self.top_frame = Tkinter.Frame(self.main_window)
        self.middle_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)


        self.prompt_label = Tkinter.Label(self.top_frame,
                                          text="Enter the number of sides in the shape:")
        self.side_entry = Tkinter.Entry(self.top_frame, width=10)


        self.prompt_label.pack(side="left")
        self.side_entry.pack(side="left")


        self.descr_label = Tkinter.Label(self.middle_frame, text="Name of shape:")
        self.value = Tkinter.StringVar()
        self.value.set("")
        self.shape_name = Tkinter.Label(self.middle_frame, textvariable=self.value)


        self.descr_label.pack(side="left")
        self.shape_name.pack(side="left")


        self.conv_button = Tkinter.Button(self.bottom_frame,
                                          text="Name",
                                          command=self.convert)

        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)


        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")


        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


        Tkinter.mainloop()


    def convert(self):
        try:
            shape_name = name_that_shape(self.side_entry.get())
            self.value.set(shape_name)
        except:
            self.value.set("")
            tkMessageBox.showinfo("Error", "Wrong value")


ntsg = NameThatShapeGUI()
