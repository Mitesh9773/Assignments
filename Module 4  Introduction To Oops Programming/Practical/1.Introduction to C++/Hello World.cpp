// 1)  First C++ Program: Hello World
//  o Write a simple C++ program to display "Hello, World!".
//  o Objective: Understand the basic structure of a C++ program, including #include,
//  main(), and cout.

#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world!";
}

// 2. Basic Input/Output
// o Write a C++ program that accepts user input for their name and age and then
// displays a personalized greeting.
// o Objective: Practice input/output operations using cin and cout.

// int main()
// {
//     char name[20];
//     int age;

//     cout << "Enter your name: ";
//     cin >> name;
//     cout << "Enter your age: ";
//     cin >> age;

//     cout << "Good Morning";
// }

class Areaofrectengle
{
public:
    float lenght, breadth, area;
};

int main()
{
    Areaofrectengle obj;
    cout << "Enter the length of rectengle:";
    cin >> obj.lenght;

    cout << "Enter the breadth of rectengle:";
    cin >> obj.breadth;

    obj.area = obj.breadth * obj.lenght;
    cout << "The area of rectengle is: " << obj.area;
}