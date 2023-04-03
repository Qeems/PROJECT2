import qrcode as qr
import PySimpleGUI as sg 

sg.theme('Darkumber')
font =('Verdana', 12)

qr_image = [sg.Image('', key = 'QRCODE')]

# the layout
index = 0
color = {0: ("white", "blue"), 1: ("red", "green")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'black', key= 'URL' )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE', mouseover_colors= color[index], use_ttk_buttons=True,size= (7,1))],
    [sg.Column([qr_image], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['URL']
        if url:
            image = qr.make(url)
            image.save('qr.png')
            window['QRCODE'].update('qr.png')
        else:
            KeyError()

window.close()