#include <iostream>
/**
 * Problem 5: Smallest multiple
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */


bool isPrime(int n){
	if (n%2 == 0)
		return false;
	for (int i=3; i*i<=n; i+=2)
		if (n%i == 0)
			return false;
	return true;
}

void generatePrimeTableOfFirst(int nTerms, int primeArray[]){
	primeArray[0] = 2;
	int i = 3;
	for(int count = 1; count < nTerms; count++){
		while (!isPrime(i))
			i+=2;
		primeArray[count] = i;
		i+=2;
	}
}

int getSmallestMultipleFrom1to(int limit){
	int primeArray[8] = {};
	generatePrimeTableOfFirst(8, primeArray);
	int primePowersArray[8] = {};

	for(int i = 2; i<= limit; i++){
		int k = i;
		for (int pc = 0; pc< 8; pc++){
			int count = 0;
			while ((k != 0) && (k % primeArray[pc] == 0)){
				k /= primeArray[pc];
				count++;
			}
			if (primePowersArray[pc] < count)
				primePowersArray[pc] = count;
		}
	}

	int smallestMultiple = 1;
	for (int i = 0; i<8; i++)
		for (int j = 0; j< primePowersArray[i]; j++)
			smallestMultiple *= primeArray[i];

	return smallestMultiple;
}

int main(void) {
    std::cout<<"the smallest positive number that is evenly divisible by all of the numbers from 1 to " << 20 << " : " << getSmallestMultipleFrom1to(20) << std::endl;
}