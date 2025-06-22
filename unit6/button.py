import tkinter as tk


def button_pressed(root):
    image = tk.PhotoImage(file="coffe.png")
    image_label = tk.Label(root, image=image)
    image_label.pack(side="bottom")
    image_label.image = image


def main():
    root = tk.Tk()
    lbl = tk.Label(root, text="Whats the only non passport picture i found on my computer?", fg="purple")
    lbl.pack(side="top")
    button = tk.Button(root, text="click to find out!",
                 command=lambda: button_pressed(root),
                 padx=10,
                 pady=5,
                 width=15)
    button.pack(padx=20, pady=20)
    root.mainloop()


if __name__ == '__main__':
    main()
