t = int(input()) # 테스트케이스 수

for _ in range(t): # 각 테스트케이스별 반복 수행
    s = list(input().split()) # 입력받은 문장을 공백 기준으로 쪼갠 후 리스트화
    
    for w in s: # 각 단어별 반복 수행
        word = list(w) # 현재 단어를 한글자씩 분리해서 리스트화
        word.reverse() # 모든 글자 뒤집기
        word_rev = ''.join(word) # 뒤집은 글자들을 다시 합쳐서 한 단어로 저장
        print(word_rev, end = ' ') # 단어를 공백으로 이어서 출력
        
    print() # 줄바꿈