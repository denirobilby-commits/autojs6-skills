---
title: "万维网 (Web)"
version: "6.6.4"
source_html: "raw/web.html"
---

# 万维网 (Web) {#web_web}

在应用里显示网页内容, 而不是打开独立的浏览器, 此时可使用 WebView 类, 以实现在 activity (activity.html) 中显示网页内容.

web 模块主要用于 WebView (https://developer.android.com/reference/android/webkit/WebView) 网页的 [ 注入 (Inject) (glossaries.html#glossaries_注入) / 构建客户端 ] 等.

注: 与 http (http.html) 模块不同, http 模块主要用于网络的请求与响应.

web

## [m] newInjectableWebView {#web_m_newinjectablewebview}

### newInjectableWebView(url?) {#web_newinjectablewebview_url}

**`6.3.0`** **`Global`** **`Overload [1-2]/3`** **`UI`**

- **[ url ]** { string (dataTypes.html#datatypes_string) } - 需要 WebView 加载的 URL
- **returns** { InjectableWebView (injectableWebViewType.html) }

新建并返回一个 InjectableWebView (injectableWebViewType.html) (可 注入 (glossaries.html#glossaries_注入) 的 WebView (https://developer.android.com/reference/android/webkit/WebView)) 实例.

```js
'ui';

ui.layout(<vertical>
    <frame id="main"/>
</vertical>);

/* 创建一个 InjectableWebView 实例. */
let webView = newInjectableWebView();
/* 加载指定的 URL, "https://" 也可省略. */
webView.loadUrl('https://www.github.com');
/* 注入 JavaScript 脚本, 显示 alert 消息框. */
webView.inject('alert("hello")');
/* 附加视图对象到 id 为 main 的视图上. */
ui.main.addView(webView);
```

上述示例也可使用 `setContentView` 实现更简单的内容加载 (但不包含代码注入):

```js
'ui';
activity.setContentView(web.newInjectableWebView('www.github.com'));
```

除上述注入简单的 `alert` 消息框外, 还支持其他更多注入方式:

```js
/* 以给定的 URL 来替换当前的资源. */
webView.inject('document.location.replace("https://www.jetbrains.com")');
/* 替换整个 document 的内容. */
webView.inject('document.write("hello")');
/* 替换 body 元素为指定的 HTML 内容. */
webView.inject('document.body.innerHTML = "<p>hello</p>"');
/* 指定 body 元素的字体颜色. */
webView.inject('document.body.style = "color:green"');
/* 在文档末尾附加一个自定义元素. */
webView.inject('let p = document.createElement("p"); p.innerHTML = "hello"; document.body.appendChild(p)');
/* 使用回调方法获取内部信息. */
webView.inject('navigator.userAgent', result => console.log(result));
```

如需对上述 `webView` 实例进行一些设置, 可通过 `webView.getSettings()` 获得 android.webkit.WebSettings (https://developer.android.com/reference/android/webkit/WebSettings) 对象, 再进行个性化设置:

```js
let settings = webView.getSettings();

/* 设置 WebView 默认字体大小, 默认值 16. */
settings.setDefaultFontSize(18);
/* 设置是否允许脚本自动弹出新窗口, 默认 false. */
settings.setJavaScriptCanOpenWindowsAutomatically(true);
/* 设置 WebView 是否支持使用屏幕控件或手势进行缩放, 默认 true. */
settings.setSupportZoom(false);

/* ... */
```

对于 `InjectableWebView`, 其内部已经对 WebView 进行了一些初始化设置, 包括:

```java
settings.setUseWideViewPort(true);
settings.setBuiltInZoomControls(true);
settings.setLoadWithOverviewMode(true);
settings.setJavaScriptEnabled(true);
settings.setJavaScriptCanOpenWindowsAutomatically(true);
settings.setDomStorageEnabled(true);
settings.setDisplayZoomControls(false);
```

注: 上述设置参考自 Auto.js 4.1.1 Alpha2 源码.

此外, `InjectableWebView` 内部还初始化了一个默认的 WebChromeClient (https://developer.android.com/reference/android/webkit/WebChromeClient) 客户端:

```java
setWebChromeClient(new WebChromeClient());
```

注:
WebChromeClient 中的 "Chrome" 与 Google Chrome 浏览器中的 "Chrome" 不同.
WebView 中的 "Chrome" 指代 WebView 外面的装饰及 UI 部分.
WebChromeClient 是 HTML/JavaScript 与 Android 客户端交互的中间件, 它将 WebView 中 JavaScript 产生的事件封装后传递到 Android 客户端, 从而避免一些可能的安全问题.
同时 WebChromeClient 也可以辅助 WebView 处理 JavaScript 对话框, 显示加载进度, 上传文件等.

在 WebView 中访问了多个网页时, 按返回键会立即关闭整个页面, 而不是回退到上一个历史网页.
如果希望在 WebView 里浏览历史网页, 可参考如下代码:

```js
ui.emitter.on('back_pressed', function (e) {
    if (webView.canGoBack()) {
        webView.goBack();
        e.consumed = true;
    }
});
```

### newInjectableWebView(activity) {#web_newinjectablewebview_activity}

**`6.3.0`** **`Global`** **`Overload 3/3`** **`UI`**

- **activity** { ScriptExecuteActivity (dataTypes.html#datatypes_scriptexecuteactivity) } - 上下文对象, 默认为 UI 模式下的全局 activity 对象
- **returns** { InjectableWebView (injectableWebViewType.html) }

新建并返回一个 InjectableWebView (dataTypes.html#datatypes_injectablewebview) (可 注入 (glossaries.html#glossaries_注入) 的 WebView (https://developer.android.com/reference/android/webkit/WebView)) 实例, 通过 `activity` 参数可传入不同的 `org.mozilla.javascript.Context` 上下文对象, 该对象主要用于执行 JavaScript 语句.

## [m] newInjectableWebClient {#web_m_newinjectablewebclient}

### newInjectableWebClient() {#web_newinjectablewebclient}

**`6.3.0`** **`Global`**

- **returns** { InjectableWebClient (injectableWebClientType.html) }

新建并返回一个 InjectableWebClient (injectableWebClientType.html) (可 注入 (glossaries.html#glossaries_注入) 的 WebViewClient (https://developer.android.com/reference/android/webkit/WebViewClient)) 实例.

```js
/* 为 webView 对象重新设置一个新的客户端. */
webView.setWebViewClient(newInjectableWebClient());
```

## [m] newWebSocket {#web_m_newwebsocket}

### newWebSocket(url) {#web_newwebsocket_url}

**`6.3.1`** **`Global`**

- **url** { string (dataTypes.html#datatypes_string) } - 请求的 URL 地址
- **returns** { WebSocket (webSocketType.html) }

构建一个 WebSocket (webSocketType.html) 实例.

相当于 `new WebSocket(url)`.

参阅: WebSocket (webSocketType.html) 章节
