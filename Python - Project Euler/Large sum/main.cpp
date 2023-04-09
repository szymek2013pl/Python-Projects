#include <iostream>

using namespace std;

int main()
{
long long sum = 0, odp;

for (int i = 0; i < 100; i++){
    cin>>odp;
    odp += sum;
}

cout<<sum;
}
