import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt():
    try:
        text = entry_text.get("1.0", tk.END).strip()
        shift = int(entry_shift.get())
        result = caesar_cipher_encrypt(text, shift)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")

def decrypt():
    try:
        text = entry_text.get("1.0", tk.END).strip()
        shift = int(entry_shift.get())
        result = caesar_cipher_decrypt(text, shift)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the widgets
label_text = tk.Label(root, text="Enter the message:")
label_text.pack()

entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.pack()

entry_shift = tk.Entry(root)
entry_shift.pack()

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_encrypt.pack()

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

entry_result = tk.Text(root, height=5, width=40)
entry_result.pack()

# Run the application
root.mainloop()
