package com.company;

/**
 * Created by Phoenix on 2014-10-28.
 */
public class XOREncryption {
    public String encrypt(String msg,String key){
        char[] encryptedArray = new char[msg.length()];

        for (int i = 0; i < msg.length(); i++)
            encryptedArray[i] = (char)(msg.charAt(i) ^ key.charAt(i % key.length()));

        return new String(encryptedArray);
    }

    public String decrypt(String msg, String key){
        return encrypt(msg,key);
    }
}
