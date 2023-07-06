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

template<class T>
DoublyLL <T>:: DoublyLL()
{
    head = NULL;
    iSize = 0;
}


template<class T>
void DoublyLL <T>:: InsertFirst(T iNo)
{
    node1 <T>*newn = new node1 <T>;
    newn->iNo = iNo;
    newn->next = NULL;
    newn->prev = NULL;

    if (head == NULL)
    {
        head = newn;
    }
    else
    {
        head->prev = newn;
        newn->next = head;
        head = newn;
    }
    iSize++;
}

template<class T>
void DoublyLL <T>:: InsertLast(T iNo)
{
    node1 <T>*newn = new node1 <T>;
    newn->iNo = iNo;
    newn->next = NULL;
    newn->prev = NULL;

    if (head == NULL)
    {
        head = newn;
    }
    else
    {
        node1 <T>*temp = head;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
        newn->prev = temp;
        newn->next = NULL;
    }
    iSize++;
}

template<class T>
void DoublyLL <T>:: InsertAtPos(int iPos, T iNo)
{
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
        node1  <T>*newn = new node1 <T>;
        newn->iNo = iNo;
        newn->next = NULL;
        newn->prev = NULL;

        node1 <T>*temp = head;

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
}

template<class T>
void DoublyLL <T>:: DeleteFirst()
{
    if (head == NULL)
    {
        cout << "Linked List Is Empty !" << endl;
        return;
    }
    else if (head->prev == NULL && head->next == NULL)
    {
        delete (head);
        head = NULL;
    }
    else
    {
        node1 <T>*temp = head;
        head->next->prev = NULL;
        head = head->next;
        delete (temp);
    }
    iSize--;
}

template<class T>
void DoublyLL <T>:: DeleteLast()
{
    if (head == NULL)
    {
        cout << "Linked List Is Empty !" << endl;
        return;
    }
    else if (head->prev == NULL && head->next == NULL)
    {
        delete (head);
        head = NULL;
    }
    else
    {
        node1 <T>*temp = head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }

        node1 <T>*temp1 = temp->prev->next;
        temp->prev->next = NULL;
        delete (temp1);
    }
    iSize--;
}

template<class T>
void DoublyLL <T>:: DeleteAtPos(int iPos)
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
        node1 <T>*temp = head;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        node1 <T>*temp1 = temp->next;

        temp->next->prev = temp;
        temp->next = temp1->next;

        delete (temp1);

        iSize--;
    }
}

template<class T>
void DoublyLL <T>:: Display()
{
    node1 <T>*temp = head;
    while (temp != NULL)
    {
        cout << "|" << temp->iNo << "|->";
        temp = temp->next;
    }
    cout << "|NULL|\n";
}

template<class T>
int DoublyLL <T>:: Count()
{
    return iSize;
}


int main()
{
    DoublyLL<int> lobj;

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

    // lobj.DeleteFirst();
    // lobj.Display();

    // lobj.DeleteLast();
    // lobj.Display();

    lobj.DeleteAtPos(2);
    lobj.Display();

    return 0;
}