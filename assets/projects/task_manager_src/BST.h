
#ifndef BST_H
#define BST_H
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;
struct Task{
    string description;
    int durationMinutes;
    string category;
    Task():durationMinutes(0){}
    Task(string d,int m,string c):description(d),durationMinutes(m),category(c){}
};
inline ostream& operator<<(ostream& os,const Task& t){
    os<<"["<<t.description<<", "<<t.durationMinutes<<", "<<t.category<<"]";
    return os;
}
inline string toLowerCopy(string s){
    transform(s.begin(),s.end(),s.begin(),[](unsigned char c){return tolower(c);});
    return s;
}
inline bool containsIgnoreCase(const string& a,const string& b){
    return toLowerCopy(a).find(toLowerCopy(b))!=string::npos;
}
class BST{
    struct Node{
        Task data; Node* left; Node* right;
        Node(Task t):data(t),left(nullptr),right(nullptr){}
    };
    Node* root;
    Node* insert(Node* n,Task t){
        if(!n) return new Node(t);
        if(t.durationMinutes<=n->data.durationMinutes) n->left=insert(n->left,t);
        else n->right=insert(n->right,t);
        return n;
    }
    void inorder(Node* n) const{
        if(!n) return;
        inorder(n->left);
        cout<<n->data<<endl;
        inorder(n->right);
    }
    void destroy(Node* n){
        if(!n) return;
        destroy(n->left); destroy(n->right); delete n;
    }
public:
    BST():root(nullptr){}
    ~BST(){destroy(root);}
    void insertTask(Task t){root=insert(root,t);}
    void displayAll() const{
        if(!root){cout<<"No tasks found."<<endl; return;}
        inorder(root);
    }
};
#endif
