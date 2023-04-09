#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;

int is_prime(int N){
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

/*
bool isPerfectSquare(int X)
{
    if (X >= 0) {
        int sr = sqrt(X);
        return (sr * sr == X);
    }
    return false;
}
*/

int main()
{
int n = 33;

while (true){
    int number;
    int root;
    if (is_prime(n) == 0){
        for (int i = n - 2; i >= 2; i--){
            if (is_prime(i) == 1){
                number = (n - i) / 2;
                if (int(sqrt(number)) ** 2 == number){
                    break;
                }
            }
        }
    }
    n += 2;
}
cout<<n;
}
