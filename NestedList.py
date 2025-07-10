if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores = []
    for scor in records:
        scores.append(scor[1])  
    sorted_score = sorted(set(scores)) 
    sec_score = sorted_score[1]
    answer = []
    for name,score in records:
        if score == sec_score:
            answer.append(name)
    answer.sort()  
    for n in answer:       
        print(n)
