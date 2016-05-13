from Tkinter import *
import tkFileDialog
import os

class Application(Frame):
    def select_folder(self):
        self.dirname=tkFileDialog.askdirectory(parent=self, initialdir="/", title='Please select a directory')
        if len(self.dirname) > 0:
            self.file_list.delete(0, END)
            self.file_list.insert(0, "Folder: " +self.dirname)
    def select_files(self):
        self.files=tkFileDialog.askopenfilenames(parent=root, initialdir='%systemdrive%\users\%username%\Desktop', title='Please select your file(s)')
        if self.files != None:
            i = 0
            self.file_list.delete(0, END)
            self.num_files = len(self.files)
            while i < self.num_files:
                # Insert code here for pdf conversion
                self.file_list.insert(i, self.files[i])
                i+=1

    def compress_pdfs(self):
        self.compress_dpi = self.dpi.get()
        print self.compress_dpi

        self.compress_contrast = self.contrast.get()
        print self.compress_contrast


    def loadMainWindow(self):

        self.browse_folder = Button(self, text='Select Folder', command=self.select_folder)
        self.browse_folder.grid(row=0, column=1)

        self.browse_file = Button(self, text='Select File(s)', command=self.select_files)
        self.browse_file.grid(row=0, column=2)

        self.dpi = StringVar(self)
        self.dpi.set("150")

        self.dpi_option_menu = OptionMenu(self, self.dpi, "75", "150", "200")
        self.dpi_option_menu.grid(row=0, column=3)

        self.contrast = StringVar(self)
        self.contrast.set("75")

        self.dpi_option_menu = OptionMenu(self, self.contrast, '5', '15', '25', '35', '45', '55', '65', '75', '85', '95')
        self.dpi_option_menu.grid(row=0, column=4)

        self.compress = Button(self, text='Compress PDF(s)', command=self.compress_pdfs)
        self.compress.grid(row=0, column=5)

        self.file_list = Listbox(self, height=5, width=50)
        self.file_list.grid(row=1, column=1, columnspan=5)

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.grid(row=2, column=5, sticky=E)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.loadMainWindow()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
