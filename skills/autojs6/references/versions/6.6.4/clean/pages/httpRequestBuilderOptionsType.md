---
title: "HttpRequestBuilderOptions"
version: "6.6.4"
source_html: "raw/httpRequestBuilderOptionsType.html"
---

# HttpRequestBuilderOptions {#httprequestbuilderoptionstype_httprequestbuilderoptions}

此章节待补充或完善...

Marked by SuperMonster003 on Mar 21, 2023.

HttpRequestBuilderOptions 是一个构建 HTTP 请求时用于传递构建选项的接口.
这些选项将影响 HTTP 请求的构建.

常见相关方法或属性:

- http.buildRequest (http.html#http_m_buildRequest)(url, **options**)
- http.request (http.html#http_m_request)(url, **options**, callback)
- http.get (http.html#http_m_get)(url, **options**, callback)
- http.post (http.html#http_m_post)(url, data, **options**, callback)
- http.postJson (http.html#http_m_postJson)(url, data, **options**, callback)
- http.postMultipart (http.html#http_m_postMultipart)(url, files, **options**, callback)

HttpRequestBuilderOptions

## [p?] timeout {#httprequestbuilderoptionstype_p_timeout}

- [ `30000` ] { number (dataTypes.html#datatypes_number) } - 超时时间, 单位为秒
