def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l = s.split()
    last_word = l[-1]
    return len(last_word)

if __name__ == "__main__":
    l= lengthOfLastWord("This is a test Sentence")
    print(l)

