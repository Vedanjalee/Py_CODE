
public class factors {
    public static void main(String[] args) {
        int n= 100;
        for (int i = 1 ; i<= n/2 ; i++)
        {
            if (n%i == 0){
                System.out.println(i);
            }
        }
        System.out.println(n);
       
    }
}
