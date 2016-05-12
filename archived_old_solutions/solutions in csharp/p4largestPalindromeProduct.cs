using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p4largestPalindromeProduct
{
    class rules
    {
        public string inputStr = "Digits: ";
        public string resultStr = "Result: ";

        public int calc(int digit)
        {
            int n1 = 999;
            int n2 = 999;

            if (digit > 0)
            {
                n1 = 0;
                for (int i = digit; i > 0; i--)
                    n1 = n1 * 10 + 9;
                n2 = n1;
            }

            for (int i = n1; i > n1 - 100; i--)
                for (int j = n2; j > n2 - 100; j--)
                    if (checkIfPalindrome(i * j))
                    {
                        n1 = i;
                        n2 = j;
                        resultStr += "" + n1 + " x " + n2;
                        return n1 * n2;
                    }

            resultStr += "" + n1 + " x " + n2;

            return n1 * n2;
        }

        private bool checkIfPalindrome(int num)
        {
            if (num == reverse(num))
                return true;
            return false;
        }

        private int reverse(int num)
        {
            int revNum = 0;
            while (num > 0)
            {
                revNum *= 10;
                revNum += num % 10;
                num /= 10;
            }

            return revNum;
        }
    }
}
