if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    max_score = -100
    runner_up = -100

    for score in arr:
        if(score > max_score):
            max_score = score
    
    for score in arr:
        if(score > runner_up and score < max_score):
            runner_up = score

    print(runner_up)
