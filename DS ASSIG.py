class ArrayQueue:
    
    DEFAULT_CAPACITY = 10          

    def __init__(self):
    
        self._info = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._capacity = 0
        self._first = 0
        self._end = 0

    def __len__(self):
        
        return self._capacity

    def is_empty(self):
        
        return self._capacity == 0

    def first(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._info[self._first]
    

    def Start(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._info[self._first]
        self._info[self._first] = None        
        self._first = (self._first + 1) % len(self._info)
        self._capacity -= 1
        self._end = (self._first + self._capacity - 1) % len(self._info)
        return answer
    
    def End(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._first + self._capacity - 1) % len(self._info)
        answer = self._info[back]
        self._info[back] = None         
        self._first = self._first
        self._capacity -= 1
        self._end = (self._first + self._capacity - 1) % len(self._info)
        return answer

    def end(self, e):
        
        if self._capacity == len(self._info):
            self._resize(2 * len(self.data))     
        avail = (self._first + self._capacity) % len(self._info)
        self._info[avail] = e
        self._capacity += 1
        self._end = (self._first + self._capacity - 1) % len(self._info)
        
    def start(self, e):
        
        if self._capacity == len(self._info):
            self._resize(2 * len(self._info))     
        self._first = (self._first - 1) % len(self._info)
        avail = (self._first + self._capacity) % len(self._info)
        self._info[self._first] = e
        self._capacity += 1
        self._end = (self._first + self._capacity - 1) % len(self._info)

    def sizeagain(self, cap):                  
        
        old = self._info                       
        self._info = [None] * cap              
        walk = self._first
        for k in range(self._capacity):            
            self._info[k] = old[walk]            
            walk = (1 + walk) % len(old)         
        self._first = 0                          
        self._end = (self._first + self._capacity - 1) % len(self._info)
        
queue = ArrayQueue()
queue.end(1)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue._info
queue.end(2)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue._info
queue.Start()
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.end(3)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.end(4)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.Start()
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.start(5)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.End()
print(f"starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
queue.end(6)
print(f"Starting Element: {queue._info[queue._first]}, Ending Element: {queue._info[queue._end]}")
