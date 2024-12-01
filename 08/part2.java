import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class part2 {

    public static void main(String[] args) throws IOException {

        // Treat the message as all transparent by default
        StringBuilder message = new StringBuilder()
                .append("2222222222222222222222222")
                .append("2222222222222222222222222")
                .append("2222222222222222222222222")
                .append("2222222222222222222222222")
                .append("2222222222222222222222222")
                .append("2222222222222222222222222");

        // Read the image into the message
        String image = new String(Files.readAllBytes(Paths.get("2019/08/input.txt")));
        while (image.length() > 149) {
            String layer = image.substring(0, 150);
            image = image.substring(150);
            for (int i = 0; i < layer.length(); i++ ) {

                // If the message is currently transparent, copy the layer value
                if (message.charAt(i) == '2') {
                    message.setCharAt(i, layer.charAt(i));
                }
            }
        }

        // Display the message
        int start = 0;
        int end = 25;
        while (end <= 150) {
            String row = message.substring(start, end);
            System.out.println(row.replaceAll("0", " "));
            start = end;
            end += 25;
        }
    }
}
