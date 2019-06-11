//Narcisstic Numbers

import java.util.LinkedList;
public class Example23  {

    public static void main(String args[])
    {
        for (int i = 1; i < 1000; i++) {
            int n = i;
            LinkedList<Integer> data = new LinkedList<>();
            while (n > 0) {
                data.push( n % 10 );
                n = n / 10;
            }
            int n1 = 0;
            for(Integer num : data) {
                n1 += Math.pow(num, data.size());
            }
            if(i == n1) {
                System.out.println(i);
            }
        }
    }
}

//Factorial Sum

import java.util.Scanner;
public class SumOfFactorial
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number : ");
        int n = sc.nextInt();
 
        int total=0;
 
        int i=1;
        
        while(i <= n) 
        {
            int factorial=1;
            int j=1;
            
            while(j <= i) 
            {
                factorial=factorial*j;
                j = j+1;
            }
            total = total + factorial;
            i=i+1;
        }

        System.out.println("Sum : " + total);
    }
}