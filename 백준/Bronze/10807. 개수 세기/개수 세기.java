import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		 Scanner sc= new Scanner(System.in);
		 
		 int len=sc.nextInt();
		 int[] listnum= new int[len];
		 
		 for(int i=0;i<listnum.length;i++) {
			 listnum[i]=sc.nextInt();
			 
		 }
		 
		 int check= sc.nextInt();
		 int count=0;
		 
		 for(int i=0;i<len;i++) {
			 if(check==listnum[i])
				 count++;
		 }
		 
		 System.out.println(count);
		

	}

}