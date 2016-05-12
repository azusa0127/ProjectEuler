using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p2EvenFibonacciNumbers
{
    class rules
    {
        public string inputStr = "Limit: ";
        public string resultStr = "Result: ";

        public int calc(int limit)
        {
            return sumFb(limit);
        }

        private int sumFb(int limit)
        {
            int sum = 2;
            int n1 = 1;
            int n2 = 2;
            int tmp;
            while ((n1 + n2) <= limit)
            {
                tmp = n1 + n2;
                if (tmp % 2 == 0)
                    sum += tmp;
                n1 = n2;
                n2 = tmp;
            }
            return sum;
        }
    }
}