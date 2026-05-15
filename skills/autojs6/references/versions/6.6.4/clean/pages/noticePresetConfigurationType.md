---
title: "NoticePresetConfiguration"
version: "6.6.4"
source_html: "raw/noticePresetConfigurationType.html"
---

# NoticePresetConfiguration {#noticepresetconfigurationtype_noticepresetconfiguration}

NoticePresetConfiguration 是一个发送 AutoJs6 通知时用于设置通知及 渠道 (notice.html#notice_通知渠道) 默认行为及默认样式的接口.

常见相关方法或属性:

- notice.config (notice.html#notice_m_config)(**preset**)

NoticePresetConfiguration

## [p?] defaultTitle {#noticepresetconfigurationtype_p_defaulttitle}

- [ `null` ] { string (dataTypes.html#datatypes_string) } - 默认通知标题

`defaultTitle` 用于为通知标题指定一个默认值.

`defaultTitle` 为 `null` 时, 通知标题的值取决于 `content` 属性值:

- `content` 为空或未设置
- 默认值为资源 `R.string.default_script_notification_title` 代表值
- 如简体中文语言对应 "脚本通知", English 语言对应 "Script notification"

- `content` 已设置
- 默认值由系统决定显示文本
- 如应用名称 (AutoJs6)

```js
/* 假设默认配置 config.defaultTitle 未设置. */

/* title 为 "脚本通知" (简体中文语言). */
notice();

/* title 可能显示为 AutoJs6 (由系统决定), 因为 content 已设置. */
notice('hello');
notice({ content: 'hello' }); /* 效果同上. */
```

相关的接口属性:

- NoticeOptions#title (noticeOptionsType.html#noticeoptionstype_p_title)

## [p?] defaultContent {#noticepresetconfigurationtype_p_defaultcontent}

- [ `null` ] { string (dataTypes.html#datatypes_string) } - 默认通知内容

`defaultContent` 用于为通知内容指定一个默认值.

`defaultContent` 为 `null` 时, 通知内容的值取决于 `title` 属性值:

- `title` 为空或未设置
- 默认值为资源 `R.string.default_script_notification_content` 代表值
- 如简体中文语言对应 "来自脚本的通知", English 语言对应 "Notification from script"

- `title` 已设置
- 默认值为空 (不显示任何内容)

```js
/* 假设默认配置 config.defaultContent 未设置. */

/* content 为 "来自脚本的通知" (简体中文语言). */
notice();

/* content 为空, 不显示通知内容, 仅显示标题. */
notice({ title: 'hello' });
notice('', 'hello'); /* 效果同上, 但不常用. */
```

相关的接口属性:

- NoticeOptions#content (noticeOptionsType.html#noticeoptionstype_p_content)

## [p?] defaultBigContent {#noticepresetconfigurationtype_p_defaultbigcontent}

- [ `null` ] { string (dataTypes.html#datatypes_string) } - 默认通知长文本内容

`defaultBigContent` 用于为通知长文本内容指定一个默认值.

`defaultBigContent` 为 `null` 时, 通知消息中将不显示长文本内容.

相关的接口属性:

- NoticeOptions#bigContent (noticeOptionsType.html#noticeoptionstype_p_bigcontent)

## [p?] defaultIsSilent {#noticepresetconfigurationtype_p_defaultissilent}

- [ `null` ] { boolean (dataTypes.html#datatypes_boolean) } - 默认的通知安静模式

`defaultIsSilent` 用于为通知的安静模式指定一个默认值.

相关的接口属性:

- NoticeOptions#isSilent (noticeOptionsType.html#noticeoptionstype_p_issilent)

## [p?] defaultAutoCancel {#noticepresetconfigurationtype_p_defaultautocancel}

- [ `null` ] { boolean (dataTypes.html#datatypes_boolean) } - 通知消息是否自动消除的默认值

`defaultAutoCancel` 用于为通知在用户点击时是否自动消除指定一个默认值.

相关的接口属性:

- NoticeOptions#autoCancel (noticeOptionsType.html#noticeoptionstype_p_autocancel)

## [p?] defaultAppendScriptName {#noticepresetconfigurationtype_p_defaultappendscriptname}

- [ `null` ] { boolean (dataTypes.html#datatypes_boolean) | `'auto'` | `'title'` | `'content'` | `'bigContent'` } - 默认的脚本文件全名附加目标

`defaultAppendScriptName` 用于指定通知消息中附加脚本文件全名的默认附加目标.

相关的接口属性:

- NoticeOptions#appendScriptName (noticeOptionsType.html#noticeoptionstype_p_appendscriptname)

## [p?] defaultPriority {#noticepresetconfigurationtype_p_defaultpriority}

- [ `null` ] { number (dataTypes.html#datatypes_number) | `'default'` | `'low'` | `'min'` | `'high'` | `'max'` } - 默认优先级

`defaultPriority` 用于为通知消息指定一个默认优先级.

`defaultPriority` 为 `null` 时, 通知默认优先级将恢复为 `'high'`.

`defaultPriority` 仅适用于以下操作系统:

- `Android API 24 (7.0) [N]`
- `Android API 25 (7.1-7.1.2) [N_MR1]`

其他版本操作系统将忽略此设置项.

相关的接口属性:

- NoticeOptions#priority (noticeOptionsType.html#noticeoptionstype_p_priority)

## [p?] defaultChannelName {#noticepresetconfigurationtype_p_defaultchannelname}

- [ `null` ] { string (dataTypes.html#datatypes_string) } - 默认渠道名称

`defaultChannelName` 用于为通知渠道名称指定一个默认值.

`defaultChannelName` 为 `null` 时, 渠道名称默认值与通知标题默认值相同, 如 "脚本通知".

相关的接口属性:

- NoticeChannelOptions#name (noticeChannelOptionsType.html#noticechanneloptionstype_p_name)

## [p?] defaultChannelDescription {#noticepresetconfigurationtype_p_defaultchanneldescription}

- [ `null` ] { string (dataTypes.html#datatypes_string) } - 默认渠道描述

`defaultChannelDescription` 用于为通知渠道描述指定一个默认值.

`defaultChannelDescription` 为 `null` 时, 渠道描述默认值与通知内容默认值相同, 如 "来自脚本的通知".

相关的接口属性:

- NoticeChannelOptions#description (noticeChannelOptionsType.html#noticechanneloptionstype_p_description)

## [p?] defaultImportanceForChannel {#noticepresetconfigurationtype_p_defaultimportanceforchannel}

- [ `null` ] { number (dataTypes.html#datatypes_number) | `'default'` | `'high'` | `'low'` | `'max'` | `'min'` | `'none'` | `'unspecified'` } - 默认的渠道通知重要性级别

`defaultImportanceForChannel` 用于为通知渠道指定一个默认重要性级别.

`defaultImportanceForChannel` 为 `null` 时, 渠道默认优先级将恢复为 `'high'`.

相关的接口属性:

- NoticeChannelOptions#importance (noticeChannelOptionsType.html#noticechanneloptionstype_p_importance)

## [p?] defaultEnableVibrationForChannel {#noticepresetconfigurationtype_p_defaultenablevibrationforchannel}

- [ `null` ] { boolean (dataTypes.html#datatypes_boolean) } - 默认渠道振动状态

`defaultEnableVibrationForChannel` 属性可设置默认的渠道振动状态.

`defaultEnableVibrationForChannel` 为 `null` 时, 渠道振动状态将恢复为 `false`, 即禁用振动.

相关的接口属性:

- NoticeChannelOptions#enableVibration (noticeChannelOptionsType.html#noticechanneloptionstype_p_enablevibration)

## [p?] defaultVibrationPatternForChannel {#noticepresetconfigurationtype_p_defaultvibrationpatternforchannel}

- [ `null` ] { OmniVibrationPattern (omniTypes.html#omnitypes_omnivibrationpattern) } - 默认渠道振动模式

`defaultVibrationPatternForChannel` 属性可设置默认的渠道振动模式.

`defaultVibrationPatternForChannel` 为 `null` 时, 渠道振动模式将恢复为 `null`.

相关的接口属性:

- NoticeChannelOptions#vibrationPattern (noticeChannelOptionsType.html#noticechanneloptionstype_p_vibrationpattern)

## [p?] defaultEnableLightsForChannel {#noticepresetconfigurationtype_p_defaultenablelightsforchannel}

- [ `null` ] { boolean (dataTypes.html#datatypes_boolean) } - 渠道的通知指示灯默认行为

`defaultEnableLightsForChannel` 属性可设置渠道的通知指示灯默认行为.

相关的接口属性:

- NoticeChannelOptions#enableLights (noticeChannelOptionsType.html#noticechanneloptionstype_p_enableLights)

## [p?] defaultLightColorForChannel {#noticepresetconfigurationtype_p_defaultlightcolorforchannel}

- [ `null` ] { OmniColor (omniTypes.html#omnitypes_omnicolor) } - 渠道的通知指示灯默认颜色

`defaultLightColorForChannel` 属性可设置渠道的通知指示灯默认颜色.

相关的接口属性:

- NoticeChannelOptions#lightColor (noticeChannelOptionsType.html#noticechanneloptionstype_p_lightcolor)

## [p?] defaultLockscreenVisibilityForChannel {#noticepresetconfigurationtype_p_defaultlockscreenvisibilityforchannel}

- [ `null` ] { number (dataTypes.html#datatypes_number) | `'public'` | `'private'` | `'secret'` | `'no_override'` } - 渠道的通知可见详情的默认级别

`defaultLockscreenVisibilityForChannel` 属性可设置渠道的通知可见详情的默认级别.

相关的接口属性:

- NoticeChannelOptions#lockscreenVisibility (noticeChannelOptionsType.html#noticechanneloptionstype_p_lockscreenvisibility)

## [p?] useDynamicDefaultNotificationId {#noticepresetconfigurationtype_p_usedynamicdefaultnotificationid}

- [ `true` ] { boolean (dataTypes.html#datatypes_boolean) } - 是否使用动态通知 ID

`useDynamicDefaultNotificationId` 属性可设置发送的通知是否使用动态通知 ID.

默认值情况:

- `true` - 动态值 `(System.currentTimeMillis() % Int.MAX_VALUE).toInt()`
- `false` - 常量值 `String('script_notification').hashCode()`

设置 `true` 时, 每一个通知将独立显示, 否则后续通知将覆盖之前的通知.

相关的接口属性:

- NoticeOptions#notificationId (noticeOptionsType.html#noticeoptionstype_p_notificationid)

## [p?] useScriptNameAsDefaultChannelId {#noticepresetconfigurationtype_p_usescriptnameasdefaultchannelid}

- [ `true` ] { boolean (dataTypes.html#datatypes_boolean) } - 是否使用脚本全程作为默认渠道 ID

通知渠道使用 `渠道 ID (Channel ID)` 作为唯一标识, `useScriptNameAsDefaultChannelId` 属性可设置当前发送通知的默认渠道 ID 是否为动态 ID.

默认值情况:

- `true` - 当前运行的脚本文件全名 (如 `test.js`)
- `false` - 常量值 `script_channel`

设置 `true` 时, 默认渠道 ID 为动态 ID, 使用脚本文件全名作为 ID 值, 如 `test.js`. 此时, 在不指定渠道 ID 发送通知时, 将默认在 `test.js` 渠道上发送.

否则, 默认渠道 ID 将固定为 `script_channel` 常量值.

相关的接口属性:

- NoticeOptions#channelId (noticeOptionsType.html#noticeoptionstype_p_channelid)
- NoticeChannelOptions#id (noticeChannelOptionsType.html#noticechanneloptionstype_p_id)

## [p?] enableChannelInvalidModificationWarnings {#noticepresetconfigurationtype_p_enablechannelinvalidmodificationwarnings}

- [ `true` ] { boolean (dataTypes.html#datatypes_boolean) } - 是否在通知渠道修改无作用时显示控制台警告信息

`enableChannelInvalidModificationWarnings` 属性可设置在通知渠道修改无作用时, 是否在显示控制台相关警告信息.

渠道创建后, 将无法通过代码更改渠道的设置 (除名称, 描述, 和受条件限制的优先级之外), 对于渠道的设置, 用户拥有最终控制权:

```js
/* 创建一个全新的通知渠道, 并设置通知指示灯为蓝色. */

let channelId = `test_channel_id_${Date.now()}`;
notice.channel.create(channelId, { lightColor: 'blue' });

/* 通知渠道创建后, 将无法再通过代码更改其配置, 只能由用户更改. */

/* 尝试通过代码修改渠道配置, 将通知指示灯修改为红色. */
notice.channel.create(channelId, { lightColor: 'red' });

/* 此时如果 enableChannelInvalidModificationWarnings 配置为 true, */
/* 将在控制台显示一条警告信息. */
/* 因为修改不会生效, 指示灯依然为蓝色. */

/* 如不希望出现这些警告信息, 可配置选项为 false. */
notice.config({ enableChannelInvalidModificationWarnings: false });
```
