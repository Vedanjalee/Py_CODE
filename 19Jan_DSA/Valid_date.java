
class valid_date{
    public static void main(String[] args) {
    int y = 2025;
    int d = 25;
    int m= 50;

    if (d<1 || d>31 ||  m<1 || m>12 || y< 1)
    {
        System.out.println("invalid date");
    }

    else if ((m==4 || m==6 || m==9 || m==1 ) && d>30)
    {
        System.out.println("invalid date");
    }

    else if (!(y%4 == 0 && y % 100 !=0 || y % 400 ==0) && m==2 && d>28 )
    {
        System.err.println("Invalid date ");
    }

    else if ((y%4 == 0 && y%100 != 0 || y%400 == 0 ) && m==2 && d>20){
        System.out.println("invalid date");
    }
    else{
        System.out.println("valid date");
    }
}}