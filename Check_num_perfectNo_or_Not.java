public class Check_num_perfectNo_or_Not {
    public static void main(String[] args) {
        int n = 6;
        int sum = 0 ;
        for (int i = 1; i<=n/2; i ++)
        {
            if (n%i == 0){
               sum += i;
            }
            
        }
        if( sum == n ){
            System.out.println("perfect number");
            }
            else{
                System.out.println("not perfect");
            }
       }
        
    }


