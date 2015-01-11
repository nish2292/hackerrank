def palindrome(str1,str2):
    str = str1+str2
    return str == str[::-1]

T = input()

for t in range(T):
    st = raw_input()
    if palindrome(st,''):
        print -1
    else:
        chr1 = [0] *26
        for i in range(len(st)):
            t1 = ord(st[i]) - 97
            chr1[t1] = chr1[t1] + 1
        for i in range(len(st)):
            t1 = ord(st[i]) - 97
            if chr1[t1]%2==0:
                continue
            if palindrome(st[0:i],st[(i+1):len(st)]):
                print i
                break
