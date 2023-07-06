#include<iostream>
#include "Header.h"


//-----------------------------------------------------------------------
// Function Definition of Singly Linear Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  SinglyL
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
SinglyL<T>::SinglyL()
{
    head = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Display linked list.
// Description:    Used to display linked list.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Return linked list element count.
// Description:    Used to return linked list element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int SinglyL <T>:: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertFirst
// Input:          Generic datatype element
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertLast
// Input:          Generic datatype element
// Output:         Insert element at position last in linked list.
// Description:    Used to insert element at position last in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


/////////////////////////////////////////////////////////////////////////////
//
// Function name:  InsertAtPos
// Input:          Generic datatype element, Integer
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
/////////////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteFirst
// Input:               -
// Output:         Delete element from first position in linked list.
// Description:    Used to delete element from first position in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteLast
// Input:               -
// Output:         Delete element from last position in linked list.
// Description:    Used to delete element from last position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteAtPos
// Input:          Integer
// Output:         Delete element from desire position in linked list.
// Description:    Used to delete element from desire position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


//-----------------------------------------------------------------------
// Function Definition of Doubly Linear Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  DoublyLL
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
DoublyLL <T>:: DoublyLL()
{
    head = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Display linked list.
// Description:    Used to display linked list.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Return linked list element count.
// Description:    Used to return linked list element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int DoublyLL <T>:: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertFirst
// Input:          Generic datatype element
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertLast
// Input:          Generic datatype element
// Output:         Insert element at position last in linked list.
// Description:    Used to insert element at position last in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


/////////////////////////////////////////////////////////////////////////////
//
// Function name:  InsertAtPos
// Input:          Generic datatype element, Integer
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
/////////////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteFirst
// Input:               -
// Output:         Delete element from first position in linked list.
// Description:    Used to delete element from first position in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteLast
// Input:               -
// Output:         Delete element from last position in linked list.
// Description:    Used to delete element from last position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteAtPos
// Input:          Integer
// Output:         Delete element from desire position in linked list.
// Description:    Used to delete element from desire position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


//-----------------------------------------------------------------------
// Function Definition of Singly Circular Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  SinglyC
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
SinglyC <T> ::SinglyC()
{
    Head = NULL;
    Tail = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Display linked list.
// Description:    Used to display linked list.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::Display()
{
    node <T> *temp = Head;

    if (temp == NULL && Tail == NULL)
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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Return linked list element count.
// Description:    Used to return linked list element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int SinglyC <T> :: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertFirst
// Input:          Generic datatype element
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::InsertFirst(T iNo)
{
    node  <T> *newn = new node <T>;
    newn->iNo = iNo;
    newn->next = NULL;

    if (Head == NULL && Tail == NULL)
    {
        Head = newn;
        Tail = newn;
    }
    else
    {
        newn->next = Head;
        Head = newn;
    }
    Tail->next = Head;
    iSize++;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertLast
// Input:          Generic datatype element
// Output:         Insert element at position last in linked list.
// Description:    Used to insert element at position last in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::InsertLast(T iNo)
{
    node <T> *newn = new node <T>;
    newn->iNo = iNo;
    newn->next = NULL;

    if (Head == NULL && Tail == NULL)
    {
        Head = newn;
        Tail = newn;
    }
    else
    {
        Tail->next = newn;
        Tail = newn;
    }
    Tail->next = Head;
    iSize++;
}


/////////////////////////////////////////////////////////////////////////////
//
// Function name:  InsertAtPos
// Input:          Generic datatype element, Integer
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::InsertAtPos(int iPos, T iNo)
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
        node <T> *temp = Head;
        node <T> *newn = new node <T>;
        newn->iNo = iNo;
        newn->next = NULL;

        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next = newn;
        iSize++;
    }
    Tail->next = Head;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteFirst
// Input:               -
// Output:         Delete element from first position in linked list.
// Description:    Used to delete element from first position in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::DeleteFirst()
{
    if ((Head == NULL) && (Tail == NULL))
    {
        cout << "No Elements found to delete from the linked list !" << endl;
        return;
    }
    else if (Head == Tail)
    {
        delete(Head);
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        node <T> *temp = Head;
        Head = Head->next;
        delete (temp);
    }
    Tail->next = Head;
    iSize--;
}


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteLast
// Input:               -
// Output:         Delete element from last position in linked list.
// Description:    Used to delete element from last position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::DeleteLast()
{
    if ((Head == NULL) && (Tail == NULL))
    {
        cout << "No Elments Ware found to delete from the linked list !" << endl;
        return;
    }
    else if (Head == Tail)
    {
        delete(Head);
        Head = NULL;
        Tail = NULL;
    }
    else
    {
        node <T> *temp = Head;
       do{
           temp = temp->next;
       }while(temp->next->next != Tail->next);

       delete(temp->next);
       Tail = temp;
       Tail->next = Head;
    }
    Tail->next = Head;
    iSize--;
}


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteAtPos
// Input:          Integer
// Output:         Delete element from desire position in linked list.
// Description:    Used to delete element from desire position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyC <T> ::DeleteAtPos(int iPos)
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
        node <T> *temp = Head;
        for (int i = 1; i < iPos - 1; i++)
        {
            temp = temp->next;
        }

        node <T> *temp1 = temp->next;
        temp->next = temp->next->next;
        delete (temp1);
    }
    Tail->next = Head;
    iSize--;
}


//-----------------------------------------------------------------------
// Function Definition of Doubly Circular Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  DoublyC
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
DoublyC <T> :: DoublyC()
{
    Head = NULL;
    Tail = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Display linked list.
// Description:    Used to display linked list.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Return linked list element count.
// Description:    Used to return linked list element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
int DoublyC <T> :: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertFirst
// Input:          Generic datatype element
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
void DoublyC <T> :: InsertFirst(T iNo)
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
        newn->next = Head;
        Head = newn;
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize++;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertLast
// Input:          Generic datatype element
// Output:         Insert element at position last in linked list.
// Description:    Used to insert element at position last in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
void DoublyC <T>:: InsertLast(T iNo)
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
        Tail = newn;
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize++;
}


/////////////////////////////////////////////////////////////////////////////
//
// Function name:  InsertAtPos
// Input:          Generic datatype element, Integer
// Output:         Insert element at position first in linked list.
// Description:    Used to insert element at position first in linked list
// Author:         Manish M Tambe
//
/////////////////////////////////////////////////////////////////////////////

template <class T>
void DoublyC <T> :: InsertAtPos(int iPos, T iNo)
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
    Tail->next = Head;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteFirst
// Input:               -
// Output:         Delete element from first position in linked list.
// Description:    Used to delete element from first position in linked list
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
void DoublyC <T> :: DeleteFirst()
{
    if (Head == NULL && Tail == NULL)
    {
        cout << "No elements ware found ! Linked List is empty !";
        return;
    }

    if (Head == Tail)
    {
        delete(Head);
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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteLast
// Input:               -
// Output:         Delete element from last position in linked list.
// Description:    Used to delete element from last position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template <class T>
void DoublyC <T> :: DeleteLast()
{
    if ((Head == NULL) && (Tail == NULL))
    {
        cout << "No elements ware found ! Linked List is empty";
        return;
    }
    if (Head == Tail)
    {
        delete(Head);
        Head = NULL;
        Tail = NULL;
    }
    else
    {
      Tail = Tail->prev;
      delete(Tail->next);
    }
    Head->prev = Tail;
    Tail->next = Head;
    iSize--;
}


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteAtPos
// Input:          Integer
// Output:         Delete element from desire position in linked list.
// Description:    Used to delete element from desire position in linked list
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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

//-----------------------------------------------------------------------
// Function Definition Prototype of Stack using Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  StackSL
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
StackSL <T> :: StackSL()
{
    Top = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Used to display stack elements.
// Description:    Display stack elements.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
void StackSL <T> :: Display()
{
    node <T> *temp = Top;
    while (temp != NULL)
    {
        cout << "|" << temp->iNo << "|->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Used to return stack element count.
// Description:    Return stack element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
int StackSL <T> :: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Push
// Input:          Generic datatype element
// Output:         Used to insert element in stack.
// Description:    Insert element in stack.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template <class T>
void StackSL <T> :: Push(T iNo)
{
    node <T> *newn = new node <T>;
    newn->next = NULL;
    newn->iNo = iNo;

    if (Top == NULL)
    {
        Top = newn;
    }
    else
    {
        newn->next = Top;
        Top = newn;
    }
    iSize++;
}


////////////////////////////////////////////////////////////////////////////
//
// Function name:  Pop
// Input:               -
// Output:         Delete element from stack.
// Description:    Used to delete element from stack.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template <class T>
T StackSL <T> :: Pop()
{
    T iStore;

    if (Top == NULL)
    {
        cout << "Stack is empty !";
        return 0;
    }
    else
    {
        iStore = Top->iNo;
        node <T> *temp = Top;
        Top = Top->next;
        delete (temp);
    }
    iSize--;
    return iStore;
}


//-----------------------------------------------------------------------
// Function Definition Prototype of Queue using Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  QueueSL
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
QueueSL <T> :: QueueSL()
{
    Top = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Used to display queue elements.
// Description:    Display queue elements.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Used to return queue element count.
// Description:    Return queue element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int QueueSL <T>:: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Enqueue
// Input:          Generic datatype element
// Output:         Used to insert element in queue.
// Description:    Insert element in queue.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  Dequeue
// Input:               -
// Output:         Delete element from queue.
// Description:    Used to delete element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template<class T>
T QueueSL <T> :: Dequeue()
{
    T iStore;

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


//-----------------------------------------------------------------------
// Function Definition Prototype of Circular Queue using Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  CircularQueueSL
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
CircularQueueSL <T> :: CircularQueueSL()
{
    Rear = NULL;
    Front = NULL;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Used to display queue elements.
// Description:    Display queue elements.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Used to return queue element count.
// Description:    Return queue element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int CircularQueueSL <T>:: Count()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Enqueue
// Input:          Generic datatype element
// Output:         Used to insert element in queue.
// Description:    Insert element in queue.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  Dequeue
// Input:               -
// Output:         Delete element from queue.
// Description:    Used to delete element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

template<class T>
T CircularQueueSL <T> :: Dequeue()
{
    T iStore;
    if (Front == NULL && Rear == NULL)
    {
        cout<< "Queue is underflow ! No elements to POP" << endl;
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


//-----------------------------------------------------------------------
// Function Definition Prototype of Doubly Ended Queue using Linked List
//-----------------------------------------------------------------------

///////////////////////////////////////////////////////////////////////
//
// Constructor name:  Dequeue
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
Dequeue <T> :: Dequeue()
{
    iSize = 0;
    Head = NULL;
    Tail = NULL;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Display
// Input:            -
// Output:         Used to display queue elements.
// Description:    Display queue elements.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


///////////////////////////////////////////////////////////////////////
//
// Function name:  Count
// Input:            -
// Output:         Used to return queue element count.
// Description:    Return queue element count.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
int Dequeue <T>:: getCount()
{
    return iSize;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertFront
// Input:          Generic datatype element
// Output:         Used to insert element in queue from Front.
// Description:    Insert element in queue.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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

///////////////////////////////////////////////////////////////////////
//
// Function name:  InsertRear
// Input:          Generic datatype element
// Output:         Used to insert element in queue from Rear.
// Description:    Insert element in queue.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteFront
// Input:               -
// Output:         Delete element from front of the queue.
// Description:    Used to delete element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteRear
// Input:               -
// Output:         Delete element from rear end of the queue.
// Description:    Used to delete element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  getFront
// Input:               -
// Output:         Get element from front of the queue.
// Description:    Used to get element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


////////////////////////////////////////////////////////////////////////////
//
// Function name:  getRear
// Input:               -
// Output:         Get element from rear end of the queue.
// Description:    Used to get element from queue.
// Author:         Manish M Tambe
//
////////////////////////////////////////////////////////////////////////////

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


//-----------------------------------------------------------------------
// Function Definition of BST Using Linked List
//-----------------------------------------------------------------------

//////////////////////////////////////////////////////////////
//
// Constructor name:  BST
// Input:          Initialization of variables.
// Output:         Variable initialized.
// Description:    Used to initialize variables.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////

template<class T>
BST <T> :: BST()
{
    root = nullptr;
    iSize = 0;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Creat
// Input:          Generic datatype element
// Output:         Create node of an BST.
// Description:    Used to create node of the BST.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
bstnode <T> * BST <T>:: Create(T iNo)
{
    bstnode <T> *newn = new bstnode <T>;
    newn->iNo = iNo;
    newn->left = NULL;
    newn->right = NULL;

    return newn;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  Insert
// Input:          Generic datatype element
// Output:         Insert element in the BST.
// Description:    Used to insert element in the BST.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
bstnode <T> * BST <T> :: Insert(bstnode <T> *root, T iNo)
{
    if(root == nullptr)
    {
        return Create(iNo);
    }

    if(root->iNo == iNo)
    {
        cout<<"Element Alredy Exixts In The BST So Element Will Be Not Get Inserted In BST !"<<endl;
        return root;
    }

    if(iNo <= root->iNo)
    {
        root->left = Insert(root->left, iNo);
    }
    else
    {
        root->right = Insert(root->right, iNo);
    }

    return root;
}

//////////////////////////////////////////////////////////////////////////////
//
// Function name:  (Overloaded) Insert
// Input:          -
// Output:         Overload Insert and insert elements in BST.
// Description:    Used to insert elements in BST.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Insert(T iNo)
{
    root = Insert(root, iNo);
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  GetMin
// Input:          root node, Generic datatype element
// Output:         Return BST node with the minimum value.
// Description:    Used to return BST node with the minimum value.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
bstnode <T> * BST <T>:: GetMin(bstnode <T> *root)
{
    bstnode <T> *temp = root;

    if(temp == nullptr)
    {
        return temp;
    }
    else
    {
        while(temp->left != nullptr)
        {
            temp = temp->left;
        }
    }
    return temp;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  GetMax
// Input:          root node, Generic datatype element
// Output:         Return BST node with the maximum value.
// Description:    Used to return BST node with the maximum value.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
bstnode <T> * BST <T>:: GetMax(bstnode <T> *root)
{
    bstnode <T> *temp = root;

    if(temp == nullptr)
    {
        return temp;
    }
    else
    {
        while(temp->right != nullptr)
        {
            temp = temp->right;
        }
    }
    return temp;
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DisplayInorder
// Input:          Root node
// Output:         Display BST in Inorder Traversal.
// Description:    Used to display BST in Inorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void BST <T>:: Inorder(bstnode <T> *root)
{
    if(root == nullptr)
    {
        return;
    }

    Inorder(root->left);
    cout<<root->iNo<<" ";
    Inorder(root->right);
}


//////////////////////////////////////////////////////////////////////////////
//
// Function name:  (Overloaded) DisplayInorder
// Input:          -
// Output:         Overload DisplayInorder and Display BST in Inorder Traversal.
// Description:    Used to display BST in Inorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Inorder()
{
    Inorder(root);
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DisplayPreorder
// Input:          Root node
// Output:         Display BST in Preorder Traversal.
// Description:    Used to display BST in Preorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Preorder(bstnode <T> *root)
{
    if(root == nullptr)
    {
        return;
    }
    cout<<root->iNo<<" ";
    Preorder(root->left);
    Preorder(root->right);
}


//////////////////////////////////////////////////////////////////////////////
//
// Function name:  (Overloaded) DisplayPreorder
// Input:          -
// Output:         Overload DisplayPreorder and Display BST in Preorder Traversal.
// Description:    Used to display BST in Preorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Preorder()
{
    Preorder(root);
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DisplayPostorder
// Input:          Root node
// Output:         Display BST in Postorder Traversal.
// Description:    Used to display BST in Postorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Postorder(bstnode <T> *root)
{
    if(root == nullptr)
    {
        return;
    }

    Postorder(root->left);
    Postorder(root->right);
    cout<<root->iNo<<" ";
}


//////////////////////////////////////////////////////////////////////////////
//
// Function name:  (Overloaded) DisplayPostorder
// Input:          -
// Output:         Overload DisplayPostorder and Display BST in Postorder Traversal.
// Description:    Used to display BST in Postorder Traversal.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: Postorder()
{
    Postorder(root);
}


///////////////////////////////////////////////////////////////////////
//
// Function name:  DeleteNode
// Input:          root node, Generic datatype element
// Output:         Remove the specified node from the BST.
// Description:    Used to remove the specified node from the BST.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////

template<class T>
bstnode <T> * BST <T> :: DeleteNode(bstnode <T> *root, T iNo)
{

    if(root == nullptr)
    {
        return root;
    }

    if(root->iNo == iNo)
    {
        if(root->left == nullptr && root->right == nullptr)
        {
            delete(root);
            return nullptr;
        }

        if(root->left != nullptr && root->right == nullptr)
        {
            bstnode <T> *temp = root->left;
            delete(root);
            return temp;
        }

        if(root->left == nullptr && root->right != nullptr)
        {
            bstnode <T> *temp = root->right;
            delete(root);
            return temp;
        }

        if(root->left != nullptr && root->right != nullptr)
        {
            T data = GetMin(root->right)->iNo;
            root->iNo = data;
            root->right = DeleteNode(root->right, data);
            return root;
        }
    }
    else if(iNo > root->iNo)
    {
        root->right = DeleteNode(root->right, iNo);
        return root;
    }
    else if(iNo < root->iNo)
    {
        root->left = DeleteNode(root->left, iNo);
        return root;
    }
    return root;
}


//////////////////////////////////////////////////////////////////////////////
//
// Function name:  (Overloaded) DeleteNode
// Input:          Generic datatype element
// Output:         Overload remove and remove specified node from BST.
// Description:    Used to remove specified node from BST.
// Author:         Manish M Tambe
//
///////////////////////////////////////////////////////////////////////////////

template<class T>
void BST <T> :: DeleteNode(T iNo)
{
    root = DeleteNode(root, iNo);
}


///////////////////////////////////////////////////////////////////////////////

template class SinglyL<int>;
template class SinglyL<double>;
template class SinglyL<float>;
template class SinglyL<char>;
template class SinglyL<std :: string>;

template class DoublyLL<int>;
template class DoublyLL<double>;
template class DoublyLL<float>;
template class DoublyLL<char>;
template class DoublyLL<std :: string>;

template class SinglyC<int>;
template class SinglyC<double>;
template class SinglyC<float>;
template class SinglyC<char>;
template class SinglyC<std :: string>;

template class DoublyC<int>;
template class DoublyC<double>;
template class DoublyC<float>;
template class DoublyC<char>;
template class DoublyC<std :: string>;

template class StackSL<int>;
template class StackSL<double>;
template class StackSL<float>;
template class StackSL<char>;
template class StackSL<std :: string>;

template class QueueSL<int>;
template class QueueSL<double>;
template class QueueSL<float>;
template class QueueSL<char>;
template class QueueSL<std :: string>;

template class CircularQueueSL<int>;
template class CircularQueueSL<double>;
template class CircularQueueSL<float>;
template class CircularQueueSL<char>;
template class CircularQueueSL<std :: string>;

template class Dequeue<int>;
template class Dequeue<double>;
template class Dequeue<float>;
template class Dequeue<char>;
template class Dequeue<std :: string>;

template class BST<int>;
template class BST<double>;
template class BST<float>;
template class BST<char>;
template class BST<std :: string>;

///////////////////////////////////////////////////////////////////////////////