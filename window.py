import tkinter as tk


def create_window():
    root = tk.Tk()
    root.title("GIF Creator")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - 300)
    center_y = int(screen_height / 2 - 200)

    root.geometry(f'600x400+{center_x}+{center_y}')

    root.mainloop()


# def get_coordinates()
# def get_user_delay()