import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class part1 {

    public static void main(String[] args) throws IOException {

        // Read our input into a list we can work with
        List<String> rows = new ArrayList<String>();
        String image = new String(Files.readAllBytes(Paths.get("2019/08/input.txt")));
        while (image.length() > 149) {
            rows.add(image.substring(0, 150));
            image = image.substring(150);
        }

        // Find layer with fewest 0s
        int min0 = 150; // 25 * 6 = 150
        int minIndex = 0;
        for(String row : rows) {
            int count = 0;
            for (int i = 0; i < row.length(); i++){
                if (row.charAt(i) == '0') {
                    count++;
                }
            }
            if (count < min0) {
                min0 = count;
                minIndex = rows.indexOf(row);
            }
        }

        // Get count of 1s
        Pattern onePattern = Pattern.compile("[^1]*1");
        Matcher oneMatcher = onePattern.matcher(rows.get(minIndex));
        int oneCount = 0;
        while (oneMatcher.find()) {
            oneCount++;
        }

        // Get count of 2s
        Pattern twoPattern = Pattern.compile("[^2]*2");
        Matcher twoMatcher = twoPattern.matcher(rows.get(minIndex));
        int twoCount = 0;
        while (twoMatcher.find()) {
            twoCount++;
        }

        // Display 1s * 2s
        System.out.println(oneCount * twoCount);
    }
}
