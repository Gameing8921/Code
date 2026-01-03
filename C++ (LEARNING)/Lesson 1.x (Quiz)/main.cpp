#include <iostream>

void addAndSubtract()
{
    int num1{};
    int num2{};

    std::cout << "Insert two numbers separated by spaces" << "\n";
    std::cin >> num1 >> num2;

    std::cout << num1 << " + " << num2 << " = " << num1 + num2 << "\n";
    std::cout << num1 << " - " << num2 << " = " << num1 - num2 << "\n";
}

int main()
{
    addAndSubtract();
    return 0;
}
