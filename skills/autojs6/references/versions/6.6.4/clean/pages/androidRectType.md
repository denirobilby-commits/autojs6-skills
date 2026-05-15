---
title: "AndroidRect"
version: "6.6.4"
source_html: "raw/androidRectType.html"
---

# AndroidRect {#androidrecttype_androidrect}

android.graphics.Rect (https://developer.android.com/reference/android/graphics/Rect) 别名.

Rect 表示一个矩形, 作为控件信息时则用于表示控件在屏幕的相对位置及空间范围, 又称 **控件矩形**.

```js
let bounds = pickup(/.+/, 'bounds');
console.log(`${bounds.centerX()}, ${bounds.centerY()}`);
```

常见相关方法或属性:

- UiObject#bounds (uiObjectType.html#uiobjecttype_m_bounds)
- UiSelector.pickup (uiSelectorType.html#uiselectortype_m_pickup)

注: 本章节仅列出部分属性或方法.

android.graphics.Rect

## [C] android.graphics.Rect {#androidrecttype_c_android_graphics_rect}

### [c] (left, top, right, bottom) {#androidrecttype_c_left_top_right_bottom}

- **left** { number (dataTypes.html#datatypes_number) } - 矩形左边界 X 坐标
- **top** { number (dataTypes.html#datatypes_number) } - 矩形上边界 Y 坐标
- **right** { number (dataTypes.html#datatypes_number) } - 矩形右边界 X 坐标
- **bottom** { number (dataTypes.html#datatypes_number) } - 矩形下边界 Y 坐标
- **returns** { android.graphics.Rect }

生成一个矩形.

```js
let rect = new android.graphics.Rect(10, 20, 80, 90);
console.log(rect); // Rect(10, 20 - 80, 90)
```

如果坐标值为浮点数, 将做向下取整处理:

```js
let rect = new android.graphics.Rect(10.2, 20.7, 80.1, 90.92);
console.log(rect); // Rect(10, 20 - 80, 90)
```

坐标值可以为 0 或负数:

```js
let rect = new android.graphics.Rect(0, 0, -80, -90);
console.log(rect); // Rect(0, 0 - -80, -90)
```

### [c] () {#androidrecttype_c}

- **returns** { android.graphics.Rect }

生成一个空矩形.

```js
let rect = new android.graphics.Rect();
console.log(rect); // Rect(0, 0 - 0, 0)
```

### [c] (rect) {#androidrecttype_c_rect}

- **rect** { android.graphics.Rect } - 参照矩形
- **returns** { android.graphics.Rect }

生成一个新矩形, 并按照参照矩形的参数初始化.

```js
let rectA = new android.graphics.Rect(10, 20, 80, 90);
let rectB = new android.graphics.Rect(rectA);
console.log(rectB); // Rect(10, 20 - 80, 90)
rectB.top = 1;
rectB.bottom = 0;
console.log(rectB); // Rect(10, 1 - 80, 0)
console.log(rectA); // Rect(10, 20 - 80, 90)
```

## [p#] left {#androidrecttype_p_left}

- { number (dataTypes.html#datatypes_number) }

矩形左边界 X 坐标.

如: Rect(**180**, 440, 750, 1200) 表示矩形左边界距屏幕左边缘 180 像素.

## [p#] top {#androidrecttype_p_top}

- { number (dataTypes.html#datatypes_number) }

矩形上边界 Y 坐标.

如: Rect(180, **440**, 750, 1200) 表示矩形上边界距屏幕上边缘 440 像素.

## [p#] right {#androidrecttype_p_right}

- { number (dataTypes.html#datatypes_number) }

矩形右边界 X 坐标.

如: Rect(180, 440, **750**, 1200) 表示矩形右边界距屏幕左边缘 750 像素.

## [p#] bottom {#androidrecttype_p_bottom}

- { number (dataTypes.html#datatypes_number) }

矩形下边界 Y 坐标.

如: Rect(180, 440, 750, **1200**) 表示矩形下边界距屏幕上边缘 1200 像素.

## [m#] width {#androidrecttype_m_width}

### width() {#androidrecttype_width}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形宽度.

```js
let rect = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rect.width()); // 570
```

宽度可能为 0 或负数:

```js
let rectA = new android.graphics.Rect(0, 440, 0, 1200);
console.log(rectA.width()); // 0
let rectB = new android.graphics.Rect(30, 440, 10, 1200);
console.log(rectB.width()); // -20
```

## [m#] height {#androidrecttype_m_height}

### height() {#androidrecttype_height}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形高度.

```js
let rect = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rect.height()); // 760
```

高度可能为 0 或负数:

```js
let rectA = new android.graphics.Rect(180, 1200, 750, 1200);
console.log(rectA.height()); // 0
let rectB = new android.graphics.Rect(180, 40, 750, 10);
console.log(rectB.height()); // -30
```

## [m#] centerX {#androidrecttype_m_centerx}

### centerX() {#androidrecttype_centerx}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形中点 X 坐标 (向下取整).

```js
let rectA = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rectA.centerX()); // 465

let rectB = new android.graphics.Rect(100, 200, 101, 201);
console.log(rectB.centerX()); // 100
```

## [m#] centerY {#androidrecttype_m_centery}

### centerY() {#androidrecttype_centery}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形中点 Y 坐标 (向下取整).

```js
let rectA = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rectA.centerY()); // 820

let rectB = new android.graphics.Rect(100, 200, 101, 201);
console.log(rectB.centerY()); // 200
```

## [m#] exactCenterX {#androidrecttype_m_exactcenterx}

### exactCenterX() {#androidrecttype_exactcenterx}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形中点 X 坐标 (浮点数).

```js
let rectA = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rectA.exactCenterX()); // 465

let rectB = new android.graphics.Rect(100, 200, 101, 201);
console.log(rectB.exactCenterX()); // 100.5
```

## [m#] exactCenterY {#androidrecttype_m_exactcentery}

### exactCenterY() {#androidrecttype_exactcentery}

- **returns** { number (dataTypes.html#datatypes_number) }

矩形中点 Y 坐标 (浮点数).

```js
let rectA = new android.graphics.Rect(180, 440, 750, 1200);
console.log(rectA.exactCenterY()); // 820

let rectB = new android.graphics.Rect(100, 200, 101, 201);
console.log(rectB.exactCenterY()); // 200.5
```

## [m#] contains {#androidrecttype_m_contains}

### contains(rect) {#androidrecttype_contains_rect}

- **rect** { android.graphics.Rect } - 参照矩形
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回是否包含另一个矩形.
参照矩形的所有边均在当前矩形内 (包含边重叠情况) 则满足包含条件.
空矩形与任何矩形不存在包含关系.

```js
let rectThis = new android.graphics.Rect(180, 440, 750, 1200);

let rectRefA = new android.graphics.Rect(rectThis);
console.log(rectThis.contains(rectRefA)); // true

let rectRefB = new android.graphics.Rect(200, 440, 750, 1200);
console.log(rectThis.contains(rectRefB)); // true

let rectRefC = new android.graphics.Rect(); /* 空矩形. */
console.log(rectThis.contains(rectRefC)); // false
```

## [m#] intersect {#androidrecttype_m_intersect}

### intersect(rect) {#androidrecttype_intersect_rect}

- **rect** { android.graphics.Rect } - 参照矩形
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回是否与参展矩形相交 (不包括边界或点重叠的情况).
如果相交, 则返回 true, **且当前矩形被设置为相交部分的矩形**.

```js
let rectThis = new android.graphics.Rect(0, 0, 600, 600);
let rectRef = new android.graphics.Rect(200, 0, 800, 800);

console.log(rectThis.intersect(rectRef)); // true

/* rectThis 被修改. */
console.log(rectThis); // Rect(200, 0 - 600, 600)
```

如果不相交, 则返回 false, 当前矩形不会被修改:

```js
let rectThis = new android.graphics.Rect(0, 0, 100, 100);
let rectRef = new android.graphics.Rect(100, 0, 800, 800);

console.log(rectThis.intersect(rectRef)); // false

/* rectThis 保持原来的值. */
console.log(rectThis); // Rect(0, 0 - 100, 100)
```

空矩形与任意矩形不相交:

```js
let rectThis = new android.graphics.Rect(0, 0, 100, 100);
let rectRef = new android.graphics.Rect();
console.log(rectThis.intersect(rectRef)); // false
```

## [m] intersects {#androidrecttype_m_intersects}

### intersects(rectA, rectB) {#androidrecttype_intersects_recta_rectb}

- **rect** { android.graphics.Rect } - 参照矩形
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回是否和另一个长方形相交.

此方法近判断是否相交, 不改变任何矩形:

```js
let rectA = new android.graphics.Rect(0, 0, 600, 600);
let rectB = new android.graphics.Rect(200, 0, 800, 800);

console.log(android.graphics.Rect.intersects(rectA, rectB)); // true

/* rectA 和 refB 均保持原来的值. */
console.log(rectA); // Rect(0, 0 - 600, 600)
console.log(rectB); // Rect(200, 0 - 800, 800)
```

需额外留意 intersects 与 intersect 的区别:

-

`[m#] intersect` 为实例方法, `rectA.intersect(rectB)` 需传入一个参数, 当相交时 `rectA` 会被改变, 返回结果为 "是否相交".

-

`[m] intersects` 为静态方法, `Rect.intersects(rectA, rectB)` 需传入两个参数, 且不改变任何矩形, 仅返回 "是否相交" 结果.
