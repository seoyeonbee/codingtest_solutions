import sys
t = int(input()) # 테스트케이스 수

for _ in range(t): # 각 테스트케이스 별 반복 수행
		s = list(sys.stdin.readline().rstrip().split()) # 문장 입력받은 후 공백 기준으로 분리해서 리스트화
		word_rev = [] # 뒤집힌 단어들을 저장할 리스트 생성

		for w in s: # 각 단어 별 반복 수행
				word_rev.append(w[::-1]) # 역순으로 슬라이싱해서 생성된 새로운 단어를 word_rev에 추가

		print(' '.join(word_rev)) # 단어들을 공백기준으로 합쳐서 출력