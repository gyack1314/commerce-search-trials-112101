# 资料约定

session_id为一次匿名购物会话，query_index仅在会话内排序，reformulation_of引用前一搜索；constraints含required和forbidden属性，展示的offer_id只证明展示，不证明有货。availability按offer及半开时间区间给出可买状态；unknown不可当作缺货。judgements为两个查询间same_need、different_need或undecided的人工意见，recorded_at是可获知时间。采购报价covers_attributes限定可满足属性，capacity_pool是共用生产批次，min_order和units_per_slot决定产能占用。trial_assignments提供试销机会的原始分配，订单引用assignment_id，未成交保留零结果；退货观察到mature_at才完整。review_actions只表达人工接受、否决或拆分的事实，不能据此预置聚类输出。承诺采购不得自动撤销；拆分后的新增承诺须把尚在途且实际兼容的数量计入覆盖。

## 文件与时间

所有数据都是本地合成记录，不代表新闻中的企业或交易。history.json为首批事实，updates.json为后续补充资料；后者可引用前者的对象。id标识一条事实；revises引用被更正的事实身份，不表示删除历史。known_at、recorded_at、published_at等字段表示资料可获知时间，occurred_at或effective_at表示实际发生或适用时间，二者不可互换。时间使用带时区的ISO 8601字符串，区间无特别说明均含起点、不含终点。历史分析只能采用指定截点已可得资料；空列表、null、数值零分别保留其含义。合成金额不触及真实账户。

## 数据表

### sessions

字段：id, started_at, known_at, account_id。

### queries

字段：id, session_id, query_index, text, constraints, reformulation_of, shown_offers, clicked_offers, known_at。

### offers

字段：id, name, attributes, ingredients, unit_price。

### availability

字段：id, offer_id, start, end, state, known_at。

### judgements

字段：id, left_query, right_query, decision, recorded_at。

### quotes

字段：id, offer_id, covers_attributes, forbidden_ingredients, capacity_pool, min_order, units_per_slot, unit_cost, delivery_week。

### capacity_pools

字段：id, slots, week。

### trial_assignments

字段：id, session_id, offer_id, assigned_at, probability, can_buy。

### orders

字段：id, assignment_id, quantity, paid_at, return_qty, mature_at, known_at。

### review_actions

字段：id, kind, judgement_id, known_at。

### purchase_commitments

字段：id, quote_id, quantity, state, accepted_at。

input-schema.json列出资料中的字段类型概况和必要外键；同一字段可能存在null值，类型概况不是严格JSON Schema。后续资料可更正事实，但原记录可按其身份回查。

## 补充领域含义

queries的constraints仅为顾客明确选择的筛选条件，空约束不代表所有属性均可接受，搜索文本仍有独立词义。人工same_need只对该对查询提供依据，不预置全体分群；相互冲突的意见须可解释。生产额度slots乘units_per_slot才是包装数量，已在途purchase_commitments按实际兼容商品计入，不可再次当空闲产能。
