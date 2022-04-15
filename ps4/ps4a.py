# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    charArray = list(sequence)
    res = []
    dfs(charArray, res, 0, len(sequence))
    return res

def dfs(charArray, res, i, end):
    if (i == end):
        res.append("".join(charArray))
    
    for c in range(i, end):
        charArray[i], charArray[c] = charArray[c], charArray[i]
        dfs(charArray, res, i + 1, end)
        charArray[i], charArray[c] = charArray[c], charArray[i]

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input1 = ''
    print('Input:', example_input1)
    print('Expected Output:', [''])
    print('Actual Output:', get_permutations(example_input1))

    example_input2 = 'abcd'
    print('Input:', example_input2)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input2))

