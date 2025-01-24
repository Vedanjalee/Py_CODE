public class Increment5 {
    public static void main(String[] args) {
            
        
        int x = 0, 
        y = 0;
    
        y = ++x  + x++ + x  + x++;
    
        System.out.println(x);
        System.out.println(y);
}
}