import tkinter as tk

latin_cyrillic = {
     'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф',
     'g': 'г', 'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к',
     'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
     'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у',
     'v': 'в', 'x': 'х', 'y': 'й', 'z': 'з',
     'A': 'А', 'B': 'Б', 'D': 'Д', 'E': 'Е', 'F': 'Ф',
     'G': 'Г', 'H': 'Ҳ', 'I': 'И', 'J': 'Ж', 'K': 'К',
     'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
     'Q': 'Қ', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У',
     'V': 'В', 'X': 'Х', 'Y': 'Й', 'Z': 'З'
}

latin_cyrillic2 = {
    'ch':'ч', 'sh':'ш', 'o\'':'ў', 'g\'':'ғ',
    'yu':'ю', 'ya':'я', ' e':' э', 'yo':'ё',
    'Ch':'Ч', 'Sh':'Ш', 'O\'':'Ў', 'G\'':'Ғ',
    'Yu':'Ю', 'Ya':'Я', ' E':' Э', 'Yo':'Ё'
}

def translate_text():
    s = input_text.get("1.0", tk.END).strip()
    a = ""
    n = len(s)
    i = 0
    if s[0] == 'e':
        a += 'э'
        i += 1
    elif s[0] == 'E':
        a += 'Э'
        i += 1
    elif s[0:2] == 'ye':
        a += 'е'
        i += 2
    elif s[0:2] == 'YE' or s[0:2] == 'Ye':
        a += 'Е'
        i += 2

    while i < n:

        

        if s[i:i+3] == ' ye':
            a += ' е'
            i += 3
        elif s[i:i+3] == ' YE' or s[i:i+3] == ' Ye':
            a += ' Е'
            i += 3

        elif i + 2 <= n and s[i:i+2] in latin_cyrillic2:
            a += latin_cyrillic2[s[i:i+2]]
            i += 2
        else:
            if s[i] in latin_cyrillic:
                a += latin_cyrillic[s[i]]
            else:
                a += s[i]
            i += 1

    chiqar_text.delete("1.0", tk.END)
    chiqar_text.insert(tk.END, a)


oyna = tk.Tk()
oyna.title("Lotin Krill o^giruvchisi")


input_label = tk.Label(oyna, text="Textni kiriting Lotinda:")
input_label.pack()
input_text = tk.Text(oyna, height=10, width=50)
input_text.pack()


translate_button = tk.Button(oyna, text="Tarjima", command=translate_text)
translate_button.pack()
chiqar_label = tk.Label(oyna, text="Krill text:")
chiqar_label.pack()
chiqar_text = tk.Text(oyna, height=10, width=50)
chiqar_text.pack()


oyna.mainloop()

# BEKFURR SINCE 2024
# 10.26.2024
