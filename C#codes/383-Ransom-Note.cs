public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        int[] checker = new int[26];

        for (int i=0; i<ransomNote.Length; i++){
            checker[(int)ransomNote[i] - 97] -= 1;
        }

        for (int i=0; i < magazine.Length; i++){
            checker[(int)magazine[i] - 97] += 1;
        }

        for (int i=0; i<checker.Length; i++){
            if (checker[i] < 0) return false;
        }

        return true;
    }
}
