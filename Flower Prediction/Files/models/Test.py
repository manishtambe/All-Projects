import glob
import numpy
import cv2
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


def Image_predict(Image_Name):
    imagePaths1 = []
    imagePaths2 = []
    imagePaths3 = []
    imagePaths = []
    imagePaths_T = []

    # input images
    # folder iris-setosa contains multiple iris-setosa in .jpg
    for img in glob.glob(
        "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\iris-setosa\\*.jpg"
    ):
        imagePaths1 = list(
            glob.glob(
                "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\iris-setosa\\*.jpg"
            )
        )

    # folder daisy contains multiple daisy in .jpg
    for img in glob.glob(
        "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\daisy\\*.jpg"
    ):
        imagePaths2 = list(
            glob.glob(
                "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\daisy\\*.jpg"
            )
        )

    # folder Sunflower contains multiple Sunflower images in .jpg
    for img in glob.glob(
        "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\Sunflower\\*.jpg"
    ):
        imagePaths3 = list(
            glob.glob(
                "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\Flower-Dataset\\Sunflower\\*.jpg"
            )
        )

    imagePaths_T = list(
        glob.glob(
            "C:\\Roadster\\My Projects\\Final Projects\\Flower Classification Using ML\\Files\\models\\TestDataset\\"
            + Image_Name
        )
    )

    # Extract the image into vector
    def image_vector(image, size=(128, 128)):
        return cv2.resize(image, size).flatten()

    imagePaths = imagePaths1 + imagePaths2 + imagePaths3

    # initialize the pixel intensities matrix, labels list
    imagematrix = list(list())
    imagelabels = list()
    pixels = None
    # Build image vector matrix
    for i, path in enumerate(imagePaths):
        # load the image and extract the class label, image intensities
        image = cv2.imread(path)
        # label = path.split(os.path.sep)[-1].split(".")[0]
        pixels = image_vector(image)

        # update the images and labels matricies respectively
        imagematrix.append(pixels)
        # imagelabels.append(label)

    print("Length of Image Matrix : " + str(len(imagematrix)))

    # Sentosa = 0-67 = 2
    # versicolour = daisy= 67 to 336 = 0
    # varginica = sunflower  = 336 and rest... = 1

    i = 0
    while i < (len(imagematrix)):
        if 0 <= i < 10:
            imagelabels.append(2)
        elif 10 <= i < 20:
            imagelabels.append(1)
        elif i >= 20:
            imagelabels.append(0)
        i += 1

    imagematrix = numpy.array(imagematrix)
    imagelabels = numpy.array(imagelabels)

    # save numpy arrays for future use
    numpy.save("matrix.npy", imagematrix)
    numpy.save("labels.npy", imagelabels)

    imagematrix = numpy.load("matrix.npy")
    imagelabels = numpy.load("labels.npy")

    # print(imagematrix)
    # print(imagelabels)

    print(imagePaths_T)

    T_imagematrix = []
    for i, path in enumerate(imagePaths_T):
        # load the image and extract the class label, image intensities
        image = cv2.imread(path)
        # label = path.split(os.path.sep)[-1].split(".")[0]
        pixels = image_vector(image)

        # update the images and labels matricies respectively
        T_imagematrix.append(pixels)

    print(imagelabels)

    Classifier = KNeighborsClassifier()
    Classifier.fit(imagematrix, imagelabels)
    Prediction = Classifier.predict(T_imagematrix)
    print(Prediction)

    Data_train, data_test, Target_train, Target_test = train_test_split(
        imagematrix, imagelabels, test_size=0.5
    )
    Classifier1 = KNeighborsClassifier()
    Classifier1.fit(Data_train, Target_train)
    Prediction1 = Classifier.predict(data_test)
    Accuracy1 = accuracy_score(Target_test, Prediction1) * 100

    Classifier2 = DecisionTreeClassifier()
    Classifier2.fit(Data_train, Target_train)
    Prediction2 = Classifier2.predict(data_test)
    Accuracy2 = accuracy_score(Target_test, Prediction2) * 100

    Classifier3 = RandomForestClassifier()
    Classifier3.fit(Data_train, Target_train)
    Prediction3 = Classifier3.predict(data_test)
    Accuracy3 = accuracy_score(Target_test, Prediction3) * 100

    Final = 0.0
    Algorithm = ""

    if Accuracy2 > Accuracy1 and Accuracy2 > Accuracy3:
        Final = Accuracy2
        Algorithm = "Decision Tree Classifier"
        cm = confusion_matrix(Target_test, Prediction2)
        print("Confusion Matrix : ")
        print(cm)

    elif Accuracy3 > Accuracy1 and Accuracy3 > Accuracy2:
        Final = Accuracy3
        Algorithm = "Random Forest Classifier"
        cm = confusion_matrix(Target_test, Prediction3)
        print("Confusion Matrix : ")
        print(cm)

    else:
        Final = Accuracy1
        Algorithm = "K-Nearest Neighbor Classifier"
        cm = confusion_matrix(Target_test, Prediction1)
        print("Confusion Matrix : ")
        print(cm)

    return Prediction[0], Final, Accuracy2, Accuracy3, Accuracy1, Algorithm
