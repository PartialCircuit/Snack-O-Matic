import tkinter as tk
import random 
SNACKS = [ "Pizza. Obviously.", 
          "A bowl of cereal at midnight.", 
          "Leftover pasta from yesterday.", 
          "Chocolate. No questions asked.",
          "Toast with way too much butter.", 
          "Just water. Boring, but healthy.", ] 
def on_click(): label.config(text=random.choice(SNACKS)) 
print("Welcome to Snack-O-Matic!")
root = tk.Tk() 
root.title("Snack-O-Matic") 
root.geometry("400x250") 

label = tk.Label(root, text="Hungry? Let fate decide.", 
                 font=("Arial", 12), wraplength=350) 
label.pack(pady=30) 
button = tk.Button(root, text="Decide my snack", command=on_click)
button.pack() 
root.mainloop() 




