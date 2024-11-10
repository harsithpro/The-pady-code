import tkinter as tk
def convert_inch_to_cm():
    try:
        # Get the value from the entry widget
        inches = float(entry_inch.get())
        
        # Convert inches to centimeters (1 inch = 2.54 cm)
        centimeters = inches * 2.54
        
        # Display the result in the result_label
        result_label.config(text=f"{inches} inches is equal to {centimeters:.2f} cm")
    except ValueError:
        # Handle the case where the input is not a valid number
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Create a label for the input field
label_inch = tk.Label(root, text="Enter length in inches:")
label_inch.pack(pady=10)

# Create an entry widget for user input
entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_inch_to_cm)
convert_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()