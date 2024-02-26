import PySimpleGUI as sg
def main():# visam kas seit jabut zem def
 dalas = [
        [sg.Text('Izvēlēties opciju:')],
        [sg.Combo(['Rudens', 'Vasara', 'Ziema', 'Pavasaris'], key='combo')],
        [sg.Checkbox('Ir migla', key='checkbox')],
        [sg.Text('Ievadi vārdu:'), sg.InputText(key='input')],
        [sg.Button('Ierakstīt failā'), sg.Button('Notīrīt visu'), sg.Button('Iziet')],
        [sg.Output(size=(50,10), key='output')],# Outpuut= Multiline

 ]
# definejam logu un galveno ciklu 
 

 window=sg.Window("Otrais uzdevums",dalas ,resizable=True)

 while True:
       event, values=window.read()

       if event==sg.WIN_CLOSED or event=="Iziet": 
           break
       # papildu apstrade notikumam var tikt pievvienota seit
       elif event =='Ierakstīt failā':
          atlase= values["combo"]
          keksis=values["checkbox"]
          ievade=values["Īnput"]

          filename="1piemers.png"
          with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Ivēlētais adalaiks:{atlase}")
            file.write(f"Migla:{keksis}\n") #\n- sakt jauna rindaa
            file.write(f"Tavs vards::{ievade}")

          window ["output"].update(value=f"ati ir ierakstīti failā {filename}")
 
 window.close()
 
if __name__ == '__main__':
    main()
  #atlauj izpildit konkretus koda gabalus


