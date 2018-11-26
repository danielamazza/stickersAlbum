import tkinter as tk
from PIL import Image, ImageTk
from album import *

myalbum = Album('fig.txt')
carte = myalbum.carte

LABEL_BG = "#ccc"  # Light gray.
ROWS, COLS = 4, 4  # Size of grid.
ROWS_DISP = 3  # Number of rows to display.
COLS_DISP = 4  # Number of columns to display.

class MyApp(tk.Tk):
    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(title)
        self.configure(background="Gray")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        master_frame = tk.Frame(self, bg="Light Blue", bd=3, relief=tk.RIDGE)
        master_frame.grid(sticky=tk.NSEW)
        master_frame.columnconfigure(0, weight=1)

        label1 = tk.Label(master_frame, text="Frame1 Contents", bg=LABEL_BG)
        label1.grid(row=0, column=0, pady=5, sticky=tk.NW)

        frame1 = tk.Frame(master_frame, bd=2, relief=tk.GROOVE)
        frame1.grid(row=1, column=0, sticky=tk.NW)

        cb_var1 = tk.IntVar()

        tk.Label(frame1, text="Scrivi il n. delle figurine separate da spazio").grid(row=0, sticky=tk.EW)

        tk.Label(frame1, text="Figurine da aggiungere").grid(row=1, sticky=tk.W)
        tk.Label(frame1, text="Figurine da togliere").grid(row=2, sticky=tk.W)
        self.var1 = tk.StringVar()
        entry1 = tk.Entry(frame1, textvariable = self.var1)
        entry1.grid(row=1, column=1, sticky=tk.E)
        self.var2 = tk.StringVar()
        entry2 = tk.Entry(frame1,textvariable = self.var2)
        entry2.grid(row=2, column=1, sticky=tk.E)
        button1 = tk.Button(frame1, text="Aggiungi", command=self.rich_aggiungi)
        button1.grid(row=1, column=2, sticky=tk.E)
        button2 = tk.Button(frame1, text="Togli", command=self.rich_togli)
        button2.grid(row=2, column=2, sticky=tk.E)


        label2 = tk.Label(master_frame, text="Frame2 Contents", bg=LABEL_BG)
        label2.grid(row=2, column=0, pady=5, sticky=tk.NW)

        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(master_frame)
        frame2.grid(row=3, column=0, sticky=tk.NW)

        # Add a canvas in that frame.
        canvas = tk.Canvas(frame2, bg="Yellow")
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="Red", bd=2)

        # Add the buttons to the frame.
        img_array = []
        for i in carte:
            if carte[i] == 0:
                img_array.append("linus-"+str(i).zfill(2)+"-t.png")
            else:
                img_array.append("linus-"+str(i).zfill(2)+".png")

        count = 0
        self.button = [tk.Button() for _ in range(16)]

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                f_name = img_array[count]
                fig=tk.PhotoImage(file=f_name)
                self.button[count] = tk.Button(buttons_frame, padx=7, pady=7, image=fig, text="fig#%d, %d" % (count + 1, carte[count + 1]), compound="left")
                self.button[count].image = fig
                self.button[count].grid(row=i, column=j, sticky='news')
                count = count + 1

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        #print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)




        label3 = tk.Label(master_frame, text="Frame3 Contents", bg=LABEL_BG)
        label3.grid(row=4, column=0, pady=5, sticky=tk.NW)

        frame3 = tk.Frame(master_frame, bg="Blue", bd=2, relief=tk.GROOVE)
        frame3.grid(row=5, column=0, sticky=tk.NW)

        cb_var2 = tk.IntVar()
        checkbutton2 = tk.Checkbutton(frame3, text="EndCheckBox", variable=cb_var2)
        checkbutton2.grid(row=0, column=0, padx=2)

    def rich_aggiungi(self):
        n_carta = int(self.var1.get())
        myalbum.add_carta(n_carta)
        quant_carta = carte[n_carta]
        if quant_carta == 0:
            fig=tk.PhotoImage(file="linus-"+str(n_carta).zfill(2)+"-t.png")
            self.button[n_carta-1].config(image=fig)
            self.button[n_carta-1].config(text="fig#%d, %d" % (n_carta, quant_carta))
            self.button[n_carta-1].image=fig
        else:
            fig=tk.PhotoImage(file="linus-"+str(n_carta).zfill(2)+".png")
            self.button[n_carta-1].config(image=fig)
            self.button[n_carta-1].config(text="fig#%d, %d" % (n_carta, quant_carta))
            self.button[n_carta-1].image=fig




    def rich_togli(self):
        n_carta = int(self.var2.get())
        myalbum.sottrai_carta(n_carta)
        self.button[n_carta-1].config(text="fig#%d, %d" % (n_carta, carte[n_carta]))
        quant_carta = carte[n_carta]
        if quant_carta == 0:
            fig=tk.PhotoImage(file="linus-"+str(n_carta).zfill(2)+"-t.png")
            self.button[n_carta-1].config(image=fig)
            self.button[n_carta-1].config(text="fig#%d, %d" % (n_carta, quant_carta))
            self.button[n_carta-1].image=fig
        else:
            fig=tk.PhotoImage(file="linus-"+str(n_carta).zfill(2)+".png")
            self.button[n_carta-1].config(image=fig)
            self.button[n_carta-1].config(text="fig#%d, %d" % (n_carta, quant_carta))
            self.button[n_carta-1].image=fig






if __name__ == "__main__":
    app = MyApp("Album Figurine")
    app.mainloop()
