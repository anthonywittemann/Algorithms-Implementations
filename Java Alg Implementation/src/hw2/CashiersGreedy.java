package hw2;

//The following implementation generalizes for any coinage that works for greedy

public class CashiersGreedy {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] coinage = {1, 5, 10, 25, 100, 500, 1000, 2000}; //can be modified
		int cents = 123456; 				 //can be modified
		
		int[] change = getChangeCashiers(cents, coinage);
		
		System.out.println("______Change_______" + "\n");
		for(int i = change.length - 1; i >= 0; i--){
			System.out.println("Number of " + coinage[i] + " Coins: " + change[i]);
		}
	}
	
	/**
	 * runs in O(1) time where the constant varies 
	 * based on the number of coins in a given coinage
	 * @param cents
	 * @param coinage
	 * @return the change with the number of each coin of the given coinage
	 */
	public static int[] getChangeCashiers(int cents, int[] coinage){
		int coin = coinage.length - 1; //number of different coins in coinage
		int[] change = new int[coin + 1];
		int remainder = cents;
		
		while(coin >= 0){
			change[coin] = remainder / coinage[coin];
			remainder = remainder % coinage[coin];
			coin --;
		}
		
		return change;
	}

}
