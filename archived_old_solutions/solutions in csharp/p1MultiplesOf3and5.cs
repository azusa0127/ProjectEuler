using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p1MultiplesOf3and5
{
    class rules
    {
        public string inputStr = "Enter a interger here: ";
        public string resultStr = "Result: ";

        public int calc(int limit)
        {
            return (threeSum(limit) + fiveSum(limit) - fifteenSum(limit));
        }

        private int threeSum(int limit)
        {
            int sum3 = 0;
            const int baseint = 3;
            for (int i = 1; (i * baseint < limit); i++)
                sum3 += baseint * i;
            return sum3;
        }

        private int fiveSum(int limit)
        {
            int sum5 = 0;
            const int baseint = 5;
            for (int i = 1; (i * baseint < limit); i++)
                sum5 += baseint * i;
            return sum5;
        }

        private int fifteenSum(int limit)
        {
            int sum15 = 0;
            const int baseint = 15;
            for (int i = 1; (i * baseint < limit); i++)
                sum15 += baseint * i;
            return sum15;
        }
    }
}
