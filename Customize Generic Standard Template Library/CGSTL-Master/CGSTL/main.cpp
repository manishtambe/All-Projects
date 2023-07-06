/////////////////////////////////////////////////
//
// Sample Code For Demonstrating Header File Use.
//1
/////////////////////////////////////////////////

#include <iostream>

/////////////////////////////////////////////////
// Include User Defined Header File.
/////////////////////////////////////////////////

#include "Header.h"

using namespace std;

int main()
{
    int ch = 0;
    while (true)
    {
        cout << endl << "-----------------------------------" << endl;
        cout << "1. Singly Linear Linked List" << endl
             << "2. Singly Circular Linked List" << endl
             << "3. Doubly Linear Linked List" << endl
             << "4. Doubly Circular Linked List" << endl
             << "5. Stack " << endl
             << "6. Queue " << endl
             << "7. Circular Queue"<< endl
             << "8. Double Ended Queue"<< endl
             << "9. Binary Search Tree" << endl
             << "10. Exit " << endl;
        cout << "-----------------------------------" << endl;
        cout << "Enter your choice : ";
        cin >> ch;

        switch (ch)
        {
            case 1:
            {
                SinglyL<int> s1;
                s1.InsertFirst(1);
                s1.InsertFirst(2);
                s1.InsertFirst(3);
                cout << endl << "Singly Linked List after Inserting Element at First Position : ";
                s1.Display();
                s1.InsertLast(9);
                s1.InsertLast(8);
                cout << endl << "Singly Linked List after Inserting Element at Last Position : ";
                s1.Display();
                s1.InsertAtPos(4,2);
                cout << endl << "Singly Linked List after Inserting Element at Specified Position : ";
                s1.Display();
                s1.DeleteFirst();
                cout << endl << "Singly Linked List after Deleting Element at First Position : ";
                s1.Display();
                s1.DeleteLast();
                cout << endl << "Singly Linked List after Deleting Element at Last Position : ";
                s1.Display();
                s1.DeleteAtPos(2);
                cout << endl << "Singly Linked List after Deleting Element at Specified Position : ";
                s1.Display();
                break;
            }
            case 2:
            {
                SinglyC<float> s1;
                s1.InsertFirst(1.01);
                s1.InsertFirst(2.02);
                s1.InsertFirst(3.03);
                cout << endl << "S Circular Linked List after Inserting Element at First Position : ";
                s1.Display();
                s1.InsertLast(9.09);
                s1.InsertLast(8.08);
                cout << endl << "S Circular Linked List after Inserting Element at Last Position : ";
                s1.Display();
                s1.InsertAtPos(3, 10.010);
                cout<< endl << "S Circular Linked List after Inserting Element at Specified Position : ";
                s1.Display();
                s1.DeleteFirst();
                cout<< endl << "S Circular Linked List after Deleting Element at First Position : ";
                s1.Display();
                s1.DeleteLast();
                cout<< endl << "S Circular Linked List after Deleting Element at Last Position : ";
                s1.Display();
                s1.DeleteAtPos(4);
                cout<< endl << "S Circular Linked List after Deleting Element at Specified Position : ";
                s1.Display();
                break;
            }
            case 3:
            {
                DoublyLL<string> s1;
                s1.InsertFirst("Hello");
                s1.InsertFirst("Hi");
                s1.InsertFirst("Hey");
                cout<< endl << "Doubly Linked List after Inserting Element at First Position : ";
                s1.Display();
                s1.InsertLast("Bonjour");
                s1.InsertLast("Hola");
                cout<< endl << "Doubly Linked List after Inserting Element at Last Position : ";
                s1.Display();
                s1.InsertAtPos(3, "Konnichiwa");
                cout<< endl << "Doubly Linked List after Inserting Element at Specified Position : ";
                s1.Display();
                s1.DeleteFirst();
                cout<< endl << "Doubly Linked List after Deleting Element at First Position : ";
                s1.Display();
                s1.DeleteLast();
                cout<< endl << "Doubly Linked List after Deleting Element at Last Position : ";
                s1.Display();
                s1.DeleteAtPos(4);
                cout<< endl << "Doubly Linked List after Deleting Element at Specified Position : ";
                s1.Display();
                break;
            }
            case 4:
            {
                DoublyC<char> s1;
                s1.InsertFirst('A');
                s1.InsertFirst('B');
                s1.InsertFirst('C');
                cout<< endl << "D Circular Linked List after Inserting Element at First Position : ";
                s1.Display();
                s1.InsertLast('E');
                s1.InsertLast('F');
                cout<< endl << "D Circular Linked List after Inserting Element at Last Position : ";
                s1.Display();
                s1.InsertAtPos(3, 'Z');
                cout<< endl << "D Circular Linked List after Inserting Element at Specified Position : ";
                s1.Display();
                s1.DeleteFirst();
                cout<< endl << "D Circular Linked List after Deleting Element at First Position : ";
                s1.Display();
                s1.DeleteLast();
                cout<< endl << "D Circular Linked List after Deleting Element at Last Position : ";
                s1.Display();
                s1.DeleteAtPos(4);
                cout<< endl << "D Circular Linked List after Deleting Element at Specified Position : ";
                s1.Display();
                break;
            }
            case 5:
            {
                StackSL<int> s1;
                s1.Push(11);
                cout<< endl << "Stack after Pushing One Element : ";
                s1.Display();
                s1.Push(22);
                s1.Push(33);
                cout<< endl << "Stack after Pushing Multiple Elements : ";
                s1.Display();
                int temp = s1.Count();
                cout<< endl << "Number of Elements in the Stack : " << temp;
                s1.Pop();
                cout<< endl << endl << "Stack after Poping One Element : ";
                s1.Display();
                s1.Pop();
                s1.Pop();
                cout<< endl << "Stack after Poping All Elements : ";
                s1.Display();
                break;
            }
            case 6:
            {
                QueueSL<char> s1;
                s1.Enqueue('A');
                cout<< endl << "Queue After Pushing One Element : ";
                s1.Display();
                s1.Enqueue('B');
                s1.Enqueue('C');
                cout<< endl << "Queue After Pushing Multiple Elements : ";
                s1.Display();
                int temp = s1.Count();
                cout<< endl << "Number of Elements in the Queue : " << temp;
                s1.Dequeue();
                cout<< endl << endl << "Queue After Poping One Element : ";
                s1.Display();
                s1.Dequeue();
                s1.Dequeue();
                cout<< endl << "Queue After Poping All Elements : ";
                s1.Display();
                break;
            }
            case 7:
            {
                CircularQueueSL<char> s1;
                s1.Enqueue('A');
                cout<< endl << "Queue After Pushing One Element : ";
                s1.Display();
                s1.Enqueue('B');
                s1.Enqueue('C');
                cout<< endl << "Queue After Pushing Multiple Elements : ";
                s1.Display();
                int temp = s1.Count();
                cout<< endl << "Number of Elements in the Queue : " << temp;
                s1.Dequeue();
                cout<< endl << endl << "Queue After Poping One Element : ";
                s1.Display();
                s1.Dequeue();
                s1.Dequeue();
                cout<< endl << "Queue After Poping All Elements : ";
                s1.Display();
                break;
            }
            case 8:
            {
                Dequeue <int> dq;
                dq.InsertRear(5);
                cout<< endl << "Queue After Pushing One Element : ";
                dq.Display();
                dq.InsertRear(10);
                dq.InsertRear(20);
                cout<< endl << "Queue After Pushing Multiple Elements : ";
                dq.Display();
                cout << "Rear end element: " << dq.getRear() << endl;
                dq.DeleteRear();
                cout << "After deleting rear element new rear is: " << dq.getRear() << endl;
                cout << "Inserting element '15' at front end";
                dq.InsertFront(15);
                cout << "Front end element: " << dq.getFront() << endl;
                cout << "Number of elements in Dequeue: " << dq.getCount()<< endl;
                dq.DeleteFront();
                cout << "After deleting front element new front is: " << dq.getFront() << endl;
                cout<<"Elements in queue after performing operations: -";
                dq.Display();
                break;
            }
            case 9:
            {
                bool loopv = true;
                int ch1 = 0;
                int No,Ret = 0;
                loop : while (loopv)
            {
                cout<<endl<<"------------"<<endl;
                cout<<"1. Integer values"<<endl<<"2. Float values"<<endl<<"3. Character values"<<endl<<"4. Exit From BST";
                cout<<endl<<"------------"<<endl;
                cout<<"Enter your choice : ";
                cin>>ch1;
                switch (ch1)
                {
                    case 1:
                    {
                        BST <int> b1;
                        b1.Insert(2);
                        b1.Insert(7);
                        b1.Insert(2);
                        b1.Insert(9);
                        b1.Insert(1);
                        b1.Insert(5);
                        b1.Insert(14);
                        cout<<"Binary Search Tree After Inserting Elements : ";
                        b1.Inorder();

                        cout<<"Binary Search Tree Displayed In Inorder Format : ";
                        b1.Inorder();

                        cout<<endl<<"Binary Search Tree Displayed In Preorder Format : ";
                        b1.Preorder();

                        cout<<endl<<"Binary Search Tree Displayed In Postorder Format : ";
                        b1.Postorder();
                        No = 0;
                        cout<<endl<<"Enter Element to be Removed From the Tree : ";
                        cin>>No;
                        b1.DeleteNode(No);
                        cout<<endl<<"Binary Search Tree After Deleting the Element : ";
                        b1.Inorder();
                        break;
                    }
                    case 2:
                    {
                        BST<float> b1;
                        b1.Insert(2.02);
                        b1.Insert(7.07);
                        b1.Insert(2.04);
                        b1.Insert(9.09);
                        b1.Insert(1.01);
                        b1.Insert(5.05);
                        b1.Insert(14.14);
                        cout<<"Binary Search Tree After Inserting Elements : ";
                        b1.Inorder();

                        cout<<"Binary Search Tree Displayed In Inorder Format : ";
                        b1.Inorder();

                        cout<<endl<<"Binary Search Tree Displayed In Preorder Format : ";
                        b1.Preorder();

                        cout<<endl<<"Binary Search Tree Displayed In Postorder Format : ";
                        b1.Postorder();
                        No = 0;
                        cout<<endl<<"Enter Element to be Removed From the Tree : ";
                        cin>>No;
                        b1.DeleteNode(No);
                        cout<<endl<<"Binary Search Tree After Deleting the Element : ";
                        b1.Inorder();
                        break;
                    }
                    case 3:
                    {
                        BST <char> b1;
                        b1.Insert('A');
                        b1.Insert('C');
                        b1.Insert('R');
                        b1.Insert('T');
                        b1.Insert('G');
                        b1.Insert('H');
                        b1.Insert('Q');
                        cout<<"Binary Search Tree After Inserting Elements : ";
                        b1.Inorder();

                        cout<<"Binary Search Tree Displayed In Inorder Format : ";
                        b1.Inorder();

                        cout<<endl<<"Binary Search Tree Displayed In Preorder Format : ";
                        b1.Preorder();

                        cout<<endl<<"Binary Search Tree Displayed In Postorder Format : ";
                        b1.Postorder();
                        No = 0;
                        cout<<endl<<"Enter Element to be Removed From the Tree : ";
                        cin>>No;
                        b1.DeleteNode(No);
                        cout<<endl<<"Binary Search Tree After Deleting the Element : ";
                        b1.Inorder();
                        break;
                    }
                    case 4:
                    {
                        loopv = false;
                        break;
                    }
                    default:
                        cout<<"Enter a valid Choice !!"<<endl;
                        break;
                }
            }
                break;
            }
            case 10:
            {
                exit(0);
            }
            default:
            {
                cout<< endl << "Enter a valid choice !!" << endl;
                break;
            }
        }
    }
    return 0;
}