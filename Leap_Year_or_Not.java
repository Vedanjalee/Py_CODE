public class Leap_Year_or_Not { 
    public static void main(String[] args) {
        int y = 2025;

        if(y%4 == 0  && y%100 != 0 ) 
            System.out.println("leap year");
        else if (y%400== 0) 
            System.out.println("leap year");
        else
            System.out.println("not leap year");    


    }
}
