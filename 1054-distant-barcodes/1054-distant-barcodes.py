class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        count = Counter(barcodes)
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        result = []
        prev_freq = 0
        prev_num = None
        while heap:
            freq, num = heapq.heappop(heap)
            if num == prev_num:
                if not heap:
                    break
                freq, num = heapq.heappop(heap)
            result.append(num)
            freq += 1
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_num))
            prev_freq = freq
            prev_num = num
        return result
        