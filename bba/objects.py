from typing import Dict, Any

class CalcObject:
    def __init__(self, data: Dict[str, Any]):
        self.payload = data
        self.result: str = data.get['result']
        self.error: bool = data.get['error']