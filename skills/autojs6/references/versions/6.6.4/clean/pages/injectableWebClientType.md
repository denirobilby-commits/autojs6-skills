---
title: "InjectableWebClient"
version: "6.6.4"
source_html: "raw/injectableWebClientType.html"
---

# InjectableWebClient {#injectablewebclienttype_injectablewebclient}

android.webkit.WebViewClient (https://developer.android.com/reference/android/webkit/WebViewClient) 的子类.

常见相关方法或属性:

- web.newInjectableWebClient (web.html#web_m_newinjectablewebclient)

注: 本章节仅列出 InjectableWebClient 独有的而不包含继承的属性及方法.

InjectableWebClient

## [m#] inject {#injectablewebclienttype_m_inject}

### inject(script, callback?) {#injectablewebclienttype_inject_script_callback}

**`Overload [1-2]/2`**

- **script** { string (dataTypes.html#datatypes_string) } - 脚本
- **[ callback ]** { ( (dataTypes.html#datatypes_function)value: string (dataTypes.html#datatypes_string)) (dataTypes.html#datatypes_function) => (dataTypes.html#datatypes_function) void (dataTypes.html#datatypes_void) } - 脚本
- **returns** { void (dataTypes.html#datatypes_void) }

注入 `script` 参数提供的 JavaScript 脚本, `callback` 回调参数可用于获取脚本语句的执行结果.

```js
'ui';

let client = web.newInjectableWebClient();
client.inject('navigator.userAgent', value => console.log(value));

let webView = web.newInjectableWebView('www.github.com');
webView.setWebViewClient(client);
activity.setContentView(webView);
```

## [m#] injectAndWait {#injectablewebclienttype_m_injectandwait}

### injectAndWait(script) {#injectablewebclienttype_injectandwait_script}

**`Overload [1-2]/2`**

- **script** { string (dataTypes.html#datatypes_string) } - 脚本
- **returns** { string (dataTypes.html#datatypes_string) } - 脚本执行结果

注入 `script` 参数提供的 JavaScript 脚本, 等待脚本执行完毕, 返回执行结果.
