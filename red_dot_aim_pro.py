import tkinter as tk
import ctypes


def make_window_clickthrough(hwnd):
    # Make the window click-through
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x80000
    WS_EX_TRANSPARENT = 0x20

    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_style | WS_EX_LAYERED | WS_EX_TRANSPARENT)


def create_aiming_helper():
    # Create a transparent window
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")

    # Get screen width and height using Tkinter
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Create a canvas to draw the dot
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white", highlightthickness=0)
    canvas.pack()

    # Draw the red dot in the center of the screen
    dot_size = 1.5
    center_x = screen_width // 2
    center_y = screen_height // 2
    canvas.create_oval(center_x - dot_size, center_y - dot_size,
                       center_x + dot_size, center_y + dot_size,
                       fill="red", outline="red")

    # Keep the window on top and transparent
    root.lift()
    root.attributes("-topmost", True)
    root.attributes("-disabled", True)  # Makes the window click-through in Tkinter
    root.attributes("-transparentcolor", "white")

    # Make the window click-through at the OS level (Windows specific)
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    make_window_clickthrough(hwnd)

    root.mainloop()


if __name__ == "__main__":
    create_aiming_helper()
