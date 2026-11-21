"""读取合成业务资料并列出资料量，不作业务判断。"""
from pathlib import Path
import json

def read_packages(directory=None):
    root = Path(directory) if directory else Path(__file__).parent / "data"
    result = []
    for path in sorted(root.glob("*.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        if value.get("synthetic") is not True or not isinstance(value.get("tables"), dict):
            raise ValueError("资料包格式无效：" + path.name)
        result.append((path.name, value))
    if not result:
        raise ValueError("没有可读取的资料包")
    return result

if __name__ == "__main__":
    print(json.dumps({name: {table: len(rows) for table, rows in package["tables"].items()}
                      for name, package in read_packages()}, ensure_ascii=False, indent=2))
