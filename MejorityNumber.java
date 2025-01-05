//https://leetcode.com/problems/majority-element/
import java.util.Scanner;


public class MejorityNumber {
    
    public static void main(String args[]){
       
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        

        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int count=0;
        int box=0;
        for (int i=0;i<n;i++){
            if (count==0){
                box=arr[i];
            }
             if(arr[i]==box){
                count++;
            }
            else{
                count--;
            }
        }
       System.out.println(box);



    }
}
