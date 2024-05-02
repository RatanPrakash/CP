#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    int t;
    std::cin >> t;  // Read the number of test cases

    while (t--) {
        std::string str;
        std::cin >> str;  // Read each test case

        std::unordered_map<char, int> charCount;
        for (char c : str) {
            charCount[c]++;
        }

        if (charCount['A'] > charCount['B']) {
            std::cout << "A" << std::endl;
        } else {
            std::cout << "B" << std::endl;
        }
    }

    return 0;
}
