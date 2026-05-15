---
title: "Storage (存储类)"
version: "6.6.4"
source_html: "raw/storageType.html"
---

# Storage (存储类) {#storagetype_storage}

存储类 Storage 是一个虚拟类, 实例通常由 storages (storages.html) 全局模块产生:

```js
/* Storage 为虚拟类, 并非真实存在. */
typeof global.Storage; // "undefined"

let sto = storages.create('test');
sto._storage instanceof org.autojs.autojs.core.storage.LocalStorage; // true
```

常见相关方法或属性:

- storages.create (storages.html#storages_m_create)

Storage

## [m#] put {#storagetype_m_put}

### put(key, value) {#storagetype_put_key_value}

**`[6.3.0]`**

- **key** { string (dataTypes.html#datatypes_string) } - 待存入键名
- **value** { AnyBut (dataTypes.html#datatypes_anybut)< (dataTypes.html#datatypes_generic)undefined (dataTypes.html#datatypes_undefined), bigint (glossaries.html#glossaries_bigint)> (dataTypes.html#datatypes_generic) } - 待存入数据
- **returns** { Storage (storageType.html) }

将 `value` 参数经 JSON 序列化后, 与 `key` 参数以键值对形式存入本地存储.

支持存入的数据类型:

- number (dataTypes.html#datatypes_number)
- boolean (dataTypes.html#datatypes_boolean)
- string (dataTypes.html#datatypes_string)
- null (dataTypes.html#datatypes_null)
- Array (dataTypes.html#datatypes_array)
- Object (dataTypes.html#datatypes_object)
- ... ...

理论上, 除 undefined (dataTypes.html#datatypes_undefined) 和 bigint (glossaries.html#glossaries_bigint) 外的任意类型数据均可存入本地存储,
试图存入不支持类型的数据时, 将抛出异常.

存入时, 由 JSON.stringify (https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) 序列化数据为 string (dataTypes.html#datatypes_string) 类型后再存入,
因此数据转换时遵循 JSON 序列化规则 (如 NaN 将被转换为 null 等).

```js
let sto = storages.create('fruit');
sto.put('total', 500); /* 存入数字. */
sto.put('products', [ 'apple', 'banana' ]); /* 存入数组时将被 JSON 序列化.  */
```

链式调用:

```js
let sto = storages.create('test');
sto.put('a', 1).put('b', 2).put('c', 3).put('d', 4);
```

## [m#] get {#storagetype_m_get}

### get(key, defaultValue?) {#storagetype_get_key_defaultvalue}

**`Overload [1-2]/2`**

- **key** { string (dataTypes.html#datatypes_string) } - 数据的键名
- **[ defaultValue ]** { any (dataTypes.html#datatypes_any) } - 数据默认值
- **returns** { any (dataTypes.html#datatypes_any) }

读取本地存储中键值与 `key` 参数对应的数据.

当本地存储中不存在键值 `key` 时, 返回 undefined (dataTypes.html#datatypes_undefined).

本地存储中返回的数据, 来源于 put 方法的 value 参数:

```js
let sto = storages.create('test');

sto.put('apple', 10); /* 原始数据是 number 类型的 10. */
sto.get('apple'); /* 获取的数据依然是 number 类型的 10. */

sto.put('fruits', [ 'apple', 'banana' ]); /* 原始数据是字符串数组. */
sto.get('fruits'); /* 获取的数据还原为同类型的字符串数组, 即 ['apple', 'banana']. */
```

存入时, 由 JSON.stringify (https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) 序列化数据为 string (dataTypes.html#datatypes_string) 类型后再存入,
读取时, 由 JSON.parse (https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) 还原为原本的数据类型.

因此部分数据受 JSON 序列化的影响, 可能导致读取数据与原始数据存在差距:

```js
sto.put('apple', NaN); /* 原始数据是 number 类型的 NaN. */
sto.get('apple'); /* 获取的数据是 null. */
```

## [m#] contains {#storagetype_m_contains}

### contains(key) {#storagetype_contains_key}

- **key** { string (dataTypes.html#datatypes_string) } - 键名
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回本地存储中是否存在键值 `key`.

```js
let sto = storages.create('fruit');
if (!sto.contains('apple')) {
    sto.put('apple', 10);
}
```

## [m#] remove {#storagetype_m_remove}

### remove(key) {#storagetype_remove_key}

- **key** { string (dataTypes.html#datatypes_string) } - 键名
- **returns** { Storage (storageType.html) }

移除本地存储中键值 `key` 对应的数据.

```js
let sto = storages.create('fruit');
sto.remove('apple').remove('banana').remove('cherry');
```

## [m#] clear {#storagetype_m_clear}

### clear() {#storagetype_clear}

- **returns** { void (dataTypes.html#datatypes_void) }

清除本地存储所有数据.

```js
let sto = storages.create('fruit');
sto.put('apple', 10);
sto.get('apple'); // 10
sto.clear();
sto.get('apple'); // undefined
```
