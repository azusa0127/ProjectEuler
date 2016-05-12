using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMod
{
    class CalcRules
    {
        public string inputStr = "Board Size ? x ?: ";
        public string resultStr = "Result: ";

        int boardSize = 2;

        Dictionary<long, Tuple<int, int>> pathBoard;

        public CalcRules()
        {
            boardSize = 20;
            pathBoard = new Dictionary<long, Tuple<int, int>>();
        }

        public CalcRules(int _boardSize)
        {
            boardSize = _boardSize;
            pathBoard = new Dictionary<long, Tuple<int, int>>();
        }

        public long Calc()
        {
            GenerateTheBoard();
            return countEndLevelNodes();
        }

        private bool ValidateCood(Tuple<int, int> c)
        {
            if ((Math.Min(c.Item1, c.Item2) < 0) || (Math.Max(c.Item1, c.Item2) > boardSize))
                return false;
            else
                return true;
        }

        private Tuple<int, int> GetLeftLeafCood(Tuple<int, int> parentCood)
        {
            var leafCood = Tuple.Create(parentCood.Item1, (parentCood.Item2 + 1));
            return leafCood;
        }

        private Tuple<int, int> GetRightLeafCood(Tuple<int, int> parentCood)
        {
            var leafCood = Tuple.Create((parentCood.Item1 + 1), parentCood.Item2);
            return leafCood;
        }

        private long GetLeftLeafIndex(long parentIndex)
        {
            return parentIndex * 2;
        }

        private long GetRightLeafIndex(long parentIndex)
        {
            return (parentIndex * 2 + 1);
        }

        private bool CheckIndexExistance(long index)
        {
            try
            {
                if (pathBoard.ContainsKey(index))
                    return true;
                else
                    return false;
            }
            catch
            {
                return false;
            }
        }

        private bool CheckLeftLeafPossibility(Tuple<int, int> parentCood)
        {
            if (ValidateCood(GetLeftLeafCood(parentCood)))
                return true;
            else
                return false;
        }

        private bool CheckRightLeafPossibility(Tuple<int, int> parentCood)
        {
            if (ValidateCood(GetRightLeafCood(parentCood)))
                return true;
            else
                return false;
        }

        private bool AddLeftLeaf(long parentIndex)
        {
            try
            {
                pathBoard.Add(GetLeftLeafIndex(parentIndex), GetLeftLeafCood(pathBoard[parentIndex]));
                return true;
            }
            catch
            {
                return false;
            }
        }

        private bool AddRightLeaf(long parentIndex)
        {
            try
            {
                pathBoard.Add(GetRightLeafIndex(parentIndex), GetRightLeafCood(pathBoard[parentIndex]));
                return true;
            }
            catch
            {
                return false;
            }
        }

        private void GenerateTheBoard()
        {
            pathBoard.Add(1, Tuple.Create(0, 0));
            Iterate(1);
        }

        private void Iterate(long parentIndex)
        {
            if (!CheckIndexExistance(parentIndex))
                return;
            else
            {
                if (CheckLeftLeafPossibility(pathBoard[parentIndex]))
                {
                    AddLeftLeaf(parentIndex);
                    Iterate(GetLeftLeafIndex(parentIndex));
                }
                if (CheckRightLeafPossibility(pathBoard[parentIndex]))
                {
                    AddRightLeaf(parentIndex);
                    Iterate(GetRightLeafIndex(parentIndex));
                }
                return;
            }
        }

        private long countEndLevelNodes()
        {
            long endLevelStarting = (long)Math.Pow(2.0, boardSize * 2.0);
            long count = 0;
            foreach (var kv in pathBoard)
                if (kv.Key >= endLevelStarting)
                    count++;
            return count;
        }
    }
}
