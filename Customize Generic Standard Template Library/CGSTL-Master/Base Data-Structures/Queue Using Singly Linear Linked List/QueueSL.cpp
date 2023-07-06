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
class QueueSL
{
private:
    node <T> *Top;
    int iSize;

public:
    QueueSL();
    void Enqueue(T);
    int Dequeue();
    void Display();
    int Count();
};

template<class T>
QueueSL <T> :: QueueSL()
{
    Top = NULL;
    iSize = 0;
}


template<class T>
void QueueSL <T> :: Enqueue(T iNo)
{
    node <T> *newn = new node <T>;
    newn->iNo = iNo;
    newn->next = NULL;

    if (Top == NULL)
    {
        Top = newn;
    }
    else
    {
        node <T> *temp = Top;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
    }
    iSize++;
}

template<class T>
int QueueSL <T> :: Dequeue()
{
    int iStore = 0;

    if (Top == NULL)
    {
        cout << "Queue is underflow";
        return 0;
    }
    else
    {
        node <T> *temp = Top;
        iStore = Top->iNo;

        Top = Top->next;
        delete (temp);
    }
    iSize--;
    return iStore;
}

template<class T>
void QueueSL <T> :: Display()
{
    node <T> *temp = Top;

    while (temp != NULL)
    {
        cout << "|" << temp->iNo << "|->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

template<class T>
int QueueSL <T>:: Count()
{
    return iSize;
}

int main()
{
    int iRet = 0;
    int iStore = 0;
    QueueSL<int> sobj;
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
