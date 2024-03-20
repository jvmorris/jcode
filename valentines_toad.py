import tkinter as tk
from tkinter import messagebox

def show_toad_image():
    global toad_image, toad_label
    # Load Toad image
    toad_image_path = 'toad_image.png'  # Replace with the correct file name or path
    toad_image = tk.PhotoImage(file=toad_image_path)
    toad_label = tk.Label(root, image=toad_image)
    toad_label.pack()
    root.after(2000, ask_to_valentines)

def ask_to_valentines():
    global yes_image, no_image
    toad_label.pack_forget()  # Remove the Toad image widget
    response = messagebox.askquestion("Valentine's Day Invitation", "Hey specialK, Life with you is an adventure like Mario's journey in the Mushroom Kingdom.🍄✨\nWill you be my Player 2 and power me up?")
    if response == 'yes':
        yes_image = tk.PhotoImage(file='yes_image.png')  # Replace with the actual file name
        show_response_image(yes_image)
    else:
        no_image = tk.PhotoImage(file='no_image.png')  # Replace with the actual file name
        show_response_image(no_image)

def show_response_image(image):
    answer_label.config(image=image)
    answer_label.image = image  # Keep a reference to the image
    root.after(2000, lambda: answer_label.pack_forget())  # After 2 seconds, remove the response image widget

# Create the main window
root = tk.Tk()
root.title("Toad's Valentine's Day")

# Create labels for Toad and response images
toad_label = None  # Initialize toad_label variable
answer_label = tk.Label(root)
answer_label.pack()

# Start the sequence by showing Toad image
show_toad_image()

# Run the application
root.mainloop()

