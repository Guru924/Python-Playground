import random

def randomChoice(chars):
    return random.choice(chars)

def encode(msg, randomChars):
    secret =""
    if len(msg) >= 3:
        l1 = msg.split(" ")
        for word in l1:
            firstCh = word[:1]
            lastch = word[1: len(word)]
            modCh = lastch + firstCh
            word = randomChoice(randomChars) + modCh + randomChoice(randomChars) + " "
            secret = secret+ word
    else:
        secret = secret + msg[::-1]
    return secret

def decode(secret):
    decodemsg = ""
    if len(secret) >= 3:
        l1 = secret.split(" ")
        l1.pop(-1)
        for word in l1:
            secWord = word[3: len(word)-3]
            firstCh = secWord[len(secWord)-1]
            remFirstCh = secWord[0: len(secWord)-1]
            decodemsg = decodemsg + firstCh + remFirstCh + " "
    else:
        decodemsg = decodemsg + secret[::-1]
    return decodemsg

def main():
    randomChars = ["ert", 'iio', 'wer', 'kjd', 'nbc','ert']
    # print(random.choice(randomChars))
    msg = input("Enter the message: ")
    encodedMsg = encode(msg, randomChars)
    print(encodedMsg)
    displayMsg = input("Want to see the decode message:(y/n)- ")
    if(displayMsg == 'y'):
        decodedMsg = decode(encodedMsg)
        print(decodedMsg)

main()