---
title: "InjectableWebView"
version: "6.6.4"
source_html: "raw/injectableWebViewType.html"
---

# InjectableWebView {#injectablewebviewtype_injectablewebview}

android.webkit.WebView (https://developer.android.com/reference/android/webkit/WebView) 的子类.

常见相关方法或属性:

- web.newInjectableWebView (web.html#web_m_newinjectablewebview)

注: 本章节仅列出 InjectableWebView 独有的而不包含继承的属性及方法.

InjectableWebView

## [m#] inject {#injectablewebviewtype_m_inject}

### inject(script, callback?) {#injectablewebviewtype_inject_script_callback}

**`Overload [1-2]/2`**

- **script** { string (dataTypes.html#datatypes_string) } - 脚本
- **[ callback ]** { ( (dataTypes.html#datatypes_function)value: string (dataTypes.html#datatypes_string)) (dataTypes.html#datatypes_function) => (dataTypes.html#datatypes_function) void (dataTypes.html#datatypes_void) } - 脚本
- **returns** { void (dataTypes.html#datatypes_void) }

注入 `script` 参数提供的 JavaScript 脚本, `callback` 回调参数可用于获取脚本语句的执行结果.

```js
'ui';
let webView = web.newInjectableWebView('www.github.com');
webView.inject('navigator.userAgent', value => console.log(value));
activity.setContentView(webView);
```
