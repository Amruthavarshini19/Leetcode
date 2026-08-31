import java.util.*;

class Solution {

    private List<Integer> values;
    private Random random;

    public Solution(ListNode head) {
        values = new ArrayList<>();
        random = new Random();

        while (head != null) {
            values.add(head.val);
            head = head.next;
        }
    }

    public int getRandom() {
        int index = random.nextInt(values.size());
        return values.get(index);
    }
}