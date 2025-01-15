//https://leetcode.com/problems/left-and-right-sum-differences/

import java.util.Scanner;

public class LeftAndRight_SumDifference {
    public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int arr[]=new int [n];
    for (int i=0;i<n;i++){
        arr[i]=sc.nextInt();
    }
  int leftsum[]=new int[n];
  int rightsum[]=new int[n];
leftsum[0]=0;
rightsum[n-1]=0;
  for(int i=1;i<n;i++){
    leftsum[i]=leftsum[i-1]+arr[i-1];

  }
  for (int i = n - 2;i>=0;i--){
   
    rightsum[i]=rightsum[i+1]+arr[i+1];



    }
    int ans[]=new int[n];

    for(int i=0;i<n;i++){
        ans[i]=Math.abs(leftsum[i]-rightsum[i]);
    }

    for(int i=0;i<n;i++){
        System.out.print(ans[i]+ " ");
    }
}
}


