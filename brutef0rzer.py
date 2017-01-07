#Brutef0rzer v 0.1
#by LaZy SeC

import time
import hashlib
def main():
    #ASCIIIIII
    print('                                           ###                               ')
    print('#####  #####  #    # ##### ###### ######  #   #  #####  ###### ###### #####  ')
    print('#    # #    # #    #   #   #      #      #     # #    #     #  #      #    # ')
    print('#####  #    # #    #   #   #####  #####  #     # #    #    #   #####  #    # ')
    print('#    # #####  #    #   #   #      #      #     # #####    #    #      #####  ')
    print('#    # #   #  #    #   #   #      #       #   #  #   #   #     #      #   #  ')
    print('#####  #    #  ####    #   ###### #        ###   #    # ###### ###### #    # ')







    print('By LaZy SeC')
    print
    print('Version 0.1')
    print
    charsets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyzABDCEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "abcdefghijklmnopqrstuvwxyzABDCEFGHIJKLMNOPQRSTUVWXYZ0123456789", "abcdefghijklmnopqrstuvwxyz0123456789", " "]
    print("Charsets:")
    print("0: lower case")
    print("1: upper case")
    print("2: upper + lower case")
    print("3: numbers")
    print("4: upper + lower + numbers")
    print("5: lower + numbers")
    print("6: your own charset")
    print("Enter the charset")
    charset_ = input("charset: ")
    charset = charsets[charset_]
    if(charset_ == 6):
        print("Write all chars!(like abcdefg1234.:/)");
        charset = str(raw_input("charset: "))
    print("Charset = " + charset)
    print
    print("Enter your MD5 Hash")
    password = str(raw_input("MD5: "))
    print
    print
    print("Starting Bruteforce")
    start = int(round(time.time() * 1000))
    while(True):
        passwordlength = 1
        if(passwordlength==1):
            print("current password length: " + str(passwordlength))
            a = 0
            for a in range(0, len(charset)):
                pwd = charset[a]
                #print(pwd)
                #print(hashlib.md5(pwd).hexdigest())
                if(hashlib.md5(pwd).hexdigest() == password):
                    print("Found password: " + pwd)
                    end = int(round(time.time() * 1000))
                    print("Time elapsed: " + str(end - start))
                    exit()
            passwordlength = passwordlength + 1
        if(passwordlength==2):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    pwd = charset[a] + charset[b]
                    #print(pwd)
                    if(hashlib.md5(pwd).hexdigest() == password):
                        print("Found password: " + pwd)
                        end = tint(round(time.time() * 1000))
                        print("Time elapsed: " + str(end - start))
                        exit()
            passwordlength = passwordlength + 1
        if(passwordlength==3):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                        for c in range(0, len(charset)):
                            pwd = charset[a] + charset[b] + charset[c]

                            #print(pwd)
                            if(hashlib.md5(pwd).hexdigest() == password):
                                print("Found password: " + pwd)
                                end = int(round(time.time() * 1000))
                                print("Time elapsed: " + str(end - start))
                                exit()
            passwordlength = passwordlength + 1
        if(passwordlength==4):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):

                            pwd = charset[a] + charset[b] + charset[c] + charset[d]
                            #print(pwd)
                            if(hashlib.md5(pwd).hexdigest() == password):
                                print("Found password: " + pwd)
                                end = int(round(time.time() * 1000))
                                print("Time elapsed: " + str(end - start))
                                exit()
            passwordlength = passwordlength + 1
        if(passwordlength==5):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):

                                pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e]
                                #print(pwd)
                                if(hashlib.md5(pwd).hexdigest() == password):
                                    print("Found password: " + pwd)
                                    end = int(round(time.time() * 1000))
                                    print("Time elapsed: " + str(end - start))
                                    exit()
            passwordlength = passwordlength + 1
        if(passwordlength==6):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):
                                for f in range(0, len(charset)):

                                    pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e] + charset[f]
                                    #print(pwd)
                                    if(hashlib.md5(pwd).hexdigest() == password):
                                        print("Found password: " + pwd)
                                        end = int(round(time.time() * 1000))
                                        print("Time elapsed: " + str(end - start))
                                        exit()
            passwordlength = passwordlength + 1
        if(passwordlength==7):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):
                                for f in range(0, len(charset)):
                                    for g in range(0, len(charset)):

                                        pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e] + charset[f] + charset[g]
                                        #print(pwd)
                                        if(hashlib.md5(pwd).hexdigest() == password):
                                            print("Found password: " + pwd)
                                            end = int(round(time.time() * 1000))
                                            print("Time elapsed: " + str(end - start))
                                            exit()
            passwordlength = passwordlength + 1
        if(passwordlength==8):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):
                                for f in range(0, len(charset)):
                                    for g in range(0, len(charset)):
                                        for h in range(0, len(charset)):

                                            pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e] + charset[f] + charset[g] + charset[h]
                                            #print(pwd)
                                            if(hashlib.md5(pwd).hexdigest() == password):
                                                print("Found password: " + pwd)
                                                end = int(round(time.time() * 1000))
                                                print("Time elapsed: " + str(end - start))
                                                exit()
            passwordlength = passwordlength + 1
        if(passwordlength==9):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            i = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):
                                for f in range(0, len(charset)):
                                    for g in range(0, len(charset)):
                                        for h in range(0, len(charset)):
                                            for i in range(0, len(charset)):

                                                pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e] + charset[f] + charset[g] + charset[h] + charset[i]
                                                #print(pwd)
                                                if(hashlib.md5(pwd).hexdigest() == password):
                                                    print("Found password: " + pwd)
                                                    end = int(round(time.time() * 1000))
                                                    print("Time elapsed: " + str(end - start))
                                                    exit()
            passwordlength = passwordlength + 1
        if(passwordlength==10):
            print("current password length: " + str(passwordlength))
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            i = 0
            j = 0
            for a in range(0, len(charset)):
                for b in range(0, len(charset)):
                    for c in range(0, len(charset)):
                        for d in range(0, len(charset)):
                            for e in range(0, len(charset)):
                                for f in range(0, len(charset)):
                                    for g in range(0, len(charset)):
                                        for h in range(0, len(charset)):
                                            for i in range(0, len(charset)):
                                                for j in range(0, len(charset)):

                                                    pwd = charset[a] + charset[b] + charset[c] + charset[d] + charset[e] + charset[f] + charset[g] + charset[h] + charset[i] + charset[j]
                                                    #print(pwd)
                                                    if(hashlib.md5(pwd).hexdigest() == password):
                                                        print("Found password: " + pwd)
                                                        end = int(round(time.time() * 1000))
                                                        print("Time elapsed: " + str(end - start))
                                                        exit()
            passwordlength = passwordlength + 1
        if(passwordlength==11):
            print("Password is too long to bruteforce!")
            end = int(round(time.time() * 1000))
            print("Time elapsed: " + str(end - start))
            exit()


main()
