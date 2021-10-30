def box(m):
    m = m.lower()  # converting lowercase
    arr = [0] * len(m)  # initializing array with same length as the length
    i = 0
    for n in m:
        if not ('a' <= n <= 'z'):  # excluding special characters
            continue
        arr[i] = ord(n) - ord('a')  # subtracting ascii character values by a so we can map it to 0-25
        i += 1
    arr_f = arr[0:i]  # array final - to exclude the special character in the array
    return arr_f


def lock(arr_f, y):
    a = len(arr_f)
    k = box(y)
    b = 1
    while b < a:  # using the loop to make the keys array
        k.append(k[b - 1])
        b += 1
    enc = [0] * len(arr_f)  # initializing array
    i = 0
    for x in arr_f:
        enc[i] = (x + k[i]) % 26  # shifting the array to its keys value %26 is for looping from z to a
        i += 1
    enc_f = enc[0:i]
    return enc_f


def unbox(enc_f):
    m = ""
    for x in enc_f:
        m += chr(x + ord('a'))
    return m


def encrypt(m, k):
    arr = box(m)
    enc = lock(arr, k)
    c = unbox(enc)
    return c


def decrypt(c, y):
    cipher = box(c)
    a = len(c)
    k = box(y)
    b = 1
    while b < a:  # using the loop to make the keys array
        k.append(k[b - 1])
        b += 1
    dec = [0] * len(c)  # initializing array
    i = 0
    for x in cipher:
        dec[i] = (x - k[i]) % 26  # shifting the array to its keys value %26 is for looping from z to a
        i += 1
    dec_f = dec[0:i]
    plain = unbox(dec_f)
    return plain


def prob(m):
    a = box(m)
    b = len(a)
    arr = [0] * 26
    arr1 = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    # arr1 is the probability distribution for general english taken from a study resource (professor's video online)
    j = 0
    while j < 26:   #these loops are counting the number of letters in the message
        ctr = 0
        i = 0
        while i < b:
            if a[i] == j:
                ctr += 1
            arr[j] = ctr
            i += 1
        j += 1
    k = 0
    while k < 26:
        arr[k] = (arr[k]/b) * (arr1[k])
        k += 1
    return arr

def prob1(m):
    a = box(m)
    b = len(a)
    arr = [0] * 26
    arr1 = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    # arr1 is the probability distribution for general english taken from a study resource (professor's video online)
    j = 0
    while j < 26:   #these loops are counting the number of letters in the message
        ctr = 0
        i = 0
        while i < b:
            if a[i] == j:
                ctr += 1
            arr[j] = ctr
            i += 1
        j += 1
    k = 0
    while k < 26:
        arr[k] = (arr[k]/b) * (arr[k]/b)
        k += 1
    return arr

def sum_prob(arr):
    s = 0
    for i in arr:
        s = s + i
    return s


def seperate(m, size):
    source = box(m) # putting the message in the array
    return [source[i::size] for i in range(size)]   # (Condensed everything in one line) seperating that array into a nested array of the specified size chunks


