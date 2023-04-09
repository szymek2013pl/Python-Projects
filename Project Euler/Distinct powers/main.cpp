#include <iostream>
#include <set>
#include <math.h>

using namespace std;

int main()
{
std::set <long long> arr;

for (int a = 2; a <= 100; a++){
    for (int b = 2; b <= 100; b++){
        arr.insert(pow(a, b));
    }
}
cout<<arr.size();
}
