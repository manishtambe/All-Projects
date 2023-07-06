<h1 align="center">Customize Generic Standard Template Library</h1>

| Project Name        | Customize Generic Standard Template Library |
| ------------------  | ------------- |
| Developer Name      | Manish Tambe  |
| Starting Date       | 2023/06/25    |
| Date Of Completion  | 2023/06/30    |
| Project Description | The project Customize Generic Data Structure Library is an collection of data structure opeartions.|

<h2>Abstract :</h2>
The Customize Generic Standard Template Library (STL) is a set of C++ template classes to
provide common programming data structures and functions such as lists, stacks, queues, etc.
It is a library of container classes, algorithms, and iterators. It is a generalized library and so,
its components are parameterized.
<h2>Motivation :</h2>
As we all know CPP provide own STL library. So, motivation behind this project is research
and development as I studied how the original STL library is implemented or how
function calls works or basically how STL works behind and based on which I created my own STL by implementing my own data structures.
<h2>What does Generic Mean?</h2>
It is type of computer programming. In this type of programming, we are designing the
algorithm where in type of data is specified at run time. Basically, we are writing the
generalized code and compiler decides for what type of data it should work. In generic
programming we are writing the algorithm which are applicable to variety of data types
<h2>What does template mean?</h2>
The Templates are newly added features in C++. & It allows us to define generic classes
classes and functions by providing a support for generic programming. Also, the Templates
are useful in achieving dynamic polymorphism. So, the Template is way of creating
generalize functions and classes which are applicable for all data types without changing the
definition of the program.
<h2>Data structures used in CGSTL :</h2>

| Data Structures  | 
| --------------------------------------------- | 
| 1. Singly Linear Linked List. |
| 2. Singly Circuler Linked List.     |                                      
| 3. Doubly Linear Linked List.  |                                           
| 4. Doubly Circuler Linked List.  |                                         
| 5. Stack Implementation Using An Linked List. |                            
| 6. Queue Implementation Using An Linked List. |   
| 7. Circular Queue Using An Linked List.|
| 8. Doubly Ended Queue Using An Linked List.|
| 9. BST Implementation Using An Linked List.|                            
       
<h2> Following classes are present in the program :</h2>

| Classes | 
| --------------------------------------------- | 
| 1. SinglyL |
| 2. SinglyC |                                      
| 3. DoublyLL |                                           
| 4. DoublyC  |                                         
| 5. StackSL |                            
| 6. QueueSL |   
| 7. CircularQueueSL|
| 8. Dequeue|
| 9. BST |    

By creating object of the respective class you can call following respective class methods and perform operations on data. 

<h2> The Following Operations You Can Perform On Above Data Structure : </h2>

On Linked List You Can Perform Following Operation 
|-----------------------------------------------------|
| 1. Insert Element At First Position In Linked List. |
| 2. Insert Element At Last Position In Linked List.  |                                      
| 3. Insert Element At Desire Postion In Linked List.  |                                           
| 4. Delete Element From First Position In Linked List.  |                                         
| 5. Delete Element From Last Position In Linked List. |                            
| 6. Delete Element From Desire Postion In Linked List. |   
| 7. Display Element From The Linked List. |
| 8. Count Element From The Linked List.|

| On Stack You Can Perform Following Operations | 
| -------------------------------------------------- | 
| 1. Push Element In Stack.  |
| 2. Pop Element From Stack   |                                      
| 3. Display Stack Elements.   |                                           
| 4. Count Stack Elements.    |                                         

|On Queue You Can Perform Following Operations|          
| -------------------------------------------------- |
|1. Enqueue Element From Front. | 
|2. Enqueue Element From Rear. |
|3. Dequeue Element From Front.|
|4. Dequeue Element From Rear. |                                    
|5. Display Queue Elements.   |                                       
|6. Count Queue Elements. |
|7. Get Element From Rear End.|
|8. Get Element From Front End.|
 
|On BST You Can Perform Following Operations| 
| -------------------------------------------------- |
|1. Insert Nodes In BST.|                                              
|2. Delete Nodes From BST|                                                                                       
|3. Display Tree In Inorder Traversal Manner.|                        
|4. Display Tree In Preorder Traversal Manner.|                       
|5. Display Tree In Postorder Traversal Manner.| 

| Steps To Use Project |
| -------------------------------------------------- |
|1. Create a folder and place the Header.h and Helper.cpp file together with the desire file in which you want to include Header file. i.e. Header.h.|
|2. While creating a object of the class you need to specify the datatype on which you gonna perform operation i.e, classname <datatype> object_name; eg. SinglyLL <int>Sobj; |                                           
|3. Now by using this object you can peform desire operations from above list of operations.|      
|4. While executing program you need to compile as: - g++ class_contining_main_method Helper.cpp -o Myexe|  

<h2>Note : </h2> 
1. Please do not delete any of the file which are given to execute code successfully.<br>  
2. while including header file please include header file as #include"Header.h".

<h2>Feature Scope : </h2>
Initially I implemented few data structures further I will try to implement rest of the data structures containing searching or sorting algorithms and also some advanced data structures. Also, I will try to add my own header file in the GCC environment
