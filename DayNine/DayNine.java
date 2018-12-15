public class DayNine {
    static int number_of_players = 424;
    static int num_of_marbles = 71482;
    public static void main(String[] args) {
        Node start = new Node(null, null, 0);
        start.right = start; start.left = start; 
        Node second = new Node(start, start, )
        int playerScores[] = new int[number_of_players];
        for(int i = 2; i < num_of_marbles; i++) {
            if(i % 23 == 0) {

            } else {
                Node newNode = new Node(start.right.right, start.right, i);
            }
        }
    }

    
}

class Node {
    Node right;
    Node left; 
    int ID;

    public Node(Node r, Node l, int data) {
        this.right = r;
        this.left = l;
        this.ID = data;
    }
}