import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("shop search")

ttk.Label(win, text="Select district :").grid(column=0, row=0)


def search():
    action.configure(text="SEARCH")
    if areaEntered.get() == '香港島':
        print("香港島")
    elif areaEntered.get() == '新界及離島':
        print("新界及離島")
        if district1Chosen.get() == ' ':
            print(" ")
        elif district1Chosen.get() == '葵青區':
            print("11qwe")
        elif district1Chosen.get() == '荃灣區':
            print("22qwe")
        elif district1Chosen.get() == '屯門區':
            print("33qwe")
        elif district1Chosen.get() == '元朗區':
            print("44qwe")
        elif district1Chosen.get() == '北區':
            print("55qwe")
        elif district1Chosen.get() == '大埔區':
            print("66qwe")
        elif district1Chosen.get() == '沙田區':
            print("77qwe")
        elif district1Chosen.get() == '西貢區':
            print("88qwe")
        elif district1Chosen.get() == '離島區':
            print("99qwe")
    elif areaEntered.get() == '九龍':
        print("九龍")
        if districtChosen.get() == ' ':
            print(" ")
        elif districtChosen.get() == '油尖旺區':
            print("1qwe")
        elif districtChosen.get() == '深水埗區':
            print("2qwe")
        elif districtChosen.get() == '九龍城區':
            print("3qwe")
        elif districtChosen.get() == '黃大仙區':
            print("4qwe")
        elif districtChosen.get() == '觀塘區':
            print("5qwe")


area = tk.StringVar()
areaEntered = ttk.Combobox(win, width=30, textvariable=area, state='readonly')
areaEntered['values'] = ('香港島', '新界及離島', '九龍')
areaEntered.grid(column=0, row=1)
areaEntered.current(1)

district = tk.StringVar()
districtChosen = ttk.Combobox(win, width=30, state='readonly')
districtChosen['values'] = ('油尖旺區  ', '深水埗區', '九龍城區', '黃大仙區', '觀塘區')
districtChosen.grid(column=0, row=2)
districtChosen.current(1)

district1 = tk.StringVar()
district1Chosen = ttk.Combobox(win, width=30, state='readonly')
district1Chosen['values'] = (
    '葵青區', '荃灣區', '屯門區', '元朗區', '北區', '大埔區', '沙田區', '西貢區', '離島區')
district1Chosen.grid(column=0, row=2)
district1Chosen.current(1)

action = ttk.Button(win, text="SEARCH", command=search)
action.grid(column=2, row=1)

win.mainloop()
