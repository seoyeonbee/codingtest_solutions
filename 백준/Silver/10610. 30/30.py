n = int(input()) # 양수 n 입력받기
n_list = [] # 각 자릿수를 담을 리스트 생성

for i in str(n):
    n_list.append(int(i)) # 각 자릿수 분리해서 리스트에 담기
    
n_list.sort(reverse=True) # 내림차순 정렬

# 10의 배수가 아니면 무조건 불가능
if n_list[-1] != 0: # n_list의 마지막 원소가 0이 아닐 경우
    print(-1) # -1 출력해서 종료

# 10의 배수가 맞다면 끝에 0을 제외한 나머지 자릿수들의 합이 3의 배수일 경우 -> 3의 배수
else: # n_list의 마지막 원소가 0일 경우
    # n_list의 첫번째부터 끝에서 두번쨰 원소까지의 합을 3으로 나눈 나머지가 0일 경우(배수판정법)
    if sum(n_list[:-1]) % 3 == 0:
        print(''.join(map(str, n_list))) # 어짜피 정렬된 상태니까 합쳐서 출력
        
    else:
        print(-1) # -1 출력해서 종료