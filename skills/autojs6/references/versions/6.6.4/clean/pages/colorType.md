---
title: "Color (颜色类)"
version: "6.6.4"
source_html: "raw/colorType.html"
---

# Color (颜色类) {#colortype_color}

颜色类 Color 是一个全局类, 用于生成一个颜色实例:

```js
typeof global.Color; // "function"

let c = new Color('red');
Object.getPrototypeOf(c) === Color.prototype; // true
c.getRed(); // 255
c.getRedDouble(); // 1
```

Color 类是对 colors (color.html) 模块的一种变式封装, 用于解决 colors 模块冗余嵌套的难题.

例如需要对颜色 `hsv(174,100,59)` 设置 `80%` 透明度然后返回其 Hex 代码:

```js
colors.toHex(colors.setAlpha(colors.hsv(174, 100, 59), 0.8));
```

或使用变量拆写形式以增加可读性:

```js
let color = colors.hsv(174, 100, 59);
let colorWithAlpha = colors.setAlpha(color, 0.8);
colors.toHex(colorWithAlpha);
```

使用 Color 实例进行链式调用, 可使代码更轻量且易读:

```js
new Color().setHsv(174, 100, 59).setAlpha(0.8).toHex();
```

链式拆行形式:

```js
new Color()
    .setHsv(174, 100, 59)
    .setAlpha(0.8)
    .toHex();
```

注: 上述示例仅用于演示, 实际可使用 colors.hsva 或 Color#setHsva 同时设置 HSV 分量与 A 分量.

Color 实例方法的使用方式与 colors 模块对应方法多数情况是类似的, 因此某些情况下可用于替代 colors 模块.

以 `set` 或 `remove` 为前缀的方法, 通常都会返回 Color 自身类型, 从而支持链式调用, 如 setAlpha, removeAlpha, setRed, removeRed, setHsv, setRgba 等.

为便于使用, Color 类在使用 JavaScript 代码设计时, 支持省略 `new` 关键字的语法形式:

```js
new Color('blue');
Color('blue'); /* 效果同上. */

new Color().setAlpha(0.5).summary();
Color().setAlpha(0.5).summary();  /* 结果同上. */
```

需额外留意, Color 类的 `new` 关键字省略, 是 AutoJs6 开发者在编写 Color 类时为便于使用而专门设计的, 并不适用于所有构造器, 详情参阅 JavaScript 语法规范.

参阅: MDN (https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new) / Ecma 标准 (https://tc39.es/ecma262/multipage/ecmascript_language_expressions.html#https://tc39.es/ecma262/multipage/ecmascript_language_expressions_sec_new_operator)

colors.build (color.html#color_m_build) 也可用于构造一个 Color 实例:

```js
new Color();
Color(); /* 同上. */
colors.build(); /* 同上. */

new Color('green');
Color('green'); /* 同上 */
colors.build('green'); /* 同上 */

new Color(120, 24, 72, 0.5);
Color(120, 24, 72, 0.5); /* 同上. */
colors.build(120, 24, 72, 0.5); /* 同上. */
```

本章节后续内容将不再赘述 `colors.build(...)` 的替代语法, 且统一使用省略 `new` 关键字的 Color 实例构造语法, 即 `Color(...)`.

Color

## [C] Color {#colortype_c_color}

### [c] (color?) {#colortype_c_color_1}

**`6.3.0`** **`Global`** **`Overload [1-2]/5`**

- **[ color = `Colors.BLACK` ]** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数
- **returns** { Color (colorType.html) } - Color 实例

构建一个颜色实例, 初始颜色由 `color` 参数指定, 参数省略时默认为 `黑色 (#FF000000)`.

```js
Color().toHex(); // #000000
Color('black').toHex(); /* 同上. */
Color(0).setAlpha(1).toHex(); /* 同上. */

Color('green').toHex(); // #00FF00
Color('#00FF00').toHex(); /* 同上. */
Color().setGreen(255).toHex(); /* 同上. */
Color('white').removeRed().removeBlue().toHex(); /* 同上. */
```

需特别留意, `Color(0)` 返回的不是默认的黑色, 而是 `透明色 (#00000000)`:

```js
Color(0).toFullHex(); // #00000000
Color().toFullHex(); // #FF000000

Color(0).setAlpha(1).toFullHex(); // #FF000000
Color().removeAlpha().toFullHex(); // #00000000
```

### [c] (red, green, blue, alpha?) {#colortype_c_red_green_blue_alpha}

**`6.3.0`** **`Global`** **`Overload [3-4]/5`**

- **red** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - R (red)
- **green** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - G (green)
- **blue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - B (blue)
- **[ alpha = `1` ]** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **returns** { Color (colorType.html) } - Color 实例

构建一个颜色实例, 初始颜色由多个参数指定, 其中 `alpha` 参数省略时默认为 `1 (100%)`.

```js
Color(255, 255, 255); /* 白色. */
Color(0, 0, 255, 0.5); /* 半透明蓝色. */
```

需特别留意, 颜色分量值为 `0` 时不可省略, 如 `Color(255, 0, 0)` 不可省略为 `Color(255)`.

### [c] (themeColor) {#colortype_c_themecolor}

**`6.3.0`** **`Global`** **`Overload 5/5`**

- **themeColor** { ThemeColor (dataTypes.html#datatypes_themecolor) } - 主题颜色实例
- **returns** { Color (colorType.html) } - Color 实例

构建一个颜色实例, 初始颜色为 AutoJs6 主题色的 `主色 (Primary Color)`.

```js
Color(autojs.themeColor).toHex(); /* AutoJs6 主题色主色的 Hex 代码. */
```

此构造方法相当于 `Color(ThemeColor#getColorPrimary)`.

```js
Color(autojs.themeColor.getColorPrimary()).toHex();
Color(autojs.themeColor).toHex(); /* 效果同上. */
```

## [m#] toInt {#colortype_m_toint}

### toInt() {#colortype_toint}

**`6.3.0`**

- **returns** { ColorInt (dataTypes.html#datatypes_colorint) } - 颜色整数

获取颜色实例的 颜色整数 (ColorInt) (dataTypes.html#datatypes_colorint).

```js
/* ColorHex - 颜色代码. */
Color('#CC5500').toInt(); // -3386112
Color('#C50').toInt(); // -3386112
Color('#FFCC5500').toInt(); // -3386112

/* ColorInt - 颜色整数. */
Color(0xFFCC5500).toInt(); // -3386112
Color(colors.web.BURNT_ORANGE).toInt(); // -3386112

/* ColorName - 颜色名称. */
Color('BURNT_ORANGE').toInt(); // -3386112
Color('burnt-orange').toInt(); // -3386112
```

## [m#] toHex {#colortype_m_tohex}

### toHex() {#colortype_tohex}

**`6.3.0`** **`Overload 1/3`**

- **returns** { ColorHex (dataTypes.html#datatypes_colorhex) } - 颜色代码

获取颜色实例的 颜色代码 (ColorHex) (dataTypes.html#datatypes_colorhex).

```js
/* ColorHex - 颜色代码. */
Color('#CC5500').toHex(); // #CC5500
Color('#C50').toHex(); // #CC5500
Color('#DECC5500').toHex(); // #DECC5500
Color('#FFCC5500').toHex(); /* #CC5500, A (alpha) 分量被省略. */

/* ColorInt - 颜色整数. */
Color(0xFFCC5500).toHex(); // #CC5500
Color(colors.web.BURNT_ORANGE).toHex(); // #CC5500

/* ColorName - 颜色名称. */
Color('BURNT_ORANGE').toHex(); // #CC5500
Color('burnt-orange').toHex(); // #CC5500
```

当 `A (alpha)` 分量为 `100% (255/255;100/100)` 时, `FF` 会自动省略,
如 `#FFC0C0C0` 将自动转换为 `#C0C0C0`, 此方法相当于 `toHex('auto')`.

### toHex(alpha) {#colortype_tohex_alpha}

**`6.3.0`** **`Overload 2/3`**

- **[ alpha = `'auto'` ]** { boolean (dataTypes.html#datatypes_boolean) | `'keep'` | `'none'` | `'auto'` } - A (alpha) 分量参数
- **returns** { ColorHex (dataTypes.html#datatypes_colorhex) } - 颜色代码

获取颜色实例的 颜色代码 (ColorHex) (dataTypes.html#datatypes_colorhex), 并根据 `alpha` 参数决定颜色代码 `A (alpha)` 分量的显示状态.

`A (alpha)` 分量参数取值表:

取值 含义 默认 'keep' / true 强制显示 A 分量, 不论 A 分量是否为 0xFF 'none' / false 强制去除 A 分量, 只保留 R / G / B 分量 'auto' 根据 A 分量是否为 0xFF 自动决定显示状态 √

```js
let cA = '#AAC0C0C0';
let cB = '#FFC0C0C0';
let cC = '#C0C0C0';

Color(cA).toHex('auto'); /* #AAC0C0C0, 'auto' 参数可省略. */
Color(cB).toHex('auto'); /* #C0C0C0, 'auto' 参数可省略. */
Color(cC).toHex('auto'); /* #C0C0C0, 'auto' 参数可省略. */

/* cA 舍弃 A 分量. */
Color(cA).toHex(false); // #C0C0C0
Color(cA).toHex('none'); /* 同上. */

/* cB 保留 A 分量. */
Color(cB).toHex(true); // #FFC0C0C0
Color(cB).toHex('keep'); /* 同上. */

/* cC 强制显示 A 分量. */
Color(cC).toHex(true); // #FFC0C0C0
Color(cC).toHex('keep'); /* 同上. */
```

### toHex(length) {#colortype_tohex_length}

**`6.3.0`** **`Overload 3/3`**

- **length** { `8` | `6` | `3` } - Hex 代码长度参数
- **returns** { ColorHex (dataTypes.html#datatypes_colorhex) } - 颜色代码

获取颜色实例的 颜色代码 (ColorHex) (dataTypes.html#datatypes_colorhex), 并根据 `length` 参数决定颜色代码的显示状态.

Hex 代码长度参数取值表:

取值 含义 8 强制显示 A 分量, 结果格式为 #AARRGGBB 6 强制去除 A 分量, 结果格式为 #RRGGBB 3 强制去除 A 分量, 结果格式为 #RGB

```js
let cA = '#AA9966CC';
let cB = '#FF9966CC';
let cC = '#9966CC';
let cD = '#FAEBD7';

/* 转换为 8 长度颜色代码, 强制保留 A 分量. */
Color(cA).toHex(8); // #AA9966CC
Color(cB).toHex(8); // #FF9966CC
Color(cC).toHex(8); // #FF9966CC
Color(cD).toHex(8); // #FFFAEBD7

/* 转换为 6 长度颜色代码, 强制去除 A 分量. */
Color(cA).toHex(6); // #9966CC
Color(cB).toHex(6); // #9966CC
Color(cC).toHex(6); // #9966CC
Color(cD).toHex(6); // #FAEBD7

/* 转换为 3 长度颜色代码, 强制去除 A 分量. */
Color(cA).toHex(3); // #96C
Color(cB).toHex(3); // #96C
Color(cC).toHex(3); // #96C
Color(cD).toHex(3); /* 抛出异常. */
```

## [m#] toFullHex {#colortype_m_tofullhex}

### toFullHex() {#colortype_tofullhex}

**`6.3.0`**

- **returns** { ColorHex (dataTypes.html#datatypes_colorhex) } - 颜色代码的完整形式

获取颜色实例 颜色代码 (ColorHex) (dataTypes.html#datatypes_colorhex) 的完整形式 (#AARRGGBB).

此方法为 `toHex(color, 8)` 的别名方法.

```js
Color('#CC5500').toHex(); // #CC5500
Color('#CC5500').toFullHex(); // #FFCC5500
```

## [m#] summary {#colortype_m_summary}

### summary() {#colortype_summary}

**`6.3.0`**

- **returns** { string (dataTypes.html#datatypes_string) } - 颜色摘要

获取颜色实例的颜色摘要.

格式为 `hex($HEX), rgba($R,$G,$B/$A), int($INT)`.

其中, `A (alpha)` 分量将显示为 `0..1` 范围, 至少一位小数, 至多两位小数:

分量值 显示值 0 0.0 1 1.0 0.64 0.64 128 0.5 255 1.0 100 0.39

示例:

```js
// hex(#009688), rgba(0,150,136/1.0), int(-16738680)
Color('#009688').summary();

// hex(#BE009688), rgba(0,150,136/0.75), int(-1107257720)
Color('#BE009688').summary();

// hex(#FF0000), rgba(255,0,0/1.0), int(-65536)
Color('red').summary();

// hex(#6400008B), rgba(0,0,139/0.39), int(1677721739)
Color('dark-blue').setAlpha(100).summary();
```

## [m#] alpha {#colortype_m_alpha}

### alpha() {#colortype_alpha}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `A (alpha)` 分量, 取值范围 `[0..255]`.

```js
Color('#663399').alpha(); // 255
Color(colors.TRANSPARENT).alpha(); // 0
Color('#05060708').alpha(); // 5
```

### alpha(options) {#colortype_alpha_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `A (alpha)` 分量.

取值范围 `[0..1]` (`options.max` 为 `1`) 或 `[0..255]` (`options.max` 为 `255` 或不指定).

```js
Color('#663399').alpha({ max: 1 }); // 1
Color('#663399').alpha({ max: 255 }); // 255
Color('#663399').alpha(); /* 同上. */

Color('#05060708').alpha({ max: 1 }); // 0.0196078431372549
Color('#05060708').alpha({ max: 255 }); // 5
Color('#05060708').alpha(); /* 同上. */
```

当 `options.max` 为 `1` 时, 相当于 alphaDouble 方法.

## [m#] alphaDouble {#colortype_m_alphadouble}

### alphaDouble() {#colortype_alphadouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `A (alpha)` 分量, 取值范围 `[0..1]`.

相当于 `alpha({ max: 1 })`.

```js
Color('#663399').alphaDouble(); // 1
Color(colors.TRANSPARENT).alphaDouble(); // 0

Color('#05060708').alphaDouble(); // 0.0196078431372549
Color('#05060708').alpha({ max: 1 }); /* 同上. */
```

## [m#] getAlpha {#colortype_m_getalpha}

### getAlpha() {#colortype_getalpha}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `A (alpha)` 分量, 取值范围 `[0..255]`.

Color#alpha() 的别名方法.

### getAlpha(options) {#colortype_getalpha_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `A (alpha)` 分量.

Color#alpha(options) 的别名方法.

## [m#] getAlphaDouble {#colortype_m_getalphadouble}

### getAlphaDouble() {#colortype_getalphadouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `A (alpha)` 分量, 取值范围 `[0..1]`.

Color#alphaDouble() 的别名方法.

## [m#] setAlpha {#colortype_m_setalpha}

### setAlpha(alpha) {#colortype_setalpha_alpha}

**`6.3.0`**

- **alpha** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **returns** { Color (colorType.html) }

设置颜色实例的 `A (alpha)` 分量, 返回自身类型.

```js
Color('#663399').setAlpha(0x80).toHex(); // #80663399
Color('#663399').setAlpha(0.5).toHex(); /* 同上, 0.5 解析为百分数分量, 即 50%. */

Color('#663399').setAlpha(255).toHex(); // #FF663399
Color('#663399').setAlpha(1).toHex(); /* 同上, 1 默认作为百分数分量, 即 100%. */
```

## [m] setAlphaRelative {#colortype_m_setalpharelative}

### setAlphaRelative(percentage) {#colortype_setalpharelative_percentage}

**`6.3.1`**

- **percentage** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 相对百分数
- **returns** { Color (colorType.html) }

针对 `A (alpha)` 分量设置其相对百分比, 返回新颜色的颜色整数.

如当前颜色 `A (alpha)` 分量为 `80`, 希望设置 `A` 分量为 `50%` 相对量, 即 `40`:

```js
Color(color).setAlphaRelative(0.5);
Color(color).setAlphaRelative('50%'); /* 效果同上. */
```

同样地, 如希望设置 `A` 分量为 `1.5` 倍相对量, 即 `120`:

```js
Color(color).setAlphaRelative(1.5);
Color(color).setAlphaRelative('150%');
```

当设置的相对量超过 `255` 时, 将以 `255` 为最终值:

```js
Color(color).setAlphaRelative(10); /* A 分量最终值为 255, 而非 800. */
```

特别地, 当原本颜色的 `A` 分量为 `0` 时, 无论如何设置相对量, `A` 分量均保持 `0` 值.

## [m#] removeAlpha {#colortype_m_removealpha}

### removeAlpha() {#colortype_removealpha}

**`6.3.0`**

- **returns** { Color (colorType.html) }

去除颜色实例的 `A (alpha)` 分量, 返回自身类型.

```js
Color('#BE663399').removeAlpha().toHex(); // #663399
Color('#CC5500').removeAlpha().toHex(); // #CC5500
`
```

相当于 `setAlpha(0)`.

## [m#] red {#colortype_m_red}

### red() {#colortype_red}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `R (red)` 分量, 取值范围 `[0..255]`.

```js
Color('#663399').red(); // 102
Color(colors.TRANSPARENT).red(); // 0
Color('#05060708').red(); // 6
```

### red(options) {#colortype_red_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `R (red)` 分量.

取值范围 `[0..1]` (`options.max` 为 `1`) 或 `[0..255]` (`options.max` 为 `255` 或不指定).

```js
Color('#663399').red({ max: 1 }); // 0.4
Color('#663399').red({ max: 255 }); // 102
Color('#663399').red(); /* 同上. */
```

当 `options.max` 为 `1` 时, 相当于 redDouble 方法.

## [m#] redDouble {#colortype_m_reddouble}

### redDouble() {#colortype_reddouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `R (red)` 分量, 取值范围 `[0..1]`.

相当于 `red({ max: 1 })`.

```js
Color('#663399').redDouble(); // 0.4
```

## [m#] getRed {#colortype_m_getred}

### getRed() {#colortype_getred}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `R (red)` 分量, 取值范围 `[0..255]`.

Color#red() 的别名方法.

### getRed(options) {#colortype_getred_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `R (red)` 分量.

Color#red(options) 的别名方法.

## [m#] getRedDouble {#colortype_m_getreddouble}

### getRedDouble() {#colortype_getreddouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `R (red)` 分量, 取值范围 `[0..1]`.

Color#redDouble() 的别名方法.

## [m#] setRed {#colortype_m_setred}

### setRed(red) {#colortype_setred_red}

**`6.3.0`**

- **red** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - R (red)
- **returns** { Color (colorType.html) }

设置颜色实例的 `R (red)` 分量, 返回自身类型.

```js
Color('#663399').setRed(0x80).toHex(); // #803399
Color('#663399').setRed(0.5).toHex(); /* 同上, 0.5 解析为百分数分量, 即 50%. */

Color('#663399').setRed(255).toHex(); // #FF3399
Color('#663399').setRed(1).toHex(); /* #013399, 不同上. 1 默认作为整数分量, 而非 100%. */
```

## [m] setRedRelative {#colortype_m_setredrelative}

### setRedRelative(percentage) {#colortype_setredrelative_percentage}

**`6.3.1`**

- **percentage** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 相对百分数
- **returns** { Color (colorType.html) }

针对 `R (red)` 分量设置其相对百分比, 返回新颜色的颜色整数.

如当前颜色 `R (red)` 分量为 `80`, 希望设置 `R` 分量为 `50%` 相对量, 即 `40`:

```js
Color(color).setRedRelative(0.5);
Color(color).setRedRelative('50%'); /* 效果同上. */
```

同样地, 如希望设置 `R` 分量为 `1.5` 倍相对量, 即 `120`:

```js
Color(color).setRedRelative(1.5);
Color(color).setRedRelative('150%');
```

当设置的相对量超过 `255` 时, 将以 `255` 为最终值:

```js
Color(color).setRedRelative(10); /* R 分量最终值为 255, 而非 800. */
```

特别地, 当原本颜色的 `R` 分量为 `0` 时, 无论如何设置相对量, `R` 分量均保持 `0` 值.

## [m#] removeRed {#colortype_m_removered}

### removeRed() {#colortype_removered}

**`6.3.0`**

- **returns** { Color (colorType.html) }

去除颜色实例的 `R (red)` 分量, 返回自身类型.

```js
Color('#BE663399').removeRed().toHex(); // #BE003399
Color('#CC5500').removeRed().toHex(); // #005500
`
```

相当于 `setRed(0)`.

## [m#] green {#colortype_m_green}

### green() {#colortype_green}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `G (green)` 分量, 取值范围 `[0..255]`.

```js
Color('#663399').green(); // 51
Color(colors.TRANSPARENT).green(); // 0
Color('#05060708').green(); // 7
```

### green(options) {#colortype_green_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `G (green)` 分量.

取值范围 `[0..1]` (`options.max` 为 `1`) 或 `[0..255]` (`options.max` 为 `255` 或不指定).

```js
Color('#663399').green({ max: 1 }); // 0.2
Color('#663399').green({ max: 255 }); // 51
Color('#663399').green(); /* 同上. */
```

当 `options.max` 为 `1` 时, 相当于 greenDouble 方法.

## [m#] greenDouble {#colortype_m_greendouble}

### greenDouble() {#colortype_greendouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `G (green)` 分量, 取值范围 `[0..1]`.

相当于 `green({ max: 1 })`.

```js
Color('#663399').greenDouble(); // 0.2
```

## [m#] getGreen {#colortype_m_getgreen}

### getGreen() {#colortype_getgreen}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `G (green)` 分量, 取值范围 `[0..255]`.

Color#green() 的别名方法.

### getGreen(options) {#colortype_getgreen_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `G (green)` 分量.

Color#green(options) 的别名方法.

## [m#] getGreenDouble {#colortype_m_getgreendouble}

### getGreenDouble() {#colortype_getgreendouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `G (green)` 分量, 取值范围 `[0..1]`.

Color#greenDouble() 的别名方法.

## [m#] setGreen {#colortype_m_setgreen}

### setGreen(green) {#colortype_setgreen_green}

**`6.3.0`**

- **green** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - G (green)
- **returns** { Color (colorType.html) }

设置颜色实例的 `G (green)` 分量, 返回自身类型.

```js
Color('#663399').setGreen(0x80).toHex(); // #668099
Color('#663399').setGreen(0.5).toHex(); /* 同上, 0.5 解析为百分数分量, 即 50%. */

Color('#663399').setGreen(255).toHex(); // #66FF99
Color('#663399').setGreen(1).toHex(); /* #660199, 不同上. 1 默认作为整数分量, 而非 100%. */
```

## [m] setGreenRelative {#colortype_m_setgreenrelative}

### setGreenRelative(percentage) {#colortype_setgreenrelative_percentage}

**`6.3.1`**

- **percentage** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 相对百分数
- **returns** { Color (colorType.html) }

针对 `G (green)` 分量设置其相对百分比, 返回新颜色的颜色整数.

如当前颜色 `G (green)` 分量为 `80`, 希望设置 `G` 分量为 `50%` 相对量, 即 `40`:

```js
Color(color).setGreenRelative(0.5);
Color(color).setGreenRelative('50%'); /* 效果同上. */
```

同样地, 如希望设置 `G` 分量为 `1.5` 倍相对量, 即 `120`:

```js
Color(color).setGreenRelative(1.5);
Color(color).setGreenRelative('150%');
```

当设置的相对量超过 `255` 时, 将以 `255` 为最终值:

```js
Color(color).setGreenRelative(10); /* G 分量最终值为 255, 而非 800. */
```

特别地, 当原本颜色的 `G` 分量为 `0` 时, 无论如何设置相对量, `G` 分量均保持 `0` 值.

## [m#] removeGreen {#colortype_m_removegreen}

### removeGreen() {#colortype_removegreen}

**`6.3.0`**

- **returns** { Color (colorType.html) }

去除颜色实例的 `G (green)` 分量, 返回自身类型.

```js
Color('#BE663399').removeGreen().toHex(); // #BE660099
Color('#CC5500').removeGreen().toHex(); // #CC0000
`
```

相当于 `setGreen(0)`.

## [m#] blue {#colortype_m_blue}

### blue() {#colortype_blue}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `B (blue)` 分量, 取值范围 `[0..255]`.

```js
Color('#663399').blue(); // 153
Color(colors.TRANSPARENT).blue(); // 0
Color('#05060708').blue(); // 8
```

### blue(options) {#colortype_blue_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `B (blue)` 分量.

取值范围 `[0..1]` (`options.max` 为 `1`) 或 `[0..255]` (`options.max` 为 `255` 或不指定).

```js
Color('#663399').blue({ max: 1 }); // 0.6
Color('#663399').blue({ max: 255 }); // 153
Color('#663399').blue(); /* 同上. */
```

当 `options.max` 为 `1` 时, 相当于 colors.blueDouble 方法.

## [m#] blueDouble {#colortype_m_bluedouble}

### blueDouble() {#colortype_bluedouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `A (blue)` 分量, 取值范围 `[0..1]`.

相当于 `blue({ max: 1 })`.

```js
Color('#663399').blueDouble(); // 0.6
```

## [m#] getBlue {#colortype_m_getblue}

### getBlue() {#colortype_getblue}

**`6.3.0`** **`Overload 1/2`**

- **returns** { IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `B (blue)` 分量, 取值范围 `[0..255]`.

Color#blue() 的别名方法.

### getBlue(options) {#colortype_getblue_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ max = `255` ]?: `1` | `255` - 范围最大值

- }} - 选项参数
- **returns** { IntRange[0..1] (dataTypes.html#datatypes_intrange) | IntRange[0..255] (dataTypes.html#datatypes_intrange) }

获取颜色实例的 `B (blue)` 分量.

Color#blue(options) 的别名方法.

## [m#] getBlueDouble {#colortype_m_getbluedouble}

### getBlueDouble() {#colortype_getbluedouble}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) }

获取颜色实例的 `A (blue)` 分量, 取值范围 `[0..1]`.

Color#blueDouble() 的别名方法.

## [m#] setBlue {#colortype_m_setblue}

### setBlue(blue) {#colortype_setblue_blue}

**`6.3.0`**

- **blue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - B (blue)
- **returns** { Color (colorType.html) }

设置颜色实例的 `B (blue)` 分量, 返回自身类型.

```js
Color('#663399').setBlue(0x80).toHex(); // #663380
Color('#663399').setBlue(0.5).toHex(); /* 同上, 0.5 解析为百分数分量, 即 50%. */

Color('#663399').setBlue(255).toHex(); // #6633FF
Color('#663399').setBlue(1).toHex(); /* #663301, 不同上. 1 默认作为整数分量, 而非 100%. */
```

## [m] setBlueRelative {#colortype_m_setbluerelative}

### setBlueRelative(percentage) {#colortype_setbluerelative_percentage}

**`6.3.1`**

- **percentage** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 相对百分数
- **returns** { Color (colorType.html) }

针对 `B (blue)` 分量设置其相对百分比, 返回新颜色的颜色整数.

如当前颜色 `B (blue)` 分量为 `80`, 希望设置 `B` 分量为 `50%` 相对量, 即 `40`:

```js
Color(color).setBlueRelative(0.5);
Color(color).setBlueRelative('50%'); /* 效果同上. */
```

同样地, 如希望设置 `B` 分量为 `1.5` 倍相对量, 即 `120`:

```js
Color(color).setBlueRelative(1.5);
Color(color).setBlueRelative('150%');
```

当设置的相对量超过 `255` 时, 将以 `255` 为最终值:

```js
Color(color).setBlueRelative(10); /* B 分量最终值为 255, 而非 800. */
```

特别地, 当原本颜色的 `B` 分量为 `0` 时, 无论如何设置相对量, `B` 分量均保持 `0` 值.

## [m#] removeBlue {#colortype_m_removeblue}

### removeBlue() {#colortype_removeblue}

**`6.3.0`**

- **returns** { Color (colorType.html) }

去除颜色实例的 `B (blue)` 分量, 返回自身类型.

```js
Color('#BE663399').removeBlue().toHex(); // #BE663300
Color('#CC5500').removeBlue().toHex(); // #CC5500
`
```

相当于 `setBlue(0)`.

## [m#] setRgb {#colortype_m_setrgb}

### setRgb(color) {#colortype_setrgb_color}

**`6.3.0`** **`Overload 1/3`**

- **color** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数
- **returns** { Color (colorType.html) }

将 `color` 参数对应的 RGB 颜色应用到 Color 实例上.

`color` 参数为颜色代码时, 支持情况如下:

格式 备注 #RRGGBB 正常 #RGB 正常 #AARRGGBB A (alpha) 分量被忽略

方法调用结果的 `A (alpha)` 分量恒为 `255`, 意味着 `color` 参数中的 `A` 分量信息将被忽略.

```js
Color().setRgb('#663399');
Color().setRgb('#DE663399'); /* 同上, A 分量被忽略. */
```

### setRgb(red, green, blue) {#colortype_setrgb_red_green_blue}

**`6.3.0`** **`Overload 2/3`**

- **red** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - R (red)
- **green** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - G (green)
- **blue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - B (blue)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 RGB 颜色应用到 Color 实例上.

```js
Color().setRgb(255, 128, 9);
Color().setRgb(0xFF, 0x80, 0x09); /* 同上. */
Color().setRgb('#FF8009'); /* 同上. */
Color().setRgb(1, 0.5, '3.53%'); /* 同上. */
```

### setRgb(components) {#colortype_setrgb_components}

**`6.3.0`** **`Overload 3/3`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 RGB 颜色应用到 Color 实例上.

```js
Color().setRgb([ 255, 128, 9 ]);
Color().setRgb([ 0xFF, 0x80, 0x09 ]); /* 同上. */
Color().setRgb([ 1, 0.5, '3.53%' ]); /* 同上. */
```

## [m#] setArgb {#colortype_m_setargb}

### setArgb(colorHex) {#colortype_setargb_colorhex}

**`6.3.0`** **`Overload 1/3`**

- **colorHex** { string (dataTypes.html#datatypes_string) } - 颜色代码
- **returns** { Color (colorType.html) }

将 `colorHex` 颜色代码对应的 ARGB 颜色应用到 Color 实例上.

格式 备注 #RRGGBB A (alpha) 分量为 0xFF #RGB A (alpha) 分量为 0xFF #AARRGGBB -

```js
Color().setArgb('#663399'); /* 相当于 setArgb('#FF663399') . */
Color().setArgb('#DE663399'); /* 结果不同上. */
```

### setArgb(alpha, red, green, blue) {#colortype_setargb_alpha_red_green_blue}

**`6.3.0`** **`Overload 2/3`**

- **alpha** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **red** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - R (red)
- **green** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - G (green)
- **blue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - B (blue)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 ARGB 颜色应用到 Color 实例上.

```js
Color().setArgb(64, 255, 128, 9);
Color().setArgb(0x40, 0xFF, 0x80, 0x09); /* 同上. */
Color().setArgb('#40FF8009'); /* 同上. */
Color().setArgb(0.25, 1, 0.5, '3.53%'); /* 同上. */
```

### setArgb(components) {#colortype_setargb_components}

**`6.3.0`** **`Overload 3/3`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 ARGB 颜色应用到 Color 实例上.

```js
Color().setArgb([ 64, 255, 128, 9 ]);
Color().setArgb([ 0x40, 0xFF, 0x80, 0x09 ]); /* 同上. */
Color().setArgb([ 0.25, 1, 0.5, '3.53%' ]); /* 同上. */
```

## [m#] setRgba {#colortype_m_setrgba}

### setRgba(colorHex) {#colortype_setrgba_colorhex}

**`6.3.0`** **`Overload 1/3`**

- **colorHex** { string (dataTypes.html#datatypes_string) } - 颜色代码
- **returns** { Color (colorType.html) }

将 `colorHex` 颜色代码对应的 RGBA 颜色应用到 Color 实例上.

格式 备注 #RRGGBB A (alpha) 分量为 0xFF #RGB A (alpha) 分量为 0xFF #RRGGBBAA -

```js
Color().setRgba('#663399'); /* 相当于 setRgba('#663399FF') . */
Color().setRgba('#663399FF'); /* 结果同上. */
Color().setRgba('#FF663399'); /* 结果不同上. */
```

注意区分 `Color#setRgba` 与 `Color#setArgb`:

```js
Color().setRgba('#11335577'); /* A (alpha) 分量为 0x77 . */
Color().setArgb('#11335577'); /* A (alpha) 分量为 0x11 . */
```

### setRgba(red, green, blue, alpha) {#colortype_setrgba_red_green_blue_alpha}

**`6.3.0`** **`Overload 2/3`**

- **red** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - R (red)
- **green** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - G (green)
- **blue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - B (blue)
- **alpha** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 RGBA 颜色应用到 Color 实例上.

```js
Color().setRgba(255, 128, 9, 64);
Color().setRgba(0xFF, 0x80, 0x09, 0x40); /* 同上. */
Color().setRgba('#FF800940'); /* 同上. */
Color().setRgba(1, 0.5, '3.53%', 0.25); /* 同上. */
```

### setRgba(components) {#colortype_setrgba_components}

**`6.3.0`** **`Overload 3/3`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 RGBA 颜色应用到 Color 实例上.

```js
Color().setRgba([ 255, 128, 9, 64 ]);
Color().setRgba([ 0xFF, 0x80, 0x09, 0x40 ]); /* 同上. */
Color().setRgba([ 1, 0.5, '3.53%', 0.25 ]); /* 同上. */
```

## [m#] setHsv {#colortype_m_sethsv}

### setHsv(hue, saturation, value) {#colortype_sethsv_hue_saturation_value}

**`6.3.0`** **`Overload 1/2`**

- **hue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - H (hue)
- **saturation** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - S (saturation)
- **value** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - V (value)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 HSV 颜色应用到 Color 实例上.

```js
Color().setHsv(90, 80, 64);
Color().setHsv(90, 0.8, 0.64); /* 同上. */
Color().setHsv(0.25, 0.8, 0.64); /* 同上. */
Color().setHsv('25%', '80%', '64%'); /* 同上. */
```

### setHsv(components) {#colortype_sethsv_components}

**`6.3.0`** **`Overload 2/2`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 HSV 颜色应用到 Color 实例上.

```js
Color().setHsv([ 90, 80, 64 ]);
Color().setHsv([ 90, 0.8, 0.64 ]); /* 同上. */
Color().setHsv([ 0.25, 0.8, 0.64 ]); /* 同上. */
Color().setHsv([ '25%', '80%', '64%' ]); /* 同上. */
```

## [m#] setHsva {#colortype_m_sethsva}

### setHsva(hue, saturation, value, alpha) {#colortype_sethsva_hue_saturation_value_alpha}

**`6.3.0`** **`Overload 1/2`**

- **hue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - H (hue)
- **saturation** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - S (saturation)
- **value** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - V (value)
- **alpha** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 HSVA 颜色应用到 Color 实例上.

```js
Color().setHsva(90, 80, 64, 64);
Color().setHsva(90, 0.8, 0.64, 0.25); /* 同上. */
Color().setHsva(0.25, 0.8, 0.64, 0.25); /* 同上. */
Color().setHsva('25%', '80%', '64%', '25%'); /* 同上. */
```

### setHsva(components) {#colortype_sethsva_components}

**`6.3.0`** **`Overload 2/2`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 HSVA 颜色应用到 Color 实例上.

```js
Color().setHsva([ 90, 80, 64, 64 ]);
Color().setHsva([ 90, 0.8, 0.64, 0.25 ]); /* 同上. */
Color().setHsva([ 0.25, 0.8, 0.64, 0.25 ]); /* 同上. */
Color().setHsva([ '25%', '80%', '64%', '25%' ]); /* 同上. */
```

## [m#] setHsl {#colortype_m_sethsl}

### setHsl(hue, saturation, lightness) {#colortype_sethsl_hue_saturation_lightness}

**`6.3.0`** **`Overload 1/2`**

- **hue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - H (hue)
- **saturation** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - S (saturation)
- **lightness** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - L (lightness)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 HSL 颜色应用到 Color 实例上.

```js
Color().setHsl(90, 80, 64);
Color().setHsl(90, 0.8, 0.64); /* 同上. */
Color().setHsl(0.25, 0.8, 0.64); /* 同上. */
Color().setHsl('25%', '80%', '64%'); /* 同上. */
```

### setHsl(components) {#colortype_sethsl_components}

**`6.3.0`** **`Overload 2/2`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 HSL 颜色应用到 Color 实例上.

```js
Color().setHsl([ 90, 80, 64 ]);
Color().setHsl([ 90, 0.8, 0.64 ]); /* 同上. */
Color().setHsl([ 0.25, 0.8, 0.64 ]); /* 同上. */
Color().setHsl([ '25%', '80%', '64%' ]); /* 同上. */
```

## [m#] setHsla {#colortype_m_sethsla}

### setHsla(hue, saturation, lightness, alpha) {#colortype_sethsla_hue_saturation_lightness_alpha}

**`6.3.0`** **`Overload 1/2`**

- **hue** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - H (hue)
- **saturation** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - S (saturation)
- **lightness** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - L (lightness)
- **alpha** { ColorComponent (dataTypes.html#datatypes_colorcomponent) } - 颜色分量 - A (alpha)
- **returns** { Color (colorType.html) }

将 颜色分量 (dataTypes.html#datatypes_colorcomponent) 对应的 HSLA 颜色应用到 Color 实例上.

```js
Color().setHsla(90, 80, 64, 64);
Color().setHsla(90, 0.8, 0.64, 0.25); /* 同上. */
Color().setHsla(0.25, 0.8, 0.64, 0.25); /* 同上. */
Color().setHsla('25%', '80%', '64%', '25%'); /* 同上. */
```

### setHsla(components) {#colortype_sethsla_components}

**`6.3.0`** **`Overload 2/2`**

- **components** { ColorComponents (dataTypes.html#datatypes_colorcomponents)[] (dataTypes.html#datatypes_array) } - 颜色分量数组
- **returns** { Color (colorType.html) }

将 颜色分量数组 (dataTypes.html#datatypes_colorcomponents) 对应的 HSLA 颜色应用到 Color 实例上.

```js
Color().setHsla([ 90, 80, 64, 64 ]);
Color().setHsla([ 90, 0.8, 0.64, 0.25 ]); /* 同上. */
Color().setHsla([ 0.25, 0.8, 0.64, 0.25 ]); /* 同上. */
Color().setHsla([ '25%', '80%', '64%', '25%' ]); /* 同上. */
```

## [m#] toRgb {#colortype_m_torgb}

### toRgb() {#colortype_torgb}

**`6.3.0`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 RGB 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ r, g, b ] = Color('#663399').toRgb();
console.log(`R: ${r}, G: ${g}, B: ${b}`);
```

## [m#] toRgba {#colortype_m_torgba}

### toRgba() {#colortype_torgba}

**`6.3.0`** **`Overload 1/2`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 RGBA 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ r, g, b, a ] = Color('#DE663399').toRgba();
console.log(`R: ${r}, G: ${g}, B: ${b}, A: ${a}`);
```

需留意上述示例的参数格式为 `#AARRGGBB`, 结果格式为 `[RR, GG, BB, AA]`.

### toRgba(options) {#colortype_torgba_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ maxAlpha = `255` ]?: `1` | `255` - A (alpha) 分量的范围最大值

- }} - 选项参数
- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

根据 `options` 选项参数获取颜色实例的 RGBA 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ r1, g1, b1, a1 ] = Color('#DE663399').toRgba();
console.log(`R: ${r1}, G: ${g1}, B: ${b1}, A: ${a1}`); /* A 分量范围为 [0..255] . */

let [ r2, g2, b2, a2 ] = Color('#DE663399').toRgba({ maxAlpha: 1 });
console.log(`R: ${r2}, G: ${g2}, B: ${b2}, A: ${a2}`); /* A 分量范围为 [0..1] . */
```

## [m#] toArgb {#colortype_m_toargb}

### toArgb() {#colortype_toargb}

**`6.3.0`** **`Overload 1/2`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 ARGB 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ a, r, g, b ] = Color('#DE663399').toArgb();
console.log(`A: ${a}, R: ${r}, G: ${g}, B: ${b}`);
```

### toArgb(options) {#colortype_toargb_options}

**`6.3.0`** **`Overload 2/2`**

- **options** {{
- [ maxAlpha = `255` ]?: `1` | `255` - A (alpha) 分量的范围最大值

- }} - 选项参数
- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

根据 `options` 选项参数获取颜色实例的 ARGB 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ a1, r1, g1, b1 ] = Color('#DE663399').toArgb();
console.log(`A: ${a1}, R: ${r1}, G: ${g1}, B: ${b1}`); /* A 分量范围为 [0..255] . */

let [ a2, r2, g2, b2 ] = Color('#DE663399').toArgb({ maxAlpha: 1 });
console.log(`A: ${a2}, R: ${r2}, G: ${g2}, B: ${b2}`); /* A 分量范围为 [0..1] . */
```

## [m#] toHsv {#colortype_m_tohsv}

### toHsv() {#colortype_tohsv}

**`6.3.0`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 HSV 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ h, s, v ] = Color('#663399').toHsv();
console.log(`H: ${h}, S: ${s}, V: ${v}`);
```

## [m#] toHsva {#colortype_m_tohsva}

### toHsva() {#colortype_tohsva}

**`6.3.0`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 HSVA 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

其中 A (alpha) 分量范围恒为 `[0..1]`.

```js
let [ h, s, v, a ] = Color('#BF663399').toHsva();
console.log(`H: ${h}, S: ${s}, V: ${v}, A: ${a}`);
```

## [m#] toHsl {#colortype_m_tohsl}

### toHsl() {#colortype_tohsl}

**`6.3.0`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 HSL 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

```js
let [ h, s, l ] = Color('#663399').toHsl();
console.log(`H: ${h}, S: ${s}, L: ${l}`);
```

## [m#] toHsla {#colortype_m_tohsla}

### toHsla() {#colortype_tohsla}

**`6.3.0`**

- **returns** { ColorComponents (dataTypes.html#datatypes_colorcomponents) } - 颜色分量数组

获取颜色实例的 HSLA 颜色分量数组 (dataTypes.html#datatypes_colorcomponents).

其中 A (alpha) 分量范围恒为 `[0..1]`.

```js
let [ h, s, l, a ] = Color('#BF663399').toHsla();
console.log(`H: ${h}, S: ${s}, L: ${l}, A: ${a}`);
```

## [m#] isSimilar {#colortype_m_issimilar}

### isSimilar(other, threshold?, algorithm?) {#colortype_issimilar_other_threshold_algorithm}

**`6.3.0`** **`Overload [1-3]/4`**

- **other** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数
- **[ threshold = `4` ]** { IntRange[0..255] (dataTypes.html#datatypes_intrange) } - 颜色匹配阈值 (glossaries.html#glossaries_颜色匹配阈值)
- **[ algorithm = `'diff'` ]** { ColorDetectionAlgorithm (dataTypes.html#datatypes_colordetectionalgorithm) } - 颜色检测算法
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 实例颜色与参数颜色是否相似

判断实例颜与于参数颜色是否相似.

不同阈值对结果的影响 (阈值越高, 条件越宽松, 阈值越低, 条件越严格):

```js
Color('orange').isSimilar('dark-orange', 5); /* false, 阈值较小, 条件相对严格. */
Color('orange').isSimilar('dark-orange', 10); /* true, 阈值增大, 条件趋于宽松. */
```

不同 颜色检测算法 (dataTypes.html#datatypes_colordetectionalgorithm) 对结果的影响:

```js
Color('orange').isSimilar('dark-orange', 9, 'rgb+'); // false
Color('orange').isSimilar('dark-orange', 9, 'diff'); // true
Color('orange').isSimilar('dark-orange', 9, 'hs'); // true

Color('orange').isSimilar('dark-orange', 8, 'rgb+'); // false
Color('orange').isSimilar('dark-orange', 8, 'diff'); // false
Color('orange').isSimilar('dark-orange', 8, 'hs'); // true
```

### isSimilar(other, options) {#colortype_issimilar_other_options}

**`6.3.0`** **`Overload 4/4`**

- **other** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数

- **options** {{
- [ similarity ≈ `0.9843` ]?: Range[0..1] (dataTypes.html#datatypes_range) - 颜色匹配相似度 (glossaries.html#glossaries_相似度)
- [ threshold = `4` ]?: IntRange[0..255] (dataTypes.html#datatypes_intrange) - 颜色匹配阈值 (glossaries.html#glossaries_颜色匹配阈值)
- [ algorithm = `'diff'` ]?: ColorDetectionAlgorithm (dataTypes.html#datatypes_colordetectionalgorithm) - 颜色检测算法

- }} - 选项参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 实例颜色与参数颜色是否相似

判断实例颜与于参数颜色是否相似.

此方法将非必要参数集中于 `options` 对象中.

```js
Color('#010101').isSimilar('#020202', { similarity: 0.95 }); // true
```

## [m#] isEqual {#colortype_m_isequal}

### isEqual(other, alphaMatters?) {#colortype_isequal_other_alphamatters}

**`6.3.0`** **`Overload[1-2]/2`**

- **other** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数
- **[ alphaMatters = `false` ]** { boolean (dataTypes.html#datatypes_boolean) } - 是否考虑 `A (alpha)` 分量
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 实例颜色与参数颜色是否相等

判断实例颜色与参数颜色是否相等, 比较时由 `alphaMatters` 参数决定是否考虑 `A (alpha)` 分量:

```js
/* Hex 代码. */
colors.isEqual('#FF0000', '#FF0000'); // true
colors.isEqual('#FF0000', '#F00'); /* 同上, 三位数简写形式. */
/* 颜色整数. */
colors.isEqual(-65536, 0xFF0000); // true
/* 颜色名称. */
colors.isEqual('red', 'RED'); /* true, 不区分大小写. */
colors.isEqual('orange', 'Orange'); /* true, 不区分大小写. */
colors.isEqual('dark-gray', 'DARK_GRAY'); /* true, 连字符与下划线均被支持. */
/* 不同类型比较. */
colors.isEqual('red', '#FF0000'); // true
colors.isEqual('orange', '#FFA500'); // true
/* A (alpha) 分量的不同情况. */
colors.isEqual('#A1FF0000', '#A2FF0000'); /* true, 默认忽略 A 分量. */
colors.isEqual('#A1FF0000', '#A2FF0000', true); /* false, 需考虑 A 分量. */
```

## [m#] equals {#colortype_m_equals}

### equals(other) {#colortype_equals_other}

**`6.3.0`** **`DEPRECATED`**

- **other** { number (dataTypes.html#datatypes_number) | string (dataTypes.html#datatypes_string) } - 颜色参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 实例颜色与参数颜色是否相等 (忽略 `A (alpha)` 分量)

判断实例颜色与参数颜色是否相等, 比较时忽略 `A (alpha)` 分量:

```js
/* Hex 代码. */
Color('#FF0000').equals('#FF0000'); // true
/* 颜色整数. */
Color(-65536).equals(0xFF0000); // true
/* 颜色名称. */
Color('red').equals('RED'); // true
/* 不同类型比较. */
Color('red').equals('#FF0000'); // true
/* A (alpha) 分量将被忽略. */
Color('#A1FF0000').equals('#A2FF0000'); // true
```

但以下示例将全部抛出异常:

```js
Color('orange').equals('#FFA500'); /* 抛出异常. */
Color('dark-gray').equals('#444'); /* 抛出异常. */
Color('#FF0000').equals('#F00'); /* 抛出异常. */
```

上述示例对于 Color#isEqual 则全部返回 `true`.

除非需要考虑多版本兼容, 否则建议始终使用 `Color#isEqual` 替代 `Color#equals`.

## [m#] luminance {#colortype_m_luminance}

### luminance() {#colortype_luminance}

**`6.3.0`**

- **returns** { Range[0..1] (dataTypes.html#datatypes_range) } - 颜色亮度

获取颜色的 亮度 (Luminance) (glossaries.html#glossaries_luminance), 取值范围 `[0..1]`.

```js
Color(colors.WHITE).luminance(); // 1
Color(colors.BLACK).luminance(); // 0
Color(colors.RED).luminance(); // 0.2126
Color(colors.GREEN).luminance(); // 0.7152
Color(colors.BLUE).luminance(); // 0.0722
Color(colors.YELLOW).luminance(); // 0.9278
```

参阅: W3C Wiki (https://www.w3.org/WAI/GL/wiki/Relative_luminance)

## [m#] toColorStateList {#colortype_m_tocolorstatelist}

### toColorStateList() {#colortype_tocolorstatelist}

**`6.3.0`**

- **returns** { android.content.res.ColorStateList (https://developer.android.com/reference/android/content/res/ColorStateList) }

将颜色实例转换为包含单一颜色的 ColorStateList 实例.

```js
Color('red').toColorStateList(); /* 包含单一颜色的 ColorStateList. */
```

## [m#] setPaintColor {#colortype_m_setpaintcolor}

### setPaintColor(paint) {#colortype_setpaintcolor_paint}

**`6.3.0`**

- **color** { ColorHex (dataTypes.html#datatypes_colorhex) | ColorInt (dataTypes.html#datatypes_colorint) | ColorName (dataTypes.html#datatypes_colorname) } - 颜色参数
- **returns** { Color (colorType.html) }

方法 `setPaintColor` 用于解决在 `Android API 29 (10) [Q]` 及以上系统中 `Paint#setColor(color)` 无法正常设置画笔颜色的问题.

```js
let paint = new android.graphics.Paint();

/* 安卓 10 及以上系统无法正常设置颜色. */
// paint.setColor(colors.toInt('blue'));

/* 使用 Color 类实现原始功能. */
Color('blue').setPaintColor(paint);
```

更多 setPaintColor 相关内容, 参阅 colors.setPaintColor (color.html#color_m_setpaintcolor) 小节.
