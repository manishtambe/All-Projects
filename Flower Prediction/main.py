import eel
from Files.models.CSV_Prediction import User_K_Neighbors_Classifier
from Files.models.login import login_user
from Files.models.Test import Image_predict

eel.init('Files')

Image_Path = ["setosa.jpg","virginica.jpg","versicolour.jpg"]

@eel.expose
def btn_recharge(Sepal_Length,Sepal_Width,Petal_Length,Petal_Width):
    Flower_Name = ""
    temp = list()
    print(Sepal_Length, Sepal_Width, Petal_Length, Petal_Width)
    msg,Accuracy = User_K_Neighbors_Classifier(Sepal_Length, Sepal_Width, Petal_Length, Petal_Width)
    if (msg == 0):
        Flower_Name = "Flower Name : Iris-Setosa"
        temp.append(Flower_Name)
        temp.append(Image_Path[0])
    elif(msg == 1):
        Flower_Name = "Flower Name : Iris-Versicolour"
        temp.append(Flower_Name)
        temp.append(Image_Path[2])
    elif(msg == 2):
        Flower_Name = "Flower Name : Iris-Virginica"
        temp.append(Flower_Name)
        temp.append(Image_Path[1])
    else:
        Flower_Name = "Couldn't Identify"
        temp.append(Flower_Name)
    temp.append("Accuracy : " + str(int(Accuracy * 100)) + "%")
    print(temp)
    eel.recharge_return(temp)


@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    eel.login_return(str(msg))

@eel.expose
def image_predict(Image_name):
    print("In Main.py")
    
    print(Image_name)
    
    Flower_Name = ""
    temp = list()
    
    msg, Final_Accuracy, Accuracy2, Accuracy3, Accuracy1 ,Algorithm = Image_predict(Image_name)
    

    if (msg == 0):
        Flower_Name = "Flower Name : SunFlower"
        temp.append(Flower_Name)
    elif (msg == 1):
        Flower_Name = "Flower Name : Daisy"
        temp.append(Flower_Name)
    elif (msg == 2):
        Flower_Name = "Flower Name : Iris-Setosa"
        temp.append(Flower_Name)
    else:
        Flower_Name = "Couldn't Identify"
        temp.append(Flower_Name)
        
    temp.append("Best Accuracy (" +Algorithm+ ") : " + str(int(Final_Accuracy)) + "%")
    print(temp)
    temp.append(str(int(Accuracy2)) + "%")
    temp.append(str(int(Accuracy3)) + "%")
    temp.append(str(int(Accuracy1)) + "%")
    eel.image_predict_return(temp)



eel.start("signlog.html", size=(1920,1080))