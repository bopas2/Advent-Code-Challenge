import java.io.File;
import java.util.Scanner;
import java.util.HashSet;

public class DayOne {
    static final File FILE = new File("C:\\Users\\langt\\Desktop\\Avent of code\\DayOne\\input.txt");

    public static void main(String[] args) throws Exception {
        System.out.println(partOne());
        System.out.println(partTwo());
    }

    private static int partOne() throws Exception {
        Scanner scan = new Scanner(FILE);
        int ans = 0;
        while(scan.hasNextLine()) {
            ans += Integer.parseInt(scan.nextLine());
        }
        return ans;
    }

    private static int partTwo() throws Exception {
        HashSet<Integer> set = new HashSet<>();
        int ans = 0;
        set.add(0);
        while(true) {
            Scanner scan = new Scanner(FILE);
            while(scan.hasNextLine()) {
                int x = Integer.parseInt(scan.nextLine());
                ans += x;
                if (set.contains(ans)) {
                    return ans;
                }
                set.add(ans);
            }
        }
    }
}
