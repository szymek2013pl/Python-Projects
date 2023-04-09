#include <iostream>

using namespace std;

int is_first(int N){
    if (N == 0 || N == 1){
        return 0;
    }
    for (int i = 2; i * i <= N; i++){
        if (N % i == 0){
            return 0;
        }
    }
    return 1;
}

int main()
{
int amount = 0;
int index = 1;
long long num = 2;
long long arr[10001];

while (amount <= 10001){
    if (is_first(num) == 1){
        arr[index] = num;
        index++;
        num++;
        amount++;
    }
    else{
        num++;
    }
}
cout<<arr[10001];
}
