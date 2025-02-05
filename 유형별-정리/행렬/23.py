"""행렬의 곱셈

행렬곱 하는법

C의 i행 j열 = A의 i행 * B의 j열

만 기억하면 된다.

행열 순서하고 배열 인덱스 순서도 동일해서

C[i][j] = A[i][:] *+ B[:][j] 인데 이걸 코드로 잘 옮겨보자.

tip: B^T는 zip(*B)로 구할 수 있다.

즉,

C[i][j] = A[i][:] *+ zip(*B)[j][:]
C[i][j] = sum(a*b for a, b in zip(A[i], zip(*B)[j]))

로 응용가능.
아니면

numpy.dot(A, B).tolist() 도 가능하다. 근데 이건 많이 안쓸거 같아서 패스.

아래 해답에선 그냥 정석대로 했다.

"""


def solution(arr1, arr2):
    N = len(arr1)
    R = len(arr2)
    M = len(arr2[0])

    Mat = [[0] * M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            Mat[n][m] = sum(arr1[n][r] * arr2[r][m] for r in range(R))

    return Mat
