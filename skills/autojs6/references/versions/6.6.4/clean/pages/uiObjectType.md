---
title: "控件节点 (UiObject)"
version: "6.6.4"
source_html: "raw/uiObjectType.html"
---

# 控件节点 (UiObject) {#uiobjecttype_uiobject}

UiObject 通常被称为 [ 控件 / 节点 / 控件节点 ], 可看做是一个通过安卓无障碍服务包装的 AccessibilityNodeInfo (https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo) 对象, 代表一个当前活动窗口中的节点, 通过此节点可收集控件信息或执行控件行为, 进而实现一系列自动化操作.

应用界面通常由控件构成, 如 ImageView (https://developer.android.com/reference/android/widget/ImageView) 构成图像控件, TextView (https://developer.android.com/reference/android/widget/TextView) 构成文本控件. 通过不同的布局可决定不同控件的位置, 如 LinearLayout (线性布局) (https://developer.android.com/reference/android/widget/LinearLayout) 按水平或垂直方式排布及显示控件, AbsListView (列表布局) (https://developer.android.com/reference/android/widget/AbsListView) 按列表方式排布及显示控件. 不同的布局方式形成了 控件层级 (glossaries.html#glossaries_控件层级).

控件拥有特定的属性, 可分为两种类型, 状态型及行为型.
行为型属性可参阅章节 控件节点行为 (UiObjectActions) (uiObjectActionsType.html).
状态型属性访问均被封装为方法调用的形式, 如访问控件的类名, 需使用 `w.className()` 而非 `w.className`.

注: 在 AutoJs6 中, 由 UiObject (uiObjectType.html) 代表一个控件节点, 它继承自 AccessibilityNodeInfoCompat (https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat), 而并非一个 View (https://developer.android.com/reference/android/view/View).

UiObject

## [@] UiObject {#uiobjecttype_uiobject_1}

**`Global`**

如需获取一个 UiObject 对象, 通常使用 选择器 (uiSelectorType.html) 获取.

```js
/* 获取一个包含任意文本的 UiObject 对象. */
let w = pickup(/.+/);

/* 当活动窗口中不存在符合筛选条件的控件时返回 null. */
console.log(w === null);

/* 使用 instanceof 操作符查看对象 w 是否为 UiObject "类" 的实例. */
console.log(w instanceof UiObject);
```

多数 UiObject 的实例方法 (如 parent 和 child 等) 均返回自身类型, 因此可实现链式调用:

```js
let w = pickup('hello');
/* 获取 w 控件的三级父控件的 2 号索引子控件. */
w.parent().parent().parent().child(2);
```

## [m#] parent {#uiobjecttype_m_parent}

### parent(i?) {#uiobjecttype_parent_i}

**`[6.3.3]`** **`A11Y`** **`Overload [1-2]/2`**

- **[ i = `1` ]** { number (dataTypes.html#datatypes_number) } - 相对级数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回其父控件.

当指定级数 `i` 时, 返回其对应级数的父控件.

`i` 为 `0` 时, 返回控件自身,
`i` 为正整数时, 返回第 `i` 级父控件,
`i` 为负数时, 将抛出异常.

```js
let w = pickup(/.+/);
w.parent();
w.parent(1); /* 同上. */
w.compass('p'); /* 同上. */
detect(w, 'p'); /* 同上. */

w.parent().parent().parent();
w.parent(3); /* 同上. */
w.compass('p3'); /* 同上. */
detect(w, 'p3'); /* 同上. */
```

## [m#] child {#uiobjecttype_m_child}

### child(i) {#uiobjecttype_child_i}

**`[6.3.3]`** **`A11Y`**

- **i** { number (dataTypes.html#datatypes_number) } - 索引
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回其索引为 `i` 的子控件.

`i` 为正整数或 `0`, 返回正数索引子控件,
`i` 为负整数, 返回倒数索引子控件,

```js
let w = pickup(/.+/);
w.child(3);
w.compass('c3'); /* 同上. */
detect(w, 'c3'); /* 同上. */

w.child(3).child(1);
w.compass('c3c1'); /* 同上. */
detect(w, 'c3>1'); /* 同上. */

w.child(-1); /* 最后一个子控件. */

w.child(-2); /* 倒数第 2 个子控件. */
w.compass('c-2'); /* 同上. */
detect(w, 'c-2'); /* 同上. */
```

## [m#] firstChild {#uiobjecttype_m_firstchild}

### firstChild() {#uiobjecttype_firstchild}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) }

返回第一个子控件.

相当于 `child(0)`.

## [m#] lastChild {#uiobjecttype_m_lastchild}

### lastChild() {#uiobjecttype_lastchild}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) }

返回最后一个子控件.

相当于 `child(-1)`.

## [m#] childCount {#uiobjecttype_m_childcount}

### childCount() {#uiobjecttype_childcount}

**`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回当前节点的子控件数量.

别名属性或方法:

- `[m#]` getChildCount

## [m#] hasChildren {#uiobjecttype_m_haschildren}

### hasChildren() {#uiobjecttype_haschildren}

**`6.2.0`** **`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回当前节点是否有子节点.

相当于 `childCount() > 0`.

## [m#] children {#uiobjecttype_m_children}

### children() {#uiobjecttype_children}

**`A11Y`**

- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

返回当前节点的子控件集合.

```js
let cc = pickup({ filter: w => w.children().length > 5 }, 'children');

console.log(cc.length); /* e.g. 10 */

cc.forEach((w) => {
    let content = w.content();
    content && console.log(content);
})
```

如需返回当前节点下的所有子孙控件集合, 可使用 UiObject#find().

```js
let w = pickup({ filter: w => w.children().length > 5 });
console.log(w.find().length); /* e.g. 20 */
```

## [m#] sibling {#uiobjecttype_m_sibling}

### sibling(i) {#uiobjecttype_sibling_i}

**`6.3.3`** **`A11Y`**

- **i** { number (dataTypes.html#datatypes_number) } - 索引
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回其索引为 `i` 的兄弟控件.

`i` 为正整数或 `0`, 返回正数索引兄弟控件,
`i` 为负整数, 返回倒数索引兄弟控件,

当 `i` 与 indexInParent() 相同时, 返回其自身.

```js
let w = pickup(/.+/);
w.sibling(0); /* 第 1 (索引为 0) 的兄弟控件. */
w.compass('s0'); /* 同上. */
detect(w, 's0'); /* 同上. */

w.sibling(-2); /* 倒数第 2 个兄弟控件. */
w.compass('s-2'); /* 同上. */
detect(w, 's-2'); /* 同上. */
```

如需获取相邻的兄弟控件, 可使用 offset, 或使用 nextSibling 与 previousSibling.

## [m#] firstSibling {#uiobjecttype_m_firstsibling}

### firstSibling() {#uiobjecttype_firstsibling}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) }

返回第一个兄弟控件 (可能为自身).

相当于 `sibling(0)`.

## [m#] lastSibling {#uiobjecttype_m_lastsibling}

### lastSibling() {#uiobjecttype_lastsibling}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) }

返回最后一个兄弟控件 (可能为自身).

相当于 `sibling(-1)`.

## [m#] offset {#uiobjecttype_m_offset}

### offset(i) {#uiobjecttype_offset_i}

**`6.3.3`** **`A11Y`**

- **i** { number (dataTypes.html#datatypes_number) } - 索引偏移量
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回其索引偏移量为 `i` 的兄弟控件.

`i` 为正整数, 返回后向兄弟控件,
`i` 为负整数, 返回前向兄弟控件,
`i` 为 `0`, 返回当前控件自身.

```js
let w = pickup(/.+/);
w.offset(3);
w.compass('s>3'); /* 同上. */
detect(w, 's>3'); /* 同上. */

w.offset(-2);
w.compass('s<2'); /* 同上. */
detect(w, 's<2'); /* 同上. */
```

如需获取相邻的兄弟控件, 除 offset 外, 还可使用 nextSibling 与 previousSibling.

## [m#] nextSibling {#uiobjecttype_m_nextsibling}

### nextSibling() {#uiobjecttype_nextsibling}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回后一个兄弟控件.

相当于 `offset(1)`.

## [m#] previousSibling {#uiobjecttype_m_previoussibling}

### previousSibling() {#uiobjecttype_previoussibling}

**`6.3.3`** **`A11Y`**

- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

返回前一个兄弟控件.

相当于 `offset(-1)`.

## [m#] siblingCount {#uiobjecttype_m_siblingcount}

### siblingCount() {#uiobjecttype_siblingcount}

**`6.3.3`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回当前节点的兄弟控件总数量 (含自身).

`siblingCount` 返回一个总是大于等于 `1` 的数字.

## [m#] isSingleton {#uiobjecttype_m_issingleton}

### isSingleton() {#uiobjecttype_issingleton}

**`6.3.3`** **`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回当前节点是否为独身节点, 即除自身外没有其他兄弟节点.

相当于 `siblingCount() === 1`.

## [m#] siblings {#uiobjecttype_m_siblings}

### siblings() {#uiobjecttype_siblings}

**`6.3.3`** **`A11Y`**

- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

返回当前节点的兄弟控件集合 (含自身).

## [m#] indexInParent {#uiobjecttype_m_indexinparent}

### indexInParent() {#uiobjecttype_indexinparent}

**`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回当前节点在其父控件的索引值.

```js
/* 例如 p 控件有 3 个子控件 (a, b, c). */

a.indexInParent(); // 0 
p.child(0); /* 对应 a. */

console.log(c.indexInParent()); // 2
p.child(2); /* 对应 c. */
```

方法 `indexInParent` 通常用于访问临近或相对位置的兄弟节点:

```js
/* 例如 p 控件有 3 个子控件 (a, b, c). */

/* c 是 b 的相邻兄弟节点 (相对索引为 1). */
p.child(b.indexInParent() + 1); /* 对应 c. */
b.compass('s>1'); /* 使用罗盘方法, 效果同上. */

/* a 也是 b 的相邻兄弟节点 (相对索引为 -1). */
p.child(b.indexInParent() - 1); /* 对应 a. */
b.compass('s<1'); /* 使用罗盘方法, 效果同上. */

/* a 是 c 的兄弟节点 (相对索引为 -2). */
p.child(c.indexInParent() - 2); /* 对应 a. */
b.compass('s<2'); /* 使用罗盘方法, 效果同上. */
```

有时也需要获取当前节点的父控件在其父控件的索引值:

```js
let p = pickup({ filter: w => w.depth() > 0 && w.parent().indexInParent() > 0 });
console.log(p.parent().indexInParent()); // e.g. 2
```

## [m#] find {#uiobjecttype_m_find}

### find() {#uiobjecttype_find}

**`Overload 1/2`** **`A11Y`**

- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

以当前节点作为根节点, 返回其所有的子孙控件集合.

与 children 方法不同, `w.children()` 返回子控件集合, 而 `w.find()` 返回所有子孙控件集合.

```js
let root = depth(0).findOnce();
console.log(root.find().length); // e.g. 500
console.log(root.children().length); // e.g. 2
```

子孙控件集合中包含根节点本身:

```js
/* 找出一个没有任何子孙控件的节点. */
let w = pickup({ filter: w => w.childCount() === 0 });

/* find() 返回的集合包含其自身, 而非空集合. */
console.log(w.find().length); // 1
```

因此, `N 层级子孙控件集合数量` = `N + 1 层级子孙控件数量总和` + `1`:

```js
let root = depth(0).findOnce();
let sumA = root.find().length;
let sumB = root.children().reduce((sum, c) => sum + c.find().length, 0);
console.log(sumA, sumB); /* sumA 和 sumB 相差 1. */
```

### find(selector) {#uiobjecttype_find_selector}

**`Overload 2/2`** **`A11Y`**

- **selector** { selector (uiSelectorType.html) } - 选择器
- **returns** { UiObjectCollection (uiObjectCollectionType.html) }

以当前节点作为根节点, 返回其所有满足选择器筛选条件的子孙控件集合.

```js
/* 找出 w 控件下所有符合有效内容长度不小于 10 的子孙控件集合. */
console.log(w.find(contentMatch(/\s*.{10,}\s*/)));
```

## [m#] findOne {#uiobjecttype_m_findone}

### findOne(selector) {#uiobjecttype_findone_selector}

**`A11Y`**

- **selector** { selector (uiSelectorType.html) } - 选择器
- **returns** { UiObject (uiObjectType.html) }

以当前节点作为根节点, 在其所有子孙控件中找出一个满足选择器筛选条件的控件.

```js
/* 找出 w 子孙控件中符合有效内容长度不小于 10 的一个控件. */
console.log(w.findOne(contentMatch(/\s*.{10,}\s*/)));
```

## [m#] bounds {#uiobjecttype_m_bounds}

### bounds() {#uiobjecttype_bounds}

**`A11Y`**

- **returns** { AndroidRect (androidRectType.html) }

方法 boundsInScreen 的别名.

返回一个 控件矩形 (Rect) (androidRectType.html), 表示控件在屏幕的相对位置及空间范围.

```js
let bounds = contentMatch(/.+/).findOnce().bounds();
console.log(bounds); // e.g. Rect(0, 48 - 112, 160)
```

别名属性或方法:

- `[m#]` boundsInScreen

## [m#] boundsInScreen {#uiobjecttype_m_boundsinscreen}

### boundsInScreen() {#uiobjecttype_boundsinscreen}

**`A11Y`**

- **returns** { AndroidRect (androidRectType.html) }

返回一个 控件矩形 (Rect) (androidRectType.html), 表示控件在屏幕的相对位置及空间范围.

```js
let bounds = contentMatch(/.+/).findOnce().boundsInScreen();
console.log(bounds); // e.g. Rect(0, 48 - 112, 160)
```

别名属性或方法:

- `[m#]` bounds

## [m#] boundsInParent {#uiobjecttype_m_boundsinparent}

### boundsInParent() {#uiobjecttype_boundsinparent}

**`A11Y`**

**`DEPRECATED`**

- **returns** { AndroidRect (androidRectType.html) }

返回一个 控件矩形 (Rect) (androidRectType.html), 表示控件于其父控件的相对位置及空间范围.

因其父控件实际上是 `View#getParentForAccessibility()` 的结果, 而非此控件的 `viewParent`, 所以得到的结果是不可靠的.

```js
let bounds = contentMatch(/.+/).findOnce().boundsInParent();
console.log(bounds); // e.g. Rect(0, 0 - 112, 112)
```

## [m#] boundsLeft {#uiobjecttype_m_boundsleft}

### boundsLeft() {#uiobjecttype_boundsleft}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形左边界距屏幕左边缘的像素距离.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().left); // e.g. 0
console.log(w.boundsLeft()); // e.g. 0
console.log(w.left()); // e.g. 0
```

## [m#] boundsTop {#uiobjecttype_m_boundstop}

### boundsTop() {#uiobjecttype_boundstop}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形上边界距屏幕上边缘的像素距离.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().top); // e.g. 48
console.log(w.boundsTop()); // e.g. 48
console.log(w.top()); // e.g. 48
```

## [m#] boundsRight {#uiobjecttype_m_boundsright}

### boundsRight() {#uiobjecttype_boundsright}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形右边界距屏幕左边缘的像素距离.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().right); // e.g. 112
console.log(w.right()); // e.g. 112
console.log(w.boundsRight()); // e.g. 112
```

## [m#] boundsBottom {#uiobjecttype_m_boundsbottom}

### boundsBottom() {#uiobjecttype_boundsbottom}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形下边界距屏幕上边缘的像素距离.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().bottom); // e.g. 160
console.log(w.bottom()); // e.g. 160
console.log(w.boundsBottom()); // e.g. 160
```

## [m#] boundsWidth {#uiobjecttype_m_boundswidth}

### boundsWidth() {#uiobjecttype_boundswidth}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的宽度.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().width()); // e.g. 112
console.log(w.boundsWidth()); // e.g. 112
console.log(w.right() - w.left()); // e.g. 112
```

## [m#] boundsHeight {#uiobjecttype_m_boundsheight}

### boundsHeight() {#uiobjecttype_boundsheight}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的高度.

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(w.bounds().height()); // e.g. 112
console.log(w.boundsHeight()); // e.g. 112
console.log(w.bottom() - w.top()); // e.g. 112
```

## [m#] boundsCenterX {#uiobjecttype_m_boundscenterx}

### boundsCenterX() {#uiobjecttype_boundscenterx}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 X 坐标 (中心点距屏幕左边缘的像素距离).

该坐标为整数, 非整数数值将按 **向下取整** 处理, 因此会损失精度.

如需保留精度, 可使用 boundsExactCenterX.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(wA.bounds().centerX()); // e.g. 56
console.log(wA.boundsCenterX()); // e.g. 56

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 20)
console.log(wB.boundsCenterX()); // e.g. 5 (5.5 向下取整得 5)

let wC = pickup(/.+/);
console.log(wC.bounds()); // e.g. Rect(0, 0 - -11, 20)
console.log(wC.boundsCenterX()); // e.g. -6 (-5.5 向下取整得 -6)
```

## [m#] boundsExactCenterX {#uiobjecttype_m_boundsexactcenterx}

### boundsExactCenterX() {#uiobjecttype_boundsexactcenterx}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 X 坐标 (中心点距屏幕左边缘的像素距离).

该坐标将保留精度 (可能为非整数), 如需返回整数结果, 可使用 boundsCenterX.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(wA.bounds().exactCenterX()); // e.g. 56
console.log(wA.boundsExactCenterX()); // e.g. 56

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 20)
console.log(wB.boundsExactCenterX()); // e.g. 5.5

let wC = pickup(/.+/);
console.log(wC.bounds()); // e.g. Rect(0, 0 - -11, 20)
console.log(wC.boundsExactCenterX()); // e.g. -5.5
```

## [m#] boundsCenterY {#uiobjecttype_m_boundscentery}

### boundsCenterY() {#uiobjecttype_boundscentery}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 Y 坐标 (中心点距屏幕上边缘的像素距离).

该坐标为整数, 非整数数值将按 **向下取整** 处理, 因此会损失精度.

如需保留精度, 可使用 boundsExactCenterY.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(wA.bounds().centerY()); // e.g. 104
console.log(wA.boundsCenterY()); // e.g. 104

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 33)
console.log(wB.boundsCenterY()); // e.g. 16 (16.5 向下取整得 16)

let wC = pickup(/.+/);
console.log(wC.bounds()); // e.g. Rect(0, 0 - 11, -33)
console.log(wC.boundsCenterY()); // e.g. -17 (-16.5 向下取整得 -17)
```

## [m#] boundsExactCenterY {#uiobjecttype_m_boundsexactcentery}

### boundsExactCenterY() {#uiobjecttype_boundsexactcentery}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 Y 坐标 (中心点距屏幕上边缘的像素距离).

该坐标将保留精度 (可能为非整数), 如需返回整数结果, 可使用 boundsCenterY.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 48 - 112, 160)
console.log(wA.bounds().exactCenterY()); // e.g. 104
console.log(wA.boundsExactCenterY()); // e.g. 104

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 33)
console.log(wB.boundsExactCenterY()); // e.g. 16.5

let wC = pickup(/.+/);
console.log(wC.bounds()); // e.g. Rect(0, 0 - 11, -33)
console.log(wC.boundsExactCenterY()); // e.g. -16.5
```

## [m#] left {#uiobjecttype_m_left}

### left() {#uiobjecttype_left}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形左边界距屏幕左边缘的像素距离.

UiObject#boundsLeft 的别名方法.

## [m#] top {#uiobjecttype_m_top}

### top() {#uiobjecttype_top}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形上边界距屏幕上边缘的像素距离.

UiObject#boundsTop 的别名方法.

## [m#] right {#uiobjecttype_m_right}

### right() {#uiobjecttype_right}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形右边界距屏幕左边缘的像素距离.

UiObject#boundsRight 的别名方法.

## [m#] bottom {#uiobjecttype_m_bottom}

### bottom() {#uiobjecttype_bottom}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形下边界距屏幕上边缘的像素距离.

UiObject#boundsBottom 的别名方法.

## [m#] width {#uiobjecttype_m_width}

### width() {#uiobjecttype_width}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的宽度.

UiObject#boundsWidth 的别名方法.

## [m#] height {#uiobjecttype_m_height}

### height() {#uiobjecttype_height}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的高度.

UiObject#boundsHeight 的别名方法.

## [m#] centerX {#uiobjecttype_m_centerx}

### centerX() {#uiobjecttype_centerx}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 X 坐标 (中心点距屏幕左边缘的像素距离).

UiObject#boundsCenterX 的别名方法.

## [m#] exactCenterX {#uiobjecttype_m_exactcenterx}

### exactCenterX() {#uiobjecttype_exactcenterx}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 X 坐标 (中心点距屏幕左边缘的像素距离).

UiObject#boundsExactCenterX 的别名方法.

## [m#] centerY {#uiobjecttype_m_centery}

### centerY() {#uiobjecttype_centery}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 Y 坐标 (中心点距屏幕上边缘的像素距离).

UiObject#boundsCenterY 的别名方法.

## [m#] exactCenterY {#uiobjecttype_m_exactcentery}

### exactCenterY() {#uiobjecttype_exactcentery}

**`6.2.0`** **`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回控件矩形的中心 Y 坐标 (中心点距屏幕上边缘的像素距离).

UiObject#boundsExactCenterY 的别名方法.

## [m#] point {#uiobjecttype_m_point}

### point() {#uiobjecttype_point}

**`6.2.0`** **`A11Y`**

- **returns** { OpenCVPoint (opencvPointType.html) }

返回控件矩形的中心点 (Point (opencvPointType.html)).

该中心点坐标由 exactCenterX 和 exactCenterY 计算获得, 因此会保留精度.

是 center 的别名方法.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 0 - 10, 12)
console.log(wA.point()); // e.g. {5.0, 6.0}
console.log(wA.point().x); // e.g. 5

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 13)
console.log(wB.point()); // e.g. {5.5, 6.5}
console.log(wB.point().y); // e.g. 6.5
```

## [m#] center {#uiobjecttype_m_center}

### center() {#uiobjecttype_center}

**`6.4.2`** **`A11Y`**

- **returns** { OpenCVPoint (opencvPointType.html) }

返回控件矩形的中心点 (Point (opencvPointType.html)).

该中心点坐标由 exactCenterX 和 exactCenterY 计算获得, 因此会保留精度.

是 point 的别名方法.

```js
let wA = pickup(/.+/);
console.log(wA.bounds()); // e.g. Rect(0, 0 - 10, 12)
console.log(wA.center()); // e.g. {5.0, 6.0}
console.log(wA.center().x); // e.g. 5

let wB = pickup(/.+/);
console.log(wB.bounds()); // e.g. Rect(0, 0 - 11, 13)
console.log(wB.center()); // e.g. {5.5, 6.5}
console.log(wB.center().y); // e.g. 6.5
```

## [m#] size {#uiobjecttype_m_size}

### size() {#uiobjecttype_size}

**`6.2.0`** **`A11Y`**

- **returns** { OpenCVSize (opencvSizeType.html) }

返回控件矩形的尺寸 (Size (opencvSizeType.html)).

```js
let w = pickup(/.+/);
console.log(w.bounds()); // e.g. Rect(0, 0 - 10, 12)
console.log(w.size()); // e.g. 10x12
console.log(w.size().width); // e.g. 10
console.log(w.size().height); // e.g. 12
```

## [m#] clickBounds {#uiobjecttype_m_clickbounds}

### clickBounds(offsetX?, offsetY?) {#uiobjecttype_clickbounds_offsetx_offsety}

**`6.2.0`** **`Overload [1-3]/3`** **`A11Y`**

- **[ offsetX = 0 ]** { number (dataTypes.html#datatypes_number) } - X 坐标偏移量 (支持负值及百分率)
- **[ offsetY = 0 ]** { number (dataTypes.html#datatypes_number) } - Y 坐标偏移量 (支持负值及百分率)
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否点击行为已执行且执行过程中无异常

点击控件矩形的中心点坐标.

点击操作借助 automator.click(x, y) (automator.html#automator_m_click) 完成, 此操作需要启用无障碍服务.

```js
let w = pickup(/.+/);

console.log(w.bounds()); // e.g. Rect(0, 60 - 100, 200)

w.clickBounds(); /* 相当于 click(50, 130) . */
click(w.centerX(), w.centerY()); /* 效果同上. */

w.clickBounds(10); /* X 坐标偏移量为 10 像素, 相当于 click(50 + 10, 130) . */
w.clickBounds(10, 15); /* X 与 Y 坐标偏移量分别为 10 和 15 像素, 相当于 click(50 + 10, 130 + 15) . */
w.clickBounds(0, -15); /* Y 坐标偏移量为 -15 像素, 相当于 click(50, 130 - 15) . */
w.clickBounds(0.2); /* X 坐标偏移量为 20% 屏幕宽度, 相当于 click(50 + 0.2 * device.width, 130) . */
w.clickBounds(0.2, -0.05); /* X 与 Y 坐标偏移量为 20% 屏幕宽度和 -5% 屏幕高度. */
```

## [m#] id {#uiobjecttype_m_id}

### id() {#uiobjecttype_id}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回节点的 ID 资源全称 (Fully-Qualified ID Resource Name).

若 ID 不存在, 返回 null.

安卓资源全称格式为 `package:type/entry`, 即 `包名:类型/资源项`.
ID 资源全称的 `类型` 为 `id`.
一个有效的 ID 资源全称: `com.test:id/some_entry`.

```js
console.log(idMatch(/.+/).findOnce().id()); // e.g. org.autojs.autojs6:id/action_bar_root
console.log(idMatch(/.+/).findOnce().fullId()); /* 同上. */
console.log(idMatch(/.+/).findOnce().getViewIdResourceName()); /* 同上. */
```

需额外留意, 部分应用的控件 ID 资源全称可能不符合标准:

```js
/* 标准 ID 全称. */
let canonicalId = "com.test:id/hello_world";

/* 可能出现的非标准 ID 全称. */
let peculiarId = "hello_world"; /* 仅含资源项, 无包名及类型标识. */
```

别名属性或方法:

- `[m#]` getViewIdResourceName
- `[m#]` fullId

## [m#] fullId {#uiobjecttype_m_fullid}

### fullId() {#uiobjecttype_fullid}

**`6.2.0`** **`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回节点的 ID 资源全称 (Fully-Qualified ID Resource Name).

若 ID 不存在, 返回 null.

UiObject#id 的别名方法.

## [m#] idEntry {#uiobjecttype_m_identry}

### idEntry() {#uiobjecttype_identry}

**`6.2.0`** **`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回节点的 ID 资源项名称 (ID Resource Entry Name).

安卓资源全称格式为 `package:type/entry`, 即 `包名:类型/资源项`.
例如对于 ID 资源全称 `com.test:id/some_entry`, 其 ID 资源项名称为 `some_entry`.

```js
/* ID 资源全称. */
console.log(idMatch(/.+/).findOnce().id()); // e.g. org.autojs.autojs6:id/action_bar_root

/* ID 资源项名称. */
console.log(idMatch(/.+/).findOnce().idEntry()); // action_bar_root
console.log(idMatch(/.+/).findOnce().simpleId()); /* 同上. */
```

别名属性或方法:

- `[m#]` simpleId

## [m#] simpleId {#uiobjecttype_m_simpleid}

### simpleId() {#uiobjecttype_simpleid}

**`6.2.0`** **`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回节点的 ID 资源项名称 (ID Resource Entry Name).

若 ID 不存在, 返回 null.

UiObject#idEntry 的别名方法.

## [m#] idHex {#uiobjecttype_m_idhex}

### idHex() {#uiobjecttype_idhex}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回节点的 ID 资源全称 的 资源 ID (glossaries.html#glossaries_资源_ID) 十六进制字符串值, 简称 `ID 资源十六进制代表值`.

- 获取 `ID 资源全称` 对应的 `资源 ID`
- 将 `资源 ID` 的十六进制值以 `0x` 作为前缀进行组合
- 返回组合的字符串值

若 ID 不存在, 返回 null.

```js
console.log(idMatch(/explorer_item_list/).findOnce().idHex()); /* e.g. 0x7f090117 */
```

## [m#] text {#uiobjecttype_m_text}

### text() {#uiobjecttype_text}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) }

返回控件文本内容.

若文本内容不存在, 返回空字符串.

出于保护隐私目的, `isPassword()` 返回 `true` 的密码类型控件, `text()` 将返回空字符串.

```js
console.log(textMatch(/.+/).findOnce().text()); /* e.g. hello */
```

别名属性或方法:

- `[m#]` getText

## [m#] desc {#uiobjecttype_m_desc}

### desc() {#uiobjecttype_desc}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回控件的内容描述标签.

若内容描述标签容不存在, 返回 null.

内容描述标签可以帮助需要无障碍服务的用户 (如视力障碍人群等) 理解当前控件的用途或说明.
如 TalkBack (https://support.google.com/accessibility/android/topic/10601570?hl=zh-Hans) 开启后可以朗读控件的内容描述标签, 对于理解那些没有文本内容的控件尤其重要.

```js
console.log(descMatch(/.+/).findOnce().desc()); /* e.g. Restart icon */
```

别名属性或方法:

- `[m#]` getContentDescription

## [m#] content {#uiobjecttype_m_content}

### content() {#uiobjecttype_content}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) }

返回控件内容 (包括内容描述标签或本文内容).

若无内容, 返回空字符串.

`content` 方法相当于 `w.desc() || w.text()`, 即优先获取 desc 返回的内容, 若为 null, 继续获取 text 返回的内容.

```js
console.log(contentMatch(/.+/).findOnce().content()); /* e.g. Avatar */
```

## [m#] className {#uiobjecttype_m_classname}

### className() {#uiobjecttype_classname}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回控件的类名.

若如类名, 返回 null.

```js
console.log(classNameMatch(/.+/).findOnce().className()); /* e.g. android.widget.EditText */
```

常见类名:

- android.view.View
- android.view.ViewGroup
- android.widget.ImageView
- android.widget.ImageButton
- android.widget.Button
- android.widget.ScrollView
- android.widget.TextView
- android.widget.EditText
- android.widget.Switch
- android.widget.LinearLayout
- android.widget.FrameLayout
- android.widget.RelativeLayout

别名属性或方法:

- `[m#]` getClassName

## [m#] packageName {#uiobjecttype_m_packagename}

### packageName() {#uiobjecttype_packagename}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string) | null (dataTypes.html#datatypes_null) }

返回控件的包名.

若如包名, 返回 null.

```js
console.log(packageNameMatch(/.+/).findOnce().packageName()); /* e.g. org.autojs.autojs6 */
```

别名属性或方法:

- `[m#]` getPackageName

## [m#] depth {#uiobjecttype_m_depth}

### depth() {#uiobjecttype_depth}

**`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回 控件层级 (glossaries.html#glossaries_控件层级) 深度.

顶层控件 (只有一个) 的深度值为 0, 次级控件 (可能有多个) 的深度值全部为 1, 以此类推.

```js
console.log(findOnce().depth()); // 0
console.log(contentMatch(/.+/).depth()); /* e.g. 5 */
```

## [m#] checkable {#uiobjecttype_m_checkable}

### checkable() {#uiobjecttype_checkable}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可勾选.

别名属性或方法:

- `[m#]` isCheckable

关联属性或方法:

- 检查状态
- `[m#]` checked (isChecked)

- 检查可用性
- `[m#]` checkable (isCheckable)

## [m#] checked {#uiobjecttype_m_checked}

### checked() {#uiobjecttype_checked}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否已勾选.

别名属性或方法:

- `[m#]` isChecked

关联属性或方法:

- 检查状态
- `[m#]` checked (isChecked)

- 检查可用性
- `[m#]` checkable (isCheckable)

## [m#] focusable {#uiobjecttype_m_focusable}

### focusable() {#uiobjecttype_focusable}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可聚焦.

别名属性或方法:

- `[m#]` isFocusable

关联属性或方法:

- 检查状态
- `[m#]` focused (isFocused)

- 检查可用性
- `[m#]` focusable (isFocusable)

## [m#] focused {#uiobjecttype_m_focused}

### focused() {#uiobjecttype_focused}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否已聚焦.

别名属性或方法:

- `[m#]` isFocused

关联属性或方法:

- 检查状态
- `[m#]` focused (isFocused)

- 检查可用性
- `[m#]` focusable (isFocusable)

## [m#] visibleToUser {#uiobjecttype_m_visibletouser}

### visibleToUser() {#uiobjecttype_visibletouser}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否对用户可见.

别名属性或方法:

- `[m#]` isVisibleToUser

## [m#] accessibilityFocused {#uiobjecttype_m_accessibilityfocused}

### accessibilityFocused() {#uiobjecttype_accessibilityfocused}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否已获取无障碍焦点.

别名属性或方法:

- `[m#]` isAccessibilityFocused

关联属性或方法:

- 检查状态
- `[m#]` accessibilityFocused (isAccessibilityFocused)

- 执行行为
- `[m#]` accessibilityFocus (uiObjectActionsType.html#uiobjectactionstype_m_accessibilityfocus)

## [m#] selected {#uiobjecttype_m_selected}

### selected() {#uiobjecttype_selected}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否已选中.

别名属性或方法:

- `[m#]` isSelected

关联属性或方法:

- 检查状态
- `[m#]` selected (isSelected)

- 执行行为
- `[m#]` select (uiObjectActionsType.html#uiobjectactionstype_m_select)

## [m#] clickable {#uiobjecttype_m_clickable}

### clickable() {#uiobjecttype_clickable}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可点击.

别名属性或方法:

- `[m#]` isClickable

关联属性或方法:

- 检查状态
- `[m#]` clickable (isClickable)

- 执行行为
- `[m#]` click (uiObjectActionsType.html#uiobjectactionstype_m_click)

## [m#] longClickable {#uiobjecttype_m_longclickable}

### longClickable() {#uiobjecttype_longclickable}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可长按.

别名属性或方法:

- `[m#]` isLongClickable

关联属性或方法:

- 检查状态
- `[m#]` longClickable (isLongClickable)

- 执行行为
- `[m#]` longClick (uiObjectActionsType.html#uiobjectactionstype_m_longclick)

## [m#] enabled {#uiobjecttype_m_enabled}

### enabled() {#uiobjecttype_enabled}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否启用 (未被禁用).

别名属性或方法:

- `[m#]` isEnabled

## [m#] password {#uiobjecttype_m_password}

### password() {#uiobjecttype_password}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否是密码型控件.

别名属性或方法:

- `[m#]` isPassword

## [m#] scrollable {#uiobjecttype_m_scrollable}

### scrollable() {#uiobjecttype_scrollable}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可滚动.

别名属性或方法:

- `[m#]` isScrollable

关联属性或方法:

- 检查状态
- `[m#]` scrollable (isScrollable)

- 执行行为
- `[m#]` scrollBackward (uiObjectActionsType.html#uiobjectactionstype_m_scrollbackward)
- `[m#]` scrollDown (uiObjectActionsType.html#uiobjectactionstype_m_scrolldown)
- `[m#]` scrollForward (uiObjectActionsType.html#uiobjectactionstype_m_scrollforward)
- `[m#]` scrollLeft (uiObjectActionsType.html#uiobjectactionstype_m_scrollleft)
- `[m#]` scrollRight (uiObjectActionsType.html#uiobjectactionstype_m_scrollright)
- `[m#]` scrollTo (uiObjectActionsType.html#uiobjectactionstype_m_scrollto)
- `[m#]` scrollUp (uiObjectActionsType.html#uiobjectactionstype_m_scrollup)

## [m#] editable {#uiobjecttype_m_editable}

### editable() {#uiobjecttype_editable}

**`6.2.0`** **`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否可编辑.

别名属性或方法:

- `[m#]` isEditable

## [m#] rowCount {#uiobjecttype_m_rowcount}

### rowCount() {#uiobjecttype_rowcount}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 信息集控件 (glossaries.html#glossaries_信息集控件) 的行数.

## [m#] columnCount {#uiobjecttype_m_columncount}

### columnCount() {#uiobjecttype_columncount}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 信息集控件 (glossaries.html#glossaries_信息集控件) 的列数.

## [m#] row {#uiobjecttype_m_row}

### row() {#uiobjecttype_row}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 子项信息集控件 (glossaries.html#glossaries_子项信息集控件) 所在行的索引值.

## [m#] column {#uiobjecttype_m_column}

### column() {#uiobjecttype_column}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 子项信息集控件 (glossaries.html#glossaries_子项信息集控件) 所在列的索引值.

## [m#] rowSpan {#uiobjecttype_m_rowspan}

### rowSpan() {#uiobjecttype_rowspan}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 子项信息集控件 (glossaries.html#glossaries_子项信息集控件) 纵跨的行数.

## [m#] columnSpan {#uiobjecttype_m_columnspan}

### columnSpan() {#uiobjecttype_columnspan}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 子项信息集控件 (glossaries.html#glossaries_子项信息集控件) 横跨的列数.

## [m#] drawingOrder {#uiobjecttype_m_drawingorder}

### drawingOrder() {#uiobjecttype_drawingorder}

**`A11Y`**

- **returns** { number (dataTypes.html#datatypes_number) }

返回节点的视图绘制次序.

此次序由其父节点决定, 是一个相对于其兄弟节点的索引值.
在某些情况下, 视图 (View) 绘制的过程本质上是同时发生的, 两个兄弟节点可能返回同一个索引值, 甚至此索引值可能被忽略 (返回默认值 0).

```js
console.log(pickup(/.+/).drawingOrder()); // e.g. 0
```

## [m#] actionNames {#uiobjecttype_m_actionnames}

### actionNames() {#uiobjecttype_actionnames}

**`A11Y`**

- **returns** { string (dataTypes.html#datatypes_string)[] (dataTypes.html#datatypes_array) }

返回控件支持的 控件行为 (uiObjectActionsType.html) 数组.

```js
let w = pickup(/.+/);

/* e.g. [ ACTION_CLICK, ACTION_SET_SELECTION, ACTION_FOCUS ] */
console.log(w.actionNames());
```

上述示例, 数组中的三个元素代表控件可以执行对应的行为, 即 `w.click()`, `w.setSelection(...)` 及 `w.focus()`.

数组中的元素均为 "ACTION_" 开头的控件行为 ID 的字符串形式.
更多控件行为 ID 可参阅 控件节点行为 (uiObjectActionsType.html) 章节的 `行为 ID` 表格.

如需判断一个控件是否支持一个或多个行为, 可使用 hasAction 方法.

## [m#] hasAction {#uiobjecttype_m_hasaction}

### hasAction(...actions) {#uiobjecttype_hasaction_actions}

**`A11Y`**

- **actions** { ... (documentation.html#documentation_可变参数)string (dataTypes.html#datatypes_string)[] (documentation.html#documentation_可变参数) }
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回控件是否 **全部支持** 指定的一个或多个 控件行为 (uiObjectActionsType.html).

参数 actions 是 可变参数 (documentation.html#documentation_可变参数), 均满足 "ACTION_" 开头的控件行为 ID 的字符串形式 ("ACTION_" 可省略).

```js
let w = pickup(/.+/);

/* 判断 w 是否可点击. */
console.log(w.hasAction("ACTION_CLICK"));
console.log(w.hasAction("CLICK")); /* ACTION_ 前缀可省略. */

/* 判断 w 是否可点击, 可聚焦, 可设置文本. */
console.log(w.hasAction("ACTION_CLICK", "ACTION_FOCUS", "ACTION_SET_TEXT"));
console.log(w.hasAction("CLICK", "FOCUS", "SET_TEXT")); /* ACTION_ 前缀可省略. */
```

更多控件行为 ID 可参阅 控件节点行为 (uiObjectActionsType.html) 章节的 `行为 ID` 表格.

## [m#] performAction {#uiobjecttype_m_performaction}

用于执行指定的控件行为.
在 控件节点行为 (uiObjectActionsType.html) 章节已详细描述相关内容, 此处仅注明几个重载方法的签名, 相关内容将不再赘述.

### performAction(action, ...arguments) {#uiobjecttype_performaction_action_arguments}

**`Overload 1/2`** **`A11Y`**

- **action** { number (dataTypes.html#datatypes_number) } - 行为的唯一标志符 (Action ID)
- **arguments** { ... (documentation.html#documentation_可变参数)ActionArgument (uiObjectActionsType.html#uiobjectactionstype_i_actionargument)[] (documentation.html#documentation_可变参数) } - 行为参数, 用于给行为传递参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

### performAction(action, bundle) {#uiobjecttype_performaction_action_bundle}

**`Overload 2/2`** **`A11Y`**

- **action** { number (dataTypes.html#datatypes_number) } - 行为的唯一标志符 (Action ID)
- **bundle** { AndroidBundle (uiObjectActionsType.html#uiobjectactionstype_i_actionargument) } - 行为参数容器, 用于给行为传递参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

## [m#] click {#uiobjecttype_m_click}

### click() {#uiobjecttype_click}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 点击 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_click).

## [m#] longClick {#uiobjecttype_m_longclick}

### longClick() {#uiobjecttype_longclick}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 长按 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_longclick).

## [m#] accessibilityFocus {#uiobjecttype_m_accessibilityfocus}

### accessibilityFocus() {#uiobjecttype_accessibilityfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 获取无障碍焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_accessibilityfocus).

## [m#] clearAccessibilityFocus {#uiobjecttype_m_clearaccessibilityfocus}

### clearAccessibilityFocus() {#uiobjecttype_clearaccessibilityfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 清除无障碍焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearaccessibilityfocus).

## [m#] focus {#uiobjecttype_m_focus}

### focus() {#uiobjecttype_focus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 获取焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_focus).

## [m#] clearFocus {#uiobjecttype_m_clearfocus}

### clearFocus() {#uiobjecttype_clearfocus}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 清除焦点 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearfocus).

## [m#] dragStart {#uiobjecttype_m_dragstart}

### dragStart() {#uiobjecttype_dragstart}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 拖放开始 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragstart).

## [m#] dragDrop {#uiobjecttype_m_dragdrop}

### dragDrop() {#uiobjecttype_dragdrop}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 拖放放下 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragdrop).

## [m#] dragCancel {#uiobjecttype_m_dragcancel}

### dragCancel() {#uiobjecttype_dragcancel}

**`6.2.0`** **`A11Y`** **`API>=32`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 拖放取消 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dragcancel).

## [m#] imeEnter {#uiobjecttype_m_imeenter}

### imeEnter() {#uiobjecttype_imeenter}

**`6.2.0`** **`A11Y`** **`API>=30`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 输入法 ENTER 键 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_imeenter).

## [m#] moveWindow {#uiobjecttype_m_movewindow}

### moveWindow(x, y) {#uiobjecttype_movewindow_x_y}

**`6.2.0`** **`A11Y`** **`API>=26`**

- **x** { number (dataTypes.html#datatypes_number) } - X 坐标
- **y** { number (dataTypes.html#datatypes_number) } - Y 坐标
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 移动窗口到新位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_movewindow).

## [m#] nextAtMovementGranularity {#uiobjecttype_m_nextatmovementgranularity}

### nextAtMovementGranularity(granularity, isExtendSelection) {#uiobjecttype_nextatmovementgranularity_granularity_isextendselection}

**`6.2.0`** **`A11Y`**

- **granularity** { number (dataTypes.html#datatypes_number) } - 粒度
- **isExtendSelection** { boolean (dataTypes.html#datatypes_boolean) } - 是否扩展选则文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 按粒度移至下一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_nextatmovementgranularity).

## [m#] nextHtmlElement {#uiobjecttype_m_nexthtmlelement}

### nextHtmlElement(element) {#uiobjecttype_nexthtmlelement_element}

**`6.2.0`** **`A11Y`**

- **element** { string (dataTypes.html#datatypes_string) } - 元素名称
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 按元素移至下一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_nexthtmlelement).

## [m#] pageLeft {#uiobjecttype_m_pageleft}

### pageLeft() {#uiobjecttype_pageleft}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗左移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageleft).

## [m#] pageUp {#uiobjecttype_m_pageup}

### pageUp() {#uiobjecttype_pageup}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗上移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageup).

## [m#] pageRight {#uiobjecttype_m_pageright}

### pageRight() {#uiobjecttype_pageright}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗右移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pageright).

## [m#] pageDown {#uiobjecttype_m_pagedown}

### pageDown() {#uiobjecttype_pagedown}

**`6.2.0`** **`A11Y`** **`API>=29`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗下移的翻页 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pagedown).

## [m#] pressAndHold {#uiobjecttype_m_pressandhold}

### pressAndHold() {#uiobjecttype_pressandhold}

**`6.2.0`** **`A11Y`** **`API>=30`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 按住 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_pressandhold).

## [m#] previousAtMovementGranularity {#uiobjecttype_m_previousatmovementgranularity}

### previousAtMovementGranularity(granularity, isExtendSelection) {#uiobjecttype_previousatmovementgranularity_granularity_isextendselection}

**`6.2.0`** **`A11Y`**

- **granularity** { number (dataTypes.html#datatypes_number) } - 粒度
- **isExtendSelection** { boolean (dataTypes.html#datatypes_boolean) } - 是否扩展选则文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 按粒度移至上一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_previousatmovementgranularity).

## [m#] previousHtmlElement {#uiobjecttype_m_previoushtmlelement}

### previousHtmlElement(element) {#uiobjecttype_previoushtmlelement_element}

**`6.2.0`** **`A11Y`**

- **element** { string (dataTypes.html#datatypes_string) } - 元素名称
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 按元素移至上一位置 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_previoushtmlelement).

## [m#] showTextSuggestions {#uiobjecttype_m_showtextsuggestions}

### showTextSuggestions() {#uiobjecttype_showtextsuggestions}

**`6.2.0`** **`A11Y`** **`API>=33`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 显示文本建议 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_showtextsuggestions).

## [m#] showTooltip {#uiobjecttype_m_showtooltip}

### showTooltip() {#uiobjecttype_showtooltip}

**`6.2.0`** **`A11Y`** **`API>=28`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 显示工具提示信息 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_showtooltip).

## [m#] hideTooltip {#uiobjecttype_m_hidetooltip}

### hideTooltip() {#uiobjecttype_hidetooltip}

**`6.2.0`** **`A11Y`** **`API>=28`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 隐藏工具提示信息 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_hidetooltip).

## [m#] show {#uiobjecttype_m_show}

### show() {#uiobjecttype_show}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 显示在视窗内 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_show).

## [m#] dismiss {#uiobjecttype_m_dismiss}

### dismiss() {#uiobjecttype_dismiss}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 消隐 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_dismiss).

## [m#] copy {#uiobjecttype_m_copy}

### copy() {#uiobjecttype_copy}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 复制文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_copy).

## [m#] cut {#uiobjecttype_m_cut}

### cut() {#uiobjecttype_cut}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 剪切文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_cut).

## [m#] paste {#uiobjecttype_m_paste}

### paste() {#uiobjecttype_paste}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 粘贴文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_paste).

## [m#] select {#uiobjecttype_m_select}

### select() {#uiobjecttype_select}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 选中 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_select).

## [m#] expand {#uiobjecttype_m_expand}

### expand() {#uiobjecttype_expand}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 展开 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_expand).

## [m#] collapse {#uiobjecttype_m_collapse}

### collapse() {#uiobjecttype_collapse}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 折叠 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_collapse).

## [m#] scrollLeft {#uiobjecttype_m_scrollleft}

### scrollLeft() {#uiobjecttype_scrollleft}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗左移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollleft).

## [m#] scrollUp {#uiobjecttype_m_scrollup}

### scrollUp() {#uiobjecttype_scrollup}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗上移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollup).

## [m#] scrollRight {#uiobjecttype_m_scrollright}

### scrollRight() {#uiobjecttype_scrollright}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗右移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollright).

## [m#] scrollDown {#uiobjecttype_m_scrolldown}

### scrollDown() {#uiobjecttype_scrolldown}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗下移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrolldown).

## [m#] scrollForward {#uiobjecttype_m_scrollforward}

### scrollForward() {#uiobjecttype_scrollforward}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗前移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollforward).

## [m#] scrollBackward {#uiobjecttype_m_scrollbackward}

### scrollBackward() {#uiobjecttype_scrollbackward}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 使视窗后移的滚动 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollbackward).

## [m#] scrollTo {#uiobjecttype_m_scrollto}

### scrollTo(row, column) {#uiobjecttype_scrollto_row_column}

**`A11Y`**

- **row** { number (dataTypes.html#datatypes_number) } - 行序数
- **column** { number (dataTypes.html#datatypes_number) } - 列序数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 将指定位置滚动至视窗内 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_scrollto).

## [m#] contextClick {#uiobjecttype_m_contextclick}

### contextClick() {#uiobjecttype_contextclick}

**`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 上下文点击 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_contextclick).

## [m#] setText {#uiobjecttype_m_settext}

### setText(text) {#uiobjecttype_settext_text}

**`A11Y`**

- **text** { string (dataTypes.html#datatypes_string) } - 文本
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 设置文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_settext).

## [m#] setSelection {#uiobjecttype_m_setselection}

### setSelection(start, end) {#uiobjecttype_setselection_start_end}

**`A11Y`**

- **start** { number (dataTypes.html#datatypes_number) } - 开始位置
- **end** { number (dataTypes.html#datatypes_number) } - 结束位置
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 选择文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_setselection).

## [m#] clearSelection {#uiobjecttype_m_clearselection}

### clearSelection() {#uiobjecttype_clearselection}

**`6.2.0`** **`A11Y`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 取消选择文本 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_clearselection).

## [m#] setProgress {#uiobjecttype_m_setprogress}

### setProgress(progress) {#uiobjecttype_setprogress_progress}

**`A11Y`**

- **progress** { number (dataTypes.html#datatypes_number) } - 进度值
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 是否行为已执行且执行过程中无异常

控件节点执行 [ 设置进度值 ] 行为 (uiObjectActionsType.html#uiobjectactionstype_m_setprogress).

## [m#] compass {#uiobjecttype_m_compass}

### compass(compassArg) {#uiobjecttype_compass_compassarg}

**`6.2.0`** **`A11Y`**

- **compassArg** { DetectCompass (dataTypes.html#datatypes_detectcompass) } - 罗盘参数, 用于控制罗盘定位
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 罗盘最终定位的控件节点

返回罗盘最终定位的 控件节点 (uiObjectType.html), 若定位失败, 返回 null.

罗盘定位类似于在 控件层级 (glossaries.html#glossaries_控件层级) 中自由移动, 最终定位在某个指定的控件节点上.

```js
let w = clickable().findOnce();

console.log(w.parent()); /* 父控件. */
console.log(w.parent().parent()); /* 二级父控件. */
console.log(w.child(0)); /* 索引 0 (首个) 子控件. */
console.log(w.child(2)); /* 索引 2 子控件. */
console.log(w.child(w.childCount() - 1)); /* 末尾子控件. */
console.log(w.parent().child(5)); /* 索引 5 兄弟控件. */
console.log(w.parent().child(w.childCount() - 2)); /* 倒数第 2 兄弟控件. */
console.log(w.parent().child(w.indexInParent() - 1)); /* 相邻左侧兄弟节点. */
console.log(w.parent().child(w.indexInParent() + 1)); /* 相邻右侧兄弟节点. */
console.log(w.parent().parent().parent().parent().child(0).child(1).child(1).child(0)); /* 多级访问. */

/* 使用控件罗盘替代上述所有语句. */

console.log(w.compass('p')); /* 父控件. */
console.log(w.compass('p2')); /* 二级父控件. */
console.log(w.compass('c0')); /* 索引 0 (首个) 子控件. */
console.log(w.compass('c2')); /* 索引 2 子控件. */
console.log(w.compass('c-1')); /* 末尾子控件. */
console.log(w.compass('s5')); /* 索引 5 兄弟控件. */
console.log(w.compass('s-2')); /* 倒数第 2 兄弟控件. */
console.log(w.compass('s<1')); /* 相邻左侧兄弟节点. */
console.log(w.compass('s>1')); /* 相邻右侧兄弟节点. */
console.log(w.compass('p4c0>1>1>0')); /* 多级访问. */
```

罗盘参数有以下几类:

- p: parent (父控件)
- c: child (子控件)
- s: sibling (兄弟控件)
- k: clickable (可点击控件)

不同种类的罗盘参数可以重复使用或组合使用.

#### parent (p) {#uiobjecttype_parent_p}

访问父控件.

如 `w.parent()` 的两种罗盘定位形式:

```js
w.compass('p'); /* 较为常用. */
w.compass('p1');
```

罗盘 `p` 可跟随一个数字, 表示层级跨度:

```js
/* 二级. */
w.parent().parent(); /* 原始方式. */
w.compass('pp');
w.compass('p2'); /* 较为常用. */

/* 五级. */
w.parent().parent().parent().parent().parent(); /* 原始方式. */
w.compass('ppppp');
w.compass('p5'); /* 较为常用. */
w.compass('p4p');
w.compass('p3p2');
w.compass('p2p1p2');
```

罗盘 `p` 每移动一次, 控件的 depth 将减少一级, 当 depth 为 0 时, 后续所有父级访问均返回 null:

```js
console.log(w.depth()); /* e.g. 23 */
console.log(w.compass('p5').depth()); /* e.g. 18 */
console.log(w.compass('p23').depth()); /* e.g. 0 */
console.log(w.compass('p24')); // null
console.log(w.compass('p40')); // null
```

罗盘 `p` 跟随负数时将抛出异常:

```js
/* e.g. java.lang.IllegalArgumentException: 无效的剩余罗盘参数: -2 */
console.log(w.compass('p-2'));
```

`p0` 将返回控件本身:

```js
console.log(w.compass('p0') === w); // true
```

#### child (c) {#uiobjecttype_child_c}

访问子控件.

如 `w.child(0)` 的罗盘定位形式:

```js
w.compass('c0');
```

罗盘 `c` 可跟随一个整数, 表示子控件索引:

```js
/* 索引 2 子控件 */
w.child(2);
w.compass('c2');

/* 倒数第 2 子控件. */
w.child(w.childCount() - 2);
w.compass('c-2');
```

连续多级子控件访问, 可使用 `cXcYcZ` 或 `cX>Y>Z` 形式:

```js
w.child(1).child(1).child(0).child(5).child(2).child(3);
w.compass('c1c1c0c5c2c3');
w.compass('c1>1>0>5>2>3'); /* 同上. */
```

#### sibling (s) {#uiobjecttype_sibling_s}

访问兄弟控件.

例如一个控件有 10 个子控件, 这些子控件互为兄弟控件, 它们拥有同一个父控件.
10 个子控件中, 索引为 n (n > 0 且 n < 9) 的子控件有两个相邻兄弟控件节点, 即索引为 n - 1 的左邻兄弟和索引为 n + 1 的右邻兄弟.

```js
/* 左邻兄弟节点. */
w.parent().child(w.indexInParent() - 1);
w.compass('s<1');

/* 右邻兄弟节点. */
w.parent().child(w.indexInParent() + 1);
w.compass('s>1');

/* 右侧第 2 个兄弟节点. */
w.parent().child(w.indexInParent() + 2);
w.compass('s>2');

/* 索引 5 的兄弟节点. */
w.parent().child(5);
w.compass('s5');

/* 倒数第 2 个兄弟节点. */
w.parent().child(w.childCount() - 2);
w.compass('s-2');
```

#### clickable (k) {#uiobjecttype_clickable_k}

访问可点击控件.

有些控件本身不可点击, 而是包含在一个可点击控件内部:

```js
let w = contentMatch(/.+/).findOnce();
console.log(w.clickable()); // false
console.log(w.parent().clickable()); // true
```

对于上述情况的控件, 通常执行 "父控件.click()" 都会达到预期, 即虽然点击的是父控件, 但实际效果和点击这个控件本身是一样的.

在某些情况下, 这样的可点击父控件可能需要两级甚至更多级:

```js
let w = contentMatch(/.+/).findOnce();
console.log(w.clickable()); // false
console.log(w.parent().clickable()); // false
console.log(w.parent().parent().clickable()); // false
console.log(w.parent().parent().parent().clickable()); // false
console.log(w.parent().parent().parent().parent().clickable()); // true
```

上述示例直到 4 级父控件才是可点击的, 对于这种情况通常需要使用循环语句结合 `clickable` 的条件检测:

```js
let w = contentMatch(/.+/).findOnce();
let max = 5;
let temp = w;
while (max--) {
    if (temp !== null && temp.clickable()) {
        temp.click();
        break;
    }
    temp = temp.parent();
}
```

上述示例的 `max` 变量表示最多尝试的层级数, 层级数过小, 可能导致错过真正可点击的父控件, 过大则可能会得到不相关的可点击控件 (这样的控件点击后将出现非预期结果), 通常这个 `max` 建议设置为 2.

将上述示例用控件罗盘表示:

```js
let w = contentMatch(/.+/).findOnce();
let temp = w.compass('k5'); /* 5 表示尝试的最大层级数, 通常建议设置为 2. */
if (temp !== null && temp.clickable()) {
    temp.click();
}
```

将上述示例用 拾取选择器 (uiSelectorType.html#uiselectortype_m_pickup) 表示:

```js
pickup(/.+/, 'k5', 'click');
```

## [m] isCompass {#uiobjecttype_m_iscompass}

### isCompass(s) {#uiobjecttype_iscompass_s}

**`6.2.0`** **`A11Y`**

- **s** { string (dataTypes.html#datatypes_string) } - 罗盘参数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

检测罗盘参数是否符合既定格式.

```js
console.log(UiObject.isCompass('p2c3')); // true
console.log(UiObject.isCompass('p-2c3')); // true
console.log(UiObject.isCompass('p2c-3')); // true
console.log(UiObject.isCompass('hello')); // false
```

上述示例中的 `p-2c3` 罗盘参数, 在使用时会抛出异常, 但因符合既定格式, 故 `isCompass` 返回 `true`.

## [m] ensureCompass {#uiobjecttype_m_ensurecompass}

### ensureCompass(s) {#uiobjecttype_ensurecompass_s}

**`6.2.0`** **`A11Y`**

- **s** { string (dataTypes.html#datatypes_string) } - 罗盘参数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) }

确保罗盘参数符合既定格式, 若不符合则抛出异常.

```js
UiObject.ensureCompass('p2c3'); /* 无异常. */
UiObject.ensureCompass('world'); /* 抛出异常. */
```

## [m] detect {#uiobjecttype_m_detect}

控件探测.

探测相当于对控件进行一系列组合操作 (罗盘定位, 结果筛选, 参化调用, 回调处理).

部分特性:

- `detect` 已全局化, 支持全局使用.
- `detect` 的首个参数固定为 UiObject (uiObjectType.html) 类型.
- compass 是 `detect` 的衍生方法.
- pickup (uiSelectorType.html#uiselectortype_m_pickup) 的内部实现引用了 `detect` 方法.

### detect(w, compass) {#uiobjecttype_detect_w_compass}

**`6.2.0`** **`Global`** **`Overload 1/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **compass** { DetectCompass (dataTypes.html#datatypes_detectcompass) } - 罗盘参数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测后的控件节点

携带 罗盘参数 (dataTypes.html#datatypes_detectcompass) 的控件探测.

相当于 w.compass(compass), 因此 `compass` 是 `detect` 的衍生方法.

### detect(w, result) {#uiobjecttype_detect_w_result}

**`6.2.0`** **`Global`** **`Overload 2/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **result** { DetectResult (dataTypes.html#datatypes_detectresult) } - 探测结果参数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测结果

携带 探测结果参数 (dataTypes.html#datatypes_detectresult) 的控件探测.

### detect(w, compass, result) {#uiobjecttype_detect_w_compass_result}

**`6.2.0`** **`Global`** **`Overload 3/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **compass** { DetectCompass (dataTypes.html#datatypes_detectcompass) } - 罗盘参数
- **result** { DetectResult (dataTypes.html#datatypes_detectresult) } - 探测结果参数
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测结果

携带 罗盘参数 (dataTypes.html#datatypes_detectcompass) 和 探测结果参数 (dataTypes.html#datatypes_detectresult) 的控件探测.

需特别留意 compass 和 result 的顺序, 两者均为字符串时, 前者会被解析为 `罗盘参数`.

```js
console.log(w.parent().parent().child(1).child(0).bounds()); /* 潜在的空指针异常. */
console.log(detect(w, 'p2c1>0', 'bounds')); /* 空指针安全. */
```

### detect(w, callback) {#uiobjecttype_detect_w_callback}

**`6.2.0`** **`Global`** **`Overload 4/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **callback** { DetectCallback (dataTypes.html#datatypes_detectcallback) } - 探测回调
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测回调的结果

携带 探测回调 (dataTypes.html#datatypes_detectcallback) 的控件探测.

```js
detect(pickup(/^[A-Z][a-z]+ ?\d*$/), (w) => {
    w ? w.click() : console.warn('未找到指定控件');
});
```

### detect(w, compass, callback) {#uiobjecttype_detect_w_compass_callback}

**`6.2.0`** **`Global`** **`Overload 5/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **compass** { DetectCompass (dataTypes.html#datatypes_detectcompass) } - 罗盘参数
- **callback** { DetectCallback (dataTypes.html#datatypes_detectcallback) } - 探测回调
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测回调的结果

携带 罗盘参数 (dataTypes.html#datatypes_detectcompass) 和 探测回调 (dataTypes.html#datatypes_detectcallback) 的控件探测.

```js
detect(pickup(/^[A-Z][a-z]+ ?\d*$/), 'k2', (w) => {
    w ? w.click() : console.warn('未找到指定控件');
});
```

### detect(w, result, callback) {#uiobjecttype_detect_w_result_callback}

**`6.2.0`** **`Global`** **`Overload 6/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **result** { DetectResult (dataTypes.html#datatypes_detectresult) } - 探测结果参数
- **callback** { DetectCallback (dataTypes.html#datatypes_detectcallback) } - 探测回调
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测回调的结果

携带 探测结果参数 (dataTypes.html#datatypes_detectresult) 和 探测回调 (dataTypes.html#datatypes_detectcallback) 的控件探测.

```js
detect(pickup(/^[A-Z][a-z]+ ?\d*$/), 'content', (content) => {
    content ? console.log(content) : console.warn('无文本内容或未能定位指定控件');
});
```

### detect(w, compass, result, callback) {#uiobjecttype_detect_w_compass_result_callback}

**`6.2.0`** **`Global`** **`Overload 7/7`** **`A11Y`**

- **w** { UiObject (uiObjectType.html) } - 控件节点
- **compass** { DetectCompass (dataTypes.html#datatypes_detectcompass) } - 罗盘参数
- **result** { DetectResult (dataTypes.html#datatypes_detectresult) } - 探测结果参数
- **callback** { DetectCallback (dataTypes.html#datatypes_detectcallback) } - 探测回调
- **returns** { UiObject (uiObjectType.html) | null (dataTypes.html#datatypes_null) } - 探测回调的结果

携带 罗盘参数 (dataTypes.html#datatypes_detectcompass), 探测结果参数 (dataTypes.html#datatypes_detectresult) 和 探测回调 (dataTypes.html#datatypes_detectcallback) 的控件探测.

需特别留意 compass 和 result 的顺序, 两者均为字符串时, 前者会被解析为 `罗盘参数`.

```js
detect(pickup({ clickable: true }), 'p2c1', 'content', (content) => {
    content ? console.log(content) : console.warn('无文本内容或未能定位指定控件');
});
```
