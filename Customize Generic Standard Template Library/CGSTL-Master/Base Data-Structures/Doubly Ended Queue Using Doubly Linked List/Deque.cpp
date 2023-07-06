#include <iostream>

using namespace std;

template<class T>
struct node1
{
    T iNo;
    struct node1 *next;
    struct node1 *prev;
};

// typedef struct node NODE;
// typedef struct node *PNODE;

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
        void Display();
        int getCount();
};

template<class T>
Dequeue <T> :: Dequeue()
{
    iSize = 0;
    Head = NULL;
    Tail = NULL;
}

template<class T>
void Dequeue <T> :: InsertFront(T iNo)
{
    node1 <T> *newn = new node1 <T>;
    newn->iNo = iNo;
    newn->next = NULL;
    newn->prev = NULL;

    if (Head == NULL && Tail == NULL)
    {
        Head = newn;
        Tail = newn;
    }
    else
    {
        Head->prev = newn;
        newn->next = Head;
        Head = newn;
    }
    iSize++;
}

template<class T>
void Dequeue <T> :: InsertRear(T iNo)
{
    node1 <T> *newn = new node1 <T>;
    newn->iNo = iNo;
    newn->next = NULL;
    newn->prev = NULL;

    if (Head == NULL && Tail == NULL)
    {
        Head = newn;
        Tail = newn;
    }
    else
    {
        Tail->next = newn;
        newn->prev = Tail;
        Tail = newn;
    }
    iSize++;
}

template<class T>
T Dequeue <T> :: DeleteFront()
{
    T iRet;

    if (Head == NULL && Tail == NULL)
    {
        cout << "Queue is underflow ! No elements to delete !" << endl;
        return 0;
    }
    else if(Head == Tail)
    {
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        iRet = Head->iNo;
        node1 <T> *temp = Head;
        Head = Head->next;
        delete (temp);
    }
    iSize--;
    return iRet;
}

template<class T>
T Dequeue <T>:: DeleteRear()
{
    T iRet;

    if (Head == NULL && Tail == NULL)
    {
        cout << "Queue is underflow ! No elements to delete !" << endl;
        return 0;
    }
    else if(Head == Tail)
    {
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        iRet = Tail->iNo;
        node1 <T> *temp = Tail;
        Tail = Tail->prev;
        Tail->next = NULL;
        delete (temp);
    }
    iSize--;
    return iRet;
}

template<class T>
T Dequeue <T>:: getFront()
{
    T iRet;

    if (Head == NULL && Tail == NULL)
    {
        cout << "Queue is undeflow ! No elements to display !" << endl;
        return 0;
    }
    else
    {
        iRet = Head->iNo;
    }
    return iRet;
}

template<class T>
T Dequeue <T> :: getRear()
{
    T iRet;

    if (Head == NULL && Tail == NULL)
    {
        cout << "Queue is underflow ! No elements to display !" << endl;
        return 0;
    }
    else
    {
        iRet = Tail->iNo;
    }
    return iRet;
}

template<class T>
void Dequeue<T> :: Display()
{
    node1 <T> *temp = Head;

    if((Head == NULL && Tail == NULL))
    {
        cout << "Queue is underflow ! No elements to display !" << endl;
        return;
    }
    else
    {
        do
        {
            cout << "|" << temp->iNo << "|->";
            temp = temp->next;
        }while(temp != Tail->next);
        cout << "NULL" << endl;
    }
}

template<class T>
int Dequeue <T>:: getCount()
{
    return iSize;
}


int main()
{
    Dequeue <int> dq;

    cout << "Insert element '5' at rear end\n";
    dq.InsertRear(5);

    cout << "Insert element '10' at rear end\n";
    dq.InsertRear(10);

    cout << "Rear end element: " << dq.getRear() << endl;

    dq.DeleteRear();
    cout << "After deleting rear element new rear"
         << " is: " << dq.getRear() << endl;

    cout << "Inserting element '15' at front end \n";
    dq.InsertFront(15);

    cout << "Front end element: " << dq.getFront() << endl;

    cout << "Number of elements in Dequeue: " << dq.getCount()
         << endl;

    dq.DeleteFront();
    cout << "After deleting front element new "
         << "front is: " << dq.getFront() << endl;

    dq.Display();

    return 0;
}