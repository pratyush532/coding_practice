/*
  You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

*/
public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int largest = 0;
        int sum;
        for (int i = 0; i<accounts.Length; i++){
            sum = 0;
            for (int j=0; j<accounts[i].Length; j++){
                sum =  sum + accounts[i][j];
            }
            if (sum > largest){
                largest = sum;
            }
        }
        return largest;
        
    }
}
