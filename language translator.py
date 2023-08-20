from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator, LANGUAGES
from ttkwidgets.autocomplete import AutocompleteCombobox

root = Tk()
root.title("Language Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="blue4")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(500, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# icon
image_icon = PhotoImage(file="Google_Translate_logo.svg.png")
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
langl = language.keys()

# first autocomplete combobox
combo1 = AutocompleteCombobox(root, completevalues=languageV, font="calibri 14")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# second autocomplete combobox
combo2 = AutocompleteCombobox(root, completevalues=languageV, font="Roboto 14")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# first frame
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar1.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(root, text="Translate", font=("roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="aliceblue", fg="black", command=translate_now)
translate.place(x=476, y=250)

label_change()
root.mainloop()
