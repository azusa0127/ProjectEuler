package com.company;
/**
 Poker hands
 Problem 54
 In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

 0 High Card: Highest value card.
 1 One Pair: Two cards of the same value.
 2 Two Pairs: Two different pairs.
 3 Three of a Kind: Three cards of the same value.
 4 Straight: All cards are consecutive values.
 5 Flush: All cards of the same suit.
 6 Full House: Three of a kind and a pair.
 7 Four of a Kind: Four cards of the same value.
 8 Straight Flush: All cards are consecutive values of same suit.
 9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
 The cards are valued in the order:
 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

 If two players have the same ranked hands then the rank made up of the highest value wins;
 for example, a pair of eights beats a pair of fives (see example 1 below).
 But if two ranks tie, for example, both players have a pair of queens,
 then highest cards in each hand are compared (see example 4 below);
 if the highest cards tie then the next highest cards are compared, and so on.
 *
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
 static ArrayList<Hand> p1 = new ArrayList<Hand>();
 static ArrayList<Hand> p2 = new ArrayList<Hand>();

    public static void main(String[] args) throws FileNotFoundException {
     loadData();

     int p1Wins = 0;
     for (int i = 0; i < p1.size(); i++) {
      if (p1.get(i).compareTo(p2.get(i))){
       p1Wins++;}}

     System.out.println("P1 has won " + p1Wins + " times.");

    }

 static void loadData() throws FileNotFoundException {
   Scanner inputFile = new Scanner(new File("p054_poker.txt"));
   String currentLine;
   while (inputFile.hasNextLine()){
    currentLine = inputFile.nextLine();
    p1.add(new Hand(currentLine.substring(0,15)));
    p2.add(new Hand(currentLine.substring(15)));
   }
   inputFile.close();
 }
}
