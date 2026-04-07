# --conding:utf-8--
import os
import regex
import math

nDecNum = 0
nBinPower = 1
MAX_INT = 2 ** 32 - 1
os.system("cls")
print("Input a binary number:")
strLine = input()
nStrLen = len(strLine)
nMaxBinLen = math.trunc(math.log(MAX_INT, 2))
oMatches = regex.fullmatch("^[0-1]+$", strLine)
bRightString = (nStrLen < nMaxBinLen and oMatches is not None)
if (not bRightString):
    print("Wrong binary number format!!!")
    exit(0)
for i in range(nStrLen):
    nBinDigit = ord(strLine[nStrLen - 1 - i]) - ord('0')
    nDecNum += (nBinDigit * nBinPower)
    nBinPower *= 2
print(f"The decenary equivalent of the binary number {strLine} is {nDecNum}")
