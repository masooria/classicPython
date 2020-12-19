from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self, name: str) -> None:
        self._container: List[T] = []
        self.name = name

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def first(self) -> str:
        return str(self._container[0])

    def last(self) -> str:
        return str(self._container[-1])

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 7
tower_a: Stack[int] = Stack("a")
tower_b: Stack[int] = Stack("b")
tower_c: Stack[int] = Stack("c")
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int):
    if n == 1:
        print("move " + begin.last() + " from " + begin.name + " to " + end.name)
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


hanoi(tower_a, tower_b, tower_c, num_discs)
print(tower_a)
print(tower_b)
print(tower_c)