import java.io.*;

public class UppercaseFile {
    public static void main(String[] args) {
        File file = new File("sample.txt");

        try {
            // Step 1: Read file content
            BufferedReader reader = new BufferedReader(new FileReader(file));
            StringBuilder content = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            reader.close();

            // Step 2: Convert to uppercase
            String upperContent = content.toString().toUpperCase();

            // Step 3: Write back to same file
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write(upperContent);
            writer.close();

            System.out.println("File converted to uppercase successfully.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}..


