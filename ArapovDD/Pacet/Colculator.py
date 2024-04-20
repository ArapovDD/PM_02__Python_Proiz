import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = variable.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка: деление на ноль"
        else:
            result = "Ошибка: неверная операция"

        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Ошибка: введите числа")

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")

# Создание меток и полей для ввода чисел
label_num1 = tk.Label(root, text="Число 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text="Число 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Создание выпадающего списка для выбора операции
label_operation = tk.Label(root, text="Операция:")
label_operation.grid(row=2, column=0, padx=5, pady=5)
operations = ["+", "-", "*", "/"]
variable = tk.StringVar(root)
variable.set("+")
dropdown = tk.OptionMenu(root, variable, *operations)
dropdown.grid(row=2, column=1, padx=5, pady=5)

# Создание кнопки для выполнения вычислений
button_calculate = tk.Button(root, text="Вычислить", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Метка для вывода результата
label_result = tk.Label(root, text="Результат:")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Запуск главного цикла
root.mainloop()
