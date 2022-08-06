n=int(input())
scores=[]
final_names=[]

student=[[str(input()),float(input())]for i in range(n)]
#print(student)
#print(student[0])
for i in range(n):
    scores.append(student[i][1])
#print(scores)

scores.sort()
#print(scores)

lowest=scores[0]
#print(lowest)

for i in range(n):
    if scores[i]>lowest:
        sec_lowest=scores[i]
        break
#print(sec_lowest)

for i in range(n):
    if student[i][1]==sec_lowest:
        final_names.append(student[i][0])

final_names.sort()
#print(final_names)
for elements in final_names: # to print all individual elements
    print(elements)

