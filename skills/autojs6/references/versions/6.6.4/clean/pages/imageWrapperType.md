---
title: "包装图像类 (ImageWrapper)"
version: "6.6.4"
source_html: "raw/imageWrapperType.html"
---

# 包装图像类 (ImageWrapper) {#imagewrappertype_imagewrapper}

此章节待补充或完善...

Marked by SuperMonster003 on Mar 24, 2023.

包装图像类用于 AutoJs6 的图像处理.

包装后的图像类隐藏了内部复杂的图像处理细节, 便于图像数据的 [ 生成 / 访问 / 传递 / 交互 ].

```js
util.getClassName(ImageWrapper); // org.autojs.autojs.core.image.ImageWrapper
images.read('./picture.jpg') instanceof ImageWrapper; /* ImageWrapper 实例判断. */
ImageWrapper.ofBitmap(bitmap); /* 将 Bitmap 包装为 ImageWrapper. */
```

在 [ images (image.html) / ocr (ocr.html) / canvas (canvas.html) ] 等模块的方法中, 均或多或少地涉及 `ImageWrapper` 类型参数或返回值.

ImageWrapper

## [m#] oneShot {#imagewrappertype_m_oneshot}

### oneShot() {#imagewrappertype_oneshot}

**`6.2.0`**

- **returns** { ImageWrapper (imageWrapperType.html) }

//// -=-= PENDING =-=- ////
