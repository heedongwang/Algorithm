 import java.util.*;
public class Main{
    public static void main(String arg[]){
        Scanner sc= new Scanner(System.in);
        
		int h=sc.nextInt();
        int m=sc.nextInt();
        int cook=sc.nextInt();
        
        h+=cook/60;
        m+=cook%60;
        
        if(m>=60){
            h+=1;
            m-=60;
        }
        if(h>=24){
            h-=24;
        }
        System.out.println(h+" "+m);

    }
}
