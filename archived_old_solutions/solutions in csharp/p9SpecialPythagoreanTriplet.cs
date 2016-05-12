using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p9SpecialPythagoreanTriplet
{
    class rules
    {
        public string inputStr = "a + b + c = ? ";
        public string resultStr = "a*b*c = ";

        struct triplet
        {
            public int a, b, c;
        }

        public int calc(int sum)
        {
            triplet tp = findTheTriplet(sum);
            return (tp.a * tp.b * tp.c);
        }

        private triplet findTheTriplet(int sum)
        {
            //a^2 + b^2 = c^2
            //a + b +c = sum
            var tri = new triplet();

            for (tri.c = (sum / 2); tri.c > (sum / 3); tri.c--)
            {
                for (tri.a = 1; tri.a <= ((sum - tri.c) / 2); tri.a++)
                {
                    tri.b = sum - tri.a - tri.c;
                    if (isValidTriplet(tri))
                        return tri;
                }
            }

            tri.a = 0;
            tri.b = 0;
            tri.c = 0;

            return tri;
        }

        private bool isValidTriplet(triplet tri)
        {
            if ((tri.a * tri.a) + (tri.b * tri.b) == (tri.c * tri.c))
                return true;
            return false;
        }
    }
}

