import PySimpleGUI as pg
from tkinter.filedialog import asksaveasfilename
import csv

headings = ['Sn', 'Surname', 'Firstname', 'Matric number', 'Score']
header = [
    pg.Text('Sn', pad=(0, 0), size=(5, 2), justification='c', font='Any 15'),
    pg.Text('Surname', pad=(0, 0), size=(30, 2), justification='c', font='Any 15'),
    pg.Text('Firstname', pad=(0, 0), size=(30, 2), justification='c', font='Any 15'),
    pg.Text('Matric number', pad=(0, 0), size=(20, 2), justification='c', font='Any 15'),
    pg.Text('Score', pad=(0, 0), size=(10, 2), justification='c', font='Any 15')
]

layout = [
    # Title within program window
    [pg.Text('Course: CSC 212', size=(
        0, 2), font='Any 20', justification='c')],
    header]


for row in range(0, 15):
    layout.append([
        pg.Input(size=(5, 2), pad=(0, 0), key=(row, 0), justification='c', font='Any 15'),
        pg.Input(size=(30, 2), pad=(0, 0), key=(row, 1), font='Any 15'),
        pg.Input(size=(30, 2), pad=(0, 0), key=(row, 2), font='Any 15'),
        pg.Input(size=(20, 2), pad=(0, 0), key=(row, 3), font='Any 15'),
        pg.Input(size=(10, 2), pad=(0, 0), key=(row, 4), font='Any 15')
    ])

layout.append([pg.Button("Save", button_color=('white', 'green'), size=(10, 2), pad=(10, 30)),
               pg.Button("Clear", button_color=('white', 'firebrick3'), size=(10, 2), pad=(10, 30))])

window = pg.Window('Score Spreadsheet', layout, font='Courier 12')


def save_file(headings, values):
    filenameforWriting = asksaveasfilename(defaultextension=".csv", filetypes = (("csv files","*.csv"),("xml files","*.xml"),("txt files","*.txt")))

    headings = ['Sn', 'Surname', 'Firstname', 'Matric number', 'Score']

    file = open(filenameforWriting, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    # write the header
    writer.writerow(headings)

    for row in range(15):
        current_row = []
        for column in range(5):
            current_row.append(values[row, column])
        writer.writerow(current_row)

    print("You can write data to " + filenameforWriting)
    file.close()


def clear_all(window):
    for row in range(15):
        for column in range(5):
            window[(row, column)].update('')


while True:
    event, values = window.read()
    if event in (pg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        save_file(headings, values)
    elif event == 'Clear':
        #   pg.popup_ok_cancel('Popup with OK and cancel buttons')
        values = []
        clear_all(window)