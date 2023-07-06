# Attendence Management System Using Face-Recognition
The Attendance management is the significant process that ware carry out in every institute to
monitor the performance of the student. Every institute does this is its own way. Some of there
institute use the old paper or file-based system and some have adopted strategies of automated
attendance system using some biometric technique. A facial recognition system is a
computerized software which is suited for determining or validating a person by performing
comparisons on patterns based on their facial appearances. In this system OpenCV & Face
Recognition libraries ware used which are one of the popular libraries for face detection by
using these libraries system first capturing the student photos and storing them into the database
which ware further used for the training purpose after that at the time of attendance when
system camera get on system will detect the faces that ware present in the frame the faces ware
detected by using HOG i.e. (Histogram of Oriented Gradients) which ware carrier out in the
system. after that if image that ware present in the frame is tilted then Face Landmark
Estimation algorithm will be carried out and face will be transformed to be as close as possible
to perfectly centered. After that system will encode all the images that ware present in the
database as well as the face which ware detected in the frame. For performing encoding Deep
Conversional Neural Network algorithm will get carried out & for each face 128 measurements
ware generated then the measurements of the face that ware detected in frame it get compared
with the measurements of the faces that ware present in the image which is earlier stored in the
database. So at last by using simple liner SVM algorithm system will find the person in
database of know peoples (i.e. capture at the starting of the project) who has closest
measurements to the image that ware detected by camera. After finding perfect match system
will generate the name and date & time & present mark and store the entry in CSV file. Which
ware further uploaded on the database and also user can open it with Microsoft Excel.

# SYSTEM ARCHITECTURE

### 1. Image acquisition:
Image is acquire using a high definition camera which is placed in the classroom or lab. This
image is given as an input to the system.

### 2. Dataset Creation:
Dataset of student is created before the recognition process. Dataset was created only to train
this system we are going to create a dataset of the whole class which involve their name, roll
number department and images of the student in different variations. Whenever we register
student’s data and image in our system to create dataset, deep learning applies to each face to
compute 128-d facial features and store in student face data file to recall that face in recognition
process. This process is applying to each image taken during registration.

### 3. Storing:
We have using SQL Server from Xampp application to store the student’s data.

### 4. Face recognition process:
![image](https://github.com/manishtambe/All-Projects/assets/52567320/319008ce-e0c1-4fac-9fab-2a4ef52c7f46)

### 5. Face Detection and Extraction:
Face detection is important as the image taken through the camera given to the system, face
detection algorithm applies to identify the human faces in that image, the number of image
processing algorithms are introduced to detect faces in an image and also the location of that
detected faces. We have used HOG method to detect human faces in given image.

### 6. Face Positioning:
There are 68 specific points in a human face. In other words, we can say 68 face landmarks.
The main function of this step is to detect landmarks of faces and to position the image. A
python script is used to automatically detect the face landmarks and to position the face as
much as possible without distorting the image.

### 7. Face Encoding:
Once the faces are detected in the given image, the next step is to extract the unique identifying
facial feature for each image. Basically, whenever we get localization of face, the 128 key
facial point are extracted for each image given input which are highly accurate and these 128-
d facial points are stored in data file for face recognition.

### 8. Face matching:
This is last step of face recognition process. We have used the one of the best learning
techniques that is deep metric learning which is highly accurate and capable of outputting real
value feature vector. The proposed system system ratifies the faces, constructing the 128-d
embedding (ratification) for each. Internally compare_faces function is used to compute the
Euclidean distance between face in image and all faces in the dataset. If the current image is
matched with the 60% threshold with the existing dataset, it will move to attendance marking.

### 9. Attendance Marking:
Once the face is identified with the image stored in SQL database, python generate roll numbers
of present students and return that, when data is returned, the system generates attendance table
which includes the name, roll number, date, day and time with corresponding subject id. And
then passes the data to python to store the table into an CSV file automatically. Letter staff can
open that file into the excel sheet to edit the sheet and make changes in it.
