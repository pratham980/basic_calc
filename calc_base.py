# def calculator():

#     num1 = float(input("enter your first no."))
    
#     num2 = float(input("enter your second no."))

#     operators = input("enter your operator")

#     if operators == "+":
#         print(num1 + num2)

#     elif operators == "*":
#         print(num1 * num2)

#     elif operators == "-":
#         print(num1 - num2)
    
#     elif operators == "/":
#         print(num1 / num2)

#     else:
#         return 0

# print(calculator())
    


 
    
import tkinter as tk

def calculator(op):
    """Performs calculation based on selected operator"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: /0")
    except ValueError:
        result.set("Invalid input")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Number 1").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Buttons
tk.Button(root, text="+", command=lambda: calculator("+")).grid(row=2, column=0)
tk.Button(root, text="-", command=lambda: calculator("-")).grid(row=2, column=1)
tk.Button(root, text="*", command=lambda: calculator("*")).grid(row=3, column=0)
tk.Button(root, text="/", command=lambda: calculator("/")).grid(row=3, column=1)

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Label(root, textvariable=result).grid(row=4, column=1)

root.mainloop()
