import PySimpleGUI as sg

sg.theme("DarkAmber")  
layout = [
    [sg.Text("Need to get some names from you")],
    [sg.Text("Name?"), sg.InputText()],
    [sg.Button("Ok"), sg.Button("Fini")],
]

names = []

window = sg.Window("Window Title", layout)
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Fini"
    ):
        break
    names.append(values[0])

print(names)
window.close()