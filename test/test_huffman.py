'''
import pytest
from huffman.huffman_coding import HuffmanCoding
from huffman.huffman_decoding import HuffmanDecoding


@staticmethod
def verify_tree(tree):
    """
    Verifica que el árbol de Huffman sea válido.
    :param tree: árbol de Huffman
    :return: True si el árbol es válido, False de lo contrario
    """
    key = tree.get_number_key()
    if key != -1:
        left = tree.get_left()
        right = tree.get_right()

        if left is not None and right is not None:
            condition = key >= left.get_number_key() and key >= right.get_number_key()
            return condition and verify_tree(left) and verify_tree(right)
        else:
            if left is None:
                condition = key >= right.get_number_key()
                return condition and verify_tree(right)
            else:
                if right is None:
                    condition = key >= left.get_number_key()
                    return condition and verify_tree(left)
                else:
                    return True
    else:
        return True

@pytest.mark.parametrize("resources", ["ejemplo1.in", "ejemplo2.in", "ejemplo3.in"])
def test_files(resources):
    with open(f'resources/{resources}', 'r') as file:
        text = file.read()

    coding = HuffmanCoding()
    encoded = coding.encode(text)
    tree = coding.getTree()
    
    decoding = HuffmanDecoding()
    decoded = decoding.decode(encoded, tree)

    assert text == decoded '''
