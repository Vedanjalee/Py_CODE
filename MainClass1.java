import java.util.Scanner;

class Biryani {
    String type ;
    double price ;
    
    Biryani(String type, double price){
        this.type = type;
        this.price = price ;
    }
}

class BiryaniHelper {
    static void displayBiryani(Biryani b)
    {
        System.out.println("price : ");
    }
    static Biryani createBiryani() 
{
    Scanner scn = new Scanner(System.in);
    System.out.println("enter Price");
    double price = scn.nextDouble();
    System.out.println("enter type");

    String type = scn.next();
    Biryani b = new Biryani(type, price);
    return b ;

}
}    




    public class MainClass1 {
        public static void main(String[] args) {
            Biryani b1 = BiryaniHelper.createBiryani();
            BiryaniHelper.displayBiryani(b1);
            

            Biryani b2 = BiryaniHelper.createBiryani();
            BiryaniHelper.displayBiryani(b2);

            Biryani b3 = BiryaniHelper.createBiryani();
            BiryaniHelper.displayBiryani(b3);

}}
