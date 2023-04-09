#include <iostream>

using namespace std;

int main()
{
int total = 0, index = 2, fib = 0;

int x0 = 1;
int x1 = 1;

while (fib < 4000000){
    fib = x0 + x1;
    x0 = x1;
    x1 = fib;
    if (fib % 2 == 0){
        total = total + fib;
    }
}
cout<<total;
}
