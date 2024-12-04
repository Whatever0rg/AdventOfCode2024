import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day4 {
    static List<List<Character>> words = new ArrayList<>();
    static int Len;

    public static void main(String[] args) {
        String filename = "DayFour/input.txt";

        try (BufferedReader file = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = file.readLine()) != null) {
                List<Character> charList = new ArrayList<>();
                for (char c : line.toCharArray()) {
                    charList.add(c);
                }
                words.add(charList);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Len = words.size();
        System.out.println(TaskOne(words, Len));
        System.out.println(TaskTwo(words, Len));
    }

    static boolean inbound(int i, int m) {
        return 0 <= i && i < Len && 0 <= m && m < Len;
    }

    static int TaskOne(List<List<Character>> search, int n) {
        int matches = 0;

        for (int i = 0; i < n; i++) {
            for (int m = 0; m < n; m++) {
                if (search.get(i).get(m) != 'X') {
                    continue;
                }

                for (int b : new int[]{-1, 0, 1}) {
                    for (int v : new int[]{-1, 0, 1}) {
                        if (b == 0 && v == 0) {
                            continue; // Cause this should be the X
                        }

                        if (inbound(i + 3 * b, m + 3 * v)) {
                            StringBuilder sb = new StringBuilder();
                            for (int k = 0; k < 4; k++) {
                                sb.append(search.get(i + k * b).get(m + k * v));
                            }
                            if (sb.toString().equals("XMAS")) {
                                matches++;
                            }
                        }
                    }
                }
            }
        }
        return matches;
    }

    static int TaskTwo(List<List<Character>> search, int n) {
        int matches = 0;

        for (int i = 0; i < n; i++) {
            for (int m = 0; m < n; m++) {
                if (search.get(i).get(m) != 'A') {
                    continue;
                }

                if (!inbound(i + 1, m + 1) || !inbound(i + 1, m - 1) || 
                    !inbound(i - 1, m + 1) || !inbound(i - 1, m - 1)) {
                    continue;
                }

                if (!((search.get(i - 1).get(m - 1) == 'M' && search.get(i + 1).get(m + 1) == 'S') ||
                      (search.get(i - 1).get(m - 1) == 'S' && search.get(i + 1).get(m + 1) == 'M'))) {
                    continue;
                }

                if (!((search.get(i + 1).get(m - 1) == 'M' && search.get(i - 1).get(m + 1) == 'S') ||
                      (search.get(i + 1).get(m - 1) == 'S' && search.get(i - 1).get(m + 1) == 'M'))) {
                    continue;
                }

                matches++;
            }
        }
        return matches;
    }
}

