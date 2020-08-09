# Explaination

### A LinkedList

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
```

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
    A:::nodeClass -->|next|B
    B:::nodeClass -->|next|C
    C:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    
```

### Stack (LIFO) - last in first out

```python
def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            
def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped
```

##### push A

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### push B

```mermaid
graph LR
		id1(head):::otherClass-->B
		%%id3([current]):::pointerClass-->A
    B:::nodeClass -->|next|A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### push C

```mermaid
graph LR
		id1(head):::otherClass-->C
		%%id3([current]):::pointerClass-->A
		C:::nodeClass -->|next|B
    B:::nodeClass -->|next|A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### pop() -> C

```mermaid
graph LR
		id1(head):::otherClass-->B
		%%id3([current]):::pointerClass-->A
		%%C:::nodeClass -->|next|B
    B:::nodeClass -->|next|A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### pop() -> B

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
		%%C:::nodeClass -->|next|B
    %%B:::nodeClass -->|next|A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

### Queue(FIFO) - first in first out

```python
def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped
```

##### push A

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### push B

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
    A:::nodeClass -->|next|B
    B:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### push C

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
		A:::nodeClass -->|next|B
    B:::nodeClass -->|next|C
    C:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### pop() -> A

```mermaid
graph LR
		id1(head):::otherClass-->B
		%%id3([current]):::pointerClass-->A
    B:::nodeClass -->|next|C
    C:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

##### pop() -> B

```mermaid
graph LR
		id1(head):::otherClass-->A
		%%id3([current]):::pointerClass-->A
    A:::nodeClass -->|next|id2(null):::nullClass
    
    classDef pointerClass fill:#f5f2c4, stroke:None;
    classDef nodeClass fill:#bcf5ef, stroke:None;
    classDef otherClass fill:#fccaae,stroke:#f66,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
    classDef nullClass fill: #c9d6d6,stroke:#c9d6d6,stroke-width:1px,color:#fff,stroke-dasharray: 5, 5
```

