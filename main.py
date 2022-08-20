from tkinter import END, Tk, Frame, Listbox, StringVar
from tkinter.ttk import Button, Entry
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showinfo
from os import walk, rename
from os.path import join


# =================================================================================== FUNCIONES 
def findFolder():
    global diccFiles
    diccFiles = {}
    folder = askdirectory(title='Select Folder')
    if folder == "": return
    listOrig.delete(0, END)
    for (root, dirs, files) in walk(folder):
        diccFiles[root] = files
        for fl in files:
            listOrig.insert(END, fl)
# ------------------------------------------------------------------ MOSTRAR RESULTADO
def showResult():
    global diccMod
    diccMod = {}
    listModf.delete(0, END)
    for values in diccFiles.items():
        lsMod = []
        for file in values[1]:
            lsMod.append(file[:-4].replace('.', ' ').replace(str1.get(), "")+file[-4:])
            listModf.insert(END, file[:-4].replace('.', ' ').replace(str1.get(), "")+file[-4:])
        diccMod[values[0]] = lsMod
# ------------------------------------------------------------------ RENOMBRAR
def renameFiles():
    switch = askyesno("WARNING", "Are you sure you want to continue?")
    for oldDict, newDict in zip(diccFiles.items(), diccMod.items()):
        for oldfiles, newfiles in zip(oldDict[1], newDict[1]):
            print(switch)
    showinfo("Information", "Successfully renamed files")
    
# =================================================================================== INTERFAZ
root = Tk()
root.title('Creado por: Rey')
root.resizable(0,0)
# =================================================================================== STRING VARIABLES
str1 = StringVar()
str2 = StringVar()
str3 = StringVar()
str4 = StringVar()
# ------------------------------------------------------------------ MARCO
Marco = Frame(root)
Marco.pack(expand=True, fill='both')
# ------------------------------------------------------------------ BOTONES
LoadFolder = Button(Marco, text="Select Folder", width=20, command=findFolder)
Preview = Button(Marco, text="Preview", width=20, command=showResult)
Rename = Button(Marco, text="Rename", width=20, command=renameFiles)
# ------------------------------------------------------------------ UBICACION BOTONES
LoadFolder.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
Preview.grid(row=1, column=2, padx=10, pady=10, columnspan=2)
Rename.grid(row=1, column=3, padx=10, pady=10, columnspan=2)
# ------------------------------------------------------------------ ENTRADA DE TEXTO
ent1 = Entry(Marco, textvariable=str1)
ent2 = Entry(Marco, textvariable=str2)
ent3 = Entry(Marco, textvariable=str3)
ent4 = Entry(Marco, textvariable=str4)
# ------------------------------------------------------------------ UBICACION ENTRADAS
ent1.grid(row=2, column=1, padx=10, pady=10, sticky='we')
ent2.grid(row=2, column=2, padx=10, pady=10, sticky='we')
ent3.grid(row=2, column=3, padx=10, pady=10, sticky='we')
ent4.grid(row=2, column=4, padx=10, pady=10, sticky='we')
# ------------------------------------------------------------------ Listas
listOrig = Listbox(Marco, height=20, font=('JetBrains Mono', 11), width=40)
listModf = Listbox(Marco, height=20, font=('JetBrains Mono', 11), width=40)
# ------------------------------------------------------------------ UBICACION
listOrig.grid(row=3, column=1, columnspan=2, sticky='nswe', padx=2, pady=5)
listModf.grid(row=3, column=3, columnspan=2, sticky='nswe', padx=2, pady=5)

root.mainloop()