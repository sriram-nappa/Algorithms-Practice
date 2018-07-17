class Solution:
    def isUnique(self, testString):
        uniqueObj = {}
        for s in testString:
            if s in uniqueObj:
                return False
            uniqueObj[s] = True
        return True

if __name__ == "__main__":
    print(Solution().isUnique("abcdefe"))


# OPTION 0: Naive approach: time O(n^2)
def unique_characters_naive_enum(input_string):
    if len(input_string)>96:
        return False
    for idx, char in enumerate(input_string):
        for idx2 in range(idx+1,len(input_string)):
            if char == input_string[idx2]:
                return False
    return True


# OPTION 1: Naive approach with set: time O(n^2)
def unique_characters_naive_set(input_string):
    if len(input_string)>96:
        return False
    chars_seen = set()
    for char in input_string:
        if char in chars_seen:
            return False
        chars_seen.add(char)
    return True


# OPTION 2: Naive approach with Short set statement: time unknown
def unique_characters_naive_set_short(input_string):
    return len(set(input_string)) == len(input_string)


# OPTION 3: Sorting way
# Time: O(nlog(n))    Space: depends on the sorting used.
def unique_characters_sorted(input_string):
    if len(input_string)>96:
        return False
    sorted_chars = sorted(input_string)
    prev_char = None
    for char in sorted_chars:
        if char == prev_char:
            return False
        prev_char = char
    return True


# OPTION 4: Array/list way
# Time: O(n)   Space: O(1) but influenced by the list of length 96
def unique_characters_list(input_string):
    if len(input_string)>96:
        return False
    chars_list = [False] * 96
    for char in input_string:
        # take list position by taking ascii position - 32 (amount of control characters)
        idx = ord(char)-32
        if chars_list[idx]:
            return False
        chars_list[idx] = True
    return True


# OPTION 5: bitwise attempt
# only consider lowercase character a-z, which fits in 4 bytes.
# Time: O(n)   Space: O(1) => 4 bytes.
def unique_characters_bitwise(input_string):
    if len(input_string)>26:
        return False
    # each bit represents the presence of a character or not (e.g. bit position 0 represents 'a')
    check_bytes = 0
    for char in input_string:
        idx = ord(char)-ord('a')
        if (check_bytes & (1 << idx)) > 0:
            return False
        check_bytes |= (1 << idx)
    return True