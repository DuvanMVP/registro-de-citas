import os

cont_odontologia = 0
cont_ginecologia = 0
cont_consulta_general = 0
cont_maternidad = 0
cont_infantes = 0


def fnt_limpiaPantalla():
    os.system('cls')
    print('Sistema de control de registro de citas')
    print('Autor: Duvan S. Oviedo M. (c)- 2024')
    
def fnt_selector(op):
    global cont_odontologia
    if op == 1:
        cont_odontologia +=1
    if op == 3:
        fnt_limpiaPantalla()
        fnt_reporte()
        
    if op == 4:
        cont_ginecologia += 1
        
    def fnt_reporte():
        print('odontologia: ', cont_odontologia)
        print('ginecologia: ', cont_ginecologia)
        print('Consulta general: ', cont_consulta_general)
        print('Maternidad: ', cont_maternidad)
        print('infantes: ', cont_infantes)
        enter = input('Presione <ENTER> para continuar')
        
sw = True
while sw == True:
    fnt_limpiaPantalla()
    opciones = int(input('---MENU DE OPCIONES---\n1. odontologia\n2. Salir\n4. gineco -> '))
    fnt_selector (opciones)

