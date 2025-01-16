"""

[1차] 뉴스 클러스터링

자카드 유사도 구하기
1.  FRANCE -> FR, RA, AN, NC, CE
    FRENCH -> FR, RE, EN, NC, CH
2. 교집합 : FR, NC
3. 합집합 : FR, RA, AN, NC, CE, RE, EN, CH
4. 유사도 : 2/8 = 0.25

대소문자 차이는 무시. 알파벳이 아닌 문자가 들어가면 버림.
합집합의 크기가 0이면 자카드 값을 1로 정의.
반환시 65536를 곱하고 정수부만 출력.


"""

from collections import Counter as cnter


def solution(str1, str2):
    Cnter1 = cnter(
        str1[i : i + 2].lower()
        for i in range(len(str1) - 1)
        if str1[i : i + 2].isalpha()
    )
    Cnter2 = cnter(
        str2[i : i + 2].lower()
        for i in range(len(str2) - 1)
        if str2[i : i + 2].isalpha()
    )

    OrLen = sum((Cnter1 | Cnter2).values())
    AndLen = sum((Cnter1 & Cnter2).values())

    if OrLen == 0:
        return 65536

    return AndLen * 65536 // OrLen
