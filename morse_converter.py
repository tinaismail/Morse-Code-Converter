from pysine import sine
import tkinter as tk
import time

unit=0.1
duration=[unit,unit*3,unit,unit*3,unit*7]

def morse():
    morse_coded=""
    text=ent_text.get()
    for letter in text:
        morse_coded+=code[letter]+"O"
    morse_read=morse_coded
    morse_read=morse_read.replace('O',' ')
    morse_read=morse_read.replace('X','  ')
    lbl_result["text"] = morse_read
    return morse_coded

def letshearit():
    play=[]
    #this is for single words
    for ditdah in morse():
        if ditdah==".":
            sineFreq(duration[0])
            time.sleep(duration[2])#between symbols of the same letter
        elif ditdah=="-":
            sineFreq(duration[1])
            time.sleep(duration[2])#between symbols of the same letter
        elif ditdah=="O":#between letters
            time.sleep(duration[3])
        elif ditdah=="X":#between words
            time.sleep(duration[4])

def sineFreq(duration):
    frequency=800
    return sine(frequency, duration)

# Morse Code Dictionary
code= {
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "0": "-----",
  " ": "X"
}

window = tk.Tk()
window.title("Plain Text to Morse Code Converter")

window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_text=tk.Entry(master=frm_entry,width=20)
lbl_morse=tk.Label(master=frm_entry,text="MORSIFY")
ent_text.grid(row=0, column=0, sticky="e")
btn_convert = tk.Button(
    master=window,
    text="MORSIFY",
    command=morse
)

btn_play=tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=letshearit
)

lbl_result = tk.Label(master=window, text="")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
btn_play.grid(row=1,column=2,padx=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
