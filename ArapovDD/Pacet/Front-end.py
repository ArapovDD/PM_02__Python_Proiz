import tkinter as tk
from tkinter import messagebox

def say_hello():
    name = entry.get()
    if name:
        messagebox.showinfo("Привет", "Привет, " + name)
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите ваше имя.")

def confirm_exit():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

# Создание главного окна
root = tk.Tk()
root.title("Приветствие")

# Создание метки и поля для ввода имени
label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Создание кнопки "Привет"
button_hello = tk.Button(root, text="Привет", command=say_hello)
button_hello.pack(pady=5)

# Создание кнопки "Выход"
button_exit = tk.Button(root, text="Выход", command=confirm_exit)
button_exit.pack(pady=5)

# Запуск главного цикла
root.mainloop()
