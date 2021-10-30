# Joshi_Hrishit_crypto_HW1_Fall_2021
from Pi import *


def problem_1():
    m = 'H.e.l.l.o.!!'
    k = 'd...'
    c = encrypt(m, k)
    p = decrypt(c, k)
    print("Ciphertext = ", c)
    print("Plaintext = ", p)
    return p


def problem_2():
    m = 'H.e.l.l.o.!!'
    k = 'y....;['
    c = encrypt(m, k)
    print("Ciphertext:", c)
    e = box(k)
    f = unbox(e)  # making k pure removing adulterants
    p = ord(f) - ord('a')
    q = chr(((26 - p) % 26) + ord('a'))  # making changes in k which allows us to use encrypt to decrypt
    x = encrypt(c, q)  # decryption using the encrypt function
    print("Plaintext:", x)
    return x


def problem_3():
    i = ord('a')
    c = 'ZQHQDQHQDGEQFTQETURFOUBTQDMXSADUFTYIQMDQXQMDZUZSMNAGFUFNQOMGEQUFUEAZQARFTQOXMEEUOMXOUBTQDEUFUEMXEAMZUOQMBBXUOMFUAZARFTQYAPGXAMDUFTYQFUOFTQADK '
    while i <= ord('z'):
        k = chr(i)
        print(k)
        dec = decrypt(c, k)
        print(dec)
        i += 1
    return 0


def problem_4():
    i = ord('a')
    c = 'ZQHQDQHQDGEQFTQETURFOUBTQDMXSADUFTYIQMDQXQMDZUZSMNAGFUFNQOMGEQUFUEAZQARFTQOXMEEUOMXOUBTQDEUFUEMXEAMZUOQMBBXUOMFUAZARFTQYAPGXAMDUFTYQFUOFTQADK'
    while i <= ord('z'):
        k = chr(i)
        dec = decrypt(c, k)
        arr = prob(dec)
        s = sum_prob(arr)
        if s >= 0.06:
            print("Key =", k)
            print("Plaintext = ", dec)
            print("IC:", s)
        i += 1
    return 0


def problem_6():
    m = 'H.e.l.l.o.!!'
    k = 'd..b t.'
    c = encrypt(m, k)
    p = decrypt(c, k)
    print("Ciphertext = ", c)
    print("Plaintext = ", p)
    return p


def problem_7a():
    m = 'TWTLPMDCOXRTTHESXCEINIPEMVTQWSSHDXXHTSLCSLTCILDCRIRDUEINTCOMNVLTXHBPRRIUXNINITGINXCRWOURZVRJVLXESETRKHZTISIWPLUCITRGHTLWOCLLWOKTCAIIWSSUCSDENSVFRSEJEEWPNQSRHXIQOCISWTWTGMNTNLVDHLPVEQJDCAVPTRAHISIWTAWSRVPYMZTSQERBTCWTGTLXESISIIGKTREHPYHTWTXSRTALGKPSLMSXRLPNTXRLBDGDLUGGTIDIDOSTWTAVUCXYKTWTJWHDJWHHPKPHOCTTRNDKPQBTG'
    j = 1
    arr_f = (9) * [0]
    while j < 10:
        x = seperate(m, j)
        abc = j * [0]
        i = 0
        while i < j:
            a = x[i]
            b = unbox(a)
            arr = prob1(b)
            s = sum_prob(arr)
            abc[i] = s
            avg_IC = (sum(abc)) / j

            i += 1
        arr_f[j - 1] = avg_IC
        j += 1
    l = 0
    while l < 9:
        if arr_f[l] == max(arr_f):
            g = l
            print("Key Length:", g + 1)
        l += 1

    return g + 1


def problem_7b():
    m = 'TWTLPMDCOXRTTHESXCEINIPEMVTQWSSHDXXHTSLCSLTCILDCRIRDUEINTCOMNVLTXHBPRRIUXNINITGINXCRWOURZVRJVLXESETRKHZTISIWPLUCITRGHTLWOCLLWOKTCAIIWSSUCSDENSVFRSEJEEWPNQSRHXIQOCISWTWTGMNTNLVDHLPVEQJDCAVPTRAHISIWTAWSRVPYMZTSQERBTCWTGTLXESISIIGKTREHPYHTWTXSRTALGKPSLMSXRLPNTXRLBDGDLUGGTIDIDOSTWTAVUCXYKTWTJWHDJWHHPKPHOCTTRNDKPQBTG'
    a = problem_7a()
    arr = seperate(m, a)
    key_arr = []
    i = 0
    while i < a:
        b = arr[i]
        c = unbox(b)
        f = ord('a')
        while f <= ord('z'):
            k = chr(f)
            dec = decrypt(c, k)
            arr1 = prob(dec)
            s = sum_prob(arr1)
            if s >= 0.059:
                key_arr.append(ord(k) - ord('a'))
            f += 1
        i += 1
    key = unbox(key_arr)
    print("Key:", key)
    plaintext = decrypt(m, key)
    print('Plaintext:', plaintext)
    return 0

# This python file contains the code for the answers of Questions 1,2,3,4,6,7a and 7b
# Every corresponding function to a question mentioned above is named as "problem_{question number}()"
# Please note that Question 7 has two functions problem_7a() and problem_7b()
# Thank you please reach out to hrishit@umd.edu if you have any problems with the execution of the code.
# Hrishit Joshi
