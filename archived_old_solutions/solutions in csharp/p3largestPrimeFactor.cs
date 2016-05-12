using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p3largestPrimeFactor
{
    class rules
    {
        public string inputStr = "Number: ";
        public string resultStr = "Largest Prime Factor: ";

        public long calc(long num)
        {
            return largestPrime(num);
        }

        private long largestPrime(long num)
        {
            long lPrimeFac = 1;
            long limit = num;
            for (long i = 1; i <= limit; i++)
            {
                if (limit % i == 0)
                {
                    limit /= i;
                    lPrimeFac = i;
                }
            }
            return lPrimeFac;
        }
    }
}