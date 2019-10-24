import pandas as pd
import csv
MyDataset = pd.read_csv("E:/Graduation Project/My GP Dataset/ubuntu-dialogue-corpus/Ubuntu-dialogue-corpus/dialogueText.csv")
MyDataframe = pd.DataFrame(MyDataset)
counter = 0
context = []
Utterence = []
UserFrom = []
UserTo = []
Skip = 0
FinalContext = []
FinalUtterance = []
index = 0
MyContextstring = ""
MyUtterenceString = ""
MyList = []
Ayman = 0
for row in MyDataframe.iterrows():
    if Ayman == 50000:
        break
    MyList.append(str(row[1][5]))
    UserFrom.append(row[1][3])
    UserTo.append(str(row[1][4]))
    counter += 1
    if counter == 3:
        if (UserFrom[0] == UserFrom[1]):
            MyContextstring += str(MyList[0]) + "..." + str(MyList[1])
            MyUtterenceString += str(MyList[2])
        elif(UserTo[0] != 'nan' and UserTo[0] == UserTo[1] and UserFrom[2] == UserTo[1]):
            MyContextstring += str(MyList[0]) + "..." + str(MyList[1])
            MyUtterenceString += str(MyList[2])
        elif (UserTo[0] == UserTo[1] and UserTo[1] == UserTo[2]):
            MyContextstring += MyList[0] + "..." + MyList[1] + "..." + MyList[2]
        elif (UserTo[0] == 'nan' and UserTo[1] == UserTo[2]):
            MyContextstring += str(MyList[0])
            MyUtterenceString += str(MyList[1]) + "..." + str(MyList[2])
        elif ((UserFrom[0] == UserTo[1])and(UserTo[0] == UserFrom[1]) and (UserFrom[0] == UserFrom[2]) and (UserTo[0] == UserTo[2])):
            MyContextstring += MyList[0] + "..." + MyList[2]
            MyUtterenceString += MyList[1]
        elif (UserFrom[0] == UserTo[1] == UserTo[2]):
            MyContextstring += MyList[0]
            MyUtterenceString += MyList[1] + "..." + MyList[2]
        elif (UserTo[0] == UserFrom[1] == UserTo[2]):
            MyContextstring += MyList[0] + "..." + MyList[2]
            MyUtterenceString += MyList[1]
        elif ((UserFrom[0] == UserTo[2])and(UserTo[0] == UserFrom[1] == UserFrom[2])):
            MyContextstring += MyList[0]
            MyUtterenceString += MyList[1] + "..." + MyList[2]
        elif((UserTo[0] == 'nan')and(UserFrom[0] == UserTo[1])and(UserFrom[1]==UserTo[2])and(UserTo[1]==UserFrom[2])):
            MyContextstring += MyList[0] + "..." + MyList[2]
            MyUtterenceString += MyList[1]
        else:
            MyContextstring += MyList[0] + "..." + MyList[2]
            MyUtterenceString += MyList[1]

        FinalContext.append(MyContextstring)
        FinalUtterance.append(MyUtterenceString)
        counter = 0
        MyContextstring = ""
        MyUtterenceString = ""
        context.clear()
        Utterence.clear()
        UserTo.clear()
        UserFrom.clear()
        MyList.clear()
        Ayman += 1
        print("Conversation Number",Ayman,"is done")
print("All is Done ;)")
MySet = []
MySet.append(['Context', 'Utterance'])
for i in range (len(FinalUtterance)):
    MySet.append([FinalContext[i],FinalUtterance[i]])

MyCsv = pd.DataFrame(MySet)
MyCsv.to_csv("E:/Graduation Project/My GP Dataset/ubuntu-dialogue-corpus/Ubuntu-dialogue-corpus/Train.csv")

print("done")

