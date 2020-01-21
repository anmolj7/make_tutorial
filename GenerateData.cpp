#include <bits/stdc++.h>
#define FIO(fname) freopen(fname, "w", stdout);
using namespace std;

int main(){
    FIO("sample_data.txt")

    int freq=100, N=20; //Modern problems require modern solutions!
    // to generate random numbers in the range 0 to N
    for(int i=0; i<freq; i++)
        cout << rand()%N << "\n";

    return 0;
}