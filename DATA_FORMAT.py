# Formats inputted data to write on excel and validated
# Also used to ensure integrity of data by use of error handling in MAIN
# Returns None if data cannot be accepted

# 1 Parameter = 1 Data segment

import re

class DATA_FORMAT:

    def convert(data):
        numArr = []

        # The max amount of parameters that can are allowed
        MAX_ALLOWED_LEN = 4

        # Each parameter requires a float indicator
        floatIndex = [False, True]

        i = -1

        toStr = str(data)

        strArr = toStr.split(",")

        strArrLen = len(strArr) - 1

        if strArrLen <= MAX_ALLOWED_LEN:
            while i < strArrLen:
                i += 1

                if floatIndex[i]:
                    numArr.append(float(re.search(r'\d+', strArr[i]).group()) / 100)
                else:
                    numArr.append(int(re.search(r'\d+', strArr[i]).group()))
        else:

            return None
        
        if None in numArr:

            return None
        
        else:

            return numArr