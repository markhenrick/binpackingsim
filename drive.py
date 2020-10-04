class Drive:
    def __init__(self, size):
        self._size = size
        self._graph = [ size ]
    
    def __str__(self):
        return f"Drive(size={self.size()}, graph={self.graph()})"
    
    def graph(self):
        return self._graph
    
    def size(self):
        return self._size
    
    def free(self):
        return self._graph[-1]
    
    def usage_absolute(self):
        return self.size() - self.free()
    
    def usage_relative(self):
        return self.usage_absolute() / self.size()

    def tick(self):
        self._graph.append(self.free())
    
    def store(self, file_size):
        assert file_size <= self.free()
        self._graph[-1] -= file_size