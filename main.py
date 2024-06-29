import pyautogui
import datetime
import time
import string

CODE = "RIY8 B5X- -CH5Y NQLMH"
# possible code "RIY8 B5X- -CH5Y NQLMH"

CHARSET = string.ascii_uppercase + string.digits

# pyautogui is overwhelmed without delays?
pyautogui.PAUSE = 0.03
WRITE_INTERVAL = 0.02

# Estimate the run time
time_per_combination = (3 * pyautogui.PAUSE * 1.025) + (len(CODE) * WRITE_INTERVAL * 1.025)

total_time = round(time_per_combination * (36 * 36), 2)  # 36 * 36 = 1296 combinations
total_time_timedelta = datetime.timedelta(seconds=total_time)

print("Estimated time: " + str(total_time_timedelta))  # Format in HH:MM:SS

print("Starting in 2 seconds, focus on the input field!")
time.sleep(2)

for first_char in CHARSET:
    for second_char in CHARSET:
        pyautogui.hotkey("ctrl", "a")
        print("> ctrl + a")

        pyautogui.press('backspace')
        print("> backspace")

        temp_code = CODE.replace("- -", first_char + " " + second_char)
        pyautogui.write(temp_code, interval=WRITE_INTERVAL)
        print("> .write() " + temp_code)

        pyautogui.press('enter')
        print("> enter")
