def solution(new_id):
    answer1 = ''
    #1
    new_id = new_id.lower()
    # print(new_id)

    #2
    for s in new_id:
        if s.islower() or s.isdigit() or s=='-' or s=='_' or s=='.':
            answer1 += s

    #3
    answer2 = ''
    for i in range(len(answer1)-1):
        if answer1[i] == '.' and answer1[i+1] == answer1[i]:
            continue
        else:
            answer2 += answer1[i]
    answer2 += answer1[-1]


    #4
    if len(answer2) >= 1:
        if answer2[0] == '.':
            if len(answer2) == 1:
                answer2 = ''
            else:
                answer2 = answer2[1:]

    if len(answer2) >= 1:
        if answer2[-1] == '.':
            if len(answer2) == 1:
                answer2 = ''
            else:
                answer2 = answer2[:-1]

    #5
    if answer2 == '':
        answer2 = 'a'

    #6
    if len(answer2) >= 16:
        answer2 = answer2[:15]
        if answer2[-1] == '.':
            answer2 = answer2[:-1]

    #7
    if len(answer2) <= 2:
        t = answer2[-1]
        while len(answer2) != 3:
            answer2 += t


    return answer2


# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
new_id = "123_.def"
print(solution(new_id))

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.