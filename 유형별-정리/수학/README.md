크게 3가지정도인듯

int(실수 + 1) 하고 int(실수) + 1 하고 뭐가 다른가요 -> 똑같음 음수가 아닌 이상
이게 ceil은

```python
int(x if x == int(x) else x+1)
```

이렇게 구현해야해서
그냥 math.ceil 쓰는게 시맨틱하고 더 좋은듯. round도 0.5 더하고 빼고
양수인지 음수인지, 또 실수인지 정수인지 구분해야해서
그냥 그럴바엔 갖다쓰는게 맞습니다.

---

1. 약수 구하기
   for하고 그냥 int(n\*\*0.5) + 1 하면 됨. ceil이 맞긴한데 귀찮잖아. 하나 더 체크해도 문제는 안생김.

2. 가우스합
   쉽게 구현할 수 있으니 패스.

3. 정수
   그냥 짝수 홀수 구분 if문으로 잘 나눠주면 됨.

4. 최소공배수, 최대공약수

gcd -> greatest common divisor 였나 암튼 최대공약수죠 누가봐도

근데 최소공배수가 없음. 프로그래머스에선 python v3.8인가봄. 3.9부터 추가됐다고는 하는데
어떻게 쓰냐면

```python
from math import gcd
from functools import reduce

def lcm(*args):
    return reduce(lambda x, y: x * y // gcd(x, y), args)
```

이렇게 써야함.
생각보다 귀찮죠 최대공약수가.

5. 진수 변환
   기본적으로 n진수 -> 10진수 변환은 지원해줌.

   ```python
   아웃풋 = int(str(인풋), n진수)
   ```

   근데 10진수 -> n진수 변환은 직접 짜야함.
   10진수->2진수 : `bin()`, 10진수->16진수 : `hex()` 가 있긴함. 이외에는 직접 짜야함.

   ```python
   10진수 = 1241
   n진수 = ""
   while 10진수 > 0	:
       10진수, r = divmod(10진수, n)
       n진수 += r

   n진수 = n진수[::-1]
   ```

   이런식으로 짜면 되겠죠
