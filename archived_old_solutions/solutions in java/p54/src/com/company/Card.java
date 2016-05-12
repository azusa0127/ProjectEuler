package com.company;

public class Card {
    char num;
    char suit;
    int cardValue;

    Card(String cd){
        num = cd.charAt(0);
        suit = cd.charAt(1);
        cardValue = getCardValue();
    }

    private int getCardValue(){
        int value;
        switch (num) {
            case 'A':
                value = 14;
                break;
            case 'K':
                value = 13;
                break;
            case 'Q':
                value = 12;
                break;
            case 'J':
                value = 11;
                break;
            case 'T':
                value = 10;
                break;
            default:
                value = Character.getNumericValue(num);
                break;
        }
        return value;
    }
}
