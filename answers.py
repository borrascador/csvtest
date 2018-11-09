def five_longest (filename):
    '''
        Question #1 
        What are the 5 longest start phrases in terms of number of characters?
    '''
    import csv
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        longest = ['', '', '', '', ''] 
        for row in reader:
            item = row[3]
            if len(longest[0]) < len(item):
                longest[0] = item
                longest = sorted(longest, key=len)
        return longest

def five_alpha (filename):
    '''
        Question #2
        What are the top 5 sent1's in alphabetical order?
    '''
    import csv
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        result = []
        for row in reader:
            sent1 = row[4].lower()
            while not sent1[0].isalpha(): sent1 = sent1[1:] 
            if len(result) < 5:
                result.append(sent1)
                result = sorted(result, reverse=True)
            elif sent1 < result[0]:
                result[0] = sent1
                result = sorted(result, reverse=True)
        return result
            
def count_unique (filename):
    '''
        Question #3
        How many unique words are there in all of the endings?
    '''
    import csv
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        unique = {}
        for index, row in enumerate(reader):
            if index == 0:
                continue
            words = row[7].split() + row[8].split() + row[9].split() + row[10].split()
            for word in words:
                unique[word] = True
        return len(unique)

def five_frequent (filename):
    '''
        Question #4
        What are the 5 most frequent words in the start phrases?
    '''
    import csv
    from collections import defaultdict
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = defaultdict(int)
        for row in reader:
            words = row[3].split()
            for word in words:
                counts[word] += 1
        most_frequent = []
        for key in sorted(counts, key=counts.get, reverse=True):
            most_frequent.append(key)
            if len(most_frequent) == 5:
                return most_frequent

def phrase_counts (filename):
    '''
        Question #5
        How many start phrases are there of length 1 word, 2 words,
        3 words, 4 words, and 5 words?
    '''
    import csv
    from collections import defaultdict
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = { x:0 for x in range(1,6) }
        for index, row in enumerate(reader):
            if index == 0:
                continue
            length = len(row[3].split())
            if 1 <= length <= 5:
                counts[length] += 1
        return counts
