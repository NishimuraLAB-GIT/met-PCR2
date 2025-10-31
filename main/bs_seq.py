import os,sys

from test import Exe
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def batchfiledialog_clicked():
    fType = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetypes=fType, initialdir=iFile)
    batch.set(iFilePath)

def fastqfiledialog():
    fType = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetypes=fType, initialdir=iFile)
    fastq.set(iFilePath)
    name = fastq.get().split("/")[-1]
    print(name)

def outputdir_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    output.set(iDirPath)

def conductMain():
    print("run")
    exe = Exe(fastq.get(), batch.get(), output.get())
    exe.run()
    exit()

if __name__ == "__main__":

    root = Tk()
    root.title("BS-seq")

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    BatchLabel = ttk.Label(frame1, text="select Batch", padding=(5,2))
    BatchLabel.pack(side=LEFT)

    batch = StringVar()
    # batch_name = batch.split("/")[-1]
    IFileEntry = ttk.Entry(frame1, textvariable=batch, width=30)
    IFileEntry.pack(side=LEFT)

    BatchButton = ttk.Button(frame1, text="browse", command=batchfiledialog_clicked)
    BatchButton.pack(side=LEFT)

    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    FastqLabel = ttk.Label(frame2, text="select fastq", padding=(5,2))
    FastqLabel.pack(side=LEFT)

    fastq = StringVar()
    fastqEntry = ttk.Entry(frame2, textvariable=fastq, width=30)
    fastqEntry.pack(side=LEFT)

    FastqButton = ttk.Button(frame2, text="browse", command=fastqfiledialog)
    FastqButton.pack(side=LEFT)

    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=4, column=1, sticky=E)

    outputLabel = ttk.Label(frame3, text="output folder", padding=(5,2))
    outputLabel.pack(side=LEFT)

    output = StringVar()
    outputEntry = ttk.Entry(frame3, textvariable=output, width=30)
    outputEntry.pack(side=LEFT)

    outputButton = ttk.Button(frame3, text="browse", command=outputdir_clicked)
    outputButton.pack(side=LEFT)

    frame_end = ttk.Frame(root, padding=10)
    frame_end.grid(row=5, column=1, sticky=W)

    buttun_run = ttk.Button(frame_end, text="run", command=conductMain)
    buttun_run.pack(fill="x", padx=30, side="left")

    buttun_quit = ttk.Button(frame_end, text="cancel", command=quit)
    buttun_quit.pack(fill="x", padx=30, side="left")

    root.mainloop()