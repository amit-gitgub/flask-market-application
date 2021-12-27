from collections import Counter
input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

votes = Counter(input)
print(votes)

max_vote = (max(votes.values()))

list1 = [i for i in votes.keys() if votes[i] == max_vote]

print(list1)
print(sorted(list1)[0])



