import PySimpleGUI as sg
dalas=[
    
    [sg.Text("Izvēlies attēlu:"), sg.InputText(key="file_path"), sg.FileBrowse()],
    [sg.Image(key="image")],# Image- klase
    [sg.Button("Pārādīt attēlu"), sg.Button("Iziet")]
]


logs=sg.Window("Attēlu bibliotēka", dalas,resizable=True)# resizable- logs pielagosies ta elementu izmeriem


while True:
    event, values=logs.read()

    if event==sg.WIN_CLOSED or event=="Iziet": 
        break
    if event== "Pārādīt attēlu":
       file_path=values("file_path")
       if file_path:
           logs["image"].update(filename= file_path)
           



logs.close()