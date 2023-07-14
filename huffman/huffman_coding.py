import heapq


class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Carlos Fernando Padilla Mesa - 202059962
            Cesar Antonio Rios Gonzales - 2059959
            Ronan Moreno Castro - 201860286>
    Version: <1>
    """

    def encode(self, root, s, huffman_code):
        """
        Codifica el texto.
        text: texto a codificar
        :return: texto codificado
        """
        if root is None:
            return

        if isLeaf(root):
            huffman_code[root.ch] = s if len(s) > 0 else '1'

        self.encode(root.left, s + '0', huffman_code)
        self.encode(root.right, s + '1', huffman_code)

    def getTree(self, text):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        if len(text) == 0:
            return

        freq = {i: text.count(i) for i in set(text)}

        pq = [Node(k, v) for k, v in freq.items()]
        heapq.heapify(pq)

        while len(pq) != 1:
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            total = left.freq + right.freq
            heapq.heappush(pq, Node(None, total, left, right))

        root = pq[0]

        return root

    def getTable(self, root):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        huffmanCode = {}
        self.encode(root, '', huffmanCode)
        return huffmanCode

    def getSummary(self, text):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        root = self.getTree(text)

        huffmanCode = self.getTable(root)

        s = ''
        for c in text:
            s += huffmanCode.get(c)

        original_size = len(text) * 256
        compressed_size = len(s)
        compression_percentage = (1 - (compressed_size / original_size)) * 100

        node_count = self.count_nodes(root)

        depth = self.get_depth(root)

        summary = {
            'compression_percentage': compression_percentage,
            'node_count': node_count,
            'depth': depth
        }

        return summary

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def get_depth(self, node):
        if node is None:
            return 0
        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        return max(left_depth, right_depth) + 1


def isLeaf(root):
    """
    Verifica si el nodo es una hoja
    """
    return root.left is None and root.right is None


class Node:
    """
    Encapsula la información y la funcionalidad necesarias para representar
    un nodo en el árbol de Huffman y realizar comparaciones entre los nodos.
    """
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq
