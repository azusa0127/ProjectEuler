/**
 * Problem 5: Smallest multiple
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */
public class P5{
    private static int getSmallestMultiple(int nLarge, int nSmall){
    	for (int i = 1; i<nSmall;i++) 
    		if ((nLarge*i)%nSmall == 0)
    			return nLarge*i;
    	return nLarge*nSmall;
    }

    private static int getSmallestMultipleFrom1to(int limit){
    	int multiple = limit;
    	for (int i=2; i<limit; i++)
    		multiple = getSmallestMultiple(multiple, i);
    	return multiple;
    }

    public static void main(String[] args) {
        System.out.println("the smallest positive number that is evenly divisible by all of the numbers from 1 to " + 20 + " : " + getSmallestMultipleFrom1to(20));
    }
}