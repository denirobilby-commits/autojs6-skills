---
title: "控件集合 (UiObjectCollection)"
version: "6.6.4"
source_html: "raw/uiObjectCollectionType.html"
---

# 控件集合 (UiObjectCollection) {#uiobjectcollectiontype_uiobjectcollection}

UiObjectCollection 代表 控件节点 (UiObject) (uiObjectType.html) 的对象集合.

UiObjectCollection

## [@] UiObjectCollection {#uiobjectcollectiontype_uiobjectcollection_1}

**`Global`**

AutoJs6 中几乎所有 UiObjectCollection 实例均已借助 Rhino 引擎将其包装为了 NativeArray 类型.
因此 JavaScript 的 Array 原型方法在 UiObjectCollection 实例上可以直接使用:

```js
let wc = contentMatch(/.+/).find();
wc.toArray().forEach(w => console.log(w.content()));
wc.forEach(w => console.log(w.content())); /* 效果同上. */

/* 包装后的对象 "是" 一个 JavaScript 数组. */
console.log(Array.isArray(wc)); // true

/* Array 的原型方法 slice. */
console.log(typeof wc.slice); // 'function'
console.log(wc.slice === Array.prototype.slice); // true

/* UiObjectCollection "类" 的实例方法依然全部可用 (如 size, click, each 等). */
console.log(typeof wc.size); // 'function'
console.log(typeof wc.click); // 'function'
console.log(typeof wc.each); // 'function'
```

经过包装的 UiObjectCollection 将不能通过 instanceof 判断其类型, 但仍可通过 getClass 方法判断:

```js
let wc = contentMatch(/.+/).find();
console.log(wc instanceof UiObjectCollection); // false
console.log(wc.getClass() === UiObjectCollection); // true
```

除上述 find 方法, children, untilFind, findOf 以及附带集合类结果筛选器的 pickup, 返回的也都是一个经过包装的 UiObjectCollection:

```js
let s = contentMatch(/.+/);
let w = pickup(s);
let wcList = [
    s.find(),
    s.untilFind(),
    s.findOf(w && w.compass('p2') || pickup()),
    pickup(s, '{}'),
];
console.log(wcList.every(o => o.getClass() === UiObjectCollection)); // true
```

当 pickup 使用 children 等作为结果筛选器时, 返回的是不经过包装的 UiObjectCollection, 因此需要使用一次 toArray 方法才能使用 JavaScript 的数组相关方法:

```js
let wc = pickup(/.+/, 'p', 'children');
/* 需使用 toArray 进行一次转换. */
wc.toArray().forEach(w => console.log(w.content()));

/* 直接使用 children 方法则不需要 toArray 转换. */
pickup(/.+/, 'p').children().forEach( /* ... */ );
```

UiObjectCollection 可能为空集合:

```js
/* 空集合. */
let wc = contentMatch(/[^\s\S]/).find();

console.log(wc.length); // 0

/* 即使是空集合, 依然是 UiObjectCollection 类型. */
console.log(wc === null); // false
console.log(wc.getClass() === UiObjectCollection); // true
```

集合的遍历即可用 UiObjectCollection 的实例方法 (如 each), 或使用 JavaScript 的数组遍历方法 (如 forEach), 或使用 [ for / for...in (不推荐) / for...of ] 循环:

```js
/**
 * @type {UiObjectCollection | Array<UiObject>}
 */
let wc = pickup(/.+/, 'wc');

wc.each(w => console.log(detect(w, 'txt')));

wc.forEach(w => console.log(detect(w, 'txt')));

for (let i = 0; i < wc.length; i += 1) {
    console.log(detect(wc[i], 'txt'));
}

for (let i in wc) {
    if (wc.hasOwnProperty(i) && /^\d+$/.test(i)) {
        console.log(detect(wc[i], 'txt'));
    }
}

for (let w of wc) {
    console.log(detect(w, 'txt'));
}
```

控件集合支持 控件行为 (UiObject Action) (uiObjectActionsType.html).
如 [ click / longClick / imeEnter / setText / focus ] 等.

performAction 源码摘要:

```kotlin
/* Updated as of Nov 2, 2022. */

override fun performAction(action: Int, vararg arguments: ActionArgument): Boolean {
    var success = true
    nodes.filterNotNull().forEach { node ->
        when (arguments.isEmpty()) {
            true -> node.performAction(action)
            else -> node.performAction(action, *arguments)
        }.also { success = success and it }
    }
    return success
}
```

由源码摘要可知, 控件集合执行控件行为, 相当于使集合中所有控件依次执行一次控件行为:

```js
let wc = contentMatch(/[^\s\S]/).find();

/* 对控件集合执行 click 控件行为. */
wc.click();

/* 相当于对集合中每个控件元素执行控件行为. */
wc.forEach(w => {
    if (w !== null) {
        w.click();
    }
});
```

执行控件行为后, 返回结果是 boolean (dataTypes.html#datatypes_boolean) 类型, 表示集合中所有控件在执行行为过程中未出现失败或异常.

常见相关方法或属性:

- UiObject#find (uiObjectType.html#uiobjecttype_m_find)
- UiObject#children (uiObjectType.html#uiobjecttype_m_children)
- UiSelector#find (uiSelectorType.html#uiselectortype_m_find)
- UiSelector#untilFind (uiSelectorType.html#uiselectortype_m_untilfind)
- UiSelector.pickup (uiSelectorType.html#uiselectortype_m_pickup)

## [m#] isEmpty {#uiobjectcollectiontype_m_isempty}

### isEmpty() {#uiobjectcollectiontype_isempty}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回集合是否为空.

## [m#] isNotEmpty {#uiobjectcollectiontype_m_isnotempty}

### isNotEmpty() {#uiobjectcollectiontype_isnotempty}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回集合是否非空.

## [m#] empty {#uiobjectcollectiontype_m_empty}

### empty() {#uiobjectcollectiontype_empty}

**`DEPRECATED`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回集合是否为空.

已弃用, 建议使用 isEmpty 替代.

## [m#] nonEmpty {#uiobjectcollectiontype_m_nonempty}

### nonEmpty() {#uiobjectcollectiontype_nonempty}

**`DEPRECATED`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回集合是否非空.

已弃用, 建议使用 isNotEmpty 替代.

## [m#] toArray {#uiobjectcollectiontype_m_toarray}

### toArray() {#uiobjectcollectiontype_toarray}

- **returns** { JavaArray (dataTypes.html#datatypes_javaarray)<UiObject (uiObjectType.html)> }

转换集合为 Java 数组 (dataTypes.html#datatypes_javaarray).

## [m#] toList {#uiobjectcollectiontype_m_tolist}

### toList() {#uiobjectcollectiontype_tolist}

**`6.2.0`**

- **returns** { JavaArrayList (dataTypes.html#datatypes_javaarraylist)<UiObject (uiObjectType.html)> }

转换集合为 Java 数组列表 (dataTypes.html#datatypes_javaarraylist).

## [m#] get {#uiobjectcollectiontype_m_get}

### get(i) {#uiobjectcollectiontype_get_i}

**`DEPRECATED`**

- **returns** { UiObject (uiObjectType.html) }

按索引获取集合中的 UiObject 元素.

已弃用, 建议使用数组下标形式访问元素.

```js
let wc = pickup(/.+/, '{}');
if (wc.length >= 2) {
    console.log(wc.get(2) instanceof UiObject); // true
    console.log(wc[2] instanceof UiObject); // true
}
```

## [m#] size {#uiobjectcollectiontype_m_size}

### size() {#uiobjectcollectiontype_size}

**`DEPRECATED`**

- **returns** { UiObject (uiObjectType.html) }

返回集合大小.

已弃用, 建议使用 length 属性.

```js
let wc = pickup(/.+/, '{}');
console.log(wc.size()); // e.g. 23
console.log(wc.length); // e.g. 23
```

## [m#] each {#uiobjectcollectiontype_m_each}

### each(consumer) {#uiobjectcollectiontype_each_consumer}

**`DEPRECATED`**

- **consumer** { ( (dataTypes.html#datatypes_function)w: UiObject (uiObjectType.html)) (dataTypes.html#datatypes_function) => (dataTypes.html#datatypes_function) void (dataTypes.html#datatypes_void) } - 消费者
- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

对集合中每个元素执行一次消费.

已弃用, 建议使用 forEach (https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).

```js
let wc = pickup(/.+/, '{}');
wc.each(w => console.log(w.content()));
wc.forEach(w => console.log(w.content()));
```

## [m#] find {#uiobjectcollectiontype_m_find}

### find(selector) {#uiobjectcollectiontype_find_selector}

**`A11Y`**

- **selector** { UiSelector (uiSelectorType.html) } - 选择器
- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

筛选新的控件集合.

以集合中每一个元素为根节点, 依次按选择器筛选出所有满足条件的后代节点加入新集合, 将此新集合作为返回结果.

```js
/* 例如此集合中共有 3 个控件. */
let wc = pickup(/.+/);
console.log(wc.length); // 3

/* 3 个控件作为根节点, 其所有的子孙节点分别有 10, 50, 200 个. */
console.log(wc.map(w => w.find().length)); // [ 10, 50, 200 ]

/* 其中 clickable 为 true 的控件分别有 2, 3, 4 个. */
console.log(wc.map(w => w.find().filter(c => c.clickable()).length)); // [ 2, 3, 4 ]

/* 因此 wc.find(clickable(true)) 应返回 2 + 3 + 4 个. */
console.log(wc.find(clickable(true)).length); // 9
```

## [m#] findOne {#uiobjectcollectiontype_m_findone}

### findOne(selector) {#uiobjectcollectiontype_findone_selector}

**`A11Y`**

- **selector** { UiSelector (uiSelectorType.html) } - 选择器
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

筛选一个控件.

以集合中每一个元素为根节点, 遍历其所有后代节点, 当满足选择器的筛选条件时, 返回此控件并停止筛选.
无满足筛选条件的控件时返回 null.

```js
let wc = pickup(/.+/);
console.log(wc.findOne(clickable(true))); /* 返回一个可点击控件或 null. */
```

## [m#] performAction {#uiobjectcollectiontype_m_performaction}

用于执行控件集合的行为.

集合中所有控件将全部执行指定的行为.

### performAction(action, ...arguments) {#uiobjectcollectiontype_performaction_action_arguments}

**`A11Y`**

- **action** { number (dataTypes.html#datatypes_number) } - 行为的唯一标志符 (Action ID)
- **arguments** { ... (documentation.html#documentation_可变参数)ActionArgument (uiObjectActionsType.html#uiobjectactionstype_i_actionargument)[] (documentation.html#documentation_可变参数) } - 行为参数, 用于给行为传递参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回行为是否全部执行成功.

注: 即使在执行过程中, 某一个控件执行失败, 后续控件依旧继续执行行为, 而非立即终止.

参阅: UiObjectActions (uiObjectActionsType.html) 章节.

## [m#] click {#uiobjectcollectiontype_m_click}

### click() {#uiobjectcollectiontype_click}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 点击 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_click).

## [m#] longClick {#uiobjectcollectiontype_m_longclick}

### longClick() {#uiobjectcollectiontype_longclick}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 长按 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_longclick).

## [m#] accessibilityFocus {#uiobjectcollectiontype_m_accessibilityfocus}

### accessibilityFocus() {#uiobjectcollectiontype_accessibilityfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 获取无障碍焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_accessibilityfocus).

## [m#] clearAccessibilityFocus {#uiobjectcollectiontype_m_clearaccessibilityfocus}

### clearAccessibilityFocus() {#uiobjectcollectiontype_clearaccessibilityfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 清除无障碍焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearaccessibilityfocus).

## [m#] focus {#uiobjectcollectiontype_m_focus}

### focus() {#uiobjectcollectiontype_focus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 获取焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_focus).

## [m#] clearFocus {#uiobjectcollectiontype_m_clearfocus}

### clearFocus() {#uiobjectcollectiontype_clearfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 清除焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearfocus).

## [m#] dragStart {#uiobjectcollectiontype_m_dragstart}

### dragStart() {#uiobjectcollectiontype_dragstart}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 拖放开始 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragstart).

## [m#] dragDrop {#uiobjectcollectiontype_m_dragdrop}

### dragDrop() {#uiobjectcollectiontype_dragdrop}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 拖放放下 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragdrop).

## [m#] dragCancel {#uiobjectcollectiontype_m_dragcancel}

### dragCancel() {#uiobjectcollectiontype_dragcancel}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 拖放取消 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragcancel).

## [m#] imeEnter {#uiobjectcollectiontype_m_imeenter}

### imeEnter() {#uiobjectcollectiontype_imeenter}

**`6.2.0`** **`A11Y`** **`API>=30`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 输入法 ENTER 键 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_imeenter).

## [m#] moveWindow {#uiobjectcollectiontype_m_movewindow}

### moveWindow(x, y) {#uiobjectcollectiontype_movewindow_x_y}

**`6.2.0`** **`A11Y`** **`API>=26`**

- **x** { number (dataTypes.html#datatypes_number) } - X 坐标
- **y** { number (dataTypes.html#datatypes_number) } - Y 坐标
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 移动窗口到新位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_movewindow).

## [m#] nextAtMovementGranularity {#uiobjectcollectiontype_m_nextatmovementgranularity}

### nextAtMovementGranularity(granularity, isExtendSelection) {#uiobjectcollectiontype_nextatmovementgranularity_granularity_isextendselection}

**`6.2.0`** **`A11Y`**

- **granularity** { number (dataTypes.html#datatypes_number) } - 粒度
- **isExtendSelection** { boolean (dataTypes.html#datatypes_boolean) } - 是否扩展选则文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 按粒度移至下一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_nextatmovementgranularity).

## [m#] nextHtmlElement {#uiobjectcollectiontype_m_nexthtmlelement}

### nextHtmlElement(element) {#uiobjectcollectiontype_nexthtmlelement_element}

**`6.2.0`** **`A11Y`**

- **element** { string (dataTypes.html#datatypes_string) } - 元素名称
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 按元素移至下一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_nexthtmlelement).

## [m#] pageLeft {#uiobjectcollectiontype_m_pageleft}

### pageLeft() {#uiobjectcollectiontype_pageleft}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗左移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageleft).

## [m#] pageUp {#uiobjectcollectiontype_m_pageup}

### pageUp() {#uiobjectcollectiontype_pageup}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗上移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageup).

## [m#] pageRight {#uiobjectcollectiontype_m_pageright}

### pageRight() {#uiobjectcollectiontype_pageright}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗右移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageright).

## [m#] pageDown {#uiobjectcollectiontype_m_pagedown}

### pageDown() {#uiobjectcollectiontype_pagedown}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗下移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pagedown).

## [m#] pressAndHold {#uiobjectcollectiontype_m_pressandhold}

### pressAndHold() {#uiobjectcollectiontype_pressandhold}

**`6.2.0`** **`A11Y`** **`API>=30`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 按住 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pressandhold).

## [m#] previousAtMovementGranularity {#uiobjectcollectiontype_m_previousatmovementgranularity}

### previousAtMovementGranularity(granularity, isExtendSelection) {#uiobjectcollectiontype_previousatmovementgranularity_granularity_isextendselection}

**`6.2.0`** **`A11Y`**

- **granularity** { number (dataTypes.html#datatypes_number) } - 粒度
- **isExtendSelection** { boolean (dataTypes.html#datatypes_boolean) } - 是否扩展选则文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 按粒度移至上一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_previousatmovementgranularity).

## [m#] previousHtmlElement {#uiobjectcollectiontype_m_previoushtmlelement}

### previousHtmlElement(element) {#uiobjectcollectiontype_previoushtmlelement_element}

**`6.2.0`** **`A11Y`**

- **element** { string (dataTypes.html#datatypes_string) } - 元素名称
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 按元素移至上一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_previoushtmlelement).

## [m#] showTextSuggestions {#uiobjectcollectiontype_m_showtextsuggestions}

### showTextSuggestions() {#uiobjectcollectiontype_showtextsuggestions}

**`6.2.0`** **`A11Y`** **`API>=33`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 显示文本建议 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_showtextsuggestions).

## [m#] showTooltip {#uiobjectcollectiontype_m_showtooltip}

### showTooltip() {#uiobjectcollectiontype_showtooltip}

**`6.2.0`** **`A11Y`** **`API>=28`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 显示工具提示信息 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_showtooltip).

## [m#] hideTooltip {#uiobjectcollectiontype_m_hidetooltip}

### hideTooltip() {#uiobjectcollectiontype_hidetooltip}

**`6.2.0`** **`A11Y`** **`API>=28`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 隐藏工具提示信息 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_hidetooltip).

## [m#] show {#uiobjectcollectiontype_m_show}

### show() {#uiobjectcollectiontype_show}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 显示在视窗内 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_show).

## [m#] dismiss {#uiobjectcollectiontype_m_dismiss}

### dismiss() {#uiobjectcollectiontype_dismiss}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 消隐 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dismiss).

## [m#] copy {#uiobjectcollectiontype_m_copy}

### copy() {#uiobjectcollectiontype_copy}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 复制文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_copy).

## [m#] cut {#uiobjectcollectiontype_m_cut}

### cut() {#uiobjectcollectiontype_cut}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 剪切文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_cut).

## [m#] paste {#uiobjectcollectiontype_m_paste}

### paste() {#uiobjectcollectiontype_paste}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 粘贴文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_paste).

## [m#] select {#uiobjectcollectiontype_m_select}

### select() {#uiobjectcollectiontype_select}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 选中 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_select).

## [m#] expand {#uiobjectcollectiontype_m_expand}

### expand() {#uiobjectcollectiontype_expand}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 展开 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_expand).

## [m#] collapse {#uiobjectcollectiontype_m_collapse}

### collapse() {#uiobjectcollectiontype_collapse}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 折叠 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_collapse).

## [m#] scrollLeft {#uiobjectcollectiontype_m_scrollleft}

### scrollLeft() {#uiobjectcollectiontype_scrollleft}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗左移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollleft).

## [m#] scrollUp {#uiobjectcollectiontype_m_scrollup}

### scrollUp() {#uiobjectcollectiontype_scrollup}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗上移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollup).

## [m#] scrollRight {#uiobjectcollectiontype_m_scrollright}

### scrollRight() {#uiobjectcollectiontype_scrollright}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗右移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollright).

## [m#] scrollDown {#uiobjectcollectiontype_m_scrolldown}

### scrollDown() {#uiobjectcollectiontype_scrolldown}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗下移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrolldown).

## [m#] scrollForward {#uiobjectcollectiontype_m_scrollforward}

### scrollForward() {#uiobjectcollectiontype_scrollforward}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗前移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollforward).

## [m#] scrollBackward {#uiobjectcollectiontype_m_scrollbackward}

### scrollBackward() {#uiobjectcollectiontype_scrollbackward}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 使视窗后移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollbackward).

## [m#] scrollTo {#uiobjectcollectiontype_m_scrollto}

### scrollTo(row, column) {#uiobjectcollectiontype_scrollto_row_column}

**`A11Y`**

- **row** { number (dataTypes.html#datatypes_number) } - 行序数
- **column** { number (dataTypes.html#datatypes_number) } - 列序数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 将指定位置滚动至视窗内 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollto).

## [m#] contextClick {#uiobjectcollectiontype_m_contextclick}

### contextClick() {#uiobjectcollectiontype_contextclick}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 上下文点击 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_contextclick).

## [m#] setText {#uiobjectcollectiontype_m_settext}

### setText(text) {#uiobjectcollectiontype_settext_text}

**`A11Y`**

- **text** { string (dataTypes.html#datatypes_string) } - 文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 设置文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_settext).

## [m#] setSelection {#uiobjectcollectiontype_m_setselection}

### setSelection(start, end) {#uiobjectcollectiontype_setselection_start_end}

**`A11Y`**

- **start** { number (dataTypes.html#datatypes_number) } - 开始位置
- **end** { number (dataTypes.html#datatypes_number) } - 结束位置
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 选择文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_setselection).

## [m#] clearSelection {#uiobjectcollectiontype_m_clearselection}

### clearSelection() {#uiobjectcollectiontype_clearselection}

**`6.2.0`** **`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 取消选择文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearselection).

## [m#] setProgress {#uiobjectcollectiontype_m_setprogress}

### setProgress(progress) {#uiobjectcollectiontype_setprogress_progress}

**`A11Y`**

- **progress** { number (dataTypes.html#datatypes_number) } - 进度值
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已全部执行且执行过程中无异常

控件集合执行 [ 设置进度值 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_setprogress).

## [m] of {#uiobjectcollectiontype_m_of}

### of(list) {#uiobjectcollectiontype_of_list}

- **list** { UiSelector (uiSelectorType.html)[] (dataTypes.html#datatypes_array) } - 控件数组
- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

将控件数组转换为 UiObjectCollection (uiObjectCollectionType.html).

```js
let wA = pickup(/hello.+/);
let wB = pickup({ clickable: true });

let wc = UiObjectCollection.of([ wA, wB ]);

/* 对 UiObjectCollection 进行操作. */
wc.click();
```
