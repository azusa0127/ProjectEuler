package p42;

import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        String context = mylib.FileOperation.ReadTextFile("p042_words.txt");
        String[] words = context.split(",");

        words[0] = "A";
        for (int i = 0; i < words.length; i++) {
            words[i] = words[i].replace("\"", "");
        }

        int count = 0;
        ArrayList tnSet = triangleNumberSet(255);

        for (int j = 0; j < words.length; j++)
            if (isTriangleNum(words[j],tnSet))
                count++;

        System.out.println(count);
    }

    private static ArrayList triangleNumberSet(int limit){
        ArrayList tnSet = new ArrayList();
        for (int i = 0; i < limit; i++)
            tnSet.add(i * (i + 1) / 2);
        return tnSet;
    }

    private static int getWordValue(String word){
        final String alphabetChars = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int value = 0;
        for (int i = 0; i < word.length(); i++)
            value += alphabetChars.indexOf(word.charAt(i));
        return value;
    }

    private static boolean isTriangleNum(String word, ArrayList tnSet){
        return tnSet.contains(getWordValue(word));
    }
}

