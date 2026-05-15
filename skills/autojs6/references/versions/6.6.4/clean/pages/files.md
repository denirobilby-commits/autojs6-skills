---
title: "文件 (Files)"
version: "6.6.4"
source_html: "raw/files.html"
---

# 文件 (Files) {#files_files}

此章节待补充或完善...

Marked by SuperMonster003 on Oct 22, 2022.

files模块提供了一些常见的文件处理, 包括文件读写、移动、复制、删掉等.

一次性的文件读写可以直接使用`files.read()`, `files.write()`, `files.append()`等方便的函数, 但如果需要频繁读写或随机读写, 则使用`open()`函数打开一个文件对象来操作文件, 并在操作完毕后调用`close()`函数关闭文件.

## files.isFile(path) {#files_files_isfile_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回路径path是否是文件.

```
log(files.isDir("/sdcard/文件夹/")); //返回false
log(files.isDir("/sdcard/文件.txt")); //返回true
```

## files.isDir(path) {#files_files_isdir_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回路径path是否是文件夹.

```
log(files.isDir("/sdcard/文件夹/")); //返回true
log(files.isDir("/sdcard/文件.txt")); //返回false
```

## files.isEmptyDir(path) {#files_files_isemptydir_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回文件夹path是否为空文件夹. 如果该路径并非文件夹, 则直接返回`false`.

## files.join(parent, child) {#files_files_join_parent_child}

- `parent` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 父目录路径
- `child` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 子路径
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

连接两个路径并返回, 例如`files.join("/sdcard/", "1.txt")`返回"/sdcard/1.txt".

## files.create(path) {#files_files_create_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

创建一个文件或文件夹并返回是否创建成功. 如果文件已经存在, 则直接返回`false`.

```
files.create("/sdcard/新文件夹/");
```

## files.createWithDirs(path) {#files_files_createwithdirs_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

创建一个文件或文件夹并返回是否创建成功. 如果文件所在文件夹不存在, 则先创建他所在的一系列文件夹. 如果文件已经存在, 则直接返回`false`.

```
files.createWithDirs("/sdcard/新文件夹/新文件夹/新文件夹/1.txt");
```

## files.exists(path) {#files_files_exists_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

返回在路径path处的文件是否存在.

## files.ensureDir(path) {#files_files_ensuredir_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径

确保路径path所在的文件夹存在. 如果该路径所在文件夹不存在, 则创建该文件夹.

例如对于路径"/sdcard/Download/ABC/1.txt", 如果/Download/文件夹不存在, 则会先创建Download, 再创建ABC文件夹.

## files.read(path[, encoding = "utf-8"]) {#files_files_read_path_encoding_utf_8}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `encoding` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 字符编码, 可选, 默认为utf-8
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

读取文本文件path的所有内容并返回. 如果文件不存在, 则抛出`FileNotFoundException`.

```
log(files.read("/sdcard/1.txt"));
```

## files.readBytes(path) {#files_files_readbytes_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { byte[] }

读取文件path的所有内容并返回一个字节数组. 如果文件不存在, 则抛出`FileNotFoundException`.

注意, 该数组是Java的数组, 不具有JavaScript数组的forEach, slice等函数.

一个以16进制形式打印文件的例子如下:

```
var data = files.readBytes("/sdcard/1.png");
var sb = new java.lang.StringBuilder();
for(var i = 0; i < data.length; i++){
    sb.append(data[i].toString(16));
}
log(sb.toString());
```

## files.write(path, text[, encoding = "utf-8"]) {#files_files_write_path_text_encoding_utf_8}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `text` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要写入的文本内容
- `encoding` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 字符编码

把text写入到文件path中. 如果文件存在则覆盖, 不存在则创建.

```
var text = "文件内容";
//写入文件
files.write("/sdcard/1.txt", text);
//用其他应用查看文件
app.viewFile("/sdcard/1.txt");
```

## files.writeBytes(path, bytes) {#files_files_writebytes_path_bytes}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `bytes` { byte[] } 字节数组, 要写入的二进制数据

把bytes写入到文件path中. 如果文件存在则覆盖, 不存在则创建.

## files.append(path, text[, encoding = 'utf-8']) {#files_files_append_path_text_encoding_utf_8}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `text` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要写入的文本内容
- `encoding` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 字符编码

把text追加到文件path的末尾. 如果文件不存在则创建.

```
var text = "追加的文件内容";
files.append("/sdcard/1.txt", text);
files.append("/sdcard/1.txt", text);
//用其他应用查看文件
app.viewFile("/sdcard/1.txt");
```

## files.appendBytes(path, text[, encoding = 'utf-8']) {#files_files_appendbytes_path_text_encoding_utf_8}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `bytes` { byte[] } 字节数组, 要写入的二进制数据

把bytes追加到文件path的末尾. 如果文件不存在则创建.

## files.copy(fromPath, toPath) {#files_files_copy_frompath_topath}

- `fromPath` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要复制的原文件路径
- `toPath` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 复制到的文件路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

复制文件, 返回是否复制成功. 例如`files.copy("/sdcard/1.txt", "/sdcard/Download/1.txt")`.

## files.move(fromPath, toPath) {#files_files_move_frompath_topath}

- `fromPath` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要移动的原文件路径
- `toPath` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 移动到的文件路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

移动文件, 返回是否移动成功. 例如`files.move("/sdcard/1.txt", "/sdcard/Download/1.txt")`会把1.txt文件从sd卡根目录移动到Download文件夹.

## files.rename(path, newName) {#files_files_rename_path_newname}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要重命名的原文件路径
- `newName` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要重命名的新文件名
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

重命名文件, 并返回是否重命名成功. 例如`files.rename("/sdcard/1.txt", "2.txt")`.

## files.renameWithoutExtension(path, newName) {#files_files_renamewithoutextension_path_newname}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要重命名的原文件路径
- `newName` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 要重命名的新文件名
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

重命名文件, 不包含拓展名, 并返回是否重命名成功. 例如`files.rename("/sdcard/1.txt", "2")`会把"1.txt"重命名为"2.txt".

## files.getName(path) {#files_files_getname_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回文件的文件名. 例如`files.getName("/sdcard/1.txt")`返回"1.txt".

## files.getNameWithoutExtension(path) {#files_files_getnamewithoutextension_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回不含拓展名的文件的文件名. 例如`files.getName("/sdcard/1.txt")`返回"1".

## files.getExtension(path) {#files_files_getextension_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回文件的拓展名. 例如`files.getExtension("/sdcard/1.txt")`返回"txt".

## files.remove(path) {#files_files_remove_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

删除文件或**空文件夹**, 返回是否删除成功.

## files.removeDir(path) {#files_files_removedir_path}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- 返回 { boolean (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) }

删除文件夹, 如果文件夹不为空, 则删除该文件夹的所有内容再删除该文件夹, 返回是否全部删除成功.

## files.getSdcardPath() {#files_files_getsdcardpath}

- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回SD卡路径. 所谓SD卡, 即外部存储器.

## files.cwd() {#files_files_cwd}

- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回脚本的"当前工作文件夹路径". 该路径指的是, 如果脚本本身为脚本文件, 则返回这个脚本文件所在目录；否则返回`null`获取其他设定路径.

例如, 对于脚本文件"/sdcard/脚本/1.js"运行`files.cwd()`返回"/sdcard/脚本/".

## files.path(relativePath) {#files_files_path_relativepath}

- `relativePath` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 相对路径
- 返回 { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) }

返回相对路径对应的绝对路径. 例如`files.path("./1.png")`, 如果运行这个语句的脚本位于文件夹"/sdcard/脚本/"中, 则返回`"/sdcard/脚本/1.png"`.

## files.listDir(path[, filter]) {#files_files_listdir_path_filter}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 路径
- `filter` { Function (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) } 过滤函数, 可选. 接收一个`string`参数（文件名）, 返回一个`boolean`值.

列出文件夹path下的满足条件的文件和文件夹的名称的数组. 如果不加filter参数, 则返回所有文件和文件夹.

列出sdcard目录下所有文件和文件夹为:

```
var arr = files.listDir("/sdcard/");
log(arr);
```

列出脚本目录下所有js脚本文件为:

```
var dir = "/sdcard/脚本/";
var jsFiles = files.listDir(dir, function(name){
    return name.endsWith(".js") && files.isFile(files.join(dir, name));
});
log(jsFiles);
```

## open(path[, mode = "r", encoding = "utf-8", bufferSize = 8192]) {#files_open_path_mode_r_encoding_utf_8_buffersize_8192}

- `path` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 文件路径, 例如"/sdcard/1.txt".

- `mode` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 文件打开模式, 包括:
- "r": 只读文本模式. 该模式下只能对文件执行**文本**读取操作.
- "w": 只写文本模式. 该模式下只能对文件执行**文本**覆盖写入操作.
- "a": 附加文本模式. 该模式下将会把写入的文本附加到文件末尾.
- "rw": 随机读写文本模式. 该模式下将会把写入的文本附加到文件末尾.
目前暂不支持二进制模式, 随机读写模式.

- `encoding` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 字符编码.
- `bufferSize` { number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 文件读写的缓冲区大小.

打开一个文件. 根据打开模式返回不同的文件对象. 包括：

- "r": 返回一个ReadableTextFile对象.
- "w", "a": 返回一个WritableTextFile对象.

对于"w"模式, 如果文件并不存在, 则会创建一个, 已存在则会清空该文件内容；其他模式文件不存在会抛出FileNotFoundException.

# ReadableTextFile {#files_readabletextfile}

可读文件对象.

## ReadableTextFile.read() {#files_readabletextfile_read}

返回该文件剩余的所有内容的字符串.

## ReadableTextFile.read(maxCount) {#files_readabletextfile_read_maxcount}

- `maxCount` { Number (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type) } 最大读取的字符数量

读取该文件接下来最长为maxCount的字符串并返回. 即使文件剩余内容不足maxCount也不会出错.

## ReadableTextFile.readline() {#files_readabletextfile_readline}

读取一行并返回（不包含换行符）.

## ReadableTextFile.readlines() {#files_readabletextfile_readlines}

读取剩余的所有行, 并返回它们按顺序组成的字符串数组.

## close() {#files_close}

关闭该文件.

**打开一个文件不再使用时务必关闭**

# PWritableTextFile {#files_pwritabletextfile}

可写文件对象.

## PWritableTextFile.write(text) {#files_pwritabletextfile_write_text}

- `text` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 文本

把文本内容text写入到文件中.

## PWritableTextFile.writeline(line) {#files_pwritabletextfile_writeline_line}

- `text` { string (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) } 文本

把文本line写入到文件中并写入一个换行符.

## PWritableTextFile.writelines(lines) {#files_pwritabletextfile_writelines_lines}

- `lines` { Array (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) } 字符串数组

把很多行写入到文件中....

## PWritableTextFile.flush() {#files_pwritabletextfile_flush}

把缓冲区内容输出到文件中.

## PWritableTextFile.close() {#files_pwritabletextfile_close}

关闭文件. 同时会被缓冲区内容输出到文件.

**打开一个文件写入后, 不再使用时务必关闭, 否则文件可能会丢失**
