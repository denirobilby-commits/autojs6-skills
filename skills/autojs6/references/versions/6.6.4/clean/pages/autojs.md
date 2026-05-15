---
title: "AutoJs6 本体应用"
version: "6.6.4"
source_html: "raw/autojs.html"
---

# AutoJs6 本体应用 {#autojs_autojs6}

autojs 全局对象主要包含与 AutoJs6 应用本身相关的属性及方法, 如获取 AutoJs6 的 [ Root 状态 / 语言标签 / 权限状态 ] 等.

autojs

## [m] getLanguage {#autojs_m_getlanguage}

### getLanguage() {#autojs_getlanguage}

**`6.2.0`**

- **returns** { java.util.Locale (https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) }

获取 AutoJs6 `语言` 设置选项.

此方法返回一个 java.util.Locale 对象, 如需返回其标签名, 如 `en-US`, `zh-CN` 等, 可使用 `autojs.getLanguage().toLanguageTag()` 或直接使用 autojs.getLanguageTag() 方法.

```js
console.log(autojs.getLanguage().getDisplayName()); /* e.g. 日本語 */
```

## [m] getLanguageTag {#autojs_m_getlanguagetag}

### getLanguageTag() {#autojs_getlanguagetag}

**`6.2.0`**

- **returns** { string (dataTypes.html#datatypes_string) }

获取 AutoJs6 语言设置选项.

此方法返回 IETF 语言标签 (https://en.wikipedia.org/wiki/IETF_language_tag), 相当于 `autojs.getLanguage().toLanguageTag()`:

```js
console.log(autojs.getLanguageTag()); /* e.g. en-US */
```

此方法可用于设定 i18n 对象的区域:

```js
i18n.setLocale(autojs.getLanguageTag());
```

## [m] isRootAvailable {#autojs_m_isrootavailable}

### isRootAvailable() {#autojs_isrootavailable}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

获取 AutoJs6 的 Root 权限有效性.

```js
console.log(autojs.isRootAvailable()); // e.g. true
```

注意上述示例的检测结果取决于 AutoJs6 的 `强制 Root 权限检查` 设置.
此设置可通过 AutoJs6 应用设置修改, 或 setRootMode 方法携带 `isWriteIntoPreference` 参数实现修改.

## [m] getRootMode {#autojs_m_getrootmode}

### getRootMode() {#autojs_getrootmode}

**`6.2.0`**

- **returns** { RootMode (dataTypes.html#datatypes_rootmode) }

获取 AutoJs6 的 Root 权限状态.

```js
 /* 是否为 '自动检测 Root 权限' 状态. */
console.log(autojs.getRootMode() === RootMode.AUTO_DETECT);
/* 是否为 '强制 Root 模式' 状态. */
console.log(autojs.getRootMode() === RootMode.FORCE_ROOT);
/* 是否为 '强制非 Root 模式' 状态. */
console.log(autojs.getRootMode() === RootMode.FORCE_NON_ROOT);
```

## [m] setRootMode {#autojs_m_setrootmode}

### setRootMode(rootMode, isWriteIntoPreference?) {#autojs_setrootmode_rootmode_iswriteintopreference}

**`6.2.0`** **`Overload [1-2]/2`**

- **rootMode** { RootMode (dataTypes.html#datatypes_rootmode) | number (dataTypes.html#datatypes_number) | boolean (dataTypes.html#datatypes_boolean) | 'auto' | 'root' | 'non-root' } - Root 模式参数
- **[ isWriteIntoPreference = `false` ]** { boolean (dataTypes.html#datatypes_boolean) } - 是否写入应用设置
- **returns** { void (dataTypes.html#datatypes_void) }

设置 AutoJs6 的 Root 模式.

默认情况下, AutoJs6 将根据 `su` 二进制名称特征来判断是否具有 Root 权限. 但有时设备可能使用了非常规 Root 方式或 Root 权限检测结果出现异常, 此时可设置 `强制 Root 模式` 或 `强制非 Root 模式` 来改变 AutoJs6 对 Root 权限的检测结果.

以设置 '强制 Root 模式' 为例:

```js
autojs.setRootMode(RootMode.FORCE_ROOT);
autojs.setRootMode('root'); /* 同上. */
autojs.setRootMode(1); /* 同上. */
autojs.setRootMode(true); /* 同上. */
```

上述示例设置的 Root 模式, 将影响 isRootAvailable 的结果, 使其固定返回 `true`.
如果设置为 `RootMode.FORCE_NON_ROOT`, isRootAvailable 将固定返回 `false`.
如果设置为 `RootMode.AUTO_DETECT`, isRootAvailable 将根据 AutoJs6 是否具有 `su` 二进制名称特征决定其返回结果.

在没有特殊需求的情况下, 建议始终保持 Root 模式为 '自动' 模式.

需额外留意, Root 模式修改仅对当前 `运行时 (Runtime)` 有效, 当脚本结束时, 已设置的 Root 模式将自动还原为 '自动' 模式, 即 `RootMode.AUTO_DETECT`.

如需将保留修改的 Root 模式, 可使用 `isWriteIntoPreference` 参数, 修改将立即写入应用设置中:

```js
autojs.setRootMode(RootMode.FORCE_ROOT, true);
```

上述示例代码的效果, 等效于在 AutoJs6 应用中进行如下设置:

```text
[ AutoJs6 设置 ] - [ 强制 Root 权限检查 ] - [ 强制 Root 模式 ] # [ 选择 ]
```

## [m] canModifySystemSettings {#autojs_m_canmodifysystemsettings}

### canModifySystemSettings() {#autojs_canmodifysystemsettings}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

获取 AutoJs6 的 `修改系统设置` 权限状态.

```js
console.log(autojs.canModifySystemSettings()); // e.g. true
```

拥有 `修改系统设置` 后, AutoJs6 可以通过脚本修改部分系统设置, 如修改屏幕超时参数, 修改媒体音量值等.

## [m] canWriteSecureSettings {#autojs_m_canwritesecuresettings}

### canWriteSecureSettings() {#autojs_canwritesecuresettings}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

获取 AutoJs6 的 `修改安全设置` 权限状态.

```js
console.log(autojs.canWriteSecureSettings()); // e.g. true
```

拥有 `修改安全设置` 后, AutoJs6 可以通过脚本修改部分安全设置, 如修改屏幕常亮类别参数, 修改无障碍服务列表内容等.

## [m] canDisplayOverOtherApps {#autojs_m_candisplayoverotherapps}

### canDisplayOverOtherApps() {#autojs_candisplayoverotherapps}

**`6.2.0`**

- **returns** { boolean (dataTypes.html#datatypes_boolean) }

获取 AutoJs6 的 `显示在其他应用上层` 权限状态.

```js
console.log(autojs.canDisplayOverOtherApps()); // e.g. true
```

拥有 `显示在其他应用上层` 后, AutoJs6 可以使用悬浮窗工具, 并可通过脚本显示对话框或自定义浮动组件等.

## [p] versionName {#autojs_p_versionname}

**`6.2.0`**

- { string (dataTypes.html#datatypes_string) }

获取版本名称.

```js
console.log(autojs.versionName); // e.g. 6.2.0-alpha9
console.log(autojs.version.name); /* 同上. */
```

## [p] versionCode {#autojs_p_versioncode}

**`6.2.0`**

- { number (dataTypes.html#datatypes_number) }

获取版本号.

```js
console.log(autojs.versionCode); // e.g. 1545
console.log(autojs.version.code); /* 同上. */
```

## [p] versionDate {#autojs_p_versiondate}

**`6.2.0`**

- { string (dataTypes.html#datatypes_string) }

获取版本日期.

```js
console.log(autojs.versionDate); // e.g. Dec 18, 2022
console.log(autojs.version.date); /* 同上. */
```

## [p] themeColor {#autojs_p_themecolor}

**`6.3.0`** **`Getter`**

- **<get>** ThemeColor (dataTypes.html#datatypes_themecolor)

获取 AutoJs6 的主题颜色实例.

```js
autojs.themeColor.getColorPrimary(); /* 获取 AutoJs6 主题色的主色色值. */
```

## [p+] version {#autojs_p_version}

### [p] name {#autojs_p_name}

**`6.2.0`**

- { string (dataTypes.html#datatypes_string) }

获取版本名称.

```js
console.log(autojs.version.name); // e.g. 6.2.0-alpha9
console.log(autojs.versionName); /* 同上. */
```

### [p] code {#autojs_p_code}

**`6.2.0`**

- { number (dataTypes.html#datatypes_number) }

获取版本号.

```js
console.log(autojs.version.code); // e.g. 1545
console.log(autojs.versionCode); /* 同上. */
```

### [p] date {#autojs_p_date}

**`6.2.0`**

- { string (dataTypes.html#datatypes_string) }

获取版本日期.

```js
console.log(autojs.version.date); // e.g. Dec 18, 2022
console.log(autojs.versionDate); /* 同上. */
```

### [m] isEqual {#autojs_m_isequal}

#### isEqual(otherVersion) {#autojs_isequal_otherversion}

**`6.2.0`**

- **otherVersion** { string (dataTypes.html#datatypes_string) | Version (versionType.html#versiontype_c_version) } - 待比较版本参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 AutoJs6 版本是否与参数对应的版本号等同.

```js
console.log(autojs.version.isEqual('6.2.0')); // e.g. true
```

### [m] isHigherThan {#autojs_m_ishigherthan}

#### isHigherThan(otherVersion) {#autojs_ishigherthan_otherversion}

**`6.2.0`**

- **otherVersion** { string (dataTypes.html#datatypes_string) | Version (versionType.html#versiontype_c_version) } - 待比较版本参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 AutoJs6 版本是否高于待比较版本.

```js
console.log(autojs.version.isHigherThan('6.1.3')); // e.g. true
```

### [m] isLowerThan {#autojs_m_islowerthan}

#### isLowerThan(otherVersion) {#autojs_islowerthan_otherversion}

**`6.2.0`**

- **otherVersion** { string (dataTypes.html#datatypes_string) | Version (versionType.html#versiontype_c_version) } - 待比较版本参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 AutoJs6 版本是否低于待比较版本.

```js
console.log(autojs.version.isLowerThan('6.2.0')); // e.g. true
```

### [m] isAtLeast {#autojs_m_isatleast}

#### isAtLeast(otherVersion) {#autojs_isatleast_otherversion}

**`6.2.0`** **`Overload 1/2`**

- **otherVersion** { string (dataTypes.html#datatypes_string) | Version (versionType.html#versiontype_c_version) } - 待比较版本参数
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 AutoJs6 版本是否不低于 (即大于等于) 参数对应的版本号.

```js
console.log(autojs.version.isAtLeast('6.1.3')); // e.g. true
```

#### isAtLeast(otherVersion, ignoreSuffix) {#autojs_isatleast_otherversion_ignoresuffix}

**`6.2.0`** **`Overload 2/2`**

- **otherVersion** { string (dataTypes.html#datatypes_string) | Version (versionType.html#versiontype_c_version) } - 待比较版本参数
- **[ ignoreSuffix = `false` ]** { boolean (dataTypes.html#datatypes_boolean) } - 是否忽略版本后缀
- **returns** { boolean (dataTypes.html#datatypes_boolean) }

返回 AutoJs6 版本是否不低于 (即大于等于) 参数对应的版本号且根据 `ignoreSuffix` 参数决定是否忽略版本后缀.

```js
console.log(autojs.version.name); // e.g. 6.2.0-alpha9
console.log(autojs.version.isAtLeast('6.2.0')); // e.g. false
console.log(autojs.version.isAtLeast('6.2.0', true)); // e.g. true
```

## [p+] R {#autojs_p_r}

使用 R 类的子类中的静态整数可访问相应的应用资源, 如 `R.string` 访问字符串资源, `R.drawable` 访问可绘制资源等.

global.R (global.html#global_p_r) 的别名属性, 参阅 全局对象 (Global) (global.html#global_p_r) 章节.
