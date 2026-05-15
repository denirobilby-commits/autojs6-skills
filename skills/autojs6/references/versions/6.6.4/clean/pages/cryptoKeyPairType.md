---
title: "CryptoKeyPair"
version: "6.6.4"
source_html: "raw/cryptoKeyPairType.html"
---

# CryptoKeyPair {#cryptokeypairtype_cryptokeypair}

CryptoKeyPair 是 `org.autojs.autojs.core.crypto.Crypto.KeyPair` 的子类, 其实例可代表一个公私密钥对, 主要用于 密文 (crypto.html) 模块.

常见相关方法或属性:

- crypto.generateKeyPair (crypto.html#crypto_m_generatekeypair)
- crypto.KeyPair (crypto.html#crypto_c_keypair)::new

注: 本章节仅列出 CryptoKeyPair 独有的而不包含继承的属性及方法.

CryptoKeyPair

## [p] publicKey {#cryptokeypairtype_p_publickey}

- { CryptoKey (cryptoKeyType.html) } - 公钥

用于非对称加密的公钥.

```js
let kp = crypto.generateKeyPair('RSA', 256);
console.log(kp.publicKey);
```

## [p] privateKey {#cryptokeypairtype_p_privatekey}

- { CryptoKey (cryptoKeyType.html) } - 私钥

用于非对称加密的私钥.

```js
let kp = crypto.generateKeyPair('DSA', 1024);
console.log(kp.privateKey);
```

## [m] toKeySpec {#cryptokeypairtype_m_tokeyspec}

### toKeySpec(transformation) {#cryptokeypairtype_tokeyspec_transformation}

- **transformation** { CryptoCipherTransformation (dataTypes.html#datatypes_cryptociphertransformation) } - 密码转换名称
- **returns** { java.security.Key (https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/class-use/Key.html) } Java 密钥

由密码对生成一个指定算法的 Java 密钥 (Java Key).

`toKeySpec` 中的 "spec" 全称为 "specification", 意为 "规范". 因此, 此方法可理解为将密钥对转换为一个规范的密钥.

需额外留意, 此方法不能通过构造函数生成的实例进行访问, 只能通过 crypto.generateKeyPair (crypto.html#crypto_m_generatekeypair) 的返回值进行访问:

```js
/* 抛出异常. */
new crypto.KeyPair('pub', 'pri').toKeySpec('DES');

/* 无异常. */
crypto.generateKeyPair('DiffieHellman').toKeySpec('DES');
```

`toKeySpec` 方法的实际应用, 可参考 crypto.generateKeyPair (crypto.html#crypto_m_generatekeypair) 小节的示例.

注: 如需转换为 `crypto.Key`, 可使用 `new crypto.Key(key)`.
