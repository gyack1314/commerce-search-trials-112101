"""资料格式与引用的完整性检查，不验证尚未存在的业务功能。"""
import unittest,json
from pathlib import Path
from materials import read_packages

class MaterialTests(unittest.TestCase):
    def test_input_packages(self):
        packages=read_packages()
        self.assertEqual(len(packages),2)
        tables={}
        for name,p in packages:
            self.assertTrue(p["synthetic"])
            for table,rows in p["tables"].items():
                self.assertIsInstance(rows,list)
                self.assertEqual(len({r["id"] for r in rows}),len(rows),(name,table))
                tables.setdefault(table,[]).extend(rows)
        contract=json.loads((Path(__file__).parents[1]/"input-schema.json").read_text(encoding="utf-8"))
        for table,field,target,key in contract["references"]:
            values={r[key] for r in tables[target]}
            for r in tables[table]:
                self.assertIn(r[field],values,(table,field,r["id"]))

    def test_updates_are_separate_facts(self):
        packages=dict(read_packages())
        self.assertTrue(packages["updates.json"]["tables"])
        self.assertTrue(any(packages["history.json"]["tables"].values()))

if __name__=="__main__":unittest.main()
