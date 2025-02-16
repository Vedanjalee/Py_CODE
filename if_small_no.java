public class if_small_no {
    public static void main(String[] args) {
        int a =100, b=4, c=30,d=200;
        int small = a;

        if (b<small)
           small = b ;
        
        if (c<small)
           small = c;
           
        if (d<small)
           small = d;   
        
           System.out.println(small);
    }
    
    
}
