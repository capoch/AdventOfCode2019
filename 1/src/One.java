import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class One {
    public static List readWithScanner(String file) throws IOException {
        List result = new ArrayList<Integer>();
        Scanner scanner = new Scanner(new File(file));
        scanner.useDelimiter("\n");

        while(scanner.hasNext()) {
            result.add(scanner.nextInt());
        }
        scanner.close();
        return result;
    }

    public static Integer calcFuel(Integer baseFuel) {
        Integer accumulator = 0;
        while(baseFuel/3 -2 > 0) {
            baseFuel = baseFuel/3 -2;
            accumulator += baseFuel;

        }
        return accumulator;
    }

    public static void main(String[] args) {
        List numbers = new ArrayList<Integer>();
        try {
            numbers = readWithScanner("input.txt");
        } catch(IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.println(calcFuel(1969));
        System.out.println(numbers.stream()
                .map(baseFuel -> calcFuel((Integer)baseFuel))
                .reduce(0, (x,y) -> (int)x+(int)y));
    }
}
