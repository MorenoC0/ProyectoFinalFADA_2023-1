from huffman_binary_tree import HuffmanBinaryTree
from huffman_coding import HuffmanCoding, isLeaf
from huffman_decoding import HuffmanDecoding

'''
Autores:<Carlos Fernando Padilla Mesa - 202059962
            Cesar Antonio Rios Gonzales - 2059959
            Ronan Moreno Castro - 201860286>
'''

if __name__ == '__main__':
    print('Codificacion de Huffman')
    print('Ingrese por favor la frase a codificar')
    text = input()
    text = text.lower()

    huffman_coding = HuffmanCoding()
    huffman_decoding = HuffmanDecoding()

    # Codificación
    root = huffman_coding.getTree(text)
    huffman_code = huffman_coding.getTable(root)

    encoded_string = ''
    for char in text:
        encoded_string += huffman_code[char]

    print('Cadena original:', text)
    print('Cadena codificada:', encoded_string)

    # Tabla de compresión
    print('Tabla de compresión:')
    for char, code in huffman_code.items():
        print(char, ':', code)

    # Decodificación
    decoded_string = ''
    current_node = root
    for bit in encoded_string:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if isLeaf(current_node):
            decoded_string += current_node.ch
            current_node = root

    print('Cadena decodificada:', decoded_string)

    # Estructura del árbol de Huffman
    print('Estructura del árbol de Huffman:')


    def print_tree(node, indent='', is_left=False):
        if node is None:
            return

        prefix = '└── ' if is_left else '├── '

        if isLeaf(node):
            print(indent + prefix + str(node.ch))
        else:
            print(indent + prefix + f'Internal Node ({node.freq})')
            print_tree(node.left, indent + ('    ' if is_left else '│   '), True)
            print_tree(node.right, indent + ('    ' if is_left else '│   '), False)


    print_tree(root)

    # Información de resumen
    summary = huffman_coding.getSummary(text)
    print('Resumen:')
    print('Porcentaje de compresión:', summary['compression_percentage'], '%')
    print('Número de nodos:', summary['node_count'])
    print('Profundidad del árbol:', summary['depth'])
