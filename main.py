# AlaXul Aimdot Python script. Ver: 0.0000001

import time
import win32gui
# import threading


def thread_func():
    """ gta v """
    # x = int(960)  # 1920 / 2 = 960 for X position on screen.
    # y = int(548)  # 1200 / 2 = 600 for Y position on screen.
    # color = int(255)  # Pixel color, 255 = Red

    # """ cs go """
    x = int(960)  # 1920 / 2 = 960 for X position on screen. <>
    y = int(540)  # 1200 / 2 = 600 for Y position on screen. ^
    color = int(255)  # Pixel color, 255 = Red
    while True:
        try:
            # x = int(958)  # 1920 / 2 = 960 for X position on screen.
            # y = int(559)  # 1200 / 2 = 600 for Y position on screen.
            # color = int(255)  # Pixel color, 255 = Red
            hwnd = win32gui.WindowFromPoint((x, y))
            hdc = win32gui.GetDC(hwnd)
            x1, y1 = win32gui.ScreenToClient(hwnd, (x, y))
            win32gui.SetPixel(hdc, x1, y1, color)
            win32gui.SetPixel(hdc, x1 - 1, y1, color)
            win32gui.SetPixel(hdc, x1 + 1, y1, color)
            win32gui.SetPixel(hdc, x1, y1 - 1, color)
            win32gui.SetPixel(hdc, x1, y1 + 1, color)
            win32gui.SetPixel(hdc, x1 - 1, y1 - 1, color)
            win32gui.SetPixel(hdc, x1 + 1, y1 + 1, color)
            win32gui.SetPixel(hdc, x1 - 1, y1 + 1, color)
            win32gui.SetPixel(hdc, x1 + 1, y1 - 1, color)

            win32gui.SetPixel(hdc, x1 - 2, y1, color)
            win32gui.SetPixel(hdc, x1 + 2, y1, color)
            win32gui.SetPixel(hdc, x1, y1 - 2, color)
            win32gui.SetPixel(hdc, x1, y1 + 2, color)
            win32gui.SetPixel(hdc, x1 - 2, y1 - 2, color)
            win32gui.SetPixel(hdc, x1 + 2, y1 + 2, color)
            win32gui.SetPixel(hdc, x1 - 2, y1 + 2, color)
            win32gui.SetPixel(hdc, x1 + 2, y1 - 2, color)

            # break
            win32gui.ReleaseDC(hwnd, hdc)

        # time.sleep(1)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    time.sleep(4)
    # x = threading.Thread(target=thread_func, args=())
    # x.start()
    thread_func()
