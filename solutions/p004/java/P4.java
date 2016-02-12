/**
 * Largest palindrome product
 * Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class P3{
    private static int getLargestPalindrome(){      
    	int pal;  
    	for (int i = 997; i>= 100; i--){
    		pal = i*1000 +inverseNum(i);
    		
    	}
    }

    private static inverseNum(int n){
    	int inv = 0;
    	while (n>0){
    		inv *= 10;
    		inv += n%10;
    		n /= 10;}
    	return inv;
    }

    private static int[] getFactors(int n){
    	int[] factors = new int[10]{1,1,1,1,1,1,1,1,1,1};
    	int count = 0;
    	if (n%2 == 0){
	    	while(n%2 == 0){
	    		factors[count] *= 2;
	    		n/=2;}
	    	count++;
    	}

    	for (int i = 3; n > 1 ;i+=2) {
	    	if (n%i == 0){
		    	while(n%i == 0){
		    		factors[count] *= i;
		    		n/=i;}
		    	count++;
	    	}
    	}
    	return factors;
    }

    private static boolean isProductOfTwo

    public static void main(String[] args) {
        System.out.println("the largest palindrome made from the product of two 3-digit numbers :" + getLargestPalindrome());
    }
}
‭