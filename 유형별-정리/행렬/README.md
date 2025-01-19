flatten 할때 reduce 사용할 때도 있는데
이때 add가 아니라 iadd 써야함.
왜냐면 add 쓰면 새로운 결과값 배열을 하나 만드는거라서 그만큼 오버헤드가 걸림.
iadd를 쓰도록 하자.

---

functools.reduce나 sort의 key, map 등에 이제 함수 전달할때 파이썬은 람다가 가독성이 별로 안좋아서
차라리 operator에서 갖다 쓰는게 가독성이 더 좋을 수 있음.

neg
add
sub
truediv
floordiv
and\_
xor
or\_
setitem : 근데 이 아래 3개는 별로 쓸일이 없을듯
delitem
getitem

itemgetter(index)
attrgetter(key이름)

---

흠..

lambda x: x[1]
itemgetter(1)

솔직히 전자가 더 직관적인거 같은데 이거 왜만든거임
흠....
