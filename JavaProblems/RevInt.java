public class RevInt {
    public int reverse (int x) {
        long reversed = 0;
        while (x != 0) {
            int digit = x % 10;
            reversed *= 10;
            reversed += digit;
            x /= 10;

        }
        if (reversed>Integer.MAX_VALUE || reversed <Integer.MIN_VALUE)
            return 0;
        return (int)reversed;                      
    }
    public static void main(String []args) {
        RevInt t = new RevInt();

    }
}