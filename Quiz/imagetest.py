from tkinter import *

def test_image_display(image_path):
    test_window = Tk()
    test_window.title("Test Image Display")

    # Load image
    img = PhotoImage(file=image_path)

    # Display image in a label
    label = Label(test_window, image=img)
    label.pack()

    test_window.mainloop()

if __name__ == "__main__":
    image_path = "./images/globe2.png"
    test_image_display(image_path)
