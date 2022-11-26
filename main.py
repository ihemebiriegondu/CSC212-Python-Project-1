from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import json


class MainPage:
    def __init__(self):

        # created the empty list to add all informations
        self.matrix = []

        # added a command variable to run diff functions when either create new file or open existing file btn is clicked
        self.command = ''

        window = Tk()
        window.title("Group six (6) project")
        window.geometry("900x500")
        # window.configure(bg='')

        # set first frame
        self.frame0 = Frame(window, bg='yellow')
        self.frame0.pack(fill="both", expand=True)

        openfile_button = Button(self.frame0, text="Open existing file", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.openFile)
        openfile_button.pack(padx=20, pady=0, ipadx=10, ipady=8,
                             anchor=CENTER, side='right')
        # anchor='ne', side='bottom'

        createfile_button = Button(self.frame0, text="create new file", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.createFile)
        createfile_button.pack(padx=20, ipadx=20, ipady=8,
                               pady=0, anchor=CENTER, side='left')

        # set create new file frame with subject title
        self.frame1 = Frame(window, bg='yellow')

        subject = Label(self.frame1, text="COURSE TITLE", anchor='w', padx=20,
                        pady=25, bg='yellow', fg='black', font=('Arial Bold', 13), justify=LEFT)
        subject.pack(anchor='w')

        # storing the course title in a string
        self.courseInput = StringVar()

        # text varible should be stored in the empty string variable created (self.courseInput)
        subjectEntry = Entry(self.frame1, width=30, font=(
            'Arial 15'), justify=LEFT, highlightthickness=2, relief='groove', textvariable=self.courseInput)
        subjectEntry.focus()
        subjectEntry.config(highlightcolor='green4',
                            highlightbackground='green4')
        subjectEntry.pack(ipadx=10, ipady=10, anchor='w', padx=20)

        # added event listener to the button for hiding the initial frame and showing frame2
        submit_button = Button(self.frame1, text="Submit", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.showFields)
        submit_button.pack(padx=20, ipadx=20, ipady=8,
                           pady=20, anchor='w', side='top')

        # for going back to frame0
        back_button = Button(self.frame1, text="Back", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.backToFrame0Btn)
        back_button.pack(padx=30, pady=30, ipadx=20,
                         ipady=8, anchor='ne', side='bottom')

        # third frame with title
        self.frame2 = Frame(window, bg='yellow')

        # initial title to be changed to the inputted value
        self.courseInputValue = Label(
            self.frame2, text='Subject Title', font=('Arial 16'), padx=20, pady=10, bg='yellow', fg='black', justify=LEFT)
        self.courseInputValue.pack(anchor='nw', side='left')

        # adding the run analysis button

        self.runAnalysisList = [
            "Average score",
            "Minimum score",
            "Maximum score",
            "Best student",
            "Students with 70 and above",
            "Students that failed"
        ]

        self.runAnalysisVariable = StringVar()
        self.runAnalysisVariable.set('Run Analysis')

        self.drop = OptionMenu(self.frame2, self.runAnalysisVariable, *self.runAnalysisList, command=self.showRunAnalysisDropdown)
        self.drop.config(bg='green', fg='white', activebackground='green', activeforeground='white',
                         cursor="hand2", borderwidth='0', relief='flat', font=('Arial 13'))
        self.drop['menu'].config(
            bg="white", fg='green', activebackground='yellow', activeforeground='green', relief=FLAT)
        self.drop.pack(anchor='nw', side='right', padx=20,
                       ipadx=20, ipady=8, pady=20)

        matricNo = Label(self.frame2, text="Matric No",
                         bg='yellow', padx=20, pady=10, font=('Arial 13'))
        matricNo.pack(pady=(30, 0))

        self.matricNo = StringVar()
        self.MatricNo = Entry(self.frame2, width=30, font=(
            'Arial 15'), highlightthickness=2, relief='flat', textvariable=self.matricNo)
        self.MatricNo.focus()
        self.MatricNo.config(highlightcolor='green4',
                             highlightbackground='green4')
        self.MatricNo.pack(ipadx=10, ipady=3, padx=20)

        FirstName = Label(self.frame2, text="First Name",
                          bg='yellow', padx=20, pady=10, font=('Arial 13'))
        FirstName.pack()

        self.firstname = StringVar()
        self.FirstName = Entry(self.frame2, width=30, font=(
            'Arial 15'), highlightthickness=2, relief='flat', textvariable=self.firstname)
        self.FirstName.config(highlightcolor='green4',
                              highlightbackground='green4')
        self.FirstName.pack(ipadx=10, ipady=3, padx=20)

        LastName = Label(self.frame2, text="Last Name",
                         bg='yellow', padx=20, pady=10, font=('Arial 13'))
        LastName.pack()

        self.lastname = StringVar()
        self.LastName = Entry(self.frame2, width=30, font=(
            'Arial 15'), highlightthickness=2, relief='flat', textvariable=self.lastname)
        self.LastName.config(highlightcolor='green4',
                             highlightbackground='green4')
        self.LastName.pack(ipadx=10, ipady=3, padx=20)

        Score = Label(self.frame2, text="Score", bg='yellow',
                      padx=20, pady=10, font=('Arial 13'))
        Score.pack()

        self.score = IntVar()
        self.Score = Entry(self.frame2, width=30, font=(
            'Arial 15'), highlightthickness=2, relief='flat', textvariable=self.score)
        self.Score.config(highlightcolor='green4',
                          highlightbackground='green4')
        self.Score.pack(ipadx=10, ipady=3, padx=20)

        # added event listener to the button to save user info
        submit_button = Button(self.frame2, text="Save Entry", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.saveUserInfos)
        submit_button.pack(padx=20, ipadx=20, ipady=8,
                           pady=20, anchor='w', side='left')

        # button to clear entry
        clear_button = Button(self.frame2, text="Clear Entry", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.clearEntry)
        clear_button.pack(padx=20, ipadx=20, ipady=8,
                          pady=20, anchor='e', side='right')

        # creating a forth frame for displaying eda results
        self.frame3 = Frame(window, bg='yellow')
        self.result = Label(self.frame3, text="", font=(
            'Arial 16'), padx=20, pady=10, bg='yellow', fg='black')
        self.result.pack()
        self.namesLabel = Label(self.frame3, text='', font=(
            'Arial 16'), padx=20, pady=4, bg='yellow', fg='black')
        self.namesLabel.pack()

        # for going back to frame2
        back_button = Button(self.frame3, text="Back", cursor="hand2", bg='green', fg='white', borderwidth='2', relief='groove', font=(
            'Arial 13'), command=self.backToFrame2Btn)
        back_button.pack(padx=30, pady=10, ipadx=20,
                         ipady=8, anchor='ne', side='bottom')

        window.mainloop()

    # opening existing file function
    def openFile(self):
        self.filename = filedialog.askopenfilename(
            initialdir='/', title='Open file', filetypes=(("Json file", "*.json"), ("xml files", "*.xml")))
        if self.filename != '':
            self.frame2.pack(fill="both", expand=True)
            self.frame0.pack_forget()

            # setting subject value from the saved file
            with open(self.filename, 'r') as openfile:
                fjson_object = json.load(openfile)
                sameTitle = fjson_object[0][0]
                self.courseInputValue['text'] = sameTitle
            # print(sameTitle)

            self.command = 'open file'

    # creating new file function
    def createFile(self):
        self.filename = filedialog.asksaveasfilename(
            initialdir='/', title='Save file', defaultextension=".json")

        if self.filename != '':
            self.frame1.pack(fill="both", expand=True)
            self.frame0.pack_forget()

            self.command = 'create file'

    # back to frame0 function
    def backToFrame0Btn(self):
        self.frame0.pack(fill="both", expand=True)
        self.frame1.pack_forget()

    def showFields(self):
        courseTitleInput = self.courseInput.get().upper()

        if courseTitleInput != "":

            # to make the third frame visible
            self.frame2.pack(fill="both", expand=True)

            # to hide the second frame
            self.frame1.pack_forget()

            # setting the subject value from the subject value input field
            if self.command == 'create file':
                self.courseInputValue['text'] = self.courseInput.get().upper()
        else:
            tkinter.messagebox.showerror(
                "Error", "Course title field is empty!")

    def saveUserInfos(self):

        if self.matricNo.get() != '' and self.score.get != '':
            # create a new row everytime new informations are added
            # new row will be added to the multi dimensional list, the matrix[] list
            current_row = [self.courseInput.get(), self.matricNo.get(), self.firstname.get(),
                           self.lastname.get(), self.score.get()]

            # appending the new row to the main list
            self.matrix.append(current_row)

            if self.command == 'create file':
                with open(self.filename, 'w') as outfile:
                    json.dump(self.matrix, outfile)
            elif self.command == 'open file':
                with open(self.filename, 'r') as openfile:
                    json_object = json.load(openfile)
                    json_object.append(current_row)

                    # print(json_object)

                # updating the newly added informations
                with open(self.filename, 'w') as outfile:
                    json.dump(json_object, outfile)

            # clearing the input fields after submission for new entry
            self.MatricNo.delete(0, END)
            self.MatricNo.insert(0, '')
            self.FirstName.delete(0, END)
            self.FirstName.insert(0, '')
            self.LastName.delete(0, END)
            self.LastName.insert(0, '')
            self.Score.delete(0, END)
            self.Score.insert(0, '')

            # autofocusing the first input field
            self.MatricNo.focus()

            # print(self.matrix)

        else:
            tkinter.messagebox.showerror(
                "Error", "Student info not complete !")

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

    def meanScore(self):
        # empty list to put all the scores obtained
        averageList = []

        # open the file to read the values
        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)

        # adding all the scores to the empty list created
        for rows in fileToAnalyze:
            # adding the element with index 4 (the scores only not all informations)
            averageList.append(rows[4])

        # calculating the sum of all the elements with python sum() function
        averageTotalScore = sum(averageList)
        # getting the total number of results entered
        averageTotalStudents = len(averageList)

        # print(averageTotalScore)
        # print(averageTotalStudents)

        # calculating the average to 2 decimal places
        self.averageScore = round(averageTotalScore / averageTotalStudents, 2)
        # print(self.averageScore)

        # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        self.result['text'] = 'The average score is ' + str(self.averageScore)

    def maxScore(self):
        # empty list to put all the scores obtained
        maxList = []

        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)
        for rows in fileToAnalyze:
            maxList.append(rows[4])

        # using python max() function to get the max element in the list and assigning it to the maxScore variable
        self.maxScore = max(maxList)
        # print(self.maxScore)

        # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        self.result['text'] = 'The maximum score is ' + str(self.maxScore)

    def minScore(self):
        minList = []

        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)
        for rows in fileToAnalyze:
            minList.append(rows[4])

        # using python min() function to get the min element in the list and assigning it to the maxScore variable
        self.minScore = min(minList)
        # print(self.minScore)

        # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        self.result['text'] = 'The minimum score is ' + str(self.minScore)

    def highStudent(self):
        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)

        # running the max function to get the maximum element
        maxList = []

        for rows in fileToAnalyze:
            maxList.append(rows[4])

        self.maxScore = max(maxList)
        # print(self.maxScore)

        # I created a list incase there are more than one student with the highest score
        self.highestStudent = []
        # iterating through the file's multidimensional list rows i and column 4,
        # to check which row has score that is equal to the maximum score and printing it out
        for i in range(len(fileToAnalyze)):
            if fileToAnalyze[i][4] == self.maxScore:
                self.highestStudent.append(fileToAnalyze[i])
        # print(self.highestStudent)

        # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # empty array to store the text to be displayed for each student with the highest mark
        someArray = []

        # iterating through the highest score array to add students info in the someArray[] array
        # and appending the results
        for i in range(len(self.highestStudent)):
            # print(self.highestStudent[i])
            self.result['text'] = 'The student(s) with the highest score is/are: '
            someArray.append(str(self.highestStudent[i][3] + " " + str(self.highestStudent[i][2]) + "           " +
                                 str(self.highestStudent[i][1]) + "             " + str(self.highestStudent[i][4])))

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        # creating the label for the students info
        self.namesLabel = Label(self.frame3, text='', font=(
            'Arial 13'), padx=20, pady=10, bg='yellow', fg='black', justify=LEFT)
        self.namesLabel.pack()

        # a function to display as many labels as possible for each high score
        def addHighScoreNameToLabel():
            element = ''
            for i in range(len(someArray)):
                element = element + someArray[i]+'\n'
            return element

        # adding the texts to the label created above
        self.namesLabel['text'] = addHighScoreNameToLabel()

    def passScore(self):
        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)

        # empty list to put all students that pass 70
        self.passScores = []

        # iterating through the file's multidimensional list rows i and column 4,
        # to check which row has score that is greater than or equal to 70 and printing it out
        for i in range(len(fileToAnalyze)):
            if fileToAnalyze[i][4] >= 70:
                self.passScores.append(fileToAnalyze[i])
        # print(self.passScores)

         # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # empty array to stored the text to be displayed for each student above the 70 mark
        someArray = []

        # iterating through the passScores array to add students info in the someArray[] array
        # and appending the results
        for i in range(len(self.passScores)):
            # print(self.passScores[i])
            self.result['text'] = 'The students with 70 and above are: '
            someArray.append(str(self.passScores[i][3] + " " + str(self.passScores[i][2]) + "           " +
                                 str(self.passScores[i][1]) + "             " + str(self.passScores[i][4])))

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        # creating the label for the students info
        self.namesLabel = Label(self.frame3, text='', font=(
            'Arial 13'), padx=20, pady=10, bg='yellow', fg='black', justify=LEFT)
        self.namesLabel.pack()
        
        # a function to display as many labels as possible for each high score

        def addPassScoreNameToLabel():
            element = ''
            for i in range(len(someArray)):
                element = element + someArray[i]+'\n'
            return element

        # adding the texts to the label created above
        self.namesLabel['text'] = addPassScoreNameToLabel()

    def failedScore(self):
        with open(self.filename, 'r') as openfile:
            fileToAnalyze = json.load(openfile)

        # empty list to put all students that got less than 40
        self.lessScores = []

        # iterating through the file's multidimensional list rows i and column 4,
        # to check which row has score that is less than 40 and printing it out
        for i in range(len(fileToAnalyze)):
            if fileToAnalyze[i][4] < 40:
                self.lessScores.append(fileToAnalyze[i])
        # print(self.passScores)

         # hiding the frame2 and showing the eda results frame
        self.frame3.pack(fill="both", expand=True)
        self.frame2.pack_forget()

        # empty array to stored the text to be displayed for each student below the 40 mark
        someArray = []

        # iterating through the lessScores array to add students info in the someArray[] array
        # and appending the results
        for i in range(len(self.lessScores)):
            self.result['text'] = 'The students that scored below 40 are: '
            someArray.append(str(self.lessScores[i][3] + " " + str(self.lessScores[i][2]) + "           " +
                                 str(self.lessScores[i][1]) + "             " + str(self.lessScores[i][4])))

        # clearing any content in the namesLabel label
        self.namesLabel.destroy()

        # creating the label for the students info
        self.namesLabel = Label(self.frame3, text='', font=(
            'Arial 13'), padx=20, pady=10, bg='yellow', fg='black', justify=LEFT)
        self.namesLabel.pack()
        # a function to display as many labels as possible for each high score

        def addFailedNameToLabel():
            element = ''
            for i in range(len(someArray)):
                element = element + someArray[i]+'\n'
            return element

        # adding the texts to the label created above
        self.namesLabel['text'] = addFailedNameToLabel()

    def showRunAnalysisDropdown(self, *args):
        runAnalysisValue = self.runAnalysisVariable.get()

        if runAnalysisValue == 'Average score':
            self.meanScore()
        elif runAnalysisValue == 'Maximum score':
            self.maxScore()
        elif runAnalysisValue == 'Minimum score':
            self.minScore()
        elif runAnalysisValue == 'Best student':
            self.highStudent()
        elif runAnalysisValue == 'Students that failed':
            self.failedScore()
        elif runAnalysisValue == 'Students with 70 and above':
            self.passScore()
        
        runAnalysisValue = self.runAnalysisVariable.set('Run Analysis')

    def backToFrame2Btn(self):
        self.frame2.pack(fill="both", expand=True)
        self.frame3.pack_forget()


MainPage()
