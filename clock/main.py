import tkinter as ui
import time
import math

window = ui.Tk()

window.geometry("400x400")


def update_clock():
    second = int(time.strftime("%S"))
    minute = int(time.strftime("%M"))
    hour = int(time.strftime("%I"))

#     Clock hand motion
    second_x = second_hand_len * math.sin(math.radians(second * 6)) + center_x
    second_y = -1 * second_hand_len * math.cos(math.radians(second * 6)) + center_y
    canvas.coords(second_hand, center_x, center_y, second_x, second_y)

    minute_x = minute_hand_len * math.sin(math.radians(minute * 6)) + center_x
    minute_y = -1 * minute_hand_len * math.cos(math.radians(minute * 6)) + center_y
    canvas.coords(minute_hand, center_x, center_y, minute_x, minute_y)

    hour_x = hour_hand_len * math.sin(math.radians(hour * 6)) + center_x
    hour_y = -1 * hour_hand_len * math.cos(math.radians(hour * 6)) + center_y
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)

    window.after(1000, update_clock)


canvas = ui.Canvas(window, width=400, height=400, bg="black")
# canvas.pack(expand=True, fiil='both')
canvas.pack()

bg = ui.PhotoImage(file='clock.png')
canvas.create_image(200, 200, image=bg)

# creating clock hands
center_x = 200
center_y = 200
second_hand_len = 105
minute_hand_len = 95
hour_hand_len = 65

# Draw clock hand
second_hand = canvas.create_line(200,200, 200 + second_hand_len, 200 + second_hand_len, width=1.5, fill='red')
minute_hand = canvas.create_line(200,200, 200 + minute_hand_len, 200 + minute_hand_len, width=2, fill='white')
hour_hand = canvas.create_line(200,200, 200 + hour_hand_len, 200 + hour_hand_len, width=2.5, fill='white')

update_clock()
window.mainloop()
