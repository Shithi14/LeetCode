//https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
import java.util.Scanner;

public class Find_minimumOperation {
    public static void main(String args[])
    {

        Scanner sc=new Scanner (System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        int count=0;
        for (int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            int rem=arr[i]%3;
            if (rem==1){
                count++;
            }
            else if (rem==2){
                count++;
            }
        }

        System.out.println(count);
    }
}
