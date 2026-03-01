#include <iostream>
using namespace std;
void increment(const int &x)
{
    x++; // LINE-1
}
int main()
{
    const int a = 10;
    int b = 20;
    increment(a); // LINE-2 increment (b); // LINE-3 cout << a << "" << b; return 0;
}