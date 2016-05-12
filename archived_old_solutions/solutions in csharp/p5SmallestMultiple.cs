using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p5SmallestMultiple
{
    class rules
    {
        public string inputStr = "From 1 to ? ";
        public string resultStr = "Result: ";

        public int calc(int num)
        {
            int multi = num;
            for (int i = 2; i < num; i++)
                multi = getSmallestMultiple(multi, i);

            return multi;
        }

        private int getSmallestMultiple(int numL, int numS)
        {
            int multip = numL;
            for (int i = 1; i <= numS; i++)
            {
                multip = numL * i;
                if (multip % numS != 0)
                    continue;
                return multip;
            }
            return multip;
        }
    }
}