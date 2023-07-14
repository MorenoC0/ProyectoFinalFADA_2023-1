"""
Autores:<Carlos Fernando Padilla Mesa - 202059962
        Cesar Antonio Rios Gonzales - 2059959
        Ronan Moreno Castro - 201860286>
Version: <1>
"""

def isLeaf(root):
    return root.left is None and root.right is None

#Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
class HuffmanDecoding:

    def decode(self, root, index, s):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param index: texto a decodificar
        :param root: árbol de Huffman
        :param self:
        :param s:
        :return: texto decodificado
        """
        if root is None:
            return index

        if isLeaf(root):
            print(root.ch, end='')
            return index

        index = index + 1
        root = root.left if s[index] == '0' else root.right
        return self.decode(root, index, s)
