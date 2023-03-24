import PySimpleGUI as sg
import os
import qrcode


def CriaPasta():
    if not os.path.isdir("QRcodes"):
        os.mkdir('QRcodes')

def TelaLogin():
    sg.theme('LightBrown')
    layout = [
        [sg.Text('SSID')],
        [sg.Input('',key='ssid')],
        [sg.Text('Senha')],
        [sg.Input('',key='password')],
        [sg.Text('Encriptação')],
        [sg.Input('',key='encryption')],
        [sg.Text('IP')],
        [sg.Input('',key='ip')],
        [sg.Text('Mesa')],
        [sg.Input('',key='mesa')],
        [sg.Button('Mesa',key='confirmComMesa'),sg.Button('Wifi',key='confirmSemMesa')]
    ]
    return sg.Window('Formulário API',layout=layout,finalize=True)



def ChamarApp():
    janela = TelaLogin()
    
    while True:
        window, event, values = sg.read_all_windows()
        #TELA LOGIN
        if window == janela and event == sg.WINDOW_CLOSED:
            break
        elif window == janela and event == 'confirmComMesa':
           if values['mesa'] == '' or values['ip'] == '':
                sg.popup('Preencha os campos mesa e ip para prosseguir!')
           else:
                ip = values['ip']
                mesa = values['mesa']
                myobj2 = {
                        'appLink': f'{ip}:5002/mesa',
                        'mesa': mesa
                        }
                mesaString = f'http://{myobj2["appLink"]}/{myobj2["mesa"]}'
                CriaPasta()
                ImgQRcode = qrcode.make(mesaString)
                ImgQRcode.save(f'QRcodes/qrcode_{myobj2["mesa"]}.png')
                # APIaug.GeraQRcode(x2,mesa)
        elif window == janela and event == 'confirmSemMesa':
            if values['ssid'] == '' or values['password'] == '' or values['encryption'] == '':
                sg.popup('Preencha os primeiros três campos para prosseguir!')
            else:
                ssid = values['ssid']
                password = values['password']
                encryption = values['encryption']
                myobj = {
                        'ssid': ssid,
                        'password': password,
                        'encryption': encryption
                        }
                wifiString = f'WIFI:S:{myobj["ssid"]};P:{myobj["password"]};H:{False};T:{myobj["encryption"]};'
                CriaPasta()
                ImgQRcode = qrcode.make(wifiString)
                ImgQRcode.save(f'QRcodes/qrcode_wifi.png')
                # APIaug.GeraQRcode(x,'wifi')



dados = ChamarApp()

