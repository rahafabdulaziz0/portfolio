
#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include "BST.h"
#include "heap.h"
using namespace std;
int main(){
    BST bst;
    cout<<"Enter input file name: ";
    string f; getline(cin,f);
    ifstream in(f);
    int n; in>>n; in.ignore();
    for(int i=0;i<n;i++){
        string d,c; int m;
        getline(in,d); in>>m; in.ignore(); getline(in,c);
        bst.insertTask(Task(d,m,c));
    }
    bst.displayAll();
    return 0;
}
