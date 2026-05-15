---
title: "Okhttp3Request"
version: "6.6.4"
source_html: "raw/okhttp3RequestType.html"
---

# Okhttp3Request {#okhttp3requesttype_okhttp3request}

此章节待补充或完善...

Marked by SuperMonster003 on Mar 2, 2023.

okhttp3.Request (https://square.github.io/okhttp/3.x/okhttp/okhttp3/Request.html) 别名.

Okhttp3Request 表示一个 HTTP 请求.

```js
let request = new okhttp3.Request.Builder()
    .url('https://www.msn.com')
    .method('GET', null)
    .build();

// Request{method=GET, url=https://www.msn.com/}
console.log(request);
```

常见相关方法或属性:

- httpResponseType#request (httpResponseType.html#httpresponsetype_p_request)
- okhttp3.Request.Builder#build (https://square.github.io/okhttp/3.x/okhttp/okhttp3/Request.Builder.html#https://square.github.io/okhttp/3.x/okhttp/okhttp3/request.builder_build__)

注: 本章节仅列出部分属性或方法.

okhttp3.Request

## [m] body {#okhttp3requesttype_m_body}

### body() {#okhttp3requesttype_body}

- **returns** { okhttp3.RequestBody (https://square.github.io/okhttp/3.x/okhttp/okhttp3/RequestBody.html) | null (dataTypes.html#datatypes_null) }

获取 HTTP 请求的 "请求体 (Request Body)".

## [m] cacheControl {#okhttp3requesttype_m_cachecontrol}

### cacheControl() {#okhttp3requesttype_cachecontrol}

- **returns** { okhttp3.CacheControl (https://square.github.io/okhttp/3.x/okhttp/okhttp3/CacheControl.html) }

获取 HTTP 请求标头字段 cache-control (httpRequestHeadersType.html#httprequestheaderstype_p_cache_control) 的信息.

```js
let cacheControl = http.get('https://www.msn.com', {
    headers: {
        'cache-control': 'no-transform, no-store, no-cache',
    },
    contentType: 'text/plain',
}).request.cacheControl();

console.log(cacheControl); // no-transform, no-store, no-cache
console.log(cacheControl.noTransform()); // true
console.log(cacheControl.noStore()); // true
console.log(cacheControl.mustRevalidate()); // false
```
