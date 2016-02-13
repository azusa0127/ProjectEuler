#include <iostream>

// Problem 6: Sum square difference
// The sum of the squares of the first ten natural numbers is,
// 12 + 22 + ... + 102 = 385
// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)2 = 552 = 3025
// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

int getDifferenceForFirst(int limit){
	int sum = 0;
	for (int i = 1; i< limit; i++)
		for (int j= i+1; j<= limit; j++)
			sum += i*j;
	return 2*sum;
}

int main(void) {
    std::cout<<"the difference between the sum of the squares and the square of the sum for first " << 100 << "th items: " << getDifferenceForFirst(100) << std::endl;
}