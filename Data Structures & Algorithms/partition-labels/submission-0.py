class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = defaultdict(int)
        for i,v in enumerate(s):
            mapping[v] = i

        size, end = 0, 0
        output = []

        for i,v in enumerate(s):
            size += 1
            end = max(end, mapping[v])

            if i == end:
                output.append(size)
                size = 0

        return output
        