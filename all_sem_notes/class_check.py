class returner():
    def __init__(self):
        self.x = 5
        
    def d(self, s):
        self.x = s
        
    def prnt(self):
        print(self.x)
    
    def __setitem__(self, key, value):
        if key == "x":
            self.x = value
        else:
            raise KeyError(f"Key '{key}' not found")

exmpl = returner()
exmpl["x"] = 3
exmpl.prnt()