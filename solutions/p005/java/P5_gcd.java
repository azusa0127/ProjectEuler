/**
 * Problem 5: Smallest multiple
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */

public class P5_gcd{
     private static int gcd(int nLarge, int nSmall){
		if (nLarge % nSmall != 0)
			return gcd(nSmall, nLarge % nSmall);
		return nSmall;
	}

	private static int lcm(int nLarge, int nSmall){
		return (nLarge*nSmall)/gcd(nLarge,nSmall);
	}

    private static int getSmallestMultipleFrom1to(int limit){
	    int multiple = limit;
	    for (int i=2; i<limit; i++)
	        multiple = lcm(multiple, i);
	    return multiple;
	}

    public static void main(String[] args) {
        System.out.println("the smallest positive number that is evenly divisible by all of the numbers from 1 to " + 20 + " : " + getSmallestMultipleFrom1to(20));
    }
}