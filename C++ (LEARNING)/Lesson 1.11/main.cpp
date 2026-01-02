#include <iostream>

int mySolution()
{
    int numberToMultiply{};

    std::cin >> numberToMultiply;

    return numberToMultiply * 2;
}

int theirSolution()
{
    std::cout << "Enter an integer: ";

    int num{};       // define variable num as an integer variable
    std::cin >> num; // get integer value from user's keyboard
}

int main()
{
    std::cout << mySolution();
    theirSolution();
}
