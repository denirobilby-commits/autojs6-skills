---
title: "OpenCVPoint"
version: "6.6.4"
source_html: "raw/opencvPointType.html"
---

# OpenCVPoint {#opencvpointtype_opencvpoint}

org.opencv.core.Point (https://docs.opencv.org/4.x/javadoc/org/opencv/core/Point.html) 别名.

Point 表示一个点, 作为控件信息时则表示点在屏幕的相对位置.

```js
let point = pickup(/.+/, '.');
console.log(`${point.x}, ${point.y}`);
```

常见相关方法或属性:

- UiSelector.pickup (uiSelectorType.html#uiselectortype_m_pickup)

注: 本章节仅列出部分属性或方法.

org.opencv.core.Point

## [C] org.opencv.core.Point {#opencvpointtype_c_org_opencv_core_point}

### [c] (x, y) {#opencvpointtype_c_x_y}

- **x** { number (dataTypes.html#datatypes_number) } - 点 X 坐标
- **y** { number (dataTypes.html#datatypes_number) } - 点 Y 坐标
- **returns** { org.opencv.core.Point }

生成一个点.

```js
console.log(new org.opencv.core.Point(10, 20)); // {10.0, 20.0}
```

坐标不会被化为整型:

```js
console.log(new org.opencv.core.Point(10.8, 20.44)); // {10.8, 20.44}
```

### [c] () {#opencvpointtype_c}

- **returns** { org.opencv.core.Point }

生成一个点, 并初始化为 `{0, 0}` 坐标.

```js
console.log(new org.opencv.core.Point()); // {0.0, 0.0}
```

### [c] (points) {#opencvpointtype_c_points}

- **points** { number (dataTypes.html#datatypes_number)[] (dataTypes.html#datatypes_array) } - 点坐标数组
- **returns** { org.opencv.core.Point }

生成一个点, 并按指定参数初始化坐标.

两个坐标:

```js
console.log(new org.opencv.core.Point([ 5, 23 ])); // {5.0, 23.0}
```

一个坐标, 此坐标作为 X 坐标, Y 坐标初始化为 0:

```js
console.log(new org.opencv.core.Point([ 5 ])); // {5.0, 0.0}
```

空数组, X 与 Y 坐标均为 0:

```js
console.log(new org.opencv.core.Point([])); // {0.0, 0.0}
```

超过两个坐标, 多余坐标将被忽略:

```js
console.log(new org.opencv.core.Point([ 5, 23, 7, 8, 9 ])); // {5.0, 23.0}
```

## [p#] x {#opencvpointtype_p_x}

- { number (dataTypes.html#datatypes_number) }

点 X 坐标.

如: Point(**180**, 440) 表示点距屏幕左边缘 180 像素.

## [p#] y {#opencvpointtype_p_y}

- { number (dataTypes.html#datatypes_number) }

点 Y 坐标.

如: Point(180, **440**) 表示点距屏幕上边缘 440 像素.
