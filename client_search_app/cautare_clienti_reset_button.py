import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


# Funcție pentru citirea fișierului și căutarea clientului
def cauta_client():
    nume_client = entry_nume.get().strip().upper()  # Obține textul din câmp și transformă în majuscule pentru potrivire
    text_afisare.delete(1.0, tk.END)  # Șterge textul existent din câmpul de afișare

    if not nume_client:
        messagebox.showwarning("Atenție", "Introduceți un nume de client pentru căutare.")
        return

    gasit = False
    with open("revizii.txt", "r") as f:  # Deschide fișierul pentru citire
        for linie in f:
            if nume_client in linie:  # Verifică dacă numele clientului se află în linie
                text_afisare.insert(tk.END, linie)  # Afișează linia în câmpul de text
                gasit = True

    if not gasit:
        messagebox.showinfo("Rezultat căutare", f"Clientul '{nume_client}' nu a fost găsit.")


# Funcție pentru resetarea câmpurilor de căutare și afișare
def resetare_campuri():
    entry_nume.delete(0, tk.END)  # Golește câmpul de căutare
    text_afisare.delete(1.0, tk.END)  # Golește câmpul de afișare a rezultatelor


# Creare fereastră principală
root = tk.Tk()
root.title("Căutare Client")

# Câmpul pentru introducerea numelui clientului
label_nume = tk.Label(root, text="Introduceți numele clientului:")
label_nume.pack(pady=5)
entry_nume = tk.Entry(root, width=50)
entry_nume.pack(pady=5)

# Butonul pentru a porni căutarea
buton_cauta = tk.Button(root, text="Caută Client", command=cauta_client)
buton_cauta.pack(pady=10)

# Butonul pentru resetarea câmpurilor
buton_resetare = tk.Button(root, text="Resetare", command=resetare_campuri)
buton_resetare.pack(pady=5)

# Câmpul pentru afișarea rezultatelor
text_afisare = scrolledtext.ScrolledText(root, width=80, height=10)
text_afisare.pack(pady=10)

# Rularea interfeței grafice
root.mainloop()
