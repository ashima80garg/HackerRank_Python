def score_words(words):
    score=0
    total_score=0
    for x in words:
        count_vowel=0
        word=list(map(str,x))
        for i in word:
            if i=='a':
                count_vowel+=1
            if i=='e':
                count_vowel+=1
            if i=='i':
                count_vowel+=1
            if i=='o':
                count_vowel+=1
            if i=='u':
                count_vowel+=1
            if i=='y':
                count_vowel+=1
        #print("count of vowels in word {} is {}".format(x,count_vowel))
        if count_vowel%2==0:
            total_score+=2
        else:
            total_score+=1
    return(total_score)

n = int(input())
words = input().split()
print(score_words(words))