---
title: "MIME Type (MIME 类型)"
version: "6.6.4"
source_html: "raw/mimeTypeGlossary.html"
---

# MIME Type (MIME 类型) {#mimetypeglossary_mime_type_mime}

媒体类型, 也称为 MIME 类型 (Multipurpose Internet Mail Extensions), 是一种标准, 用来表示 [ 文档 / 文件 / 字节流 ] 的性质和格式.

通用结构为 `type/subtype`.

MIME 的组成结构由类型与子类型两个字符串及 '/' 组成, 无空格.

MIME 类型对大小写不敏感, 传统写法为全部小写.

类型 子类型 MIME text plain text/plain html text/html css text/css javascript text/javascript image gif image/gif png image/png jpeg image/jpeg webp image/webp svg+xml image/svg+xml bmp image/bmp x-icon image/x-icon vnd.microsoft.icon image/vnd.microsoft.icon audio wav audio/wav wave audio/wave x-wav audio/x-wav x-pn-wav audio/x-pn-wav midi audio/midi mpeg audio/mpeg webm audio/webm ogg audio/ogg video webm video/webm ogg video/ogg application octet-stream application/octet-stream pkcs12 application/pkcs12 vnd.mspowerpoint application/vnd.mspowerpoint xhtml+xml application/xhtml+xml xml+html application/xml+html xml application/xml pdf application/pdf ogg application/ogg json application/json x-rar-compressed application/x-rar-compressed multipart form-data multipart/form-data byteranges multipart/byteranges

参阅: MDN (https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types)

## text {#mimetypeglossary_text}

普通文本文件.

### plain {#mimetypeglossary_plain}

文本文件默认值.

`text/plain` 可代表未知的文本文件.

### html {#mimetypeglossary_html}

HTML 类型.

### css {#mimetypeglossary_css}

CSS 类型.

网页中要被解析为 CSS 的任何文件必须指定 MIME 为 `text/css`.

通常, 服务器不识别 `*.css` 文件的 MIME 类型, 必须为其指定明确的 MIME 类型.

### javascript {#mimetypeglossary_javascript}

JavaScript 类型.

据 HTML 标准, 应该总是使用 MIME 类型 `text/javascript` 表示 JavaScript 文件.

## image {#mimetypeglossary_image}

图像文件.

### gif {#mimetypeglossary_gif}

GIF 图像 (无损耗压缩方面被 PNG 所替代).

该图像类型是 Web 安全的, 可随时在 Web 页面中使用.

### png {#mimetypeglossary_png}

PNG 图像.

该图像类型是 Web 安全的, 可随时在 Web 页面中使用.

### jpeg {#mimetypeglossary_jpeg}

JPEG 图像.

该图像类型是 Web 安全的, 可随时在 Web 页面中使用.

### webp {#mimetypeglossary_webp}

WebP 图像.

该图像类型 **并非** Web 安全的.

因每个新增图像类型都会增加代码量, 并带来一些安全问题, 浏览器供应商对此会额外谨慎.

### svg+xml {#mimetypeglossary_svg_xml}

SVG 图像 (矢量图).

### bmp {#mimetypeglossary_bmp}

JPEG 图像.

### x-icon {#mimetypeglossary_x_icon}

ICO 图像.

很多浏览器已支持 `image/x-icon` MIME 类型.

### vnd.microsoft.icon {#mimetypeglossary_vnd_microsoft_icon}

微软 ICO 图像.

尽管 `image/vnd.microsoft.icon` 在 ANA 已注册, 它仍为得到广泛支持.

可使用 `image/x-icon` 作为替代品.

参阅: https://www.iana.org/assignments/media-types/image/vnd.microsoft.icon (https://www.iana.org/assignments/media-types/image/vnd.microsoft.icon)

## audio {#mimetypeglossary_audio}

音频文件.

### wav {#mimetypeglossary_wav}

音频流媒体文件类型, 一般支持 PCM 音频编码.

### wave {#mimetypeglossary_wave}

音频流媒体文件类型, 一般支持 PCM 音频编码.

### x-wav {#mimetypeglossary_x_wav}

音频流媒体文件类型, 一般支持 PCM 音频编码.

### x-pn-wav {#mimetypeglossary_x_pn_wav}

音频流媒体文件类型, 一般支持 PCM 音频编码.

### midi {#mimetypeglossary_midi}

MIDI 类型.

### mpeg {#mimetypeglossary_mpeg}

MPEG 类型.

### webm {#mimetypeglossary_webm}

WebM 音频文件类型.

Vorbis 和 Opus 是其最常用的解码器.

### ogg {#mimetypeglossary_ogg}

采用 OGG 多媒体文件格式的音频文件.

Vorbis 是其最常用的音频解码器.

## video {#mimetypeglossary_video}

视频文件.

### webm {#mimetypeglossary_webm_1}

采用 WebM 视频文件格式的音视频文件.

VP8 和 VP9 是其最常用的视频解码器, Vorbis 和 Opus 是其最常用的音频解码器.

### ogg {#mimetypeglossary_ogg_1}

采用 OGG 多媒体文件格式的音视频文件.

常用的视频解码器是 Theora, 音频解码器为 Vorbis.

## application {#mimetypeglossary_application}

二进制数据类型.

### octet-stream {#mimetypeglossary_octet_stream}

这是应用程序文件的默认值, 代表未知的应用程序文件.

### pkcs12 {#mimetypeglossary_pkcs12}

PKCS#12 类型.

在密码学中, PKCS#12 定义了一种存档文件格式, 用于将许多密码学对象作为一个文件来存储.

它通常用于捆绑私钥及其 X.509 证书, 或捆绑信任链的所有成员.

### vnd.mspowerpoint {#mimetypeglossary_vnd_mspowerpoint}

微软 PowerPoint 类型.

### xhtml+xml {#mimetypeglossary_xhtml_xml}

XHTML 类型.

### xml+html {#mimetypeglossary_xml_html}

XHTML 的 MIME 类型之一.

因 HTML5 统一了这些格式, 现已较少使用, 建议使用 `text/html`

### xml {#mimetypeglossary_xml}

XML 类型.

### pdf {#mimetypeglossary_pdf}

PDF 类型.

### ogg {#mimetypeglossary_ogg_2}

采用 OGG 多媒体文件格式的音视频文件类型.

常用的视频解码器是 Theora, 音频解码器为 Vorbis.

### json {#mimetypeglossary_json}

JSON 类型.

参阅: https://www.iana.org/assignments/media-types/application/json (https://www.iana.org/assignments/media-types/application/json)

### x-rar-compressed {#mimetypeglossary_x_rar_compressed}

RAR 编码文件.

## multipart {#mimetypeglossary_multipart}

Multipart 类型表示细分领域的文件类型的种类, 经常对应不同的 MIME 类型, 是复合文件的一种表现方式.

### form-data {#mimetypeglossary_form_data}

`multipart/form-data` 可用于 HTML 表单从浏览器发送信息给服务器.

### byteranges {#mimetypeglossary_byteranges}

`multipart/byteranges` 用于把部分响应报文发送回浏览器.
