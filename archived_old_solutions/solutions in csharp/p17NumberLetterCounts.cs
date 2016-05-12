using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace p17NumberLetterCounts
{
    class CalcRules
    {
        public string inputStr = "From 1 to ?: ";
        public string resultStr = "Result: ";

        int limit = 1000;

        Dictionary<int, string> unitDigitDic = new Dictionary<int, string> { { 1, "One" }, { 2, "Two" }, { 3, "Three" }, { 4, "Four" }, { 5, "Five" }, { 6, "Six" }, { 7, "Seven" }, { 8, "Eight" }, { 9, "Nine" }, { 0, "" } };
        Dictionary<int, string> tenthDigitDic = new Dictionary<int, string> { { 1, "Ten" }, { 2, "Twenty" }, { 3, "Thirty" }, { 4, "Forty" }, { 5, "Fifty" }, { 60, "Sixty" }, { 6, "Sixty" }, { 7, "Seventy" }, { 8, "Eighty" }, { 9, "Nighty" }, { 0, "" } };
        Dictionary<int, string> hundredDigitDic = new Dictionary<int, string> { { 1, "OneHundred" }, { 2, "TwoHundred" }, { 3, "ThreeHundred" }, { 4, "FourHundred" }, { 5, "FiveHundred" }, { 6, "SixHundred" }, { 7, "SevenHundred" }, { 8, "EightHundred" }, { 9, "NineHundred" }, { 0, "" } };
        Dictionary<int, string> thousandDigitDic = new Dictionary<int, string> { { 1, "OneThousand" }, { 2, "TwoThousand" }, { 3, "ThreeThousand" }, { 4, "FourThousand" }, { 5, "FiveThousand" }, { 6, "SixThousand" }, { 7, "SevenThousand" }, { 8, "EightThousand" }, { 9, "NineThousand" }, { 0, "" } };
        Dictionary<int, string> specialDic = new Dictionary<int, string> { { 11, "Eleven" }, { 12, "Twelve" }, { 13, "Thirteen" }, { 14, "Fourteen" }, { 15, "Fifteen" }, { 16, "Sixteen" }, { 17, "Seventeen" }, { 18, "Eighteen" }, { 19, "Nineteen" } };

        public CalcRules()
        {
            limit = 1000;
        }

        public CalcRules(int _limit)
        {
            limit = _limit;
        }

        public string Calc()
        {
            return SumAllTheLetters().ToString();
        }

        private string ConvertNumberToString(int n)
        {
            string nStr = "";
            int digitPlace = 1;
            while (n > 0)
            {
                switch (digitPlace)
                {
                    case 1:
                        if ((n % 100 > 10) && (n % 100 < 20))
                        {
                            nStr += specialDic[n % 100];
                            n /= 100;
                            digitPlace += 2;
                        }
                        else
                        {
                            nStr += unitDigitDic[n % 10];
                            n /= 10;
                            digitPlace++;
                        }
                        break;
                    case 2:
                        nStr += tenthDigitDic[n % 10];
                        n /= 10;
                        digitPlace++;
                        break;
                    case 3:
                        if (nStr == "")
                        {
                            nStr += hundredDigitDic[n % 10];
                            n /= 10;
                            digitPlace++;
                        }

                        else
                        {
                            nStr += "And";
                            nStr += hundredDigitDic[n % 10];
                            n /= 10;
                            digitPlace++;
                        }
                        break;
                    case 4:
                        nStr += thousandDigitDic[n % 10];
                        n /= 10;
                        digitPlace++;
                        break;
                    default:
                        return "";
                }
            }
            return nStr;
        }

        private int SumAllTheLetters()
        {
            int sum = 0;
            for (int i = 1; i <= limit; i++)
                sum += ConvertNumberToString(i).Length;
            return sum;
        }
    }
}
