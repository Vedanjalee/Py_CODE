// SHALLOW COPY CODE 
package Jan_16;
class Score 
{
    int x  = 30 ;
}
public class MainClass1 {
    public static void main(String[] args) {
        
        Score s1 = new Score();
        Score s2 = s1;

        s2.x = 6 ;

        System.out.println("The value of x is: " + s1.x);  

    }
}
