import PySimpleGUI as sg

class TelaPy:
    def __init__(self):
        sg.change_look_and_feel('Topanga')

        #layout
        layout =[
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais tipo de email voce usa?')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Solteiro?')],
            [sg.Radio('Sim', 'civil', key='sim_solteiro'), sg.Radio('Nao', key='nao_solteiro')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]