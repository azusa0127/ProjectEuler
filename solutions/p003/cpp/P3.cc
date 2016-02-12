#include <iostream>
/**
 * Largest prime factor
 * Problem 3
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */
int getLargestPrimeFactorOf(long n){        
    while (n%2 == 0)
        n /= 2;

    int lPrimeFactor = 1;

    while (n > 1){
        lPrimeFactor += 2;
        while (n%lPrimeFactor == 0)
            n /= lPrimeFactor;
    }

    return lPrimeFactor;
}

int main(void) {
    std::cout<<"the largest prime factor of the number " << 600851475143L << " : " << getLargestPrimeFactorOf(600851475143L) << std::endl;
}