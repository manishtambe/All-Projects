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

template<class T>
SinglyL<T>::SinglyL()
{
    head = NULL;
    iSize = 0;
}

template<class T>
void SinglyL<T>::InsertFirst(T iNo)
{
    node <T> *newn = new node <T>;
    newn->iNo = iNo;
    newn->next = NULL;

    if (head == NULL)
    {
        head = newn;
    }
    else
    {
        newn->next = head;
        head = newn;
    }
    iSize++;
}

template<class T>
void SinglyL<T>::InsertLast(T iNo)
{
    node <T> *newn = new node <T>;
    newn->iNo = iNo;
    newn->next = NULL;

    if (head == NULL)
    {
        head = newn;
    }
    else
    {
        node <T> *temp = head;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
        newn->next = NULL;
    }
    iSize++;
}

template<class T>
void SinglyL<T>:: InsertAtPos(T iNo, int iPos)
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
        node <T> *newn = new node <T>;
        newn->next = NULL;
        newn->iNo = iNo;

        node <T> *temp = head;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next = newn;
        iSize++;
    }
}

template<class T>
void SinglyL <T>:: DeleteFirst()
{
    if (head == NULL)
    {
        cout << "Linked List Is Empty !";
        return;
    }
    else
    {
        node <T> *temp = head;
        head = head->next;
        delete (temp);
    }
    iSize--;
}

template<class T>
void SinglyL <T>:: DeleteLast()
{
    if (head == NULL)
    {
        cout << "Linked List Is Empty !";
        return;
    }
    else if (head->next == NULL)
    {
        delete (head);
        head = NULL;
    }
    else
    {
        node <T> *temp = head;
        while (temp->next->next != NULL)
        {
            temp = temp->next;
        }
        delete (temp->next);
        temp->next = NULL;
    }
    iSize--;
}

template<class T>
void SinglyL <T>:: DeleteAtPos(int iPos)
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
        node <T> *temp = head;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        node <T> *temp1 = temp->next;
        temp->next = temp1->next;
        delete (temp1);
        iSize++;
    }
}

template<class T>
void SinglyL <T>:: Display()
{
    node <T> *temp = head;
    while (temp != NULL)
    {
        cout << "|" << temp->iNo << "|->";
        temp = temp->next;
    }
    cout << "|NULL|\n";
}

template<class T>
int SinglyL <T>:: Count()
{
    return iSize;
}

int main()
{
    SinglyL<int> lobj;
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

    lobj.DeleteAtPos(3);
    lobj.Display();

    return 0;
}