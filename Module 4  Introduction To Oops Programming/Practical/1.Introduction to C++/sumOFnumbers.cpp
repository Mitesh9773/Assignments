// 4. Setting Up Development Environment
// o Write a program that asks for two numbers and displays their sum. Ensure this is
// done after setting up the IDE (like Dev C++ or CodeBlocks).
// o Objective: Help students understand how to install, configure, and run programs

#include <iostream>
using namespace std;

int main()
{
    int num1, num2, sum;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    sum = num1 + num2;
    cout << "Sum = " << sum << endl;

    return 0;
}
