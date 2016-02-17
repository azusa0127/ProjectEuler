/**
 * Even Fibonacci numbers
 * Problem 2
 * Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
 *
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * 
 * By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
 */
public class P2{
    private static int getEvenFibSumsBelow(int limit){
        int sum = 0;
        int prev1 = 8,  prev2 = 2;
        int next = 4*prev1 + prev2;

        while (next <= limit){
            sum += next;
            prev2 = prev1;
            prev1 = next;
            next = 4*prev1 + prev2;
        }

        return sum;
    }

    public static void main(String[] args) {
        System.out.println("sum of the even-valued Fibonacci sequence terms below " + 4000000 + " : " + getEvenFibSumsBelow(4000000));
    }
}