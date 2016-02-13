// Problem 7: 10001st prime

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

public class P7{
	private static boolean isPrime(int n){
		if (n%2 == 0)
			return false;
		for (int i=3; i*i <= n; i+=2)
			if (n%i == 0)
				return false;
		return true;
	}

    private static int getTheNthPrime(int nTH){
    	if (nTH == 1)
    		return 2;
    	
    	int cur = 1;
    	while (nTH > 1){
    		cur += 2;
    		while (!isPrime(cur))
    			cur+=2;
    		nTH--;
    	}
    	return cur;
    }

    public static void main(String[] args) {
        System.out.println("the " + 10001 + "th prime number : " + getTheNthPrime(10001));
    }
}