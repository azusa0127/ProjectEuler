#include <iostream>
/**
 * Largest palindrome product
 * Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
int inverseNum(int n){
	int inv = 0;
	while (n>0){
		inv *= 10;
		inv += n%10;
		n /= 10;}
	return inv;
}

bool isProductOfTwo3DigitNumber(int n){
    int factor = 1000;
    while (--factor > 100){
        if (n%factor == 0){
            if (n/factor > 999)
                return false;
            else if (n/factor > 99)
                return true;
        }
    }
    return false;
}

int getLargestPalindrome(){      
	int pal;  
	for (int i = 997; i>= 100; i--){
		pal = i*1000 +inverseNum(i);
		if (isProductOfTwo3DigitNumber(pal))
			return pal;
	}

	for (int i = 999; i>=100; i--){
		pal = i*100 + inverseNum(i/10);
		if (isProductOfTwo3DigitNumber(pal))
			return pal;
	}
	return -1;
}

int main(void) {
    std::cout<<"the largest palindrome made from the product of two 3-digit numbers :" << getLargestPalindrome() << std::endl;
}