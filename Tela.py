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
            [sg.Radio('Sim', 'civil', key='sim_solteiro'), sg.Radio('Nao', 'Nao é solteiro', key='nao_solteiro')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)

    def Iniciar(self):
        while True:
            #extrair os dados da tela
            self.button,self.value = self.janela.read()

            nome = self.value['nome']
            idade = self.value['idade']
            o_gmail = self.value['gmail']
            o_outlook = self.value['outlook']
            o_yahoo = self.value['yahoo']
            s_solteiro = self.value['sim_solteiro']
            n_solteiro = self.value['nao_solteiro']
            sliderVelocidade = self.value['sliderVelocidade']

            print(f'nome>{nome}')
            print(f'idade>{idade}')
            print(f'gmail>{o_gmail}')
            print(f'outlook>{o_outlook}')
            print(f'yahoo>{o_yahoo}')
            print(f'sim_solteiro>{s_solteiro}')
            print(f'nao_solteiro>{n_solteiro}')
            print(f'sliderVelocidade>{sliderVelocidade}')

tela = TelaPy()
tela.Iniciar()
