##Albane Keraudren-Riguidel
#BSP1 code v1.0

import csv
from tkinter import *


#################################################getting data from the knowledge base############################################################

filepath_symptom = './knowledge_base/symptoms.csv'
filepath_oil = './knowledge_base/essentialOils.csv'
filepath_param = './knowledge_base/parameters.csv'


#creating list with symptoms
File_S = open(filepath_symptom)
Reader_S = csv.reader(File_S)
Data_S = list(Reader_S)
del(Data_S[0])
File_S.close()

list_symptoms = []
for x in list(range(0, len(Data_S))):
    list_symptoms.append(Data_S[x][1])


#creating list with essential oils
File_O = open(filepath_oil)
Reader_O = csv.reader(File_O)
Data_O = list(Reader_O)
del(Data_O[0])
File_O.close()

list_oil = []
for x in list(range(0, len(Data_O))):
    list_oil.append(Data_O[x][1])

#creating list with parameters
File_P = open(filepath_param)
Reader_P = csv.reader(File_P)
Data_P = list(Reader_P)
del(Data_P[0])
File_P.close()


####################################################################graphics####################################################################

####creation of the main window (title window)###
mainpage = Tk(
    screenName=None, 
    baseName=None, 
    className='Oil2Cure',
    useTk=1
)
mainpage.state("zoomed")


###title###
title = PhotoImage(file=".\mockup\Title2.png")
titleBox = Label(mainpage,
    image=title,
    bg="#9ac1b8"
)
titleBox.place(x=40,y=1)


###instruction box###
instruction_box = PhotoImage(file=".\mockup\Instruction_Box.png")
instructionBox = Label(
    mainpage,
    image=instruction_box, 
    bg="#9ac1b8"
)
instructionBox.place(x=180,y=180)


def print_list_symptom():

    elemList.config(listvariable=StringVar(value=list_symptoms))
    
    searchOilButton = Button(
        mainpage, 
        image=search_button, 
        bg="#9ac1b8", 
        bd=0, 
        command=searchOil
    )
    searchOilButton.place(x=740,y=620)


def print_list_oil():

    elemList.config(listvariable=StringVar(value=list_oil))
    
    searchSymptomButton = Button(
        mainpage,
        image=search_button,
        bg="#9ac1b8", 
        bd=0, 
        command=searchSymptom
    )
    searchSymptomButton.place(x=740,y=620)

    
#button to search for essential oil
symptom_button = PhotoImage(file=".\mockup\Button_symptoms.png")
symptomButton = Button(
    mainpage,
    image=symptom_button, 
    bg="#9ac1b8", 
    bd=0, 
    command=print_list_symptom
)
symptomButton.place(x=110, y=350)

#button to search for symptom
oil_button = PhotoImage(file=".\mockup\Button_essential_oils.png")
oilButton = Button(
    mainpage, 
    image=oil_button, 
    bg="#9ac1b8", 
    bd=0, 
    command=print_list_oil
)
oilButton.place(x=110,y=470)

###search###
search_list = PhotoImage(file=".\mockup\Frame_1.png")
searchList = Label(
    mainpage, 
    image=search_list, 
    bg="#9ac1b8"
)
searchList.place(x=675, y=175)
searchFrame = Frame(
    mainpage, 
    bd=0, 
    bg="#9ac1b8", 
    relief=RIDGE
)
searchFrame.place(
    x=685,y=240,
    width=305,
    height=356
)

search_button = PhotoImage(file=".\mockup\Frame_5.png")

scroll_search = Scrollbar(
    searchFrame,
    orient='vertical',
)
elemList = Listbox(
    searchFrame, 
    listvariable= [], 
    width=300, 
    font=("Jim Nightshade", 24), 
    bd=0, 
    bg="#9ac1b8", 
    fg="#274E13", 
    selectbackground="#274E13", 
    yscrollcommand=scroll_search.set, 
    selectmode=SINGLE
)
scroll_search.config(command=elemList.yview)
scroll_search.pack(side=RIGHT, fill=Y)
elemList.pack(side=LEFT, fill=BOTH)

def searchOil():
    
    result_index = []
    result_oil_list = []

    active_index = elemList.curselection()[0]
    index_symptom = Data_S[active_index][0] 
    result_symptom.config(listvariable=StringVar(value=Data_S[active_index][1]))

    for i in Data_P:
        if index_symptom == i[0]: # checks first index of the list i
            result_index.append(i[1])

    for j in Data_O:
        for target_index in result_index:
            if target_index == j[0]:
                result_oil_list.append(j[1])
    
    result_oil.config(listvariable= StringVar(value=result_oil_list))
    
    return None


def searchSymptom():

    result_index = []
    result_symptom_list = []

    active_index = elemList.curselection()[0]
    index_oil = Data_O[active_index][0]
    result_oil.config(listvariable=StringVar(value=Data_O[active_index][1])) 

    for i in Data_P:
        if index_oil == i[1]: # checks first index of the list i
            result_index.append(i[0])

    for j in Data_S:
        for target_index in result_index:
            if target_index == j[0]:
                result_symptom_list.append(j[1])
    
    result_symptom.config(listvariable= StringVar(value=result_symptom_list))

    return None


###result###

result_box = PhotoImage(file=".\mockup\Result2.png")
resultBox = Label(
    mainpage, 
    image=result_box, 
    bg="#9ac1b8"
)
resultBox.place(x=1150, y=90)
    
#essential oil(s) of the result group
oilFrame = Frame(
    mainpage, 
    bd=0, 
    bg="#9ac1b8", 
    relief=RIDGE, 
    highlightthickness=0
)
oilFrame.place(
    x=1169,y=275,
    width=305,
    height=180
)

scroll_result_oil = Scrollbar(oilFrame)
result_oil = Listbox(
    oilFrame, 
    listvariable=[], 
    font=("Jim Nightshade", 24), 
    bd=0, 
    bg="#9ac1b8", 
    fg="#274E13", 
    yscrollcommand=scroll_result_oil.set
)
scroll_result_oil.config(command=elemList.yview)
scroll_result_oil.pack(side=RIGHT, fill=Y)
result_oil.pack(side=RIGHT, fill=Y)

#symptom(s) of the result group     
symptomFrame = Frame(
    mainpage, 
    bd=0, 
    bg="#9ac1b8", 
    relief=RIDGE
)
symptomFrame.place(
    x=1169,y=500,
    width=305,
    height=180
)

scroll_result_symptom = Scrollbar(symptomFrame)
result_symptom = Listbox(
    symptomFrame, 
    listvariable=[], 
    font=("Jim Nightshade", 20), 
    bd=0, 
    bg="#9ac1b8", 
    fg="#274E13", 
    yscrollcommand=scroll_result_symptom.set
)
scroll_result_symptom.config(command=result_symptom.yview)
scroll_result_symptom.pack(side=RIGHT, fill=Y)
result_symptom.pack(side=RIGHT, fill=Y)

#fn that resets the search
def reset_search():

    elemList.config(listvariable=StringVar(value=None))
    result_oil.config(listvariable=StringVar(value=None))
    result_symptom.config(listvariable= StringVar(value=None))


reset_button = PhotoImage(file=".\mockup\Frame_6.png")
resetButton = Button(
    mainpage, 
    image=reset_button, 
    bg="#9ac1b8", 
    bd=0, 
    command=reset_search
)
resetButton.place(x=1170,y=715)

#fn that leads to a window with messages
def notice_fn():

    notice = Toplevel()
    notice.state("zoomed")
    notice.configure(background="#9ac1b8")

    usage_of_oil = PhotoImage(file=".\mockup\Frame_8.png") 
    usageOil = Label(
        notice, 
        image=usage_of_oil, 
        bg="#9ac1b8"
    )
    usageOil.place(x=50, y=90)

    warning_image = PhotoImage(file=".\mockup\Frame_9.png") 
    warning = Label(
        notice, 
        image=warning_image, 
        bg="#9ac1b8"
    )
    warning.place(x=50, y=300)  

    disclaimer_image = PhotoImage(file=".\mockup\Frame_10.png")
    disclaimer = Label(
        notice, 
        image=disclaimer_image, 
        bg="#9ac1b8"
    )
    disclaimer.place(x=50, y=530)

    def close():
        notice.destroy()

    back_image = PhotoImage(file=".\mockup\Back.png")
    back = Button(
        notice,
        image=back_image,
        bg="#9ac1b8", 
        bd=0,
        command=close
    )
    back.place(x=1380, y=40)

    notice.mainloop()

next_button = PhotoImage(file=".\mockup\Frame_7.png")
nextButton = Button(
    mainpage, 
    image=next_button, 
    bg="#9ac1b8", 
    bd=0, 
    command=notice_fn
)
nextButton.place(x=1360,y=715)

####menu#####

menu = Menu(mainpage)
mainpage.config(menu=menu)
filemainmenu = Menu(
    menu, 
    tearoff=0
)
filesubmenu = Menu(
    filemainmenu,
    tearoff=0
)
menu.add_cascade(
    label="Menu", 
    menu=filemainmenu
)
filemainmenu.add_command(
    label="See notice and disclaimer",
    command=notice_fn
)
filemainmenu.add_separator()
filemainmenu.add_command(
    label="Leave Oil2Cure",
    command=mainpage.destroy
)


mainpage.mainloop()





