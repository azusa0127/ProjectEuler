// Problem 6: Sum square difference
// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + ... + 10^2 = 385The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^2 = 3025Hence the difference between the sum of the squares 
// of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

public class P6{
    private static int getDifferenceForFirst(int limit){
    	int sum = (limit+1)*limit/2;
    	int sum_sq = (2*limit+1)*(limit+1)*limit/6;
    	return sum*sum - sum_sq;
    }

    public static void main(String[] args) {
        System.out.println("the difference between the sum of the squares and the square of the sum for first " + 100 + "th items: " + getDifferenceForFirst(100));
    }
}