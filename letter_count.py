"""
Example 1:
Input: chars array = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = [“a”,"b”,”b”,”b”,”b”,”b”,”b”,”b”,”b”,”b”,”b”,”b”,”b”]
Output: Return 4, and the first 4 ch  aracters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

"""

def letter_count():

    str1 = "aabc"
    str2 =""
    counter =1
    endpoint = len(str1)
    print("Beginning")
    if endpoint ==1:
        str2 = str1
        # print(str2)
    else:
        for c in range (1,endpoint):
            if str1[c] != str1[c-1]:
                if counter == 1:
                    str2 = str2+str1[c-1]
                else:
                    str2 = str2+str1[c-1]+str(counter)
                counter =1
            else:
                counter +=1
        print("debug point")
        if counter == 1:
            str2 =str2+str1[c]
            print("=======>",)
        else:
            str2 = str2+str1[c-1]+str(counter)
    return(str2)

print(letter_count())
