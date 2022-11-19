from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import json


class MainPage:
    def __init__(self):

        #created the empty list to add all informations
        self.matrix = []

        self.command = ''

        window = Tk()
        window.title("Python Project")
        window.geometry("500x500")

        #set first frame
        self.frame0 = Frame(window)
        self.frame0.pack()

        openfile_button = Button(self.frame0, text="Open existing file", font=(
            'Arial 13'), command=self.openFile)
        openfile_button.pack()

        createfile_button = Button(self.frame0, text="create new file", font=(
            'Arial 13'), command=self.createFile)
        createfile_button.pack()

        # set create new file frame with subject title
        self.frame1 = Frame(window)

        subject = Label(self.frame1, text="Enter the subject / course")
        subject.pack()

        # storing the course title in a string
        self.courseInput = StringVar()

        # text varible should be stored in the empty string variable created (self.courseInput)
        subjectEntry = Entry(self.frame1, width=30, font=(
            'Arial 16'), textvariable=self.courseInput)
        subjectEntry.pack()

        # added event listener to the button for hiding the initial frame and showing frame2
        submit_button = Button(self.frame1, text="Submit", font=(
            'Arial 13'), command=self.showFields)
        submit_button.pack()

        back_button = Button(self.frame1, text="Back", font=(
            'Arial 13'), command=self.backToFrame0Btn)
        back_button.pack()

        # second frame with title
        self.frame2 = Frame(window)
        # initial title to be changed to the inputted value
        self.courseInputValue = Label(
            self.frame2, text='Subject Title', font=('Arial 16'))
        self.courseInputValue.pack()

        matricNo = Label(self.frame2, text="Matric No")
        matricNo.pack()

        self.matricNo = StringVar()
        self.MatricNo = Entry(self.frame2, width=30, font=(
            'Arial 16'), textvariable=self.matricNo)
        self.MatricNo.pack()

        FirstName = Label(self.frame2, text="First Name")
        FirstName.pack()

        self.firstname = StringVar()
        self.FirstName = Entry(self.frame2, width=30, font=(
            'Arial 16'), textvariable=self.firstname)
        self.FirstName.pack()

        LastName = Label(self.frame2, text="Last Name")
        LastName.pack()

        self.lastname = StringVar()
        self.LastName = Entry(self.frame2, width=30, font=(
            'Arial 16'), textvariable=self.lastname)
        self.LastName.pack()

        Score = Label(self.frame2, text="Score")
        Score.pack()

        self.score = IntVar()
        self.Score = Entry(self.frame2, width=30, font=('Arial 16'), textvariable=self.score)
        self.Score.pack()

        # added event listener to the button to save user info
        submit_button = Button(self.frame2, text="Save Entry", font=(
            'Arial 13'), command=self.saveUserInfos)
        submit_button.pack()

        #button to clear entry
        clear_button = Button(self.frame2, text="Clear Entry", font=(
            'Arial 13'), command=self.clearEntry)
        clear_button.pack()

        window.mainloop()

    def openFile(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes = (("Json file","*.json"),("xml files","*.xml")))
        if self.filename != '':
            self.frame2.pack()
            self.frame0.pack_forget()

            self.command = 'open file'

    def createFile(self):
        self.filename = filedialog.asksaveasfilename(initialdir='/', title='Save file', defaultextension=".json")

        if self.filename != '':
            self.frame1.pack()
            self.frame0.pack_forget()

            self.command = 'create file'

    def backToFrame0Btn(self):
        self.frame0.pack()
        self.frame1.pack_forget()

    def showFields(self):
        courseTitleInput = self.courseInput.get()

        if courseTitleInput != "":

            #to make the second frame visible
            self.frame2.pack()

            #to hide the first frame
            self.frame1.pack_forget()
            self.courseInputValue['text'] = self.courseInput.get()

            #created the file for adding all infos
            
            #self.newfile = open('newfile.json', "w", encoding='UTF8', newline='')
            #self.newfile.writelines(self.matrix)
            #self.newfile.close()
        else:
            tkinter.messagebox.showinfo("Input", "Subject field is empty!")

    def saveUserInfos(self):

        #create a new row everytime new informations are added
        #new row will be added to the multi dimensional list, the matrix[] list
        current_row = [self.matricNo.get(), self.firstname.get(),
                       self.lastname.get(), self.score.get()]

        #appending the new row to the main list
        self.matrix.append(current_row)

        if self.command == 'create file':
            with open(self.filename, 'w') as outfile:
                json.dump(self.matrix, outfile)
        elif self.command == 'open file':
            with open(self.filename, 'r') as openfile:
                json_object = json.load(openfile)
                json_object.append(current_row)

                #print(json_object)

            with open(self.filename, 'w') as outfile:
                json.dump(json_object, outfile)

        #self.newfile = open('newfile.csv', "a")
        #self.newfile.writelines(self.matrix)
        #self.newfile.close()

        #clearing the input fields after submission for new entry
        self.MatricNo.delete(0, END)
        self.MatricNo.insert(0, '')
        self.FirstName.delete(0, END)
        self.FirstName.insert(0, '')
        self.LastName.delete(0, END)
        self.LastName.insert(0, '')
        self.Score.delete(0, END)
        self.Score.insert(0, '')

        #autofocusing the first input field
        self.MatricNo.focus()

        #print(self.matrix)


    def clearEntry(self):
        self.MatricNo.delete(0, END)
        self.MatricNo.insert(0, '')
        self.FirstName.delete(0, END)
        self.FirstName.insert(0, '')
        self.LastName.delete(0, END)
        self.LastName.insert(0, '')
        self.Score.delete(0, END)
        self.Score.insert(0, '')

        self.MatricNo.focus()



MainPage()
