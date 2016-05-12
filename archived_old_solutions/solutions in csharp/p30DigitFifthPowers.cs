using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace p30DigitFifthPowers
{
    class CalcRules
    {
        public string inputStr = "Enter the power of 2: ";
        public string resultStr = "Result: ";

        int power;

        public CalcRules()
        {
            power = 5;
        }

        public CalcRules(int _power)
        {
            power = _power;
        }

        public string Calc()
        {
            return CalcTheSumOfList(GenerateArray()).ToString();
        }


        private int CalcTheSumOfList(List<int> arr)
        {
            int sum = 0;
            foreach (int i in arr)
                sum += i;
            return sum;
        }

        private List<int> GenerateArray()
        {
            List<int> arrayList = new List<int>();
            int limit = (int)Math.Pow(9,(double)power+1)*power;
            for (int i = 2; i < limit; i++)
                if (CheckTheNumber(i))
                    arrayList.Add(i);

            return arrayList;
        }

        private bool CheckTheNumber(int n)
        {
            string strN = n.ToString();
            int sumOfStrN = 0;
            foreach (char c in strN)
                sumOfStrN += (int)Math.Pow((double)Char.GetNumericValue(c), (double)power);
            if (n == sumOfStrN)
                return true;
            else
                return false;
        }
    }
}
