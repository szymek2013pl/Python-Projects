#include <iostream>
#include <vector>
#include <numeric>
#include <set>

using namespace std;

int main()
{
int sum = 0, sum2 = 0, amount = 0;

vector <int> div1;
vector <int> div2;

vector <int> answers;

for (int i = 2; i < 10000; i++){
    for (int j = 1; j < i; j++){
        if (i % j == 0){
            div1.push_back(j);
            sum = std::accumulate(div1.begin(), div1.end(), 0);
        }
    }
    for (int k = 1; k < sum; k++){
        if (sum % k == 0){
            div2.push_back(k);
            sum2 = std::accumulate(div2.begin(), div2.end(), 0);
        }
    }
    if (sum == sum2){
        answers.push_back(i);
    }
    div1.clear();
    div2.clear();
    sum = 0;
    sum2 = 0;
}
amount = std::accumulate(answers.begin(), answers.end(), 0);

cout<<amount;
}
