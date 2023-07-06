#include <iostream>

using namespace std;

template <class T>
struct node
{
    T iNo;
    struct node *next;
};

// typedef struct node NODE;
// typedef struct node *PNODE;

template <class T>
class StackSL
{
    private:
        node <T> *Top;
        int iSize;

    public:
        StackSL();
        void Push(T);
        int Pop();
        void Display();
        int Count();
};

template <class T>
StackSL <T> :: StackSL()
{
    Top = NULL;
    iSize = 0;
}

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

template <class T>
int StackSL <T> :: Pop()
{
    int iStore = 0;

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

template <class T>
int StackSL <T> :: Count()
{
    return iSize;
}

int main()
{
    int iRet = 0;
    int iStore = 0;
    StackSL<int> sobj;
    sobj.Push(51);
    sobj.Push(21);
    sobj.Push(11);
    sobj.Display();
    iRet = sobj.Count();
    cout << "The Elements Present In The Linked List Are = " << iRet << "\n\n";

    iStore = sobj.Pop();
    cout << "The Element Deleted From The Stack Are = " << iStore << "\n";
    cout << "The Element From The Stack After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Pop();
    cout << "The Element Deleted From The Stack Are = " << iStore << "\n";
    cout << "The Element From The Stack After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Pop();
    cout << "The Element Deleted From The Stack Are = " << iStore << "\n";
    cout << "The Element From The Stack After Deleting An Element Are\n";
    sobj.Display();

    iStore = sobj.Pop();
    cout << "The Element Deleted From The Stack Are = " << iStore << "\n";
    cout << "The Element From The Stack After Deleting An Element Are\n";
    sobj.Display();

    iRet = sobj.Count();
    cout << "The Elements Present In The Linked List Are = " << iRet << "\n";
    return 0;
}