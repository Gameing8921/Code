#include <iostream>

int doubleInput(int input)
{
    return input * 2;
}

int main()
{
    int num{};

    std::cout << "Enter an integer: ";
    std::cin >> num;

    std::cout << num << " doubled is equal to " << doubleInput(num) << "\n";
    return 0;
}
