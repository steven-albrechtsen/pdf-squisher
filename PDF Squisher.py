from Tkinter import *
import tkFileDialog
import os

original_file_list = []
compressed_file_list = []

class Application(Frame):
    def select_files(self):
        global original_file_list
        global compressed_file_list

        self.files=tkFileDialog.askopenfilenames(parent=root, initialdir='%systemdrive%\users\%username%\Desktop', title='Please select your file(s)')
        if self.files != None:
            i = 0
            self.file_list.delete(0, END)
            original_file_list = []
            compressed_file_list = []
            self.num_files = len(self.files)
            while i < self.num_files:
                self.file_list.insert(i, self.files[i])
                original_file_list.append(str(self.files[i]))
                modify = str(self.files[i])
                modify = modify[:-4]
                compressed_file_list.append(modify + "-compressed.pdf")
                i+=1
            print compressed_file_list


    def compress_pdfs(self):
        global original_file_list
        global compressed_file_list
        print original_file_list
        print compressed_file_list

        self.compress_dpi = self.dpi.get()
        filter_dpi = self.compress_dpi

        if len(filter_dpi) == 32:
            filter_dpi = "75"
        if len(filter_dpi) == 14:
            filter_dpi = "150"
        if len(filter_dpi) == 33:
            filter_dpi = "200"

        self.compress_contrast = self.contrast.get()
        contrast_percent = self.compress_contrast + "%"

        print filter_dpi
        print contrast_percent

        print "----------"

        i = 0
        #while i < len(original_file_list):
            #cline = "magick -density %s \"%s\" -threshold %s -type bilevel -compress fax \"%s\"" % (filter_dpi, original_file_list[i], contrast_percent, compressed_file_list[i])
            #print cline
            #os.system(cline)
            #i+=1


    def loadMainWindow(self):

        self.browse_file = Button(self, text='Select File(s)', command=self.select_files)
        self.browse_file.grid(row=1, column=1, rowspan=2, padx=5, pady=5)

        self.dpi_label = Label(self, text="DPI - Dots Per Inch.")
        self.dpi_label.grid(row=1, column=3)

        self.dpi = StringVar(self)
        self.dpi.set("150")

        self.dpi_option_menu = OptionMenu(self, self.dpi, "75 - Grainy image, smallest file", "150 - Balanced", "200 - Sharper image, biggest file")
        self.dpi_option_menu.grid(row=1, column=4, padx=5, pady=5)

        self.contrast_label = Label(self, text="Contrast - Lower is darker, higher is lighter")
        self.contrast_label.grid(row=2, column=3)

        self.contrast = StringVar(self)
        self.contrast.set("75")

        self.contrast_option_menu = OptionMenu(self, self.contrast, '5', '15', '25', '35', '45', '55', '65', '75', '85', '95')
        self.contrast_option_menu.grid(row=2, column=4, padx=5, pady=5)

        self.compress = Button(self, text='Compress PDF(s)', background="green", command=self.compress_pdfs)
        self.compress.grid(row=4, column=3, rowspan=2, padx=5, pady=5)

        self.file_list = Listbox(self, height=5, width=80)
        self.file_list.grid(row=0, column=1, columnspan=5, padx=5, pady=5)

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.grid(row=4, column=5, padx=5, pady=5)




    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.loadMainWindow()

root = Tk()
root.resizable(width=FALSE, height=FALSE)
app = Application(master=root)
app.mainloop()
root.destroy()
