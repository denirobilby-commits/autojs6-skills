---
title: "条码 (Barcode)"
version: "6.6.4"
source_html: "raw/barcode.html"
---

# 条码 (Barcode) {#barcode_barcode}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 30, 2023.

barcode 模块用于识别图像中的条码.

barcode

```ts
interface Barcode {

    (options?: DetectOptions): string | string[] | null;
    (isAll: boolean): string | string[] | null;
    (img: ImageWrapper | string, options?: DetectOptions): string | string[] | null;
    (img: ImageWrapper | string, isAll: boolean): string | string[] | null;

    detect(options?: DetectOptions): Barcode.Result | Barcode.Result[] | null;
    detect(isAll: boolean): Barcode.Result | Barcode.Result[] | null;
    detect(img: ImageWrapper | string, options?: DetectOptions): Barcode.Result | Barcode.Result[] | null;
    detect(img: ImageWrapper | string, isAll: boolean): Barcode.Result | Barcode.Result[] | null;

    detectAll(options?: DetectOptionsWithoutIsAll): Barcode.Result[];
    detectAll(img: ImageWrapper | string, options?: DetectOptionsWithoutIsAll): Barcode.Result[];

    recognizeText(options?: DetectOptions): string | string[] | null;
    recognizeText(isAll: boolean): string | string[] | null;
    recognizeText(img: ImageWrapper | string, options?: DetectOptions): string | string[] | null;
    recognizeText(img: ImageWrapper | string, isAll: boolean): string | string[] | null;

    recognizeTexts(options?: DetectOptionsWithoutIsAll): string[];
    recognizeTexts(img: ImageWrapper | string, options?: DetectOptionsWithoutIsAll): string[];

}
```
