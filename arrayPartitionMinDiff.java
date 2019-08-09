/*
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.



Write a function that, given an array A of N integers, of which represents loads caused by successive processes, the function should return the minimum absolute difference of server loads.



For example, given array A such that:

  A[0] = 1

  A[1] = 2

  A[2] = 3

  A[3] = 4

  A[4] = 5



your function should return 1. We can distribute the processes with loads 1, 2, 4 to the first server and 3, 5 to the second one, so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.



Assume that:

N is an integer within the range [1..1,000]

the sum of the elements of array A does not exceed 100,000


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


*/


import java.util.Scanner;
import java.util.stream.Stream;
 
class Solution {
 
  static int solution(Integer[] loads) {
    // put your solution here
    int ans=minPartition(loads, loads.length - 1, 0, 0);
    
    return ans;
  }
  public static int minPartition(Integer[] S, int n, int S1, int S2)
	{
		// base case: if list becomes empty, return the absolute
		// difference between two sets
		if (n < 0) {
			return Math.abs(S1 - S2);
		}

		// Case 1. include current item in the subset S1 and recur
		// for remaining items (n - 1)
		int inc = minPartition(S, n - 1, S1 + S[n], S2);

		// Case 2. exclude current item from subset S1 and recur for
		// remaining items (n - 1)
		int exc = minPartition(S, n - 1, S1, S2 + S[n]);

		return Integer.min(inc, exc);
	}


 
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Integer[] loads = getIntegerArray(in.next());
 
    System.out.print(solution(loads));
  }
 
  private static Integer[] getIntegerArray(String str) {
    return Stream.of(str.split("\\,"))
          .map(Integer::valueOf)
          .toArray(Integer[]::new);
  }
}