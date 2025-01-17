// Deep copy code

package Jan_16;

class Score 
    {
        int x  = 30 ;
    }


    public class MainClass2  {
        public static void main(String[] args) {
            
            Score s1 = new Score();
            Score s2 =new Score();
    
            s2.x = 6 ;
    
            System.out.println("The value of x is: " + s1.x);  
    
        }
    }
