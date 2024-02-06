import tkinter as tk

def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

def binary_to_decimal(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

def convert_button_clicked():
    try:
        if conversion_type.get() == "Decimal to Binary":
            decimal_input = int(entry.get())
            result_label.config(text=f"Binary representation: {decimal_to_binary(decimal_input)}", fg="green")
        elif conversion_type.get() == "Binary to Decimal":
            binary_input = entry.get()
            result_label.config(text=f"Decimal representation: {binary_to_decimal(binary_input)}", fg="green")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.", fg="red")

# Create the main window
app = tk.Tk()
app.title("Number Converter")
app.geometry("400x250")  # Set initial window size

# Configure styles
app.configure(bg="#f0f0f0")  # Set background color

# Create and place widgets with some basic styling
label = tk.Label(app, text="Enter a number:", bg="#f0f0f0", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(app, font=("Arial", 12))
entry.pack(pady=10)

conversion_type = tk.StringVar()
conversion_type.set("Decimal to Binary")  # Default conversion type

conversion_dropdown = tk.OptionMenu(app, conversion_type, "Decimal to Binary", "Binary to Decimal")
conversion_dropdown.config(font=("Arial", 12), bg="#4CAF50", fg="white")
conversion_dropdown.pack(pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_button_clicked, font=("Arial", 12), bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the application
app.mainloop()
