//https://leetcode.com/problems/shuffle-the-array/

import java.util.Scanner;
public class Shuffle{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int arr[]=new int[2*n];
        for(int i=0;i<2*n;i++){
            arr[i]=sc.nextInt();

        }
        int ans[]=new int [2*n];
        for(int i=0;i<n;i++){

            ans[2*i]=arr[i];
            ans[2*i+1]=arr[i+n];
        }
        for(int i=0;i<2*n;i++){
            System.out.print(ans[i]+ " ");
        }


    }


}