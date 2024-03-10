import numpy as np
import sys

def hill_encrypt(K, PT, m = 2):

    pt, key = get_mats(K, PT, m)

    if round(np.linalg.det(key)) == 0:
        print("Entered key is singular, expected an invertible.")
        sys.exit()

    return mat_2_text(pt, key) # working beta


def hill_decrypt(K, CT, m = 2):

    ct, key = get_mats(K, CT, m)

    det_K = round(np.linalg.det(key))
    if det_K == 0:
        print("Entered key is singular, expected an invertible.")
        sys.exit()

    dec_K = get_dec_key(key)

    return mat_2_text(ct, dec_K) # working beta

'''                          !!!!                    Do not delete -- Contains helper functions                      !!!!                           '''

# some globals

# mapping char -> ind and reverse
char_ind = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 0
}

ind_char = {val: key for key, val in char_ind.items()}

mod_inv_dict = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}


def get_dec_key(key):

    # get the reciprocal modulo of the determinant
    det = round(np.linalg.det(key))                             # try the algo
    det_inv_mod = pow(det, -1, 26)                              # use mod_inv_dict instead?

    # get adjoint of key
    adj_key = np.linalg.inv(key) * round(det)

    # get modulo deciphering key ( = key_inv modulo)
    raw_dec_key = det_inv_mod * adj_key
    dec_key = np.where((raw_dec_key > 26) | (raw_dec_key < 0), raw_dec_key % 26, raw_dec_key)

    # return dec_key as int type
    return np.round(dec_key).astype(int)



def get_mats(K, PT, m):

    # remove all spaces and force lower-case
    pt = PT.strip()
    pt = pt.replace(" ", "")
    pt = pt.lower()

    # make P array as per given m (block-size)
    pt_ind_array = np.asarray([char_ind[i] for i in pt])
    PT_mat = pt_ind_array.reshape(len(pt_ind_array) // m, m)

    # make K array as per given m
    key_ind = np.asarray([int(i) for i in K.split(',')])
    K_mat = key_ind.reshape(len(key_ind) // m, m)

    return PT_mat, K_mat


# testing
def mat_2_text(mat, key):

    # implement Pi = (Ci x K_inv) mod 26
    prod_mat = np.asarray([(key @ block.T) for block in mat])
    prod_mat[prod_mat >= 26] = prod_mat[prod_mat >= 26] % 26

    # map back to letters and get a string
    str_ind = prod_mat.flatten()
    str_chars = [ind_char[(i)] for i in str_ind]

    return ''.join(str_chars)