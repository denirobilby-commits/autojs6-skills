---
title: "设备 (Device)"
version: "6.6.4"
source_html: "raw/device.html"
---

# 设备 (Device) {#device_device}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 22, 2022.

device模块提供了与设备有关的信息与操作, 例如获取设备宽高, 内存使用率, IMEI, 调整设备亮度、音量等.

此模块的部分函数, 例如调整音量, 需要"修改系统设置"的权限. 如果没有该权限, 会抛出`SecurityException`并跳转到权限设置界面.

## device.width {#device_device_width}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

设备屏幕分辨率宽度. 例如1080.

## device.height {#device_device_height}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

设备屏幕分辨率高度. 例如1920.

## device.buildId {#device_device_buildid}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

Either a changelist number, or a label like "M4-rc20".

修订版本号, 或者诸如"M4-rc20"的标识.

## device.broad {#device_device_broad}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The name of the underlying board, like "goldfish".

设备的主板(?)型号.

## device.brand {#device_device_brand}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The consumer-visible brand with which the product/hardware will be associated, if any.

与产品或硬件相关的厂商品牌, 如"Xiaomi", "Huawei"等.

## device.device {#device_device_device}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The name of the industrial design.

设备在工业设计中的名称.

## device.model {#device_device_model}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The end-user-visible name for the end product.

设备型号.

## device.product {#device_device_product}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The name of the overall product.

整个产品的名称.

## device.bootloader {#device_device_bootloader}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The system bootloader version number.

设备Bootloader的版本.

## device.hardware {#device_device_hardware}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The name of the hardware (from the kernel command line or /proc).

设备的硬件名称(来自内核命令行或者/proc).

## device.fingerprint {#device_device_fingerprint}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

A string that uniquely identifies this build. Do not attempt to parse this value.

构建(build)的唯一标识码.

## device.serial {#device_device_serial}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

A hardware serial number, if available. Alphanumeric only, case-insensitive.

硬件序列号.

## device.sdkInt {#device_device_sdkint}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

The user-visible SDK version of the framework; its possible values are defined in Build.VERSION_CODES.

安卓系统API版本. 例如安卓4.4的sdkInt为19.

## device.incremental {#device_device_incremental}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The internal value used by the underlying source control to represent this build. E.g., a perforce changelist number or a git hash.

## device.release {#device_device_release}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The user-visible version string. E.g., "1.0" or "3.4b5".

Android系统版本号. 例如"5.0", "7.1.1".

## device.baseOS {#device_device_baseos}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The base OS build the product is based on.

## device.securityPatch {#device_device_securitypatch}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The user-visible security patch level.

安全补丁程序级别.

## device.codename {#device_device_codename}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

The current development codename, or the string "REL" if this is a release build.

开发代号, 例如发行版是"REL".

## device.getIMEI() {#device_device_getimei}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回设备的IMEI.

## device.getAndroidId() {#device_device_getandroidid}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回设备的Android ID.

Android ID为一个用16进制字符串表示的64位整数, 在设备第一次使用时随机生成, 之后不会更改, 除非恢复出厂设置.

## device.getMacAddress() {#device_device_getmacaddress}

- { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回设备的Mac地址. 该函数需要在有WLAN连接的情况下才能获取, 否则会返回null.

**可能的后续修改**：未来可能增加有root权限的情况下通过root权限获取, 从而在没有WLAN连接的情况下也能返回正确的Mac地址, 因此请勿使用此函数判断WLAN连接.

## device.getBrightness() {#device_device_getbrightness}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

返回当前的(手动)亮度. 范围为0~255.

## device.getBrightnessMode() {#device_device_getbrightnessmode}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

返回当前亮度模式, 0为手动亮度, 1为自动亮度.

## device.setBrightness(b) {#device_device_setbrightness_b}

- `b` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 亮度, 范围0~255

设置当前手动亮度. 如果当前是自动亮度模式, 该函数不会影响屏幕的亮度.

此函数需要"修改系统设置"的权限. 如果没有该权限, 会抛出SecurityException并跳转到权限设置界面.

## device.setBrightnessMode(mode) {#device_device_setbrightnessmode_mode}

- `mode` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 亮度模式, 0为手动亮度, 1为自动亮度

设置当前亮度模式.

此函数需要"修改系统设置"的权限. 如果没有该权限, 会抛出SecurityException并跳转到权限设置界面.

## device.getMusicVolume() {#device_device_getmusicvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回当前媒体音量.

## device.getNotificationVolume() {#device_device_getnotificationvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回当前通知音量.

## device.getAlarmVolume() {#device_device_getalarmvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回当前闹钟音量.

## device.getMusicMaxVolume() {#device_device_getmusicmaxvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回媒体音量的最大值.

## device.getNotificationMaxVolume() {#device_device_getnotificationmaxvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回通知音量的最大值.

## device.getAlarmMaxVolume() {#device_device_getalarmmaxvolume}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 整数值

返回闹钟音量的最大值.

## device.setMusicVolume(volume) {#device_device_setmusicvolume_volume}

- `volume` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 音量

设置当前媒体音量.

此函数需要"修改系统设置"的权限. 如果没有该权限, 会抛出SecurityException并跳转到权限设置界面.

## device.setNotificationVolume(volume) {#device_device_setnotificationvolume_volume}

- `volume` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 音量

设置当前通知音量.

此函数需要"修改系统设置"的权限. 如果没有该权限, 会抛出SecurityException并跳转到权限设置界面.

## device.setAlarmVolume(volume) {#device_device_setalarmvolume_volume}

- `volume` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 音量

设置当前闹钟音量.

此函数需要"修改系统设置"的权限. 如果没有该权限, 会抛出SecurityException并跳转到权限设置界面.

## device.getBattery() {#device_device_getbattery}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 0.0~100.0的浮点数

返回当前电量百分比.

## device.isCharging() {#device_device_ischarging}

- { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回设备是否正在充电.

## device.getTotalMem() {#device_device_gettotalmem}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

返回设备内存总量, 单位字节(B). 1MB = 1024 * 1024B.

## device.getAvailMem() {#device_device_getavailmem}

- { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) }

返回设备当前可用的内存, 单位字节(B).

## device.isScreenOn() {#device_device_isscreenon}

- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回设备屏幕是否是亮着的. 如果屏幕亮着, 返回`true`; 否则返回`false`.

需要注意的是, 类似于vivo xplay系列的息屏时钟不属于"屏幕亮着"的情况, 虽然屏幕确实亮着但只能显示时钟而且不可交互, 此时`isScreenOn()`也会返回`false`.

## device.wakeUp() {#device_device_wakeup}

唤醒设备. 包括唤醒设备CPU、屏幕等. 可以用来点亮屏幕.

## device.wakeUpIfNeeded() {#device_device_wakeupifneeded}

如果屏幕没有点亮, 则唤醒设备.

## device.keepScreenOn([timeout]) {#device_device_keepscreenon_timeout}

- `timeout` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 屏幕保持常亮的时间, 单位毫秒. 如果不加此参数, 则一直保持屏幕常亮.

保持屏幕常亮.

此函数无法阻止用户使用锁屏键等正常关闭屏幕, 只能使得设备在无人操作的情况下保持屏幕常亮；同时, 如果此函数调用时屏幕没有点亮, 则会唤醒屏幕.

在某些设备上, 如果不加参数timeout, 只能在Auto.js的界面保持屏幕常亮, 在其他界面会自动失效, 这是因为设备的省电策略造成的. 因此, 建议使用比较长的时长来代替"一直保持屏幕常亮"的功能, 例如`device.keepScreenOn(3600 * 1000)`.

可以使用`device.cancelKeepingAwake()`来取消屏幕常亮.

```
//一直保持屏幕常亮
device.keepScreenOn()
```

## device.keepScreenDim([timeout]) {#device_device_keepscreendim_timeout}

- `timeout` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 屏幕保持常亮的时间, 单位毫秒. 如果不加此参数, 则一直保持屏幕常亮.

保持屏幕常亮, 但允许屏幕变暗来节省电量. 此函数可以用于定时脚本唤醒屏幕操作, 不需要用户观看屏幕, 可以让屏幕变暗来节省电量.

此函数无法阻止用户使用锁屏键等正常关闭屏幕, 只能使得设备在无人操作的情况下保持屏幕常亮；同时, 如果此函数调用时屏幕没有点亮, 则会唤醒屏幕.

可以使用`device.cancelKeepingAwake()`来取消屏幕常亮.

## device.cancelKeepingAwake() {#device_device_cancelkeepingawake}

取消设备保持唤醒状态. 用于取消`device.keepScreenOn()`, `device.keepScreenDim()`等函数设置的屏幕常亮.

## device.vibrate(millis) {#device_device_vibrate_millis}

- `millis` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 振动时间, 单位毫秒

使设备振动一段时间.

```
//振动两秒
device.vibrate(2000);
```

## device.cancelVibration() {#device_device_cancelvibration}

如果设备处于振动状态, 则取消振动.
