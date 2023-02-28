package CodingProblems.JavaProblems;
 
import java.util.Scanner;
import java.util.Random;
 
 
public class Clock {
    private int hour;
    private int minute;
    private double second;
    Scanner in = new Scanner(System.in);
    Timer timer = new Timer();
    Timer wait = new Timer();
    Random random = new Random();
 
    public Clock() {
        System.out.println("Enter what hour it is.");
        hour = in.nextInt();
        System.out.println("Ok, it is " + hour + ".");
        System.out.println("Enter what minute it is.");
        minute = in.nextInt();
        if (minute < 10) {
            System.out.println("Ok, it is " + hour + ":0" + minute + ".");
        }
        if (minute >= 10) {
            System.out.println("Ok, it is " + hour + ":" + minute + ".");
        }
        System.out.println("Enter what second it is.");
        second = in.nextDouble();
        if (minute < 10) {
            if (second < 10) {
                System.out.println("Ok, it is " + hour + ":0" + minute + ":0" + second + ".");
            }
            if (second >= 10) {
                System.out.println("Ok, it is " + hour + ":0" + minute + ":" + second + ".");
            }
        }
        if (minute >= 10) {
            if (second < 10) {
                System.out.println("Ok, it is " + hour + ":" + minute + ":0" + second + ".");
            }
            if (second >= 10) {
                System.out.println("Ok, it is " + hour + ":" + minute + ":" + second + ".");
            }
        }
        int waitTime = random.nextInt(50) + 30;
        while (true) {
            if (advanceTime()) {
                prntTime();
            }
        }
    }
 
    public boolean advanceTime() {
        boolean result = false;
        if(timer.passed(1000)) {
            second = second + 1;
            result = true;
            timer.reset();
        }
        if (second >= 60) {
            second = second - 60;
            minute = minute + 1;
        }
        if (minute >= 60) {
            minute = minute - 60;
            hour = hour + 1;
        }
        if (hour >= 24) {
            hour = hour % 24;
        }
        return result;
    }
 
    public void prntTime() {
        if (minute < 10) {
            if (second < 10) {
                System.out.println("It is currently " + hour + ":0" + minute + ":0" + second + ".");
            }
            if (second >= 10) {
                System.out.println("It is currently " + hour + ":0" + minute + ":" + second + ".");
            }
        }
        if (minute >= 10) {
            if (second < 10) {
                System.out.println("It is currently " + hour + ":" + minute + ":0" + second + ".");
            }
            if (second >= 10) {
                System.out.println("It is currently " + hour + ":" + minute + ":" + second + ".");
            }
        }
    }
 
}
