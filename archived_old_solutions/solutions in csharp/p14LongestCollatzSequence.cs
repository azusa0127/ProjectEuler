using System;
using System.Collections.Generic;
using System.Linq;

namespace p14LongestCollatzSequence
{
    class rules
    {
        public string inputStr = "Limit: ";
        public string resultStr = "Result: ";

        Dictionary<int, int> nextColSeqs = new Dictionary<int, int>();
        Dictionary<int, int> colSeqsCounts = new Dictionary<int, int>();

        public int calc(int limit)
        {
            buildSequence(limit);
            int maxStarting = getMaxCountKey(limit);
            return maxStarting;
        }

        private void addSeqsCount(int n)
        {
            int tmp = n;
            int count = 1;
            while (n > 1)
            {
                if (colSeqsCounts.ContainsKey(nextNum(n)))
                {
                    count = (count + colSeqsCounts[nextNum(n)]);
                    break;
                }
                else
                {
                    tmp = nextNum(tmp);
                    count++;
                    addSeqsCount(tmp);
                }
            }
            colSeqsCounts.Add(n, count);
        }

        private int nextNum(int n)
        {
            if (nextColSeqs.ContainsKey(n))
                return nextColSeqs[n];
            else
            {
                int nNum = n;
                if (nNum % 2 == 0)
                    nNum = nNum / 2;
                else
                    nNum = 3 * nNum + 1;
                nextColSeqs.Add(n, nNum);
                return nNum;
            }
        }

        private void buildSequence(int limit)
        {
            colSeqsCounts.Add(1, 1);
            nextColSeqs.Add(1, 0);

            for (int i = 2; i <= limit; i++)
                addSeqsCount(i);
        }

        private int getMaxCountKey(int limit)
        {
            int maxValue = 1;
            int maxKey = 0;
            for (int i = 1; i <= limit; i++)
                if (colSeqsCounts[i] > maxValue)
                {
                    maxValue = colSeqsCounts[i];
                    maxKey = i;
                }
            return maxKey;
        }
    }
}