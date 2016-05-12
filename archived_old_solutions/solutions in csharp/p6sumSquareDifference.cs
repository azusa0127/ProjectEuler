using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p6sumSquareDifference
{
    class rules
    {
        public string inputStr = "From 1 to ? ";
        public string resultStr = "Result: ";

        public int calc(int limit)
        {
            return (squareOfSums(limit) - sumOfSquare(limit));
        }

        private int sumOfSquare(int limit)
        {
            int sum = 0;
            for (int i = 1; i <= limit; i++)
                sum += i * i;
            return sum;
        }

        private int squareOfSums(int limit)
        {
            int sum = 0;
            for (int i = 1; i <= limit; i++)
                sum += i;
            sum *= sum;
            return sum;
        }
    }
}
