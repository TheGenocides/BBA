from typing import Dict, Any

class ResponseObject:
    def __init__(self, data: Dict[str, Any]):
        self.payload = data
        for k, v in data.items():
            setattr(self, k, v)