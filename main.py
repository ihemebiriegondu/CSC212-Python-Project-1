from tkinter import *
import tkinter.messagebox


class MainPage:
    def __init__(self):

        #created the empty list to add all informations
        self.matrix = []

        window = Tk()
        window.title("Python Project")
        window.geometry("500x500")

        # set first frame with subject title
        self.frame1 = Frame(window)
        self.frame1.pack()

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

    def showFields(self):
        courseTitleInput = self.courseInput.get()

        if courseTitleInput != "":

            #to make the second frame visible
            self.frame2.pack()

            #to hide the first frame
            self.frame1.pack_forget()
            self.courseInputValue['text'] = self.courseInput.get()

            #created the file for adding all infos
            self.newfile = open('newfile.csv', "w")
            self.newfile.writelines(self.matrix)
        else:
            tkinter.messagebox.showinfo("Input", "Subject field is empty!")

    def saveUserInfos(self):

        #create a new row everytime new informations are added
        #new row will be added to the multi dimensional list, the matrix[] list
        current_row = [self.matricNo.get(), self.firstname.get(),
                       self.lastname.get(), self.score.get()]

        #appending the new row to the main list
        self.matrix.append(current_row)

        self.newfile.writelines(self.matrix)
        self.newfile.close()

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

        print(self.matrix)


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
