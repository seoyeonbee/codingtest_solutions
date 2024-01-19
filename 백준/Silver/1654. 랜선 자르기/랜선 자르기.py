import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 갖고 있는 랜선 수, 필요한 랜선 수
length = list(int(input()) for _ in range(k)) # 랜선 별 길이

# 이진탐색을 위한 시작점, 끝점 설정
start = 1
end = max(length)

# 이진탐색 수행
def bin_search(start, end, n):
		if start > end:
				return end

		total = 0 # 절단된 랜선 개수 합
		mid = (start + end) // 2 # 중간점 설정

		# 절단된 랜선 개수 계산
		for x in length:
				total += (x // mid)

		if total >= n: # 절단된 랜선 개수가 n보다 클 경우
				return bin_search(mid+1, end, n) # 더 크게 자른다
		else: # 절단된 랜선 개수가 n보다 작을 경우
				return bin_search(start, mid-1, n) # 더 작게 자른다

print(bin_search(start, end, n)) # 정답 출력