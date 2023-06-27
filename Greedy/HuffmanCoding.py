# Huffman coding implementing using Python both coding and de-coding


import heapq


# creating huffman tree code
class Node:
    def __init__(self, freq, ch, left, right):
        self.freq = freq  # frequency of character
        self.ch = ch  # character ($ for non-leaf node)
        self.left = left  # node left of current node
        self.right = right  # node right of current node

    # less than function (used by heapq)
    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Building Huffman Tree
def buildTheHuffman(arr, freq):
    h = []  # creating minheap or priority q

    for i in range(arr):
        heapq.heappush(h, Node(freq[i], arr[i], None, None))

    # h already sorted in ascending order
    while len(h) > 1:
        lt = heapq.heappop(h)  # left node
        rt = heapq.heappop(h)  # right node
        heapq.heappush(h, Node(lt.freq + rt.freq, '$', lt, rt))  # Non-leaf node

    # root = h[0]
    return h[0]  # root node


# print Huffman's codes
def printCodes(root, s=''):  # current codes are present in s (empty string)
    if root is None:  # if tree is empty just return
        return
    if root.ch != '$':  # if not leaf node
        print(root.ch + '' + s)
        return
    # if a leaf node then
    printCodes(root.left, s+'0')
    printCodes(root.right, s+'1')


if __name__ == "__main__":
    printCodes()

