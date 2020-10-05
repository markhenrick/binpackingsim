class Drive:
    def __init__(self, size):
        assert size > 0
        self._size = size
        self._graph = [ 0 ]
    
    def __str__(self):
        return f"Drive(size={self.size()}, graph={self.graph_absolute_usage()})"
    
    def graph_absolute_usage(self):
        return self._graph
    
    def graph_relative_usage(self):
        return list(map(lambda x: x / self.size(), self.graph_absolute_usage()))
    
    def graph_absolute_free(self):
        return list(map(lambda x: self.size() - x, self.graph_absolute_usage()))
    
    def size(self):
        return self._size
    
    def free(self):
        return self.size() - self.usage_absolute()
    
    def usage_absolute(self):
        return self._graph[-1]
    
    def usage_relative(self):
        return self.usage_absolute() / self.size()

    def tick(self):
        self._graph.append(self._graph[-1])
    
    def store(self, file_size):
        assert file_size <= self.free()
        self._graph[-1] += file_size