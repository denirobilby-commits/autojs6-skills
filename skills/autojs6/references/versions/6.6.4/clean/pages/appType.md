---
title: "应用枚举类 (App)"
version: "6.6.4"
source_html: "raw/appType.html"
---

# 应用枚举类 (App) {#apptype_app}

为便于与其他应用交互, AutoJs6 内置了部分常见应用的信息, 如下表:

枚举实例名 中文名 英文名 包名 别名 ACCUWEATHER AccuWeather ~ com.accuweather.android accuweather ADM ADM ~ com.dv.adm adm ALIPAY 支付宝 Alipay com.eg.android.AlipayGphone alipay AMAP 高德地图 Amap com.autonavi.minimap amap APPOPS App Ops ~ rikka.appops appops AQUAMAIL Aqua Mail ~ org.kman.AquaMail aquamail AUTOJS Auto.js ~ org.autojs.autojs autojs AUTOJS6 AutoJs6 ~ org.autojs.autojs6 autojs6 AUTOJSPRO AutoJsPro ~ org.autojs.autojspro autojspro BAIDUMAP 百度地图 BaiduMap com.baidu.BaiduMap baidumap BILIBILI 哔哩哔哩 bilibili tv.danmaku.bili bilibili BREVENT 黑阈 Brevent mie.piebridge.brevent brevent CALENDAR 日历 Calendar com.google.android.calendar calendar CHROME Chrome ~ com.android.chrome chrome COOLAPK 酷安 CoolApk com.coolapk.market coolapk DIANPING 大众点评 Dianping com.dianping.v1 dianping DIGICAL DigiCal ~ com.digibites.calendar digical DRIVE 云端硬盘 Drive com.google.android.apps.docs drive ES ES文件浏览器 ES File Explorer com.estrongs.android.pop es EUDIC 欧路词典 Eudic com.qianyan.eudic eudic EXCEL Excel ~ com.microsoft.office.excel excel FIREFOX Firefox ~ org.mozilla.firefox firefox FX FX ~ nextapp.fx fx GEOMETRICWEATHER 几何天气 Geometric Weather wangdaye.com.geometricweather geometricweather HTTPCANARY HttpCanary ~ com.guoshi.httpcanary.premium httpcanary IDLEFISH 闲鱼 ~ com.taobao.idlefish idlefish IDMPLUS IDM+ ~ idm.internet.download.manager.plus idm+ JD 京东 ~ com.jingdong.app.mall jd KEEP Keep ~ com.gotokeep.keep keep KEEPNOTES Keep 记事 Keep Notes com.google.android.keep keepnotes MAGISK Magisk ~ com.topjohnwu.magisk magisk MEITUAN 美团 Meituan com.sankuai.meituan meituan MT MT管理器 MT Manager bin.mt.plus mt MXPRO MX 播放器专业版 MX Player Pro com.mxtech.videoplayer.pro mxpro ONEDRIVE OneDrive ~ com.microsoft.skydrive onedrive PACKETCAPTURE Packet Capture ~ app.greyshirts.sslcapture packetcapture PARALLELSPACE 平行空间(原双开大师) Parallel Space com.lbe.parallel.intl parallelspace POWERPOINT PowerPoint ~ com.microsoft.office.powerpoint powerpoint PULSARPLUS Pulsar+ ~ com.rhmsoft.pulsar.pro pulsarplus PUREWEATHER Pure天气 ~ hanjie.app.pureweather pureweather QQ QQ ~ com.tencent.mobileqq qq QQMUSIC QQ音乐 QQMusic com.tencent.qqmusic qqmusic SDMAID SD Maid ~ eu.thedarken.sdm sdmaid SHIZUKU Shizuku ~ moe.shizuku.privileged.api shizuku STOPAPP 小黑屋 ~ web1n.stopapp stopapp TAOBAO 淘宝 ~ com.taobao.taobao taobao TRAINNOTE 训记 ~ com.trainnote.rn trainnote TWITTER Twitter ~ com.twitter.android twitter UNIONPAY 云闪付 ~ com.unionpay unionpay VIA Via ~ mark.via.gp via VYSOR Vysor ~ com.koushikdutta.vysor vysor WECHAT 微信 WeChat com.tencent.mm wechat WORD Word ~ com.microsoft.office.word word ZHIHU 知乎 ~ com.zhihu.android zhihu

通常 "别名" 字段取自 "枚举实例名" 字段的名称小写形式.
表列 "英文名" 中波浪符号表示与 "中文名" 对应字段名称相同.

注: 上述信息可能发生变更.
例如一些应用在某个时间点开始去除了 "英文名" 并统一使用 "中文名" 字段, 甚至部分应用会在每个版本均变更其应用名.
如果用户编写的脚本对应用名十分敏感, 建议使用 App#getAppName 或 app.getAppName 等方式获取设备中已安装应用的真实应用名.

App

## [@] App {#apptype_app_1}

**`6.2.0`** **`Global`** **`Enum`**

App 为枚举类, 因此可使用 Java 通用的枚举类方法:

```js
/* 打印所有枚举实例名. */
console.log(App.values().map(o => o.name()));

/* 获取一个枚举实例. */
const tt = App.FIREFOX;

/* 调用实例方法. */
console.log(tt.getAppName());
console.log(tt.getPackageName());
console.log(tt.getAlias());
```

## [m#] getAppName {#apptype_m_getappname}

获取枚举实例的应用名.

### getAppName() {#apptype_getappname}

- **returns** { string (dataTypes.html#datatypes_string) }

优先获取设备中已安装应用的应用名, 若应用未安装, 则获取 App 枚举实例中预置的应用名.

```js
// "Firefox"
console.log(App.FIREFOX.getAppName());
```

## [m#] getAppNameZh {#apptype_m_getappnamezh}

获取枚举实例中预置的中文应用名.

### getAppNameZh() {#apptype_getappnamezh}

- **returns** { string (dataTypes.html#datatypes_string) }

```js
// "支付宝"
console.log(App.ALIPAY.getAppNameZh());
```

## [m#] getAppNameEn {#apptype_m_getappnameen}

获取枚举实例中预置的英文应用名.

### getAppNameEn() {#apptype_getappnameen}

- **returns** { string (dataTypes.html#datatypes_string) }

```js
// "Alipay"
console.log(App.ALIPAY.getAppNameEn());
```

## [m#] getPackageName {#apptype_m_getpackagename}

获取枚举实例中预置的应用包名.

### getPackageName() {#apptype_getpackagename}

- **returns** { string (dataTypes.html#datatypes_string) }

```js
// "com.eg.android.AlipayGphone"
console.log(App.ALIPAY.getPackageName());
```

## [m#] getAlias {#apptype_m_getalias}

获取枚举实例中预置的应用别名.

### getAlias() {#apptype_getalias}

- **returns** { string (dataTypes.html#datatypes_string) }

```js
// "alipay"
console.log(App.ALIPAY.getAlias());
```

## [m#] isInstalled {#apptype_m_isinstalled}

检查枚举实例是否在设备安装.

### isInstalled() {#apptype_isinstalled}

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

```js
/* e.g. true */
console.log(App.ALIPAY.isInstalled());
```

## [m#] ensureInstalled {#apptype_m_ensureinstalled}

确保枚举实例在设备安装, 否则抛出异常.

### ensureInstalled() {#apptype_ensureinstalled}

- **returns** { void (dataTypes.html#datatypes_void) }

```js
App.FIREFOX.ensureInstalled();
```

## [m#] uninstall {#apptype_m_uninstall}

卸载设备中存在的枚举实例应用.

### uninstall() {#apptype_uninstall}

- **returns** { void (dataTypes.html#datatypes_void) }

```js
App.FIREFOX.uninstall();
```

## [m#] launch {#apptype_m_launch}

启动设备中的枚举实例应用.

### launch() {#apptype_launch}

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

若应用未安装或启动过程中出错, 将返回 false (而非抛出异常).

```js
/* e.g. true */
console.log(App.FIREFOX.launch());
```

## [m#] openSettings {#apptype_m_opensettings}

跳转至枚举实例应用的应用详情页面.

### openSettings() {#apptype_opensettings}

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

若应用未安装或跳转页面过程中出错, 将返回 false (而非抛出异常).

```js
/* e.g. true */
console.log(App.FIREFOX.openSettings());
```

## [m#] toString {#apptype_m_tostring}

获取枚举实例自定义的实例信息字符串.

### toString() {#apptype_tostring}

- **returns** { string (dataTypes.html#datatypes_string) }

```js
/* e.g. {appName: "Firefox", packageName: "org.mozilla.firefox", alias: "firefox"} */
console.log(App.FIREFOX.toString());
console.log(App.FIREFOX); /* 同上. */
```

## [m] getAppByAlias {#apptype_m_getappbyalias}

通过应用别名获取对应的 App 实例.

### getAppByAlias(alias) {#apptype_getappbyalias_alias}

- **alias** { string (dataTypes.html#datatypes_string) } - 应用别名
- **returns** { App (appType.html) | null (dataTypes.html#datatypes_null) }

应用别名对应的枚举实例不存在时将返回 null:

```js
let tt = App.getAppByAlias('twitter');
if (tt !== null) {
    console.log(tt.getPackageName());
}
```
