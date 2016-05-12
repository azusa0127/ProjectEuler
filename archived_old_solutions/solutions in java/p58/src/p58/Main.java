/*
Problem 58: Spiral primes


Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
 38 17 16 15 14 13 30
 39 18  5  4  3 12 29
 40 19  6  1  2 11 28
 41 20  7  8  9 10 27
 42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
 */

package p58;

public class Main {
    static int lastNum = 1, primeCounts = 0, numsCounts = 0;

    public static void main(String[] args) {
        int matrixSize = 1; // matrix: n x n, n = 2 * matrixSize + 1

        do{
            CurrentLayerLoop(matrixSize);
            matrixSize++;
        } while (PercentageVarify(primeCounts,numsCounts));

        System.out.println("" + (2*matrixSize+1));
    }

    private static void CurrentLayerLoop(int spiralSize){
        int[] currentLoopNums = DiagonalNumber(lastNum, spiralSize);
        for (int i = 0; i < 4; i++) {
            if (isPrime(currentLoopNums[i]))
                primeCounts++; }
        numsCounts += 4;
        lastNum = currentLoopNums[3];
    }
    private static boolean PercentageVarify(int a, int u){
        if ((double)a/u < 0.1)
            return false;
        return true;
    }

    private static int[] DiagonalNumber(int n, int i){
		int[] diaNums= new int[4];
		for (int q = 0;q<4;q++)
			diaNums[q] = (n += Math.pow(2,i));
        return diaNums;
    }

    private static boolean isPrime(int num){
        int limit = (int)Math.sqrt(num);
        for (int i = 3; i <= limit; i+=2)
            if (num % i == 0)
                return false;
        return true;
    }
}
