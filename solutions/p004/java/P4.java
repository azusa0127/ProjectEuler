/**
 * Largest palindrome product
 * Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class P4{
    private static int inverseNum(int n){
    	int inv = 0;
    	while (n>0){
    		inv *= 10;
    		inv += n%10;
    		n /= 10;}
    	return inv;
    }

    private static boolean isPalindrome(int n){
    	return (n == inverseNum(n));
    }
 
    private static int getLargestPalindrome(){      
    	int largestPalindrome = 0;

    	for(int a = 999; a > 100; a--){
    		int b, db;
    		if (a%11 != 0){
    			b = 990;
    			db = 11;
    		} else {
    			b = 999;
    			db = 1;
    		}
    		for(; b >= a; b-=db){
				if (a*b <= largestPalindrome)
					break;
				else if(isPalindrome(a*b))
					largestPalindrome = a*b;
			}
    	}
    	return largestPalindrome;
    }

    public static void main(String[] args) {
        System.out.println("the largest palindrome made from the product of two 3-digit numbers :" + getLargestPalindrome());
    }
}
