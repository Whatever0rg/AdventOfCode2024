import java.io.*;
import java.util.*;

public class Day2 {

    public static void main(String[] args) {

        String filename = "DayTwo/sampleinput.txt";

        readAndCheckNumbers(filename);

    }

    public static void readAndCheckNumbers(String filename) {
        int count = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            int lineNumber = 1;

            while ((line = br.readLine()) != null) {

                line = line.trim();

                String[] tokens = line.split("\\s+");

                List<Integer> numbers = new ArrayList<>();

                for (String token : tokens) {
                    try {
                        numbers.add(Integer.parseInt(token));
                    } catch (NumberFormatException e) {
                    }
                }

                if (numbers.size() >= 2) {

                    boolean result = checkIfSafeOrNot(numbers);
                    System.out.println("Line " + lineNumber + ": " + (result ? "Safe" : "Unsafe"));
                    if (result) {
                        count++;
                    }
                    System.out.println("'Safe' Lines:" + count);
                    System.out.println(numbers);
                } else {
                    System.out.println("Line " + lineNumber + ": Safe.");
                }

                lineNumber++;
            }
        } catch (IOException e) {

            System.err.println("Error reading the file: " + e.getMessage());
        }
    }

    public static boolean checkIfSafeOrNot(List<Integer> numbers) {
        int maxThreshold = 3;
        int minThreshold = -3;
        int notZero = 0;
        boolean isSafe = false;

        for (int i = 0; i < numbers.size(); i++) {
            boolean isIncreasing = true;
            boolean isDecreasing = true;

            List <Integer> tempList = new ArrayList<>(numbers);
            tempList.remove(i);                                                                         // Comment this out for Task One

            for (int n = 1; n < tempList.size(); n++) {
                int difference = tempList.get(n) - tempList.get(n - 1);
    
                if (difference <= maxThreshold & difference >= minThreshold & difference != notZero) {
                    if (tempList.get(n) > tempList.get(n - 1)) {

                        isDecreasing = false;
                    } else if (tempList.get(n) < tempList.get(n - 1)) {

                        isIncreasing = false;

                    } else {
                        isIncreasing = false;
                        isDecreasing = false;
                    }
                } else {
                    isIncreasing = false;
                    isDecreasing = false;
                }
            }
            if (isDecreasing | isIncreasing){
                isSafe = true;
            }
        }

        return isSafe;
    }
}