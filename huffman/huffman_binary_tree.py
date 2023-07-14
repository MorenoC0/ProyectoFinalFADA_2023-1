"""
Clase que implementa un árbol binario de Huffman
Autores:<Carlos Fernando Padilla Mesa - 202059962
        Cesar Antonio Rios Gonzales - 2059959
        Ronan Moreno Castro - 201860286>
"""

#Clase que implementa un árbol binario de Huffman
class HuffmanBinaryTree:
    def getNumberKey(self, root):
        """
        Retorna el valor de la llave,
        si es un string retorna -1, si es un
        numero retorna el numero.
        """
        if root.ch.isdigit():
            return int(root.ch)
        else:
            return -1

    def getLeft(self, root):
        """
        Retorna el hijo izquierdo del arbol.
        """
        return root.left

    def getRight(self, root):
        """
        Retorna el hijo derecho del arbol.
        """
        return root.right
