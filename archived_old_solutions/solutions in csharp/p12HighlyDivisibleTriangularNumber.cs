using System;
using System.Collections.Generic;
using System.Linq;

namespace p12HighlyDivisibleTriangularNumber
{
    class rules
    {
        public string inputStr = "Number of required Divisors: ";
        public string resultStr = "First triangular number: ";

        public long calc(long limit)
        {
            long largestDivByFar = 0;

            long Sum = 0;
            long nextNum = 1;

            while (largestDivByFar < limit)
            {
                Sum += nextNum++;
                largestDivByFar = checkDivisors(Sum);
            }
            return Sum;
        }

        private int checkDivisors(long num)
        {
            Dictionary<long, int> divs = new Dictionary<long, int>();

            int count = 0;

            for (long i = 1; i * i <= num; i++)
            {
                if ((num % i) == 0)
                {
                    try
                    {
                        divs.Add(i, ++count);
                        divs.Add((num / i), ++count);
                    }
                    catch { }
                }
            }
            return divs.Count;
        }
    }
}