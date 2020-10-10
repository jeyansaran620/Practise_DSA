import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner sc = new Scanner(System.in);
		int t = Integer.valueOf(sc.nextLine());
		while(t-- > 0)
		{
		    int n = Integer.valueOf(sc.nextLine());
		    
		    String[] arr = sc.nextLine().split(" ");
		    
		    char[] st = sc.nextLine().toCharArray();
		    
		    Arrays.sort(arr);
		    
		    int i = 0;
		    int j = n-1;
		    
		    while (i < st.length)
		    {
		        while(j >= 0 && arr[j].toCharArray()[0] != st[i])
		        {
		            j--;
		        }
		        if(j>=0)
		        {
		            int k = 1;
		            int z = i+1;
		            while(k < arr[j].length() && z < st.length && arr[j].toCharArray()[k] == st[z])
		            {
		                z++;
		                k++;
		            }
		            if(k == arr[j].length())
		            {
		                i = z;
		                j = n-1;
		            }
		            else
		            {
		                j--;
		            }
		        }
		        else
		        {
		            System.out.println("0");
		            break;
		        }
		    }
		    if(i==st.length)
		    {
		      System.out.println("1");
		    }
		}
	}
}
