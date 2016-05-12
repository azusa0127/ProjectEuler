using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p10summationOfPrimes_
{
    class rules
    {
        public string inputStr = "find sum of prime numbers, from 2 to ? ";
        public string resultStr = "Result: ";

        public long calc(int limit)
        {
            return (findAndSumPrimes(limit));
        }

        private long findAndSumPrimes(int limit)
        {
            long sum = 0;
            int i = 1;
            while (i < limit)
            {
                i++;
                if (checkIfPrime(i))
                    sum += i;
            }
            return sum;
        }

        private bool checkIfPrime(int num)
        {
            for (int i = 2; i * i <= num; i++)
                if (num % i == 0)
                    return false;
            return true;
        }
    }
}
