#파일을 열 때 경로를 정확하게 작성할것
#split을 하려변 공백 문자여선 안됨!
# 문제가 일어날 것을 방지하는 코드 = Guardian Line

han = open('D:\\coding\\pythonStudy03\\mbox-short.txt', 'r')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    wds = line.split()
    #print('Words:', wds)

    #Guardian 1
    #if len(wds) < 3:
    #    continue

    #Guardian in a compound statement
    #Guardian comes before check code : 앞에 오는 문장이 오류를 막아야할것
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])