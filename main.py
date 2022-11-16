import PySimpleGUI as pg
import csv

headings = ['Sn', 'Surname', 'Firstname', 'Matric number', 'Score']
header = [
    pg.Text('Sn', pad=(0, 0), size=(5, 1), justification='c'),
    pg.Text('Surname', pad=(0, 0), size=(15, 1), justification='c'),
    pg.Text('Firstname', pad=(0, 0), size=(30, 1), justification='c'),
    pg.Text('Matric number', pad=(0, 0), size=(30, 1), justification='c'),
    pg.Text('Score', pad=(0, 0), size=(15, 1), justification='c')
]

layout = [
    # Title within program window
    [pg.Text('Course: CSC 212', pad=(0, 5), size=(0, 0), font='Any 20', justification='c')],
    header]


for row in range(0, 15):
    layout.append([
        pg.Input(size=(5, 1), pad=(0, 0), key=(row, 0), justification='c'),
        pg.Input(size=(15, 1), pad=(0, 0), key=(row, 1)),
        pg.Input(size=(30, 1), pad=(0, 0), key=(row, 2)),
        pg.Input(size=(30, 1), pad=(0, 0), key=(row, 3)),
        pg.Input(size=(15, 1), pad=(0, 0), key=(row, 4))
    ])

layout.append([pg.Button("Submit", button_color=('white', 'green')),
               pg.Button("Generate CSV"),
               pg.Button("Clear", button_color=('white', 'firebrick3'))])

window = pg.Window('Score Spreadsheet', layout, font='Courier 12')


def generate_csv(headings, values):
    headings = ['Sn', 'Surname', 'Firstname', 'Matric number', 'Score']

    file = open('contacts.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    # write the header
    writer.writerow(headings)

    for row in range(15):
        current_row = []
        for column in range(4):
            current_row.append(values[row, column])
        writer.writerow(current_row)

    file.close()


def clear_all(window):
    for row in range(15):
        for column in range(4):
            window[(row, column)].update('')


while True:
    event, values = window.read()
    if event in (pg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit':
        print(values[0, 0])
    elif event == 'Generate CSV':
        generate_csv(headings, values)
    elif event == 'Clear':
        #   pg.popup_ok_cancel('Popup with OK and cancel buttons')
        values = []
        clear_all(window)


window.mainloop()