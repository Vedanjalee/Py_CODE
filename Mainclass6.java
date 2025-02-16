package jan_20;

class Product 
{
    int pid;
    double price ;
    Product(int arg1,double arg2 )
    {
        pid = arg1;
        price= arg2;
    }
}
public class Mainclass6 {
    public static void main(String[] args) {
        
        Product p1 = new Product(101, 3700.0) ;
        System.out.println(p1.pid);
        System.out.println(p1.price);

        Product p2 = new Product(102, 3400.0) ;
        System.out.println(p2.pid);
        System.out.println(p2.price);

        Product p3=new Product(101, 3700.0) ;
        System.out.println(p3.pid);
        System.out.println(p3.price);

        Product p4 = new Product(101, 3700.0) ;
        System.out.println(p4.pid);
        System.out.println(p4.price);
        
        
        


    }
    
}
