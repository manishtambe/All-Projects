//------------------------------------------------------------------------------------
// Built-in Header File Inclusion
//------------------------------------------------------------------------------------

#include<iostream>


//------------------------------------------------------------------------------------
// Defining Namespace
//------------------------------------------------------------------------------------

using namespace std;


//------------------------------------------------------------------------------------
// Creation Of Structures
//------------------------------------------------------------------------------------

template<class T>
struct node {
    T iNo;
    struct node * next;
};


template <class T>
struct node1 {
    T iNo;
    struct node1 * next;
    struct node1 * prev;
};


template<class T>
struct bstnode{
    T iNo;
    struct bstnode * left;
    struct bstnode * right;
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Singly Linear Linked List
//------------------------------------------------------------------------------------

template<class T>
class SinglyL
{
private:
    node<T> *head;
    int iSize;

public:
    SinglyL();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(T, int);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Doubly Linear Linked List
//------------------------------------------------------------------------------------

template<class T>
class DoublyLL
{

private:
    node1 <T> *head;
    int iSize;

public:
    DoublyLL();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(int, T);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();

};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Singly Circular Linked List
//------------------------------------------------------------------------------------

template<class T>
class SinglyC
{
private:
    int iSize;
    node <T> *Head;
    node <T> *Tail;

public:
    SinglyC();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(int, T);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Doubly Circular Linked List
//------------------------------------------------------------------------------------

template <class T>
class DoublyC
{

private:
    node1 <T> *Head;
    node1 <T> *Tail;
    int iSize;

public:
    DoublyC();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(int, T);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Stack using Linked List
//------------------------------------------------------------------------------------

template <class T>
class StackSL
{
private:
    node <T> *Top;
    int iSize;

public:
    StackSL();
    void Push(T);
    T Pop();
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Queue using Linked List
//------------------------------------------------------------------------------------

template<class T>
class QueueSL
{
private:
    node <T> *Top;
    int iSize;

public:
    QueueSL();
    void Enqueue(T);
    T Dequeue();
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Circular Queue using Linked List
//------------------------------------------------------------------------------------

template<class T>
class CircularQueueSL
{
private:
    node <T> *Rear;
    node <T> *Front;
    int iSize;

public:
    CircularQueueSL();
    void Enqueue(int);
    T Dequeue();
    void Display();
    int Count();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Doubly ended Queue using Linked List
//------------------------------------------------------------------------------------

template<class T>
class Dequeue
{
private:
    int iSize;
    node1 <T> *Head;
    node1 <T> *Tail;

public:
    Dequeue();
    void InsertFront(T);
    void InsertRear(T);
    T DeleteFront();
    T DeleteRear();
    T getFront();
    T getRear();
    int getCount();
    void Display();
};


//------------------------------------------------------------------------------------
// Class Definition And Function Prototype of Binary Search Tree using Linked List
//------------------------------------------------------------------------------------

template<class T>
class BST{

private:
    int iSize;
    bstnode <T> *root;

public:
    BST();
    bstnode <T> * Create(T);
    bstnode <T> * Insert(bstnode <T> *root, T iNo);
    void Insert(T);
    void Inorder(bstnode <T> *root);
    void Preorder(bstnode <T> *root);
    void Postorder(bstnode <T> *root);
    void Inorder();
    void Preorder();
    void Postorder();
    bstnode <T> * GetMin(bstnode <T> *root);
    bstnode <T> * GetMax(bstnode <T> *root);
    bstnode <T> * DeleteNode(bstnode <T> *root, T);
    void DeleteNode(T);

};

//-------------------------------------------------------------------------------------------