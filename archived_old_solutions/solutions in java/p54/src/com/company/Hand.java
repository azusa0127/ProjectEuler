package com.company;

public class Hand {
    Card[] cards;
    int rank;
    int refWeight;

    Hand(String cardStr){
        rank = 0;
        refWeight = 0;
        cards = cvtToCards(cardStr);
        sort();
        calcRank();
    }

    private Card[] cvtToCards(String str){
        Card[] c = new Card[5];
        int count = 0;
        for (String s : str.split(" ")) {
            c[count] = new Card(s);
            count++;
        }
        return c;
    }

    private void sort(){
        for (int i = 0; i < 4; i++) {
            for (int j = i+1; j < 5; j++) {
                if (cards[j].cardValue > cards[i].cardValue){
                    Card tmp = cards[j];
                    cards[j] = cards[i];
                    cards[i] = tmp;
                }
            }
        }
    }

    private boolean isFlush(){
        for (int i = 1; i < 5; i++) {
            if (cards[i].suit != cards[0].suit)
                return false;}
        return true;
    }

    private boolean isStraight(){
        for (int i = 0; i < 4; i++) {
            if (cards[i].cardValue != cards[i+1].cardValue+1)
                return false;}
        return true;
    }

    private void lowerRankDetermine(){
        int cscCount = 0;
        for (int i = 0; i < 4; i++) {
            if (cards[i].num == cards[i+1].num){
                cscCount++;
            } else {
                if (cscCount == 1){
                    if (rank == 0){
                        rank = 1;
                        refWeight = cards[i].cardValue;
                    } else if (rank == 1){
                        rank = 2;
                        refWeight = refWeight*100 + cards[i].cardValue;
                    } else if (rank == 3){
                        rank = 6;
                        refWeight = refWeight*100 + cards[i].cardValue;
                    }
                } else if (cscCount == 2){
                    if (rank == 1) {
                        rank = 6;
                        refWeight = refWeight + cards[i].cardValue*100;
                    }else{
                        rank = 3;
                        refWeight = cards[i].cardValue;
                    }
                } else if (cscCount == 3){
                    rank = 7;
                    refWeight = cards[i].cardValue;
                }
                cscCount = 0;
            }
        }

        if (cscCount != 0){
            if (cscCount == 1){
                if (rank == 0){
                    rank = 1;
                    refWeight = cards[4].cardValue;
                } else if (rank == 1){
                    rank = 2;
                    refWeight = refWeight*100 + cards[4].cardValue;
                } else if (rank == 3){
                    rank = 6;
                    refWeight = refWeight*100 + cards[4].cardValue;
                }
            } else if (cscCount == 2){
                if (rank == 1) {
                    rank = 6;
                    refWeight = refWeight + cards[4].cardValue*100;
                }else{
                    rank = 3;
                    refWeight = cards[4].cardValue;
                }
            } else if (cscCount == 3){
                rank = 7;
                refWeight = cards[4].cardValue;
            }
        }
    }

    private void calcRank(){
        if (isFlush()){
            if (isStraight()){
                if (cards[0].cardValue == 14)
                    rank = 9;
                else
                    rank = 8;
            } else {
                rank = 5;
            }
        } else {
            if (isStraight()){
                rank = 4;
            } else {
                lowerRankDetermine();
            }
        }
    }

    boolean compareTo(Hand hand2){
        if (rank != hand2.rank){
            return (rank > hand2.rank);
        } else {
            if (refWeight != hand2.refWeight)
                return refWeight > hand2.refWeight;
            for (int i = 0; i < 5; i++) {
                if (cards[i].cardValue != hand2.cards[i].cardValue){
                    return (cards[i].cardValue > hand2.cards[i].cardValue);}}
            return false;
        }
    }
}
