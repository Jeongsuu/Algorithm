# Stack & Queue with Swift


## Stack
---
```swift

struct Stack<T> {
    
    var stack = [T]()
    
    var isEmpty: Bool {
        return self.stack.isEmpty
    }
    
    var top: T? {
        return self.stack.last
    }
    
    mutating func push(_ item: T) {
        self.stack.append(item)
    }
    
    mutating func pop() -> T? {
        guard self.isEmpty == false else { return nil }
        return self.stack.popLast()
    }
}

```

- LIFO, `Array`를 이용해 구현하였다.

- 다양한 자료형을 수용할 수 있도록 `Generic`을 이용하여 유연성을 더한다.

- `push` , `pop` 메서드의 경우 구조체 내부에서 데이터를 수정하기 때문에 `mutating` 키워드를 통해 정의한다.

<br>

## Queue
---

```swift
struct Queue<T> {
    
    var queue = [T]()
    
    var isEmpty: Bool {
        return self.queue.isEmpty
    }
    
    var front: T? {
        return self.queue.first
    }
    
    var rear: T? {
        return self.queue.last
    }
    
    mutating func enqueue(_ item: T) {
        self.queue.append(item)
    }
    
    mutating func dequeue() -> T? {
        guard self.isEmpty == false else { return nil }
        return self.queue.removeFirst()
    }
}
```

- FIFO, `Array`를 이용해 구현하였다.

- 큐 또한 스택과 동일하게 다양한 자료형을 수용할 수 있도록 `Generic`을 이용하여 정의한다.

- `enqueue`, `dequeue` 메서드의 경우 구조체 내부에서 데이터를 수정하기 떄문에 `mutating` 키워드를 통해 정의한다.

