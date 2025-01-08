//  https://leetcode.com/problems/concatenation-of-array/

import java.util.Scanner;
public class Final_valueOfVariableAfterPerformingOperation {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        sc.nextLine();
        int X=0;
        String str[]=new String[n];
        for(int i=0;i<n;i++){
            str[i]=sc.nextLine();
        }
        for (int i=0;i<n;i++){
            if (str[i].equals("++X") || str[i].equals("X++")){
                   X++;
            }
            else if (str[i].equals("X--") || str[i].equals("--X")){
                X--;
            }
        }
        System.out.println(X);
    }
}
