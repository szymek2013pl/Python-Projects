#include <iostream>

using namespace std;

int main()
{

long long sum = 28;
int num = 8;

int divisors = 0;

while (true){

    for (int i = sum; i >= 1; i--){
        if (sum % i == 0){
            divisors++;
            if (divisors >= 500){
                break;
            }
            else {
                divisors = 0;
                sum += num;
                num += 1;
            }
        }
    }
}
cout<<sum;
}


