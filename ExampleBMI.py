from tkinter import *

window = Tk()
window.config(width=340, height=260)

FONT = ('Arial', 10, "normal")

def ekran_sonuc():
    kilon_text = entry_weight.get()
    boyun_text = entry_height.get()


    if kilon_text.isdigit() and boyun_text.isdigit():
        age = float(kilon_text)
        weight = float(boyun_text) / 100

        bmi = age / (weight ** 2)

        #sonuc_label.config(text=f"sonuc: {bmi}")

        if bmi >= 18 and bmi < 25:
            sonuc_label.config(text=f"bmi: {bmi} Normalsin")

        elif bmi >= 25 and bmi < 30:
            sonuc_label.config(text=f"bmi: {bmi} Biraz kilolusun")

        elif bmi >= 30 and bmi < 40:
            sonuc_label.config(text=f"bmi: {bmi} Obezsin !!!!!")

        elif bmi >= 40:
            sonuc_label.config(text=f"bmi: {bmi} ULTRA Obezsin !!!!!")

    elif kilon_text == "" or boyun_text == "":
        #print("lütfen kilonuzu veya yaşınızı giribiz")
        sonuc_label.config(text="lütfen kilonuzu veya yaşınızı giribiz")

label_weight = Label()
label_weight.config(text="Enter Your Age (kg)", font=FONT)
label_weight.pack()

entry_weight = Entry()
entry_weight.config(width=15)
entry_weight.pack()

label_height = Label()
label_height.config(text="Enter Your height (kg)", font=FONT)
label_height.pack()

entry_height = Entry()
entry_height.config(width=15)
entry_height.pack()

button = Button()
button.config(text="Calcute", command=ekran_sonuc)
button.pack()

sonuc_label = Label()
sonuc_label.config(text="sonuc")
sonuc_label.config(pady=20)
sonuc_label.pack()









window.mainloop()