import tkinter as tk
print("Welcome to Snack-O-Matic!")
root = tk.Tk() 
root.title("Snack-O-Matic") 
root.geometry("400x250") 

label = tk.Label(root, text="Hungry? Let fate decide.", 
                 font=("Arial", 12), wraplength=350) 
label.pack(pady=30) 
root.mainloop() 




