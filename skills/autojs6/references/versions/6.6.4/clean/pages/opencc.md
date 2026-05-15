---
title: "OpenCC"
version: "6.6.4"
source_html: "raw/opencc.html"
---

# OpenCC {#opencc_opencc}

OpenCC, 全称 "Open Chinese Convert", 译为 "开放中文转换".

opencc 模块是一个中文简繁转换模块, 支持词汇级别的转换, 异体字转换和地区习惯用词转换 (中国大陆/台湾/香港/日本新字体).

参阅:
OpenCC 官方网站: https://opencc.byvoid.com (https://opencc.byvoid.com)
OpenCC 官方文档: https://byvoid.github.io/OpenCC (https://byvoid.github.io/OpenCC)
OpenCC 开源项目: https://github.com/BYVoid/OpenCC (https://github.com/BYVoid/OpenCC)
OpenCC (Android) 开源项目: https://github.com/qichuan/android-opencc (https://github.com/qichuan/android-opencc)

下表列举了一些简体中文的转换示例:

程序员 文档 文件 文件夹 荞麦面 心里为之喜悦 繁体 程序員 文檔 文件 文件夾 蕎麥麪 心裏爲之喜悅 香港繁体 程序員 文檔 文件 文件夾 蕎麥麪 心裏為之喜悦 台湾正体 程序員 文檔 文件 文件夾 蕎麥麵 心裡為之喜悅 台湾正体 (惯) 程式設計師 文件 檔案 資料夾 蕎麥麵 心裡為之喜悅

注: 表中 "惯" 表示惯用词.

转换方法对照表:

简体 繁体 香港繁体 台湾正体 台湾正体 (惯) 日本汉字 简体 - s2t s2hk s2tw s2twi < s2jp > 繁体 t2s - t2hk t2tw < t2twi > t2jp 香港繁体 hk2s hk2t - < hk2tw > < hk2twi > < hk2jp > 台湾正体 tw2s tw2t < tw2hk > - < tw2twi > < tw2jp > 台湾正体 (惯) twi2s < twi2t > < twi2hk > < twi2tw > - << twi2jp >> 日本汉字 < jp2s > jp2t < jp2hk > < jp2tw > << jp2twi >> -

注:

尖括号表示 AutoJs6 封装方法, 内部经 1 次转换.
双尖括号表示 AutoJs6 封装方法, 内部经 2 次转换.

台湾正体存在惯用词.
在转换时, 如涉及到台湾正体, 方法名称将以 "twi" 体现惯用词转换.
如 twi2s 表示台湾正体转简体并应用惯用词转换.
再如 hk2twi 表示香港繁体转台湾正体并应用惯用词转换.

opencc

## [@] opencc {#opencc_opencc_1}

opencc 可作为全局对象使用:

```js
typeof opencc; // "function"
typeof opencc.convert; // "function"
```

### opencc(s, type) {#opencc_opencc_s_type}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **type** { OpenCCConversion (openCCConversionType.html) } - 转换类型
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

将字符串转换为目标类型.

```js
/* 简体. */
let s = '鼠标里面的硅二极管坏了, 导致光标分辨率降低';

/* 繁體 (臺灣正體標準) [惯用词]. */
let t = '滑鼠裡面的矽二極體壞了, 導致游標解析度降低';

/* s 转换为 t. */
console.log(opencc(s, 'S2TWI'));

/* t 转换为 s. */
console.log(opencc(t, 'TWI2S'));
```

`opencc(s, type)` 与 opencc.convert(s, type) 等价.

## [m] convert {#opencc_m_convert}

### convert(s, type) {#opencc_convert_s_type}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **type** { OpenCCConversion (openCCConversionType.html) } - 转换类型
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

将字符串转换为目标类型.

`opencc.convert(s, type)` 与 opencc(s, type) 等价.

## [m] s2t {#opencc_m_s2t}

### s2t(s) {#opencc_s2t_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从简体到繁体.

相当于 `opencc(s, 'S2T')`;

```js
let str = '心里为何充满喜悦';
console.log(opencc.s2t(str)); // 心裏爲何充滿喜悅
console.log(opencc(str, 'S2T')); /* 同上. */
```

注: s2t 的逆转换方法为 t2s.

## [m] s2hk {#opencc_m_s2hk}

### s2hk(s) {#opencc_s2hk_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从简体到香港繁体 (香港小学学习字词表标准).

相当于 `opencc(s, 'S2HK')`;

```js
let str = '心里为何充满喜悦';
console.log(opencc.s2hk(str)); // 心裏為何充滿喜悦
console.log(opencc(str, 'S2HK')); /* 同上. */
```

注: s2hk 的逆转换方法为 hk2s.

## [m] s2tw {#opencc_m_s2tw}

### s2tw(s) {#opencc_s2tw_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从简体到台湾正体.

相当于 `opencc(s, 'S2TW')`;

```js
let str = '心里为何充满喜悦';
console.log(opencc.s2tw(str)); // 心裡為何充滿喜悅
console.log(opencc(str, 'S2TW')); /* 同上. */
```

注: s2tw 的逆转换方法为 tw2s.

## [m] s2twi {#opencc_m_s2twi}

### s2twi(s) {#opencc_s2twi_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从简体到繁体 (台湾正体标准) [惯用词].

相当于 `opencc(s, 'S2TWI')`;

```js
let strA = '心里为何充满喜悦';
console.log(opencc.s2twi(strA)); // 心裡為何充滿喜悅
console.log(opencc(strA, 'S2TWI')); /* 同上. */

let strB = '使用鼠标完成文件重命名操作';
console.log(opencc.s2twi(strB)); // 使用滑鼠完成檔案重新命名操作
console.log(opencc(strB, 'S2TWI')); /* 同上. */
```

注: s2twi 的逆转换方法为 twi2s.

## [m] s2jp {#opencc_m_s2jp}

### s2jp(s) {#opencc_s2jp_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从简体到日本汉字.

相当于 `opencc(s, 'S2JP')`.

```js
let str = '黑/废/泪/稻/亚';
console.log(opencc.s2jp(str)); // 黒/廃/涙/稲/亜
console.log(opencc(str, 'S2JP')); /* 同上. */
```

注: s2jp 的逆转换方法为 jp2s.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
s2t -> t2jp
```

## [m] t2s {#opencc_m_t2s}

### t2s(s) {#opencc_t2s_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体到简体.

相当于 `opencc(s, 'T2S')`;

```js
let str = '心裏爲何充滿喜悅';
console.log(opencc.t2s(str)); // 心里为何充满喜悦
console.log(opencc(str, 'T2S')); /* 同上. */
```

注: t2s 的逆转换方法为 s2t.

## [m] t2hk {#opencc_m_t2hk}

### t2hk(s) {#opencc_t2hk_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体到香港繁体 (香港小学学习字词表标准).

相当于 `opencc(s, 'T2HK')`;

```js
let str = '心裏爲何充滿喜悅';
console.log(opencc.t2hk(str)); // 心裏為何充滿喜悦
console.log(opencc(str, 'T2HK')); /* 同上. */
```

注: t2hk 的逆转换方法为 hk2t.

## [m] t2tw {#opencc_m_t2tw}

### t2tw(s) {#opencc_t2tw_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体到台湾正体.

相当于 `opencc(s, 'T2TW')`;

```js
let str = '心裏爲何充滿喜悅';
console.log(opencc.t2tw(str)); // 心裡為何充滿喜悅
console.log(opencc(str, 'T2TW')); /* 同上. */
```

注: t2tw 的逆转换方法为 tw2t.

## [m] t2twi {#opencc_m_t2twi}

### t2twi(s) {#opencc_t2twi_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体到台湾正体 [惯用词].

相当于 `opencc(s, 'T2TWI')`.

```js
let strA = '心裏爲何充滿喜悅';
console.log(opencc.t2twi(strA)); // 心裡為何充滿喜悅
console.log(opencc(strA, 'T2TWI')); /* 同上. */

let strB = '使用鼠標完成文件重命名操作';
console.log(opencc.t2twi(strB)); // 使用滑鼠完成檔案重新命名操作
console.log(opencc(strB, 'T2TWI')); /* 同上. */
```

注: t2twi 的逆转换方法为 twi2t.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
t2s -> s2twi
```

## [m] t2jp {#opencc_m_t2jp}

### t2jp(s) {#opencc_t2jp_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体到日本汉字.

相当于 `opencc(s, 'T2JP')`;

```js
let str = '黑/廢/淚/稻/亞';
console.log(opencc.t2jp(str)); // 黒/廃/涙/稲/亜
console.log(opencc(str, 'T2JP')); /* 同上. */
```

注: t2jp 的逆转换方法为 jp2t.

## [m] hk2s {#opencc_m_hk2s}

### hk2s(s) {#opencc_hk2s_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从香港繁体 (香港小学学习字词表标准) 到简体.

相当于 `opencc(s, 'HK2S')`;

```js
let str = '心裏為何充滿喜悦';
console.log(opencc.hk2s(str)); // 心里为何充满喜悦
console.log(opencc(str, 'HK2S')); /* 同上. */
```

注: hk2s 的逆转换方法为 s2hk.

## [m] hk2t {#opencc_m_hk2t}

### hk2t(s) {#opencc_hk2t_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从香港繁体 (香港小学学习字词表标准) 到繁体.

相当于 `opencc(s, 'HK2T')`;

```js
let str = '心裏為何充滿喜悦';
console.log(opencc.hk2t(str)); // 心裏爲何充滿喜悅
console.log(opencc(str, 'HK2T')); /* 同上. */
```

注: hk2t 的逆转换方法为 t2hk.

## [m] hk2tw {#opencc_m_hk2tw}

### hk2tw(s) {#opencc_hk2tw_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从香港繁体 (香港小学学习字词表标准) 到台湾正体.

相当于 `opencc(s, 'HK2TW')`.

```js
let str = '心裏為何充滿喜悦';
console.log(opencc.hk2tw(str)); // 心裡為何充滿喜悅
console.log(opencc(str, 'HK2TW')); /* 同上. */
```

注: hk2tw 的逆转换方法为 tw2hk.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
hk2t -> t2tw
```

## [m] hk2twi {#opencc_m_hk2twi}

### hk2twi(s) {#opencc_hk2twi_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从香港繁体 (香港小学学习字词表标准) 到台湾正体 [惯用词].

相当于 `opencc(s, 'HK2TWI')`.

```js
let strA = '心裏為何充滿喜悦';
console.log(opencc.hk2twi(strA)); // 心裡為何充滿喜悅
console.log(opencc(strA, 'HK2TWI')); /* 同上. */

let strB = '使用鼠標完成文件重命名操作';
console.log(opencc.hk2twi(strB)); // 使用滑鼠完成檔案重新命名操作
console.log(opencc(strB, 'HK2TWI')); /* 同上. */
```

注: hk2twi 的逆转换方法为 twi2hk.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
hk2s -> s2twi
```

## [m] hk2jp {#opencc_m_hk2jp}

### hk2jp(s) {#opencc_hk2jp_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从香港繁体 (香港小学学习字词表标准) 到日本汉字.

相当于 `opencc(s, 'HK2JP')`.

```js
let str = '黑/廢/淚/稻/亞';
console.log(opencc.hk2jp(str)); // 黒/廃/涙/稲/亜
console.log(opencc(str, 'HK2JP')); /* 同上. */
```

注: hk2jp 的逆转换方法为 jp2hk.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
hk2t -> t2jp
```

## [m] tw2s {#opencc_m_tw2s}

### tw2s(s) {#opencc_tw2s_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体到简体.

相当于 `opencc(s, 'TW2S')`;

```js
let str = '心裡為何充滿喜悅';
console.log(opencc.tw2s(str)); // 心里为何充满喜悦
console.log(opencc(str, 'TW2S')); /* 同上. */
```

注: tw2s 的逆转换方法为 s2tw.

## [m] tw2t {#opencc_m_tw2t}

### tw2t(s) {#opencc_tw2t_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体到繁体.

相当于 `opencc(s, 'TW2T')`;

```js
let str = '心裡為何充滿喜悅';
console.log(opencc.tw2t(str)); // 心裏爲何充滿喜悅
console.log(opencc(str, 'TW2T')); /* 同上. */
```

注: tw2t 的逆转换方法为 t2tw.

## [m] tw2hk {#opencc_m_tw2hk}

### tw2hk(s) {#opencc_tw2hk_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体到香港繁体 (香港小学学习字词表标准).

相当于 `opencc(s, 'TW2HK')`.

```js
let str = '心裡為何充滿喜悅';
console.log(opencc.tw2hk(str)); // 心裏為何充滿喜悦
console.log(opencc(str, 'TW2HK')); /* 同上. */
```

注: tw2hk 的逆转换方法为 hk2tw.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
tw2t -> t2hk
```

## [m] tw2twi {#opencc_m_tw2twi}

### tw2twi(s) {#opencc_tw2twi_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体到台湾正体 [惯用词].

相当于 `opencc(s, 'TW2TWI')`.

```js
let str = '使用鼠標完成文件重命名操作';
console.log(opencc.tw2twi(str)); // 使用滑鼠完成檔案重新命名操作
console.log(opencc(str, 'TW2TWI')); /* 同上. */
```

注: tw2twi 的逆转换方法为 twi2tw.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
tw2s -> s2twi
```

## [m] tw2jp {#opencc_m_tw2jp}

### tw2jp(s) {#opencc_tw2jp_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体到日本汉字.

相当于 `opencc(s, 'TW2JP')`.

```js
let str = '黑/廢/淚/稻/亞';
console.log(opencc.tw2jp(str)); // 黒/廃/涙/稲/亜
console.log(opencc(str, 'TW2JP')); /* 同上. */
```

注: tw2jp 的逆转换方法为 jp2tw.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
tw2t -> t2jp
```

## [m] twi2s {#opencc_m_twi2s}

### twi2s(s) {#opencc_twi2s_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从繁体 (台湾正体标准) [惯用词] 到简体.

相当于 `opencc(s, 'TWI2S')`;

```js
let strA = '心裡為何充滿喜悅';
console.log(opencc.twi2s(strA)); // 心里为何充满喜悦
console.log(opencc(strA, 'TWI2S')); /* 同上. */

let strB = '使用滑鼠完成檔案重新命名操作';
console.log(opencc.twi2s(strB)); // 使用鼠标完成文件重命名操作
console.log(opencc(strB, 'TWI2S')); /* 同上. */
```

注: twi2s 的逆转换方法为 s2twi.

## [m] twi2t {#opencc_m_twi2t}

### twi2t(s) {#opencc_twi2t_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体 [惯用词] 到繁体.

相当于 `opencc(s, 'TWI2T')`.

```js
let strA = '心裡為何充滿喜悅';
console.log(opencc.twi2t(strA)); // 心裏爲何充滿喜悅
console.log(opencc(strA, 'TWI2T')); /* 同上. */

let strB = '使用滑鼠完成檔案重新命名操作';
console.log(opencc.twi2t(strB)); // 使用鼠標完成文件重命名操作
console.log(opencc(strB, 'TWI2T')); /* 同上. */
```

注: twi2t 的逆转换方法为 t2twi.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
twi2s -> s2t
```

## [m] twi2hk {#opencc_m_twi2hk}

### twi2hk(s) {#opencc_twi2hk_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体 [惯用词] 到香港繁体 (香港小学学习字词表标准).

相当于 `opencc(s, 'TWI2HK')`.

```js
let strA = '心裡為何充滿喜悅';
console.log(opencc.twi2hk(strA)); // 心裏為何充滿喜悦
console.log(opencc(strA, 'TWI2HK')); /* 同上. */

let strB = '使用滑鼠完成檔案重新命名操作';
console.log(opencc.twi2hk(strB)); // 使用鼠標完成文件重命名操作
console.log(opencc(strB, 'TWI2HK')); /* 同上. */
```

注: twi2hk 的逆转换方法为 hk2twi.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
twi2s -> s2hk
```

## [m] twi2tw {#opencc_m_twi2tw}

### twi2tw(s) {#opencc_twi2tw_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体 [惯用词] 到台湾正体.

相当于 `opencc(s, 'TWI2TW')`.

```js
let str = '使用滑鼠完成檔案重新命名操作';
console.log(opencc.twi2tw(str)); // 使用鼠標完成文件重命名操作
console.log(opencc(str, 'TWI2TW')); /* 同上. */
```

注: twi2tw 的逆转换方法为 tw2twi.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
twi2s -> s2tw
```

## [m] twi2jp {#opencc_m_twi2jp}

### twi2jp(s) {#opencc_twi2jp_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从台湾正体 [惯用词] 到日本汉字.

相当于 `opencc(s, 'TWI2JP')`.

```js
let str = '黑/廢/淚/稻/亞';
console.log(opencc.twi2jp(str)); // 黒/廃/涙/稲/亜
console.log(opencc(str, 'TWI2JP')); /* 同上. */
```

注: twi2jp 的逆转换方法为 jp2twi.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
twi2s -> s2t -> t2jp
```

## [m] jp2s {#opencc_m_jp2s}

### jp2s(s) {#opencc_jp2s_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从日本汉字到简体.

相当于 `opencc(s, 'JP2S')`.

```js
let str = '黒/廃/涙/稲/亜';
console.log(opencc.jp2s(str)); // 黑/废/泪/稻/亚
console.log(opencc(str, 'JP2S')); /* 同上. */
```

注: jp2s 的逆转换方法为 s2jp.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
jp2t -> t2s
```

## [m] jp2t {#opencc_m_jp2t}

### jp2t(s) {#opencc_jp2t_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从日本汉字到繁体.

相当于 `opencc(s, 'JP2T')`;

```js
let str = '黒/廃/涙/稲/亜';
console.log(opencc.jp2t(str)); // 黑/廢/淚/稻/亞
console.log(opencc(str, 'JP2T')); /* 同上. */
```

注: jp2t 的逆转换方法为 2tjp.

## [m] jp2hk {#opencc_m_jp2hk}

### jp2hk(s) {#opencc_jp2hk_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从日本汉字到香港繁体 (香港小学学习字词表标准).

相当于 `opencc(s, 'JP2HK')`.

```js
let str = '黒/廃/涙/稲/亜';
console.log(opencc.jp2hk(str)); // 黑/廢/淚/稻/亞
console.log(opencc(str, 'JP2HK')); /* 同上. */
```

注: jp2hk 的逆转换方法为 hk2jp.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
jp2t -> t2hk
```

## [m] jp2tw {#opencc_m_jp2tw}

### jp2tw(s) {#opencc_jp2tw_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从日本汉字到台湾正体.

相当于 `opencc(s, 'JP2TW')`.

```js
let str = '黒/廃/涙/稲/亜';
console.log(opencc.jp2tw(str)); // 黑/廢/淚/稻/亞
console.log(opencc(str, 'JP2TW')); /* 同上. */
```

注: jp2tw 的逆转换方法为 tw2jp.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
jp2t -> t2tw
```

## [m] jp2twi {#opencc_m_jp2twi}

### jp2twi(s) {#opencc_jp2twi_s}

**`6.5.0`**

- **s** { string (dataTypes.html#datatypes_string) } - 待转换字符串
- **returns** { string (dataTypes.html#datatypes_string) } - 转换结果

字符串转换, 从日本汉字到台湾正体 [惯用词].

相当于 `opencc(s, 'JP2TWI')`.

```js
let str = '黒/廃/涙/稲/亜';
console.log(opencc.jp2twi(str)); // 黑/廢/淚/稻/亞
console.log(opencc(str, 'JP2TWI')); /* 同上. */
```

注: jp2twi 的逆转换方法为 twi2jp.

此方法为 AutoJs6 封装方法, 内部进行如下转换:

```text
jp2t -> t2s -> s2twi
```
