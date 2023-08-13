from pynput.mouse import Listener

selection_started = False
x1, y1, x2, y2 = 0, 0, 0, 0


def on_click(x, y, button, pressed):
    global selection_started, x1, y1, x2, y2

    if pressed:
        if not selection_started:
            x1, y1 = x, y
            selection_started = True
        else:
            x2, y2 = x, y
            selection_started = False
            print(f"Selected region: x1={x1}, y1={y1}, x2={x2}, y2={y2}")


with Listener(on_click=on_click) as listener:
    listener.join()
