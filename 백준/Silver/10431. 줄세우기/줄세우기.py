input = open(0).readline

for i in range(P := int(input())):
    back_shift = 0
    heights = list(map(int, input().split()))
    seq = heights[0]
    heights.remove(heights[0])

    for h in range(20):
        for c in range(h):
            if heights[h] < heights[c]:
                back_shift += (h-c)
                heights.insert(c, heights[h])
                heights.pop(h+1)
                break
    print(seq, back_shift)