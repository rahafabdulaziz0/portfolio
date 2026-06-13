
#ifndef HEAP_H
#define HEAP_H
#include "BST.h"
#include <vector>
#include <unordered_map>
using namespace std;
class MinHeap{
    vector<Task> heap;
    void up(int i){
        while(i>0){
            int p=(i-1)/2;
            if(heap[i].durationMinutes<heap[p].durationMinutes){
                swap(heap[i],heap[p]); i=p;
            }else break;
        }
    }
    void down(int i){
        int n=heap.size();
        while(true){
            int l=2*i+1,r=2*i+2,s=i;
            if(l<n&&heap[l].durationMinutes<heap[s].durationMinutes) s=l;
            if(r<n&&heap[r].durationMinutes<heap[s].durationMinutes) s=r;
            if(s!=i){swap(heap[i],heap[s]); i=s;}
            else break;
        }
    }
public:
    void insert(Task t){heap.push_back(t); up(heap.size()-1);}
};
#endif
