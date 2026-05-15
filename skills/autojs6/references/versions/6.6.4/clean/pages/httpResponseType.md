---
title: "HttpResponse"
version: "6.6.4"
source_html: "raw/httpResponseType.html"
---

# HttpResponse {#httpresponsetype_httpresponse}

此章节待补充或完善...

Marked by SuperMonster003 on Mar 21, 2023.

HTTP 请求回应类 HttpResponse 是一个虚拟类, 实例通常由 http (http.html) 全局模块产生:

```js
/* HttpResponse 为虚拟类, 并非真实存在. */
typeof global.HttpResponse; // "undefined"
```

常见相关方法或属性:

- http.get (http.html#http_m_get)
- http.post (http.html#http_m_post)
- http.postMultipart (http.html#http_m_postmultipart)
- http.request (http.html#http_m_request)

HttpResponse

## [p#] statusCode {#httpresponsetype_p_statuscode}

- { number (dataTypes.html#datatypes_number) }

...

## [p#] statusMessage {#httpresponsetype_p_statusmessage}

- { string (dataTypes.html#datatypes_string) }

...

## [p#] body {#httpresponsetype_p_body}

- { HttpResponseBody (httpResponseBodyType.html) }

...

## [p#] method {#httpresponsetype_p_method}

- { string (dataTypes.html#datatypes_string) }

...

## [p#] url {#httpresponsetype_p_url}

- { Okhttp3HttpUrl (okhttp3HttpUrlType.html) }

...

## [p#] request {#httpresponsetype_p_request}

- { Okhttp3Request (okhttp3RequestType.html) }

当前响应对应的请求, 是一个 Okhttp3Request (okhttp3RequestType.html) 实例.

```js
http.get('https://www.msn.com').request.method(); // GET
```

## [p#] headers {#httpresponsetype_p_headers}

- { HttpResponseHeaders (httpResponseHeadersType.html) }

当前响应的 响应标头 (httpHeaderGlossary.html#httpheaderglossary_响应标头) 信息, 是一个 JavaScript 对象.

该对象的 `键 (Key)` 是响应头名称, `值 (Value)` 是对应的响应头数据.

所有响应头名称均为小写形式.

```js
Object.entries(http.get('https://www.msn.com').headers).forEach((entry) => {
    let [ key, value ] = entry;
    console.log(`${key}: ${value}`);
});
```

# ResponseLegacy {#httpresponsetype_responselegacy}

HTTP请求的响应.

## Response.statusCode {#httpresponsetype_response_statuscode}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

当前响应的HTTP状态码. 例如200(OK), 404(Not Found)等.

有关HTTP状态码的信息, 参见菜鸟教程：HTTP状态码 (http://www.runoob.com/http/http-status-codes.html).

## Response.statusMessage {#httpresponsetype_response_statusmessage}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

当前响应的HTTP状态信息. 例如"OK", "Bad Request", "Forbidden".

有关HTTP状态码的信息, 参见菜鸟教程：HTTP状态码 (http://www.runoob.com/http/http-status-codes.html).

例子：

```
var res = http.get("www.baidu.com");
if(res.statusCode >= 200 && res.statusCode < 300){
    toast("页面获取成功!");
}else if(res.statusCode == 404){
    toast("页面没找到哦...");
}else{
    toast("错误: " + res.statusCode + " " + res.statusMessage);
}
```

## Response.body {#httpresponsetype_response_body}

- { Object (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) }

当前响应的内容. 他有以下属性和函数：

- bytes() { Array (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) } 以字节数组形式返回响应内容
- string() { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 以字符串形式返回响应内容
- json() { Object (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) } 把响应内容作为JSON格式的数据并调用JSON.parse, 返回解析后的对象
- contentType { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 当前响应的内容类型

## Response.url {#httpresponsetype_response_url}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 当前响应所对应的请求URL.

## Response.method {#httpresponsetype_response_method}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 当前响应所对应的HTTP请求的方法. 例如"GET", "POST", "PUT"等.
