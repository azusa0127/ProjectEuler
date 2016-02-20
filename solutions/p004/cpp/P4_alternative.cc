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
    for (int factor = 999; factor*factor >= n;factor--)
        if ((n%factor == 0) && (n/factor > 99))
            return true;
    return false;
}

int getLargestPalindrome(){      
	int pal;  
    //case of 6-digit palindrome
	for (int i = 997; i>= 100; i--){
		pal = i*1000 +inverseNum(i);
		if (isProductOfTwo3DigitNumber(pal))
			return pal;
	}

    //case of 5-digit palindrome
	for (int i = 999; i>=100; i--){
		pal = i*100 + inverseNum(i/10);
		if (isProductOfTwo3DigitNumber(pal))
			return pal;
	}
	return -1;
}

int main(void) {
	// for(int i= 0; i< 1000; i++)   //for benchmark only
	// 	getLargestPalindrome();      //for benchmark only
    std::cout<<"the largest palindrome made from the product of two 3-digit numbers :" << getLargestPalindrome() << std::endl;
}