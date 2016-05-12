using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p710001stPrime
{
    class rules
    {
        public string inputStr = "find nth prime number, n = ? ";
        public string resultStr = "Result: ";

        public int calc(int n)
        {
            return (findTheNthPrime(n));
        }

        private int findTheNthPrime(int n)
        {
            int count = 1;
            int i = 2;
            while (count < n)
            {
                i++;
                if (checkIfPrime(i))
                    count++;
            }
            return i;

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