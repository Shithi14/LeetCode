//https://leetcode.com/problems/richest-customer-wealth/

import java.util.Scanner;
public class Richest_CustomerWealth {
    public static void main(String args[])
    {

        Scanner sc=new Scanner(System.in);
        int m=sc.nextInt();
        int n=sc.nextInt();
        int mat[][]=new int [m][n];
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++){
                mat[i][j]=sc.nextInt();
            }
        }
        int maxsum=0;
        for(int i=0;i<m;i++){
            int sum=0;
            for(int j=0;j<n;j++){
                sum+=mat[i][j];
                
            }
            maxsum=Math.max(maxsum,sum);
        }
        System.err.println(maxsum);


    }
}
