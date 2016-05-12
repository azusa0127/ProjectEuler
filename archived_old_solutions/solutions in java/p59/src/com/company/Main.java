package com.company;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();

        int[] encodedContext = ReadTheFileIntoIntArray("p059_cipher.txt");
        String decodedString = decodedMsg(encodedContext);
        System.out.println("Decoded msg:");
        System.out.println(decodedString);
        System.out.println();
        System.out.println("Sum of ASCII codes: " + SumASCIINumbers(decodedString));

        long endTime = System.currentTimeMillis();
        System.out.println("Took "+(endTime - startTime) + " ms");
    }

    public static long SumASCIINumbers(String str){
        long sum = 0;
        for (int i = 0; i < str.length(); i++)
            sum += (int)str.charAt(i);
        return sum;
    }

    public static String decodedMsg(int[] codedMsg){
        char[] ASCIILowerAlphabets = new char[26];
        for (int i = 0; i < 26; i++)
            ASCIILowerAlphabets[i] = (char)(i+97);

        String currentDecodedContext = "";

        char[] key = new char[3];
        for (int i = 0; i < 26; i++) {
            key[0] = ASCIILowerAlphabets[i];
            for (int j = 0; j < 26; j++) {
                key[1] = ASCIILowerAlphabets[j];
                for (int k = 0; k < 26; k++) {
                    key[2] = ASCIILowerAlphabets[k];
                    currentDecodedContext = encrypt(codedMsg,key);
                    if (CheckIfTermInString("the ", currentDecodedContext)){
                        System.out.println("Found the key: "+ new String(key));
                        return currentDecodedContext;}
                }
            }
        }

        return currentDecodedContext;
    }

    public static String encrypt(int[] msg,char[] key){
        char[] encryptedArray = new char[msg.length];

        for (int i = 0; i < msg.length; i++)
            encryptedArray[i] = (char)(msg[i] ^ key[i % key.length]);

        return new String(encryptedArray);
    }

    public static boolean CheckIfTermInString(String term, String context){
        if (!CheckIfInASCIIRange(context))
                return false;
        int checkRange = context.length()-term.length();
        for (int i = 0; i < checkRange; i++)
            if (context.charAt(i) == term.charAt(0))
                if (context.substring(i, i + term.length()).equals(term))
                    return true;
        return false;
    }

    public static boolean CheckIfInASCIIRange(String context){
        if ((context.charAt(2) >= ' ') && (context.charAt(2) <= '~'))
            return true;
        return false;
    }

    public static int[] ReadTheFileIntoIntArray(String fileName) throws IOException{
        String[] test = ReadTextFile(fileName).split(",");
        int[] contentInt = new int[test.length];
        for (int i = 0; i < contentInt.length-1; i++)
            contentInt[i] = Integer.parseInt(test[i]);
        contentInt[contentInt.length-1]=73;
        return contentInt;
    }

    public static String ReadTextFile(String fileName) throws IOException{
        String content = "";
        Scanner inputFile = new Scanner(new File(fileName));
        while (inputFile.hasNextLine())
            content += inputFile.nextLine() + "\n";
        inputFile.close();
        return content;
    }
}
