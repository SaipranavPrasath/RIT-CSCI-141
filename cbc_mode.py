file name: cbc_mode.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

from encryption import *
from linked_list_type import *
from mutable_list import *

def xor_gate(list1, list2):
    """
    Create a list of outputs of a XOR gate performed on elements of list1 and list2.
    :param list1: list of zeros/ones
    :param list2: list of zeros/ones
    :return: list of zeros/ones
    """
    xor_list = []
    if len(list1) != len(list2):
        raise ValueError("The lists are not the same length.")
    else:
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                xor_list.append(0)
            else:
                xor_list.append(1)
        return xor_list

def cbc_mode_encryption(plaintext, IV, key):
    """
    this function, when executed, loops over each node block in plaintext, which is a linked list given to us. next,
    it makes an empty list which will eventually contain the cipher of plaintext. lastly, it computes the cipher for
    each node block using the xor_gate and encryption functions, appends the cipher to a new linked list, and returns
    the new linked list.
    :param plaintext: a linked list
    :param IV: a python list
    :param key: a python list
    :return:list1, which is the cipher of plaintext
    """
    node = plaintext.head
    list1 = make_empty_list()
    cipher_text = IV
    while node is not None:
        vector = xor_gate(node.value, cipher_text)
        cipher_text = encryption(vector, key)
        append(list1, cipher_text)
        node = node.next
    return list1

def cbc_mode_decryption(ciphertext, IV, key):
    """
    this function, when executed, loops over each node block in ciphertext, which is a linked list given to us. next,
    it makes an empty list which will eventually contain the decryption of ciphertext. lastly, it computes the
    decryption for each node block using the decryption and xor_gate functions, appends the decryption to a new linked
    list, and returns the new linked list.
    :param ciphertext: a linked list
    :param IV: a python list
    :param key: a python list
    :return:list1, which is the decryption of ciphertext
    """
    node = ciphertext.head
    list1 = make_empty_list()
    cipher_text = IV
    while node is not None:
        decrypted_text = decryption(node.value, key)
        vector = xor_gate(cipher_text, decrypted_text)
        cipher_text = node.value
        append(list1, vector)
        node = node.next
    return list1
