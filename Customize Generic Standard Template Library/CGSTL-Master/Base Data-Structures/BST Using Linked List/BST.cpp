#include<iostream>

using namespace std;

template<class T>
struct bstnode{
    T iNo;
    struct bstnode *left;
    struct bstnode *right;
};

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

template<class T>
BST <T> :: BST()
{
    root = nullptr;
    iSize = 0;
}

template<class T>
bstnode <T> * BST <T>:: Create(T iNo)
{
    bstnode <T> *newn = new bstnode <T>;
    newn->iNo = iNo;
    newn->left = NULL;
    newn->right = NULL;

    return newn;
}

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

template<class T>
void BST <T> :: Insert(T iNo)
{
    root = Insert(root, iNo);
}

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

template<class T>
void BST <T> :: Inorder()
{
    Inorder(root);
}

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

template<class T>
void BST <T> :: Preorder()
{
    Preorder(root);
}

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

template<class T>
void BST <T> :: Postorder()
{
    Postorder(root);
}

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
            int data = GetMin(root->right)->iNo;
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

template<class T>
void BST <T> :: DeleteNode(T iNo)
{
    root = DeleteNode(root, iNo);
}

int main()
{
    BST<int> bobj;

    bobj.Insert(50);
    bobj.Insert(20);
    bobj.Insert(70);
    bobj.Insert(10);
    bobj.Insert(30);
    bobj.Insert(90);
    bobj.Insert(110);

    cout<<"Tree Displayed In Inorder traversal: - "<<endl;
    bobj.Inorder();

    cout<<"\nTree Displayed In Preorder traversal: - "<<endl;
    bobj.Preorder();

    cout<<"\nTree Displayed In Postorder traversal: - "<<endl;
    bobj.Postorder();

    bobj.DeleteNode(50);

    cout<<"Tree Displayed In Inorder traversal: - "<<endl;
    bobj.Inorder();

    cout<<"\nTree Displayed In Preorder traversal: - "<<endl;
    bobj.Preorder();

    cout<<"\nTree Displayed In Postorder traversal: - "<<endl;
    bobj.Postorder();

    return 0;
}


