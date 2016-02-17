#include <iostream>

/**
 * Multiples of 3 and 5 (Problem 1)
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 * Created by Phoenix on 2016-02-12.
 */
int sumsOfItemsDivisibleBy(int n, int limit){
    int p = limit/n;
    return n*p*(p+1)/2;
}

int getSumOfAllMultiplesOf3or5Below(int limit){
    return sumsOfItemsDivisibleBy(3,limit-1) + sumsOfItemsDivisibleBy(5,limit-1) - sumsOfItemsDivisibleBy(15,limit-1);
}

int main(void) {
    std::cout<<"Sum of all multiples of 3 or 5 below " << 1000 << " : " << getSumOfAllMultiplesOf3or5Below(1000) << std::endl;
}