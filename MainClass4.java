package Jan_16;


class Laptop 
{
    String wallpaper = "Alia.jpg";
}

public class MainClass4 {
    public static void main(String[] args) {
        Laptop l1 = new Laptop() ;
        Laptop l2 = l1;

        System.out.println(l1.wallpaper);
        System.out.println(l2.wallpaper);

       l1.wallpaper = "kajal.jpg";

       System.out.println(l1.wallpaper);

       System.out.println(l2.wallpaper);

  }
}


    

