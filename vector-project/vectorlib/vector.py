class Vector:
    def __init__ (self, values:list[float]):
        if len(values) == 0:
            raise ValueError("Vector must be not empty")        
        self.values=list(values)

    def dimension(self)->int:
        return len(self.values)
        
    
        