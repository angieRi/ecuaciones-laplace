import PySimpleGUI as sg
from sympy import *
from sympy.abc import t, s

init_printing(use_latex='msathjax')
x, y, z = symbols('x, y, z')
var('t')
var('s', positive=True)

sg.ChangeLookAndFeel('DarkAmber')
# ------ Menu Definition ------ #

layout = [
    [sg.Text('Transformada de Laplace', size=(50, 1), justification='center', font=("Helvetica", 14),
             relief=sg.RELIEF_RIDGE)],
    [sg.Text('Ecuación Diferencial', size=(50, 1), justification='left', font=("Helvetica", 13))],
    [sg.Input(size=(4, 3), key='-Y1-'), sg.Text('Y\''), sg.Text('+'), sg.Input(size=(4, 3), key='-Y-'), sg.Text('Y'),
     sg.Text('='), sg.InputText(size=(4, 3), key='-N-', default_text='0')],
    [sg.Text('Ejemplos de f(t) : t, t^n = t**n, sen(t) = sin(nt), cos(nt) = cos(nt), e^n = exp**n')],
    [sg.Frame('Valores iniciales ', [[
        # sg.Text('y\'(0)'), sg.Input(size=(4, 2), key='-V1-', default_text='0'),
        sg.Text('y(0)'), sg.Input(size=(4, 2), key='-V-', default_text='0')
    ]])],
    [sg.Text('_' * 80, justification='center')],
    [sg.Text('  '), sg.Output(key='_DISPLAY_', size=(60, 25), background_color='white', text_color='black' )],
    [sg.Submit(tooltip='Guardar', button_text='Ver resultado'), sg.Cancel(button_text='Salir')]
]
window = sg.Window('Ecuación diferencial Laplace', layout, default_element_size=(60, 1), grab_anywhere=False)
event, values = window.read()


def ecuacionSubsidiaria(values: int):

    v_inicial = int(values['-V-'])
    v_dv1 = int(values['-Y1-'])

    v_dv = int(values['-Y-'])
    valor_n = (values['-N-'])
    l_fun = laplace_transform(valor_n, t, s)
    l_sdv = expand(v_dv1 * (s * y - v_inicial) + (v_dv * y))
    print('L(y\') = sY -  y(0) :')
    pprint(l_sdv)
    print('')
    print('L(' + str(valor_n)+'):')
    pprint(l_fun[0])
    print('')

    result = solve(l_sdv - l_fun[0], y)
    print('Ecuación subsidiaria: ')
    pprint(result[0])
    print('')
    lap = inverse_laplace_transform(result[0], s, t)
    print('Resultado de ecuación diferencial:')
    return pprint(lap)


while True:
    event, values = window.read()
    window['_DISPLAY_'](ecuacionSubsidiaria(values))

    if event in (sg.WIN_CLOSED, 'Salir'):
        break

window.close()
