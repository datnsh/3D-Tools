from typing import Optional, Callable
class ValidationError():
    def __init__(self,message:str, can_fix: bool, fix_func:Optional[Callable] = None, data: dict | None = None,type = None):
        self.type = type
        self.message = message
        self.can_fix = False
        self.fix_func = fix_func
        self.data = data
