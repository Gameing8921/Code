#include <iostream>

int mySolution()
{
    int numberToMultiply{};

    std::cin >> numberToMultiply;

    return numberToMultiply * 2;
}

// int theirSolution()
// {
// }

int main()
{
    std::cout << mySolution();
}
