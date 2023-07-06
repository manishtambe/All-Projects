#include <iostream>

using namespace std;

template <class T>
struct node1
{
    T iNo;
    struct node1 *next;
    struct node1 *prev;
};

// typedef struct node NODE;
// typedef struct node *PNODE;

template <class T>
class DoublyC
{

private:
    node1 <T> *Head;
    node1 <T> *Tail;
    int iSize;

public:
    DoublyC();
    void InsertFirst(int);
    void InsertLast(int);
    void InsertAtPos(int, int);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();
};

template <class T>
DoublyC <T> :: DoublyC()
{
    Head = NULL;
    Tail = NULL;
    iSize = 0;
}

template <class T>
void DoublyC <T> :: InsertFirst(int iNo)
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
    Head->prev = Tail;
    Tail->next = Head;
    iSize++;
}

template <class T>
void DoublyC <T>:: InsertLast(int iNo)
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
        newn->prev = Tail;
        Tail->next = newn;
        newn->next = Head;
        Tail = newn;
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize++;
}

template <class T>
void DoublyC <T> :: InsertAtPos(int iPos, int iNo)
{
    node1 <T> *newn = new node1 <T>;
    newn->iNo = iNo;
    newn->next = NULL;
    newn->prev = NULL;
    if (iPos > (iSize + 1) || iPos < 1)
    {
        cout << "Unable to insert an element ! Please Give Valid Position !" << endl;
        return;
    }
    else if (iPos == (iSize + 1))
    {
        InsertLast(iNo);
    }
    else if (iPos == 1)
    {
        InsertFirst(iNo);
    }
    else
    {
        node1 <T> *newn = new node1<T>;
        newn->iNo = iNo;
        newn->next = NULL;
        newn->prev = NULL;

        node1 <T> *temp = Head;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        newn->prev = temp;
        newn->next = temp->next;
        temp->next = newn;
        newn->next->prev = newn;
        iSize++;
    }
    Head->prev = Tail;
    Tail->prev = Head;
}

template <class T>
void DoublyC <T> :: DeleteFirst()
{
    if (Head == NULL && Tail == NULL)
    {
        cout << "No elements ware found ! Linked List is empty !";
        return;
    }
    else if (Head == Tail)
    {
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        node1 <T> *temp = Head;
        Head = Head->next;
        delete (temp);
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize--;
}

template <class T>
void DoublyC <T> :: DeleteLast()
{
    if (Head == NULL && Tail == NULL)
    {
        cout << "No elements ware found ! Linked List is empty";
        return;
    }
    else if (Head == Tail)
    {
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        node1 <T> *temp = Tail->prev;
        Tail = temp;
        delete (temp->next);
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize--;
}

template <class T>
void DoublyC <T> :: DeleteAtPos(int iPos)
{
    if (iPos > iSize || iPos < 1)
    {
        cout << "Unable to delete an element ! Please Give Valid Position !" << endl;
        return;
    }
    else if (iPos == iSize)
    {
        DeleteLast();
    }
    else if (iPos == 1)
    {
        DeleteFirst();
    }
    else
    {
        node1 <T> *temp = Head;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        node1 <T> *temp1 = temp->next;

        temp->next->prev = temp;
        temp->next = temp1->next;

        delete (temp1);

        iSize--;
    }
    Head->prev = Tail;
    Tail->next = Head;
}

template <class T>
void DoublyC <T> :: Display()
{
    node1  <T> *temp = Head;
    if (Head == NULL && Tail == NULL)
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
        } while (temp != Tail->next);
        cout << "NULL" << endl;
    }
}

template <class T>
int DoublyC <T> :: Count()
{
    return iSize;
}

int main()
{
    DoublyC <int> lobj;
    lobj.InsertFirst(1);
    lobj.InsertFirst(2);
    lobj.InsertFirst(3);
    lobj.InsertFirst(4);
    lobj.InsertFirst(5);
    lobj.Display();

    // lobj.InsertLast(0);
    // lobj.InsertLast(-1);
    // lobj.InsertLast(-2);
    // lobj.Display();

    cout << "The total number of elements present in the linked list: -" << lobj.Count() << endl;

    // lobj.InsertAtPos(0, 6);
    // lobj.Display();

    lobj.DeleteFirst();
    lobj.Display();

    lobj.DeleteLast();
    lobj.Display();

    lobj.DeleteAtPos(3);
    lobj.Display();

    return 0;
}