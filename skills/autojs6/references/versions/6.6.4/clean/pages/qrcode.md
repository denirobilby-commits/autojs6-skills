---
title: "二维码 (QR Code)"
version: "6.6.4"
source_html: "raw/qrcode.html"
---

# 二维码 (QR Code) {#qrcode_qr_code}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 30, 2023.

qrcode 模块用于识别图像中的二维码.

qrcode

```ts
interface QrCode {

    (options?: DetectOptions): string | string[] | null;
    (isAll: boolean): string | string[] | null;
    (img: ImageWrapper | string, options?: DetectOptions): string | string[] | null;
    (img: ImageWrapper | string, isAll: boolean): string | string[] | null;

    detect(options?: DetectOptions): QrCode.Result | QrCode.Result[] | null;
    detect(isAll: boolean): QrCode.Result | QrCode.Result[] | null;
    detect(img: ImageWrapper | string, options?: DetectOptions): QrCode.Result | QrCode.Result[] | null;
    detect(img: ImageWrapper | string, isAll: boolean): QrCode.Result | QrCode.Result[] | null;

    detectAll(options?: DetectOptionsWithoutIsAll): QrCode.Result[];
    detectAll(img: ImageWrapper | string, options?: DetectOptionsWithoutIsAll): QrCode.Result[];

    recognizeText(options?: DetectOptions): string | string[] | null;
    recognizeText(isAll: boolean): string | string[] | null;
    recognizeText(img: ImageWrapper | string, options?: DetectOptions): string | string[] | null;
    recognizeText(img: ImageWrapper | string, isAll: boolean): string | string[] | null;

    recognizeTexts(options?: DetectOptionsWithoutIsAll): string[];
    recognizeTexts(img: ImageWrapper | string, options?: DetectOptionsWithoutIsAll): string[];

}
```
