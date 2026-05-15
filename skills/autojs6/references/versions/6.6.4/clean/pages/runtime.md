---
title: "运行时 (Runtime)"
version: "6.6.4"
source_html: "raw/runtime.html"
---

# 运行时 (Runtime) {#runtime_runtime}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 31, 2022.

## runtime.requestPermissions(permissions) {#runtime_runtime_requestpermissions_permissions}

- `permissions` { Array (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) } 权限的字符串数组

动态申请安卓的权限. 例如：

```
//请求GPS权限
runtime.requestPermissions(["access_fine_location"]);
```

尽管安卓有很多权限, 但必须写入Manifest才能动态申请, 为了防止权限的滥用, 目前Auto.js只能额外申请两个权限：

- `access_fine_location` GPS权限
- `record_audio` 录音权限

您可以通过APK编辑器来增加Auto.js以及Auto.js打包的应用的权限.

安卓所有的权限列表参见Permissions Overview (https://developer.android.com/guide/topics/permissions/overview/). （并没有用）

## runtime.loadJar(path) {#runtime_runtime_loadjar_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } jar文件路径

加载目标jar文件, 加载成功后将可以使用该Jar文件的类.

```
// 加载jsoup.jar
runtime.loadJar("./jsoup.jar");
// 使用jsoup解析html
importClass(org.jsoup.Jsoup);
log(Jsoup.parse(files.read("./test.html")));
```

(jsoup是一个Java实现的解析Html DOM的库, 可以在Jsoup (https://jsoup.org/download/)下载/)

## runtime.loadDex(path) {#runtime_runtime_loaddex_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } dex文件路径

加载目标dex文件, 加载成功后将可以使用该dex文件的类.

因为加载jar实际上是把jar转换为dex再加载的, 因此加载dex文件会比jar文件快得多. 可以使用Android SDK的build tools的dx工具把jar转换为dex.
