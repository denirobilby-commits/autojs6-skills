---
title: "WebSocket"
version: "6.6.4"
source_html: "raw/webSocketType.html"
---

# WebSocket {#websockettype_websocket}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 30, 2023.

WebSocket 类主要用于构建一个 OkHttp3 WebSocket (https://square.github.io/okhttp/4.x/okhttp/okhttp3/-web-socket/) 接口实现类的实例, 以便完成基于 WebSocket 协议 (https://zh.wikipedia.org/wiki/WebSocket) 的网络请求.

注: WebSocket 不同于 Socket.
WebSocket 是应用层的网络传输协议. 而 Socket 并非协议, 是位于应用层和传输控制层之间的一组接口, 是对 TCP/IP 协议的封装.

一个流程相对完备的 WebSocket 示例:

```js
console.setExitOnClose(7e3).show();

let ws = new WebSocket('wss://echo.websocket.events');

ws
    .on(WebSocket.EVENT_OPEN, (res, ws) => {
        console.log('WebSocket 已连接');
    })
    .on(WebSocket.EVENT_MESSAGE, (message, ws) => {
        console.log('接收到消息');
        // if (message instanceof okio.ByteString) {
        //     console.log(`消息类型: ByteString`);
        // } else if (typeof message === 'string') {
        //     console.log(`消息类型: String`);
        // } else {
        //     throw TypeError('Should never happen');
        // }
    })
    .on(WebSocket.EVENT_TEXT, (text, ws) => {
        console.info('接收到文本消息:');
        console.info(`text: ${text}`);
    })
    .on(WebSocket.EVENT_BYTES, (bytes, ws) => {
        console.info('接收到字节数组消息:');
        console.info(`utf8: ${bytes.utf8()}`);
        console.info(`base64: ${bytes.base64()}`);
        console.info(`md5: ${bytes.md5()}`);
        console.info(`hex: ${bytes.hex()}`);
    })
    .on(WebSocket.EVENT_CLOSING, (code, reason, ws) => {
        console.log('WebSocket 关闭中');
    })
    .on(WebSocket.EVENT_CLOSED, (code, reason, ws) => {
        console.log('WebSocket 已关闭');
        console.log(`code: ${code}`);
        if (reason) console.log(`reason: ${reason}`);
    })
    .on(WebSocket.EVENT_FAILURE, (err, res, ws) => {
        console.error('WebSocket 连接失败');
        console.error(err);
    });

/* 发送文本消息. */
ws.send('Hello WebSocket');

/* 发送字节数组消息. */
ws.send(new okio.ByteString(new java.lang.String('Hello WebSocket').getBytes()));

setTimeout(() => {
    console.log('断开 WebSocket');
    ws.close('由用户断开连接');
}, 8e3);
```

WebSocket

## [C] WebSocket {#websockettype_c_websocket}

- **extends** { EventEmitter (eventEmitterType.html) }

WebSocket 类继承自 EventEmitter (eventEmitterType.html) 类.

因此 WebSocket 实例拥有继承而来的 on (eventEmitterType.html#eventemittertype_m_on), once (eventEmitterType.html#eventemittertype_m_once), emit (eventEmitterType.html#eventemittertype_m_emit), eventNames (eventEmitterType.html#eventemittertype_m_eventnames), addListener (eventEmitterType.html#eventemittertype_m_addlistener), removeListener (eventEmitterType.html#eventemittertype_m_removelistener) 等方法, 详情参阅 事件发射器 (EventEmitter) (eventEmitterType.html) 章节.

注:
特别地, on 和 once 方法在子类进行了 `覆写 (override)`, 其返回值类型被具体化为 WebSocket, 以便于链式调用.
为节约篇幅, 本章节仅列举了 on 方法的相关文档, once 方法与 on 的用法相同.

### [c] (url) {#websockettype_c_url}

**`6.3.4`** **`Global`**

- **url** { string (dataTypes.html#datatypes_string) } - 请求的 URL 地址
- **returns** { WebSocket (webSocketType.html) }

构建一个 WebSocket (webSocketType.html) 实例.

注: 构建实例时, 已经隐含客户端建立连接的过程.

以下示例建立一个 WebSocket 连接, 并在 5 秒钟后主动断开连接.

```js
let ws = new WebSocket('wss://echo.websocket.events');
setTimeout(() => {
    console.log('断开 WebSocket');
    ws.close(WebSocket.CODE_CLOSE_NORMAL, 'Closed by user');
}, 5e3);
```

## [m] send {#websockettype_m_send}

### send(text) {#websockettype_send_text}

**`Overload 1/2`**

Attempts to enqueue text to be UTF-8 encoded and sent as a the data of a text (type 0x1) message. This method returns true if the message was enqueued. Messages that would overflow the outgoing message buffer will be rejected and trigger a graceful shutdown of this web socket. This method returns false in that case, and in any other case where this web socket is closing, closed, or canceled. This method returns immediately.

```js
let ws = new WebSocket('wss://echo.websocket.events');
ws.send('Hello WebSocket');
ws.exitOnClose();
```

### send(bytes) {#websockettype_send_bytes}

**`Overload 2/2`**

Attempts to enqueue bytes to be sent as a the data of a binary (type 0x2) message. This method returns true if the message was enqueued. Messages that would overflow the outgoing message buffer (16 MiB) will be rejected and trigger a graceful shutdown of this web socket. This method returns false in that case, and in any other case where this web socket is closing, closed, or canceled. This method returns immediately.

```js
let ws = new WebSocket('wss://echo.websocket.events');
ws.send(new okio.ByteString(new java.lang.String('Hello WebSocket').getBytes()));
ws.exitOnClose();
```

## [m] close {#websockettype_m_close}

### close(code?, reason?) {#websockettype_close_code_reason}

**`Overload [1-3]/4`**

- **[ code = `WebSocket.CODE_CLOSE_NORMAL [1000]` ]** { number (dataTypes.html#datatypes_number) } - 状态码
- **[ reason = `null` ]** { string (dataTypes.html#datatypes_string) } - 连接关闭原因
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 优雅关闭是否已经启动

尝试启动 WebSocket 优雅关闭, 此时已排队的报文将在 WebSocket 断开前被传送.

注: 相对应地, cancel 则会立即释放资源, 而丢弃所有排队的报文.

如果调用 `close` 时启动了优雅关闭, 返回 true.
如果调用 `close` 时, 优雅关闭已经启动, 或 WebSocket 已关闭或取消, 返回 false.

参数 `code` 可选, 代表状态码, 通过状态码可以获取或判断连接关闭的原因. 其范围为 `[1000..5000)`.

参数 `reason` 可选, 代表关闭原因, 方便用户直接通过阅读字符串获取连接关闭的原因.

以下调用方式均被支持 (其中 `ws` 代表一个 WebSocket 实例):

```js
ws.close(); /* 默认状态码, 无具体关闭原因. */
ws.close(WebSocket.CODE_CLOSE_NORMAL); /* 指定状态码, 无具体关闭原因. */
ws.close(WebSocket.CODE_CLOSE_NORMAL, '用户正常关闭'); /* 指定状态码, 指定具体关闭原因. */
```

### close(reason) {#websockettype_close_reason}

**`Overload 4/4`**

- **reason** { string (dataTypes.html#datatypes_string) } - 连接关闭原因
- **returns** { boolean (dataTypes.html#datatypes_boolean) } - 优雅关闭是否已经启动

相当于 `close(WebSocket.CODE_CLOSE_NORMAL, reason)`.

## [m] exitOnClose {#websockettype_m_exitonclose}

### exitOnClose() {#websockettype_exitonclose}

**`Overload 1/2`**

... ...

### exitOnClose(timeout) {#websockettype_exitonclose_timeout}

**`Overload 2/2`**

... ...

## [m] cancel {#websockettype_m_cancel}

### cancel() {#websockettype_cancel}

- **returns** { void (dataTypes.html#datatypes_void) }

立即强制释放该 WebSocket 所占用的资源, 并丢弃所有排队的报文.

注: 相对应地, close 则会在释放资源之前将排队的报文完成传送.

## [m] queueSize {#websockettype_m_queuesize}

### queueSize() {#websockettype_queuesize}

- **returns** { number (dataTypes.html#datatypes_number) }

Returns the size in bytes of all messages enqueued to be transmitted to the server. This doesn't include framing overhead. If compression is enabled, uncompressed messages size is used to calculate this value. It also doesn't include any bytes buffered by the operating system or network intermediaries. This method returns 0 if no messages are waiting in the queue. If may return a nonzero value after the web socket has been canceled; this indicates that enqueued messages were not transmitted.

## [m] on {#websockettype_m_on}

### on(eventName, callback) {#websockettype_on_eventname_callback}

- **eventName** { string (dataTypes.html#datatypes_string) } - 最大连接重建次数
- **callback** { ( (dataTypes.html#datatypes_function)args: ... (documentation.html#documentation_可变参数)any (dataTypes.html#datatypes_any)[] (documentation.html#documentation_可变参数)) (dataTypes.html#datatypes_function) => (dataTypes.html#datatypes_function) any (dataTypes.html#datatypes_any) } - 事件监听回调参数
- **returns** { WebSocket (webSocketType.html) }

注册一个 WebSocket 相关的事件监听器, 当事件名称与 `eventName` 参数一致时, 触发执行回调函数 `callback`.

... ...

不同事件名称, 其对应监听回调函数的参数也不同 (给出具体对应的在 [p] 文档内).

... ...

## [m] rebuild {#websockettype_m_rebuild}

### rebuild(maxRebuildTimes?) {#websockettype_rebuild_maxrebuildtimes}

**`Overload [1-2]/2`**

- **maxRebuildTimes** { number (dataTypes.html#datatypes_number) } - 最大连接重建次数
- **returns** { void (dataTypes.html#datatypes_void) }

... ...

## [m] request {#websockettype_m_request}

### request() {#websockettype_request}

- **returns** { Okhttp3Request (okhttp3RequestType.html) }

Returns the original request that initiated this web socket.

## [p] EVENT_OPEN {#websockettype_p_event_open}

**`6.3.4`** **`CONSTANT`**

- [ `open` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量.

- 事件触发: 远程对等端接受网络套接字, 并且可以开始信息传输.
- 事件监听: WebSocket#on

```js
let ws = new WebSocket('wss://echo.websocket.events');
ws.on(WebSocket.EVENT_OPEN, (res, ws) => console.log('WebSocket 已连接'));
ws.exitOnClose();
```

## [p] EVENT_MESSAGE {#websockettype_p_event_message}

**`6.3.4`** **`CONSTANT`**

- [ `message` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when a text (type 0x1) message has been received.

## [p] EVENT_TEXT {#websockettype_p_event_text}

**`6.3.4`** **`CONSTANT`**

- [ `text` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when a text (type 0x1) message has been received.

## [p] EVENT_BYTES {#websockettype_p_event_bytes}

**`6.3.4`** **`CONSTANT`**

- [ `bytes` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when a text (type 0x1) message has been received.

## [p] EVENT_CLOSING {#websockettype_p_event_closing}

**`6.3.4`** **`CONSTANT`**

- [ `closing` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when the remote peer has indicated that no more incoming messages will be transmitted.

## [p] EVENT_CLOSED {#websockettype_p_event_closed}

**`6.3.4`** **`CONSTANT`**

- [ `closed` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when both peers have indicated that no more messages will be transmitted and the connection has been successfully released. No further calls to this listener will be made.

## [p] EVENT_FAILURE {#websockettype_p_event_failure}

**`6.3.4`** **`CONSTANT`**

- [ `failure` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

Invoked when a web socket has been closed due to an error reading from or writing to the network. Both outgoing and incoming messages may have been lost. No further calls to this listener will be made.

## [p] EVENT_MAX_REBUILDS {#websockettype_p_event_max_rebuilds}

**`6.3.4`** **`CONSTANT`**

- [ `max_rebuilds` ] { string (dataTypes.html#datatypes_string) }

WebSocket 事件名称常量, 用于 xxx 事件.

## [p] CODE_CLOSE_NORMAL {#websockettype_p_code_close_normal}

**`6.3.4`** **`CONSTANT`**

- [ `1000` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示成功操作或常规的 Socket 关闭操作.

## [p] CODE_CLOSE_GOING_AWAY {#websockettype_p_code_close_going_away}

**`6.3.4`** **`CONSTANT`**

- [ `1001` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端正在处于移除状态, 服务端或客户端即将不可用.

## [p] CODE_CLOSE_PROTOCOL_ERROR {#websockettype_p_code_close_protocol_error}

**`6.3.4`** **`CONSTANT`**

- [ `1002` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端因协议错误或无效帧而即将终止连接.

## [p] CODE_CLOSE_UNSUPPORTED {#websockettype_p_code_close_unsupported}

**`6.3.4`** **`CONSTANT`**

- [ `1003` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端因帧数据类型不支持而即将终止连接.

## [p] CODE_CLOSED_NO_STATUS {#websockettype_p_code_closed_no_status}

**`6.3.4`** **`CONSTANT`**

- [ `1005` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示不包含错误原因, 仅代表已经关闭的状态.

## [p] CODE_CLOSE_ABNORMAL {#websockettype_p_code_close_abnormal}

**`6.3.4`** **`CONSTANT`**

- [ `1006` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示异常关闭 (如浏览器关闭).

## [p] CODE_UNSUPPORTED_PAYLOAD {#websockettype_p_code_unsupported_payload}

**`6.3.4`** **`CONSTANT`**

- [ `1007` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端接收到不一致的报文 (如异常格式的 UTF-8).

## [p] CODE_POLICY_VIOLATION {#websockettype_p_code_policy_violation}

**`6.3.4`** **`CONSTANT`**

- [ `1008` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端因收到了违反其策略的报文而即将终止连接.

## [p] CODE_CLOSE_TOO_LARGE {#websockettype_p_code_close_too_large}

**`6.3.4`** **`CONSTANT`**

- [ `1009` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端因无法处理长度过大的报文而即将终止连接.

## [p] CODE_MANDATORY_EXTENSION {#websockettype_p_code_mandatory_extension}

**`6.3.4`** **`CONSTANT`**

- [ `1010` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示终端因期望与服务端进行扩展协商而即将终止连接.

## [p] CODE_SERVER_ERROR {#websockettype_p_code_server_error}

**`6.3.4`** **`CONSTANT`**

- [ `1011` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示服务端因发生内部错误而即将终止连接.

## [p] CODE_SERVICE_RESTART {#websockettype_p_code_service_restart}

**`6.3.4`** **`CONSTANT`**

- [ `1012` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示服务端正在重启过程中.

## [p] CODE_TRY_AGAIN_LATER {#websockettype_p_code_try_again_later}

**`6.3.4`** **`CONSTANT`**

- [ `1013` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示服务端临时拒绝了终端请求.

## [p] CODE_BAD_GATEWAY {#websockettype_p_code_bad_gateway}

**`6.3.4`** **`CONSTANT`**

- [ `1014` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示网关服务器接收到无效的请求.

## [p] CODE_TLS_HANDSHAKE_FAIL {#websockettype_p_code_tls_handshake_fail}

**`6.3.4`** **`CONSTANT`**

- [ `1015` ] { number (dataTypes.html#datatypes_number) }

WebSocket 状态码, 表示 TLS 握手失败 (如服务端证书未通过验证等).
