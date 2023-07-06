#include <iostream>

using namespace std;

template<class T>
struct node
{
    T iNo;
    struct node *next;
};

// typedef struct node NODE;
// typedef struct node *PNODE;

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
        int Dequeue();
        void Display();
        int Count();
};

template<class T>
CircularQueueSL <T> :: CircularQueueSL()
{
    Rear = NULL;
    Front = NULL;
    iSize = 0;
}

template<class T>
void CircularQueueSL <T> :: Enqueue(int iNo)
{
    node <T> *newn = new node <T>;
    newn->next = NULL;
    newn->iNo = iNo;

    if (Front == NULL && Rear == NULL)
    {
        Front = newn;
        Rear = newn;
    }
    else
    {
        Rear->next = newn;
        Rear = newn;
    }
    Rear->next = Front;
    iSize++;
}

template<class T>
int CircularQueueSL <T> :: Dequeue()
{
    int iStore = 0;
    if (Front == NULL && Rear == NULL)
    {
        cout<< "Queue is empty ! No elements to POP" << endl;
        return 0;
    }
    else if (Front == Rear)
    {
        iStore = Front->iNo;
        delete (Front);
        Front = NULL;
        Rear = NULL;
    }
    else
    {
        node <T> *temp = Front;
        iStore = Front->iNo;
        Front = Front->next;
        delete (temp);
        Rear->next = Front;
    }
    iSize--;
    return iStore;
}

template<class T>
void CircularQueueSL <T> :: Display()
{
    node <T> *temp = Front;

    if (Front == NULL && Rear == NULL)
    {
        cout << "NULL" << endl;
        return;
    }
    else
    {
        do
        {
            cout << "|" << temp->iNo << "|->";
            temp = temp->next;
        } while (temp != Rear->next);
        cout << "NULL" << endl;
    }
}

template<class T>
int CircularQueueSL <T>:: Count()
{
    return iSize;
}

int main()
{
    int iRet = 0;
    int iStore = 0;
    CircularQueueSL <int> sobj;
    sobj.Enqueue(51);
    sobj.Enqueue(21);
    sobj.Enqueue(11);
    sobj.Display();
    iRet = sobj.Count();
    cout << "The Elements Present In The Linked List Are = " << iRet << "\n\n";

    iStore = sobj.Dequeue();
    cout << "The Element Deleted From The Queue Are = " << iStore << "\n";
    cout << "The Element From The Queue After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Dequeue();
    cout << "The Element Deleted From The Queue Are = " << iStore << "\n";
    cout << "The Element From The Queue After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Dequeue();
    cout << "The Element Deleted From The Queue Are = " << iStore << "\n";
    cout << "The Element From The Queue After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Dequeue();
    cout << "The Element Deleted From The Queue Are = " << iStore << "\n";
    cout << "The Element From The Queue After Deleting An Element Are\n";
    sobj.Display();

    iRet = sobj.Count();
    cout << "The Elements Present In The Linked List Are = " << iRet << "\n";
    return 0;
}
