    class CalcRules
    {
        public string inputStr = "Enter the total sum of the coin: ";
        public string resultStr = "Numbers of combinitions: ";

        int arrg;

        public CalcRules()
        {
        }

        public CalcRules(string _arrg)
        {
            if (!int.TryParse(_arrg,out arrg))
                arrg = 0;
        }

        public string Calc()
        {
            return IterateCoins();
        }
        
        private int IterateCoins()
        {
            const int total = arrg;
            int count = 0;
            
            for (int s200 = 0;s200<=total;s200 += 200)
                for (int s100 = s200;s100 <= total; s100 += 100)
                    for (int s50 = s100; s50 <= total; s50 += 50)
                        for (int s20 = s50; s20 <= total; s20 += 20)
                            for (int s10 = s20; s10 <= total; s10 += 10)
                                for (int s5 = s10; s5 <= total; s5 += 5)
                                    for (int s2 = s5; s2 <= total; s2 += 2)
                                        for (int s1 = s2; s1 <= total; s1++)
                                        {
                                            if (s1 == total)
                                                count++;
                                            else
                                                continue;
                                        }
            return count;
        }
    }
