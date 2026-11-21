# 无结果搜索需求的商品归并与试销承接

项目资料用于无结果搜索需求的商品归并与试销承接的本地业务研发。当前提供合成记录、字段契约、资料读取工具和完整性检查；资料读取工具只列出数据量，不作分析或办理业务。

## 资料

data/history.json和data/updates.json分开保留原始与后补事实。金额、时间、适用范围及状态含义见[资料约定](docs/input-contract.md)。全部记录由合成过程产生，不含真实个人或商家资料。

## 环境与现有入口

使用Python 3.11。依赖版本固定在requirements.txt，含表格分析、数值与统计库。已有入口为资料读取，业务操作入口尚未建立。

```sh
python -m pip install -r requirements.txt
python materials.py
python -m unittest discover -s tests -v
python -m compileall -q materials.py tests
```

也可在容器内读取资料和检查环境：

```sh
docker build -t search-trials-local .
docker run --rm search-trials-local
docker run --rm search-trials-local python -m unittest discover -s tests -v
```

测试只核查资料格式、记录身份及引用关系，不代表业务分析或办理功能已完成。运行产生的状态与结果建议放在state/和output/，两者不加入版本控制。
