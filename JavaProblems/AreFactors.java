import java.util.Scanner;
import java.util.LinkedList;
 
public class AreFactors {
 
    public areFactors() {
        System.out.println("What is your number? ");
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println("Ok, your number is " + n + ".");
        LinkedList<Integer> a = new LinkedList();
        System.out.println("What are the factors you want to test for?");
        System.out.println("Input the first factor.");
        int factor1 = in.nextInt();
        a.add(factor1);
        System.out.println("Input the next one.");
        int factor2 = in.nextInt();
        a.add(factor2);
        System.out.println("Input the next one.");
        int factor3 = in.nextInt();
        a.add(factor3);
        System.out.println("Input the next one.");
        int factor4 = in.nextInt();
        a.add(factor4);
        System.out.println("Input the next one.");
        int factor5 = in.nextInt();
        a.add(factor5);
        areFactors(n, a);
    }
 
    public static void areFactors(int n, LinkedList<Integer> a) {
        for (int i = 0; i < a.size(); i++) {
            if (a.get(i) == 0) {
                System.out.println("Do not divide by zero.");
                continue;
            }
            else if (isPrime(n)) {
                System.out.println(n + " is a prime number, so it won't be divisible by anything.");
                break;
            }
            else if (i < a.size() && n % a.get(i) == 0) {
                if (!isPrime(a.get(i))) {
                    System.out.println("The number is divisible by " + a.get(i) + ".");
                }
                else if (a.get(i) == 1) {
                    System.out.println("1 is a factor of any integer.");
                }
                else {
                    System.out.println("The number is divisible by the prime number " + a.get(i) + ".");
                }
            }
            else if (n % a.get(i) == 0) {
                continue;
            }
            else {
                if (!isPrime(a.get(i))) {
                    System.out.println("The number is not divisible by " + a.get(i) + ".");
                } else {
                    System.out.println("The number is not divisible by the prime number " + a.get(i) + ".");
                }
            }
        }
    }
 
    public static boolean isPrime(int p) {
        int sqrtp = ((int)Math.floor(Math.sqrt(p)));
        for (int i = 2; i <= sqrtp; i++) {
            if (p % i != 0) continue;
            else return false;
        }
        return true;
    }
}
 
