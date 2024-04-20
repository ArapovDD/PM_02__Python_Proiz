import tkinter as tk
from tkinter import messagebox  # Импорт функции messagebox из модуля tkinter
from PIL import Image, ImageTk
import os
import time

def change_background():
    global current_background_index
    current_background_index = (current_background_index + 1) % len(backgrounds)
    image_path = os.path.join(os.getcwd(), backgrounds[current_background_index])
    load = Image.open(image_path)
    render = ImageTk.PhotoImage(load)
    img_label.configure(image=render)
    img_label.image = render
    root.after(7000, change_background)  # Change background every 7 seconds

def request_call():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        # Placeholder action - print name and phone
        print("Name:", name)
        print("Phone:", phone)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        messagebox.showinfo("Успешно", "Ваш запрос на звонок отправлен.")
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите имя и номер телефона.")

# Инициализация главного окна
root = tk.Tk()
root.title("Запросить звонок")
root.geometry("400x300")

# Список файлов для фона
backgrounds = ["fon1.png", "fon2.png"]
current_background_index = 0

# Задание начального фона
image_path = os.path.join(os.getcwd(), backgrounds[current_background_index])
load = Image.open(image_path)
render = ImageTk.PhotoImage(load)
img_label = tk.Label(root, image=render)
img_label.place(x=0, y=0, relwidth=1, relheight=1)

# Форма для ввода имени и номера телефона
frame_form = tk.Frame(root, bg="white", bd=2)
frame_form.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_name = tk.Label(frame_form, text="Имя:", bg="white")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_form, text="Телефон:", bg="white")
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_form)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

button_request = tk.Button(frame_form, text="Запросить звонок", command=request_call)
button_request.grid(row=2, columnspan=2, padx=5, pady=5)

# Запуск смены фона
change_background()

# Запуск главного цикла
root.mainloop()
