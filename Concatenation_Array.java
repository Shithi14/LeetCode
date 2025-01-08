//  https://leetcode.com/problems/concatenation-of-array/

import java.util.Scanner;
public class Concatenation_Array{

    public static void main (String args[]){

        Scanner sc=new Scanner (System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for (int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }

        int arr2[]=new int[2*n];
        for (int i=0;i<n;i++){
            arr2[i]=arr[i];
            arr2[i+n]=arr[i];
        }
        for (int i=0;i<2*n;i++){
            System.out.print(arr2[i] + " ");
        }
    }
}




/*arr=list(map(int,input().split()))

print(arr+arr)*/