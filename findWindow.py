import win32api, win32gui

save = win32gui.FindWindow(None, "Adobe Connect")

(left, top, right, bottom) = win32gui.GetWindowRect(save)

position = (left, top, right, bottom)

print(position)


