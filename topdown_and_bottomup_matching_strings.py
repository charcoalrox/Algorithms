def dna_match_bottomup(DNA1, DNA2):
#Find the greatest amount of matching chars between two strings 

    #initialize variables
    cache = [[0 for x in range(len(DNA1)+1)] for x in range(len(DNA2)+1)] #create a 2d array properly sized for both given input strings
    maxval = 0

    #iterate through both strings. Compare all chars
    for i in range(len(DNA2)+1):
        for j in range(len(DNA1)+1):
            if i == 0 or j == 0: #find empty strings/fills in base cases
                cache[i][j] = 0
            elif (i <= j or j <= i) and DNA1[j-1] == DNA2[i-1]:  #Iterate when two strings match
                cache[i][j] = cache[i-1][j-1] + 1
            else: #Find the largest of the two subproblems if they don't match and go that way
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

            if cache[i][j] > maxval:
                maxval = cache[i][j] #Captures the largest value found from calculating the subproblems

    #Debug variables
    #print(cache)
    #print(maxval)

    return maxval



def dna_match_topdown(DNA1, DNA2):
#LCS function but recursively calls functions to do it top-down using a nested function approach
    cache = [[0 for x in range(len(DNA1)+1)] for x in range(len(DNA2)+1)] #create a 2d array properly sized for both given input strings
    
    #Define a recursive function for memoization
    def recursive_memoization(i, j):
        if i == 0 or j == 0:
            return 0
        elif DNA1[i-1] == DNA2[j-1]:
            cache[j][i] = recursive_memoization(i-1, j-1) + 1
        else:
            cache[j][i] = max(recursive_memoization(i-1, j), recursive_memoization(i, j-1))

        return cache[j][i]

    return recursive_memoization(len(DNA1), len(DNA2))
