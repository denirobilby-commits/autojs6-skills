---
title: "Shizuku"
version: "6.6.4"
source_html: "raw/shizuku.html"
---

# Shizuku {#shizuku_shizuku}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 30, 2023.

通过 Shizuku (https://shizuku.rikka.app/introduction/) 可以获得 ADB 特权并使用系统 API.

使用 Shizuku 需满足以下全部条件

- 设备已安装 Shizuku 应用 (https://github.com/RikkaApps/Shizuku/releases) (版本不低于 `11`)
- Shizuku 服务已启动 (参阅 Shizuku 用户手册 (https://shizuku.rikka.app/guide/setup/#start-shizuku))
- AutoJs6 首页抽屉开启 Shizuku 权限开关

shizuku

## [@] shizuku {#shizuku_shizuku_1}

shizuku 可作为全局对象使用:

```js
typeof shizuku; // "function"
typeof shizuku.execCommand; // "function"
```

### shizuku(cmd) {#shizuku_shizuku_cmd}

**`6.4.0`** **`Overload 1/2`**

- **cmd** { string (dataTypes.html#datatypes_string) } - 待执行命令
- **returns** { ShellResult (shellResultType.html) } - Shell 结果

使用 Shizuku 执行命令.

```js
/* 模拟返回键. */
shizuku('input keyevent 4');
shizuku(`input keyevent ${KeyEvent.KEYCODE_BACK}`); /* 同上. */

/* 模拟电源键. */
shizuku('input keyevent 26');
shizuku(`input keyevent ${KeyEvent.KEYCODE_POWER}`); /* 同上. */

/* 点击屏幕坐标 (100, 120). */
shizuku('input tap 100 120');

/* 授予 AutoJs6 "修改安全设置" 权限. */
shizuku('pm grant org.autojs.autojs6 android.permission.WRITE_SECURE_SETTINGS');

/* 授予 AutoJs6 "投影媒体" 权限. */
shizuku('appops set org.autojs.autojs6 PROJECT_MEDIA allow');

/* 获取当前时间. */
console.log(shizuku('date').result.trim());
```

使用 shizuku 启用 AutoJs6 无障碍服务 (共计 4 步):

```js

/* [ 1. 获取无障碍服务列表, 列表是一个字符串, 不同无障碍服务之间以 ":" 分隔. ] */
let services = shizuku('settings get secure enabled_accessibility_services').result.trim(); /* 结尾 "\n" 可通过 trim() 方法去除. */

/* [ 2. 确保无障碍服务列表中不存在 AutoJs6. ] */
let servicesWithoutAutoJs6 = services
    .split(':') /* 通过 ":" 分割, 获取无障碍服务数组. */
    .filter(it => !it.startsWith(`${autojs.packageName}/`)) /* 过滤可能的 AutoJs6 无障碍服务, 避免重复. */
    .join(':'); /* 重新组合过滤后的无障碍服务, 生成列表. */

/* [ 3. 无障碍服务列表中加入 AutoJs6. ] */
let servicesWithAutoJs6 = (() => {
    /* 无障碍服务格式: "包名/服务类名" */
    let serviceAutoJs6 = `${autojs.packageName}/${org.autojs.autojs.core.accessibility.AccessibilityServiceUsher.class.getName()}`;
    return servicesWithoutAutoJs6.length > 0 ? `${servicesWithoutAutoJs6}:${serviceAutoJs6}` : serviceAutoJs6;
})();

/* [ 4. 通过覆盖系统的无障碍物服列表, 使 AutoJs6 无障碍服务生效. ] */
shizuku(`settings put secure enabled_accessibility_services ${servicesWithAutoJs6}`);

/* 需特别留意, 如果只执行 shizuku(`settings put secure enabled_accessibility_services ${AutoJs6 包名}/${AutoJs6 服务类名}`), 系统将只启用 AutoJs6 无障碍服务, 其他应用的无障碍服务将全部关闭. */

/* 另, 禁用 AutoJs6 无障碍服务, 只需执行上述示例的 [ 1, 2, 4 ] 步骤即可. */
```

### shizuku(cmdList) {#shizuku_shizuku_cmdlist}

**`6.4.0`** **`Overload 2/2`**

- **cmdList** { string (dataTypes.html#datatypes_string)[] (dataTypes.html#datatypes_array) } - 待执行的多行命令
- **returns** { ShellResult (shellResultType.html) } - Shell 结果

使用 Shizuku 一次性执行多行命令, 每行命令对应 `cmdList` 数组中的一个元素.

```js
shizuku([ 'cmd-a', 'cmd-b', 'cmd-c' ]);
shizuku('cmd-a\ncmd-b\ncmd-c'); /* 同上. */
```
