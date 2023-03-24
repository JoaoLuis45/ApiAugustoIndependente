import PySimpleGUI as sg
import APIaug
import requests


url = 'http://192.168.0.93:5000/generate_qrcode'

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
            return '','','','';
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
                x2 = requests.post(url, json = myobj2)
                APIaug.GeraQRcode(x2,mesa)
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
                x = requests.post(url, json = myobj)
                APIaug.GeraQRcode(x,'wifi')



dados = ChamarApp()

