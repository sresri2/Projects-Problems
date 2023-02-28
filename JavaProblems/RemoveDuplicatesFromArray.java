import java.util.ArrayList;

public class RemoveDuplicatesFromArray {
    public int removeDuplicates(int[] nums) {
        int check = nums[0];
        int pos = 0;

        int finalReturn = 1;
        for (int num : nums) {
            if (pos != 0) {
                if (num != check) {
                    finalReturn += 1;
                    check = num;
        
                }
            }
            pos+=1;
        }
        return finalReturn;

    }
    public static void main(String[] args){
        RemoveDuplicatesFromArray num = new RemoveDuplicatesFromArray();
        System.out.println(num);
    }
}

