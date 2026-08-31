import java.util.*;

class RandomizedCollection {

    private List<Integer> list;
    private Map<Integer, Set<Integer>> map;
    private Random random;

    public RandomizedCollection() {
        list = new ArrayList<>();
        map = new HashMap<>();
        random = new Random();
    }

    public boolean insert(int val) {
        if (!map.containsKey(val)) {
            map.put(val, new HashSet<>());
        }

        map.get(val).add(list.size());
        list.add(val);

        return map.get(val).size() == 1;
    }

    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }

        Set<Integer> indices = map.get(val);
        int index = indices.iterator().next();

        int lastIndex = list.size() - 1;
        int lastValue = list.get(lastIndex);

        indices.remove(index);

        if (index != lastIndex) {
            list.set(index, lastValue);

            Set<Integer> lastIndices = map.get(lastValue);
            lastIndices.remove(lastIndex);
            lastIndices.add(index);
        }

        list.remove(lastIndex);

        if (indices.isEmpty()) {
            map.remove(val);
        }

        return true;
    }

    public int getRandom() {
        return list.get(random.nextInt(list.size()));
    }
}