public class DayFourteen2 {
    static final Integer NUM_OF_RECIPES = 909441;
    public static void main(String[] args) {
        Node first = new Node(null, null, 3);
        Node second = new Node(first, first, 7);
        first.right = second; first.left = second;
        int size = 2;
        Node end = second; Node start = first;
        Node workerOne = first; Node workerTwo = second;
        while (true) { 
            if (workerOne.data + workerTwo.data < 10) {
                Node toAdd = new Node(end, end.right, workerOne.data + workerTwo.data);
                end.right = toAdd; start.left = toAdd;
                end = toAdd;
                size++;
            } else {
                Node toAdd = new Node(end, end.right, new Integer((workerOne.data + workerTwo.data) / 10));
                end.right = toAdd; start.left = toAdd;
                end = toAdd;
                toAdd = new Node(end, end.right, new Integer((workerOne.data + workerTwo.data) % 10));
                end.right = toAdd; start.left = toAdd;
                end = toAdd;
                size += 2;
            }
            int stop = workerOne.data + 1;
            for (int j = 0; j < stop; j++) {
                workerOne = workerOne.right;
            }
            stop = workerTwo.data + 1;
            for (int j = 0; j < stop; j++) {
                workerTwo = workerTwo.right;
            }

            if (size == NUM_OF_RECIPES + 10 || size == NUM_OF_RECIPES + 11) {
                System.out.println("Part One: ");
                getData(start, NUM_OF_RECIPES);
                System.out.println("Part Two: ");
            }
            
            boolean toBreak = false;
            for (int j = 0; j < 2; j++) {
                Node temp;
                if (j == 0) temp = end;
                else temp = end.left;
                StringBuilder tempStr = new StringBuilder("");  
                for (int i = 0; i < (NUM_OF_RECIPES + "").length(); i++) {
                    if (!(NUM_OF_RECIPES + "").substring((NUM_OF_RECIPES + "").length() - i - 1, (NUM_OF_RECIPES + "").length() - i).equals(temp.data + "")) { break; }
                    tempStr.append(temp.data);
                    temp = temp.left;
                }
                if (tempStr.reverse().toString().equals(NUM_OF_RECIPES + "")) {
                    System.out.println(size - (NUM_OF_RECIPES + "").length() - j);
                    toBreak = true;
                    break;
                }
            }
            if (toBreak) break;
        }
    }

    static void getData(Node start, int numOfRecipes) {
        String data = "";
        for (int i = 0; i < numOfRecipes; i++) { start = start.right; }
        for (int i = 0; i < 10; i++) {
            data = data + start.data;
            start = start.right;
        }
        System.out.println(data);
    }

    static void print(Node start, Node end) {
        Node cursor = start;
        String result = "[" + cursor.data + ", ";
        cursor = cursor.right;
        while(!cursor.equals(start)) {
            result += cursor.data + ", ";
            cursor = cursor.right;
        }
        result = result.substring(0, result.length() - 2) + "]";
        System.out.println(result); 
    }
}

class Node {
    Node left;
    Node right;
    Integer data;

    public Node(Node left, Node right, Integer data) {
        this.left = left;
        this.right = right;
        this.data = data;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Node)) return false;
        Node x = (Node) obj;
        return left == x.left && right == x.right && data == x.data;
    }
}