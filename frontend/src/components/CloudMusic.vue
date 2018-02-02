<template>

</template>

<script>
  import axios from "axios"
  import crypto from "crypto"
  import bigInt from "big-integer"
  import Buffer from "buffer"

  const cloudMusicInst = axios.create({
    baseURL: "music.163.com/weapi",
  });

  export default {
    name: "cloud-music",
    mounted: function() {
      this.login();
    },
    methods: {
      addPadding(encText, modulus) {
        let len = modulus.length;
        for (let i = 0; len > 0 && modulus[i] === "0"; i++) len--;
        const num = len - encText.length;
        let prefix = "";
        for (let i = 0; i < num; i++) {
          prefix += "0";
        }
        return prefix + encText;
      },
      rsaEncrypt(text, exponent, modulus) {
        let rText = "";
        let radix = 16;
        for (let i = text.length - 1; i >= 0; i--) rText += text[i];
        var biText = bigInt(new Buffer(rText).toString('hex'), radix),
          biEx = bigInt(exponent, radix),
          biMod = bigInt(modulus, radix),
          biRet = biText.modPow(biEx, biMod);
        return addPadding(biRet.toString(radix), modulus);
      },
      aesEncrypt(text, secKey) {
        var cipher = crypto.createCipheriv('AES-128-CBC', secKey, '0102030405060708');
        return cipher.update(text, 'utf-8', 'base64') + cipher.final('base64');
      },
      createSecretKey(size) {
        let keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        let key = "";
        for (let i = 0; i < size; i++) {
          let pos = Math.random() * keys.length;
          pos = Math.floor(pos);
          key = key + keys.charAt(pos)
        }
        return key;
      },
      md5(text) {
        return crypto.createHash("md5").update(text).digest("hex");
      },
      aesRsaEncrypt(text) {
        let modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7';
        let nonce = '0CoJUm6Qyw8W8jud';
        let pubKey = '010001';
        let secKey = this.createSecretKey(16);
        return {
          params: this.aesEncrypt(this.aesEncrypt(text, nonce), secKey),
          encSecKey: this.rsaEncrypt(secKey, pubKey, modulus)
        }
      },
      login() {
        let username = "15267002566";
        let password = "zx37294631";
        let data = {
          phone: username,
          password: this.md5(password),
          rememberLogin: 'true',
        };
        data = crypto.aesRsaEncrypt(JSON.stringify(data));
        cloudMusicInst.post("/login/cellphone", data).then(function(response) {
          console.log(response);
        });
      },
    }
  }
</script>

<style scoped>

</style>
