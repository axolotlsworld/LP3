# DAA-2 : Huffman encoding using greedy strategy (always merge the two least frequent nodes)
import heapq
from collections import Counter


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch, self.freq, self.left, self.right = ch, freq, left, right

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(text):
    heap = [Node(c, f) for c, f in Counter(text).items()]
    heapq.heapify(heap)
    while len(heap) > 1:                      # greedy choice
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, a.freq + b.freq, a, b))
    return heap[0]


def make_codes(node, code="", table=None):
    table = {} if table is None else table
    if node.ch is not None:
        table[node.ch] = code or "0"          # single-character text gets code "0"
    else:
        make_codes(node.left, code + "0", table)
        make_codes(node.right, code + "1", table)
    return table


def decode(bits, root):
    if root.ch is not None:                   # FIX: only one distinct character
        return root.ch * len(bits)
    out, node = [], root
    for b in bits:
        node = node.left if b == "0" else node.right
        if node.ch is not None:
            out.append(node.ch)
            node = root
    return "".join(out)


if __name__ == "__main__":
    text = input("Enter text to encode : ")
    if not text:                              # FIX: empty input crashed before
        raise SystemExit("Please enter some text.")
    root = build_tree(text)
    codes = make_codes(root)
    print("\nChar  Freq  Huffman code")
    for ch, f in sorted(Counter(text).items(), key=lambda x: (-x[1], x[0])):
        print(f"{ch!r:<5} {f:<5} {codes[ch]}")
    encoded = "".join(codes[c] for c in text)
    print("\nEncoded bits :", encoded)
    print("Original size :", len(text) * 8, "bits (8 bits per char)")
    print("Encoded size  :", len(encoded), "bits")
    print(f"Saving        : {100 - len(encoded) * 100 / (len(text) * 8):.1f} %")
    print("Decoded text  :", decode(encoded, root))
