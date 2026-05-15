---
title: "Base64"
version: "6.6.4"
source_html: "raw/base64.html"
---

# Base64 {#base64_base64}

Base64 是一种编码方式, 同时可作为一种数据的存储格式, 并非严格意义上的加密与解密.

base64 模块主要用于对数据进行 Base64 编码及解码.

注: 与 crypto (crypto.html) 模块不同, crypto 模块主要用于信息的加密与解密.

参阅:
Wikipedia (英) (https://en.wikipedia.org/wiki/Base64) / Wikipedia (中) (https://zh.wikipedia.org/wiki/Base64)
Base64 笔记 (from 阮一峰的网络日志) (http://www.ruanyifeng.com/blog/2008/06/base64.html)
Base64 是加密算法吗 (from 稀土掘金) (https://juejin.cn/post/6887498543494660109)

## 可逆性 {#base64}

Base64 是一种可逆的编码方式:

```js
console.log(base64.decode(base64.encode('orange'))); // orange
console.log(base64.decode(base64.encode('简体中文'))); // 简体中文
```

但需注意参数的字符编码方式 (默认为 `UTF-8`), 当存在超出编码表示范围的字符时, 可逆性将遭到破坏:

```js
/* us-ascii 编码无法表示 "出" 和 "口". */
console.log(base64.decode(base64.encode('E2 出口', 'us-ascii'), 'us-ascii')); // E2 ??
```

编解码使用了不同的编码方式, 也可能导致可逆性失效:

```js
/* utf-16 与 utf-8 不一致. */
console.log(base64.decode(base64.encode('简体中文', 'utf-16'), 'utf-8')); // ��{�OSN-e�
```

base64

## [m] encode {#base64_m_encode}

### encode(o, encoding?) {#base64_encode_o_encoding}

- **o** { string (dataTypes.html#datatypes_string) | JsByteArray (dataTypes.html#datatypes_jsbytearray) | ByteArray (dataTypes.html#datatypes_bytearray) } - 待编码数据
- **[ encoding = `'UTF_8'` ]** { StandardCharset (dataTypes.html#datatypes_standardcharset) } - 字符编码
- **returns** { string (dataTypes.html#datatypes_string) }

对数据进行 Base64 编码.

```js
/* 字符串. */

console.log(base64.encode('hello', 'iso-8859-1')); // aGVsbG8=
console.log(base64.encode('hello', 'us-ascii')); // aGVsbG8=
console.log(base64.encode('hello', 'utf-8')); // aGVsbG8=
console.log(base64.encode('hello', 'utf-16')); // /v8AaABlAGwAbABv
console.log(base64.encode('hello', 'utf-16be')); // AGgAZQBsAGwAbw==
console.log(base64.encode('hello', 'utf-16le')); // aABlAGwAbABvAA==

/* JavaScript 字节数组. */

console.log(base64.encode([ 104, 101, 108, 108, 111 ], 'utf-8')); // aGVsbG8=

/* Java 字节数组. */

console.log(base64.encode(new java.lang.String('hello').getBytes(), 'utf-8')); // aGVsbG8=

let jsArr = [ 104, 101, 108, 108, 111 ];
let javaArr = util.java.array('byte', jsArr.length);
jsArr.forEach((o, i) => javaArr[i] = o);
console.log(base64.encode(javaArr, 'utf-8')); /* 效果同上. */
```

## [m] decode {#base64_m_decode}

### decode(o, encoding?) {#base64_decode_o_encoding}

- **o** { string (dataTypes.html#datatypes_string) | JsByteArray (dataTypes.html#datatypes_jsbytearray) | ByteArray (dataTypes.html#datatypes_bytearray) } - 待解码数据
- **[ encoding = `'UTF_8'` ]** { StandardCharset (dataTypes.html#datatypes_standardcharset) } - 字符编码
- **returns** { string (dataTypes.html#datatypes_string) }

对数据进行 Base64 解码.

```js
/* 字符串. */

console.log(base64.decode('aGVsbG8=', 'iso-8859-1')); // hello
console.log(base64.decode('aGVsbG8=', 'us-ascii')); // hello
console.log(base64.decode('aGVsbG8=', 'utf-8')); // hello
console.log(base64.decode('/v8AaABlAGwAbABv', 'utf-16')); // hello
console.log(base64.decode('AGgAZQBsAGwAbw==', 'utf-16be')); // hello
console.log(base64.decode('aABlAGwAbABvAA==', 'utf-16le')); // hello

/* JavaScript 字节数组. */

console.log(base64.decode([ 97, 71, 86, 115, 98, 71, 56, 61 ], 'utf-8')); // hello

/* Java 字节数组. */

console.log(base64.decode(new java.lang.String('aGVsbG8=').getBytes(), 'utf-8')); // hello

let jsArr = [ 97, 71, 86, 115, 98, 71, 56, 61 ];
let javaArr = util.java.array('byte', jsArr.length);
jsArr.forEach((o, i) => javaArr[i] = o);
console.log(base64.decode(javaArr, 'utf-8')); /* 效果同上. */
```
