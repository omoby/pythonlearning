!function(t, n) {
    "object" == typeof exports ? module.exports = exports = n() : "function" == typeof define && define.amd ? define([], n) : t.CryptoJS = n()
}(this, function() {
    var t = t || function(t, n) {
        var i = Object.create || function() {
            function t() {}
            return function(n) {
                var i;
                return t.prototype = n,
                i = new t,
                t.prototype = null ,
                i
            }
        }()
          , e = {}
          , r = e.lib = {}
          , o = r.Base = function() {
            return {
                extend: function(t) {
                    var n = i(this);
                    return t && n.mixIn(t),
                    n.hasOwnProperty("init") && this.init !== n.init || (n.init = function() {
                        n.$super.init.apply(this, arguments)
                    }
                    ),
                    n.init.prototype = n,
                    n.$super = this,
                    n
                },
                create: function() {
                    var t = this.extend();
                    return t.init.apply(t, arguments),
                    t
                },
                init: function() {},
                mixIn: function(t) {
                    for (var n in t)
                        t.hasOwnProperty(n) && (this[n] = t[n]);
                    t.hasOwnProperty("toString") && (this.toString = t.toString)
                },
                clone: function() {
                    return this.init.prototype.extend(this)
                }
            }
        }()
          , s = r.WordArray = o.extend({
            init: function(t, i) {
                t = this.words = t || [],
                i != n ? this.sigBytes = i : this.sigBytes = 4 * t.length
            },
            toString: function(t) {
                return (t || c).stringify(this)
            },
            concat: function(t) {
                var n = this.words
                  , i = t.words
                  , e = this.sigBytes
                  , r = t.sigBytes;
                if (this.clamp(),
                e % 4)
                    for (var o = 0; o < r; o++) {
                        var s = i[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                        n[e + o >>> 2] |= s << 24 - (e + o) % 4 * 8
                    }
                else
                    for (var o = 0; o < r; o += 4)
                        n[e + o >>> 2] = i[o >>> 2];
                return this.sigBytes += r,
                this
            },
            clamp: function() {
                var n = this.words
                  , i = this.sigBytes;
                n[i >>> 2] &= 4294967295 << 32 - i % 4 * 8,
                n.length = t.ceil(i / 4)
            },
            clone: function() {
                var t = o.clone.call(this);
                return t.words = this.words.slice(0),
                t
            },
            random: function(n) {
                for (var i, e = [], r = function(n) {
                    var n = n
                      , i = 987654321
                      , e = 4294967295;
                    return function() {
                        i = 36969 * (65535 & i) + (i >> 16) & e,
                        n = 18e3 * (65535 & n) + (n >> 16) & e;
                        var r = (i << 16) + n & e;
                        return r /= 4294967296,
                        r += .5,
                        r * (t.random() > .5 ? 1 : -1)
                    }
                }, o = 0; o < n; o += 4) {
                    var a = r(4294967296 * (i || t.random()));
                    i = 987654071 * a(),
                    e.push(4294967296 * a() | 0)
                }
                return new s.init(e,n)
            }
        })
          , a = e.enc = {}
          , c = a.Hex = {
            stringify: function(t) {
                for (var n = t.words, i = t.sigBytes, e = [], r = 0; r < i; r++) {
                    var o = n[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                    e.push((o >>> 4).toString(16)),
                    e.push((15 & o).toString(16))
                }
                return e.join("")
            },
            parse: function(t) {
                for (var n = t.length, i = [], e = 0; e < n; e += 2)
                    i[e >>> 3] |= parseInt(t.substr(e, 2), 16) << 24 - e % 8 * 4;
                return new s.init(i,n / 2)
            }
        }
          , u = a.Latin1 = {
            stringify: function(t) {
                for (var n = t.words, i = t.sigBytes, e = [], r = 0; r < i; r++) {
                    var o = n[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                    e.push(String.fromCharCode(o))
                }
                return e.join("")
            },
            parse: function(t) {
                for (var n = t.length, i = [], e = 0; e < n; e++)
                    i[e >>> 2] |= (255 & t.charCodeAt(e)) << 24 - e % 4 * 8;
                return new s.init(i,n)
            }
        }
          , f = a.Utf8 = {
            stringify: function(t) {
                try {
                    return decodeURIComponent(escape(u.stringify(t)))
                } catch (t) {
                    throw new Error("Malformed UTF-8 data")
                }
            },
            parse: function(t) {
                return u.parse(unescape(encodeURIComponent(t)))
            }
        }
          , h = r.BufferedBlockAlgorithm = o.extend({
            reset: function() {
                this._data = new s.init,
                this._nDataBytes = 0
            },
            _append: function(t) {
                "string" == typeof t && (t = f.parse(t)),
                this._data.concat(t),
                this._nDataBytes += t.sigBytes
            },
            _process: function(n) {
                var i = this._data
                  , e = i.words
                  , r = i.sigBytes
                  , o = this.blockSize
                  , a = 4 * o
                  , c = r / a;
                c = n ? t.ceil(c) : t.max((0 | c) - this._minBufferSize, 0);
                var u = c * o
                  , f = t.min(4 * u, r);
                if (u) {
                    for (var h = 0; h < u; h += o)
                        this._doProcessBlock(e, h);
                    var p = e.splice(0, u);
                    i.sigBytes -= f
                }
                return new s.init(p,f)
            },
            clone: function() {
                var t = o.clone.call(this);
                return t._data = this._data.clone(),
                t
            },
            _minBufferSize: 0
        })
          , p = (r.Hasher = h.extend({
            cfg: o.extend(),
            init: function(t) {
                this.cfg = this.cfg.extend(t),
                this.reset()
            },
            reset: function() {
                h.reset.call(this),
                this._doReset()
            },
            update: function(t) {
                return this._append(t),
                this._process(),
                this
            },
            finalize: function(t) {
                t && this._append(t);
                var n = this._doFinalize();
                return n
            },
            blockSize: 16,
            _createHelper: function(t) {
                return function(n, i) {
                    return new t.init(i).finalize(n)
                }
            },
            _createHmacHelper: function(t) {
                return function(n, i) {
                    return new p.HMAC.init(t,i).finalize(n)
                }
            }
        }),
        e.algo = {});
        return e
    }(Math);
    return t
});
//# sourceMappingURL=core.min.js.map
!function(e, t, i) {
    "object" == typeof exports ? module.exports = exports = t(require("./core.min"), require("./sha1.min"), require("./hmac.min")) : "function" == typeof define && define.amd ? define(["./core.min", "./sha1.min", "./hmac.min"], t) : t(e.CryptoJS)
}(this, function(e) {
    return function() {
        var t = e
          , i = t.lib
          , r = i.Base
          , n = i.WordArray
          , o = t.algo
          , a = o.MD5
          , c = o.EvpKDF = r.extend({
            cfg: r.extend({
                keySize: 4,
                hasher: a,
                iterations: 1
            }),
            init: function(e) {
                this.cfg = this.cfg.extend(e)
            },
            compute: function(e, t) {
                for (var i = this.cfg, r = i.hasher.create(), o = n.create(), a = o.words, c = i.keySize, f = i.iterations; a.length < c; ) {
                    s && r.update(s);
                    var s = r.update(e).finalize(t);
                    r.reset();
                    for (var u = 1; u < f; u++)
                        s = r.finalize(s),
                        r.reset();
                    o.concat(s)
                }
                return o.sigBytes = 4 * c,
                o
            }
        });
        t.EvpKDF = function(e, t, i) {
            return c.create(i).compute(e, t)
        }
    }(),
    e.EvpKDF
});
//# sourceMappingURL=evpkdf.min.js.map
!function(r, e) {
    "object" == typeof exports ? module.exports = exports = e(require("./core.min")) : "function" == typeof define && define.amd ? define(["./core.min"], e) : e(r.CryptoJS)
}(this, function(r) {
    return function() {
        function e(r, e, t) {
            for (var n = [], i = 0, o = 0; o < e; o++)
                if (o % 4) {
                    var f = t[r.charCodeAt(o - 1)] << o % 4 * 2
                      , c = t[r.charCodeAt(o)] >>> 6 - o % 4 * 2;
                    n[i >>> 2] |= (f | c) << 24 - i % 4 * 8,
                    i++
                }
            return a.create(n, i)
        }
        var t = r
          , n = t.lib
          , a = n.WordArray
          , i = t.enc;
        i.Base64 = {
            stringify: function(r) {
                var e = r.words
                  , t = r.sigBytes
                  , n = this._map;
                r.clamp();
                for (var a = [], i = 0; i < t; i += 3)
                    for (var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255, f = e[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255, c = e[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, s = o << 16 | f << 8 | c, h = 0; h < 4 && i + .75 * h < t; h++)
                        a.push(n.charAt(s >>> 6 * (3 - h) & 63));
                var p = n.charAt(64);
                if (p)
                    for (; a.length % 4; )
                        a.push(p);
                return a.join("")
            },
            parse: function(r) {
                var t = r.length
                  , n = this._map
                  , a = this._reverseMap;
                if (!a) {
                    a = this._reverseMap = [];
                    for (var i = 0; i < n.length; i++)
                        a[n.charCodeAt(i)] = i
                }
                var o = n.charAt(64);
                if (o) {
                    var f = r.indexOf(o);
                    f !== -1 && (t = f)
                }
                return e(r, t, a)
            },
            _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        }
    }(),
    r.enc.Base64
});
//# sourceMappingURL=enc-base64.min.js.map
!function(e, t, r) {
    "object" == typeof exports ? module.exports = exports = t(require("./core.min"), require("./evpkdf.min")) : "function" == typeof define && define.amd ? define(["./core.min", "./evpkdf.min"], t) : t(e.CryptoJS)
}(this, function(e) {
    e.lib.Cipher || function(t) {
        var r = e
          , i = r.lib
          , n = i.Base
          , c = i.WordArray
          , o = i.BufferedBlockAlgorithm
          , s = r.enc
          , a = (s.Utf8,
        s.Base64)
          , f = r.algo
          , p = f.EvpKDF
          , d = i.Cipher = o.extend({
            cfg: n.extend(),
            createEncryptor: function(e, t) {
                return this.create(this._ENC_XFORM_MODE, e, t)
            },
            createDecryptor: function(e, t) {
                return this.create(this._DEC_XFORM_MODE, e, t)
            },
            init: function(e, t, r) {
                this.cfg = this.cfg.extend(r),
                this._xformMode = e,
                this._key = t,
                this.reset()
            },
            reset: function() {
                o.reset.call(this),
                this._doReset()
            },
            process: function(e) {
                return this._append(e),
                this._process()
            },
            finalize: function(e) {
                e && this._append(e);
                var t = this._doFinalize();
                return t
            },
            keySize: 4,
            ivSize: 4,
            _ENC_XFORM_MODE: 1,
            _DEC_XFORM_MODE: 2,
            _createHelper: function() {
                function e(e) {
                    return "string" == typeof e ? B : x
                }
                return function(t) {
                    return {
                        encrypt: function(r, i, n) {
                            return e(i).encrypt(t, r, i, n)
                        },
                        decrypt: function(r, i, n) {
                            return e(i).decrypt(t, r, i, n)
                        }
                    }
                }
            }()
        })
          , h = (i.StreamCipher = d.extend({
            _doFinalize: function() {
                var e = this._process(!0);
                return e
            },
            blockSize: 1
        }),
        r.mode = {})
          , u = i.BlockCipherMode = n.extend({
            createEncryptor: function(e, t) {
                return this.Encryptor.create(e, t)
            },
            createDecryptor: function(e, t) {
                return this.Decryptor.create(e, t)
            },
            init: function(e, t) {
                this._cipher = e,
                this._iv = t
            }
        })
          , l = h.CBC = function() {
            function e(e, r, i) {
                var n = this._iv;
                if (n) {
                    var c = n;
                    this._iv = t
                } else
                    var c = this._prevBlock;
                for (var o = 0; o < i; o++)
                    e[r + o] ^= c[o]
            }
            var r = u.extend();
            return r.Encryptor = r.extend({
                processBlock: function(t, r) {
                    var i = this._cipher
                      , n = i.blockSize;
                    e.call(this, t, r, n),
                    i.encryptBlock(t, r),
                    this._prevBlock = t.slice(r, r + n)
                }
            }),
            r.Decryptor = r.extend({
                processBlock: function(t, r) {
                    var i = this._cipher
                      , n = i.blockSize
                      , c = t.slice(r, r + n);
                    i.decryptBlock(t, r),
                    e.call(this, t, r, n),
                    this._prevBlock = c
                }
            }),
            r
        }()
          , _ = r.pad = {}
          , v = _.Pkcs7 = {
            pad: function(e, t) {
                for (var r = 4 * t, i = r - e.sigBytes % r, n = i << 24 | i << 16 | i << 8 | i, o = [], s = 0; s < i; s += 4)
                    o.push(n);
                var a = c.create(o, i);
                e.concat(a)
            },
            unpad: function(e) {
                var t = 255 & e.words[e.sigBytes - 1 >>> 2];
                e.sigBytes -= t
            }
        }
          , y = (i.BlockCipher = d.extend({
            cfg: d.cfg.extend({
                mode: l,
                padding: v
            }),
            reset: function() {
                d.reset.call(this);
                var e = this.cfg
                  , t = e.iv
                  , r = e.mode;
                if (this._xformMode == this._ENC_XFORM_MODE)
                    var i = r.createEncryptor;
                else {
                    var i = r.createDecryptor;
                    this._minBufferSize = 1
                }
                this._mode && this._mode.__creator == i ? this._mode.init(this, t && t.words) : (this._mode = i.call(r, this, t && t.words),
                this._mode.__creator = i)
            },
            _doProcessBlock: function(e, t) {
                this._mode.processBlock(e, t)
            },
            _doFinalize: function() {
                var e = this.cfg.padding;
                if (this._xformMode == this._ENC_XFORM_MODE) {
                    e.pad(this._data, this.blockSize);
                    var t = this._process(!0)
                } else {
                    var t = this._process(!0);
                    e.unpad(t)
                }
                return t
            },
            blockSize: 4
        }),
        i.CipherParams = n.extend({
            init: function(e) {
                this.mixIn(e)
            },
            toString: function(e) {
                return (e || this.formatter).stringify(this)
            }
        }))
          , m = r.format = {}
          , k = m.OpenSSL = {
            stringify: function(e) {
                var t = e.ciphertext
                  , r = e.salt;
                if (r)
                    var i = c.create([1398893684, 1701076831]).concat(r).concat(t);
                else
                    var i = t;
                return i.toString(a)
            },
            parse: function(e) {
                var t = a.parse(e)
                  , r = t.words;
                if (1398893684 == r[0] && 1701076831 == r[1]) {
                    var i = c.create(r.slice(2, 4));
                    r.splice(0, 4),
                    t.sigBytes -= 16
                }
                return y.create({
                    ciphertext: t,
                    salt: i
                })
            }
        }
          , x = i.SerializableCipher = n.extend({
            cfg: n.extend({
                format: k
            }),
            encrypt: function(e, t, r, i) {
                i = this.cfg.extend(i);
                var n = e.createEncryptor(r, i)
                  , c = n.finalize(t)
                  , o = n.cfg;
                return y.create({
                    ciphertext: c,
                    key: r,
                    iv: o.iv,
                    algorithm: e,
                    mode: o.mode,
                    padding: o.padding,
                    blockSize: e.blockSize,
                    formatter: i.format
                })
            },
            decrypt: function(e, t, r, i) {
                i = this.cfg.extend(i),
                t = this._parse(t, i.format);
                var n = e.createDecryptor(r, i).finalize(t.ciphertext);
                return n
            },
            _parse: function(e, t) {
                return "string" == typeof e ? t.parse(e, this) : e
            }
        })
          , g = r.kdf = {}
          , S = g.OpenSSL = {
            execute: function(e, t, r, i) {
                i || (i = c.random(8));
                var n = p.create({
                    keySize: t + r
                }).compute(e, i)
                  , o = c.create(n.words.slice(t), 4 * r);
                return n.sigBytes = 4 * t,
                y.create({
                    key: n,
                    iv: o,
                    salt: i
                })
            }
        }
          , B = i.PasswordBasedCipher = x.extend({
            cfg: x.cfg.extend({
                kdf: S
            }),
            encrypt: function(e, t, r, i) {
                i = this.cfg.extend(i);
                var n = i.kdf.execute(r, e.keySize, e.ivSize);
                i.iv = n.iv;
                var c = x.encrypt.call(this, e, t, n.key, i);
                return c.mixIn(n),
                c
            },
            decrypt: function(e, t, r, i) {
                i = this.cfg.extend(i),
                t = this._parse(t, i.format);
                var n = i.kdf.execute(r, e.keySize, e.ivSize, t.salt);
                i.iv = n.iv;
                var c = x.decrypt.call(this, e, t, n.key, i);
                return c
            }
        })
    }()
});
//# sourceMappingURL=cipher-core.min.js.map
!function(e, i) {
    "object" == typeof exports ? module.exports = exports = i(require("./core.min")) : "function" == typeof define && define.amd ? define(["./core.min"], i) : i(e.CryptoJS)
}(this, function(e) {
    !function() {
        var i = e
          , t = i.lib
          , n = t.Base
          , s = i.enc
          , r = s.Utf8
          , o = i.algo;
        o.HMAC = n.extend({
            init: function(e, i) {
                e = this._hasher = new e.init,
                "string" == typeof i && (i = r.parse(i));
                var t = e.blockSize
                  , n = 4 * t;
                i.sigBytes > n && (i = e.finalize(i)),
                i.clamp();
                for (var s = this._oKey = i.clone(), o = this._iKey = i.clone(), a = s.words, f = o.words, c = 0; c < t; c++)
                    a[c] ^= 1549556828,
                    f[c] ^= 909522486;
                s.sigBytes = o.sigBytes = n,
                this.reset()
            },
            reset: function() {
                var e = this._hasher;
                e.reset(),
                e.update(this._iKey)
            },
            update: function(e) {
                return this._hasher.update(e),
                this
            },
            finalize: function(e) {
                var i = this._hasher
                  , t = i.finalize(e);
                i.reset();
                var n = i.finalize(this._oKey.clone().concat(t));
                return n
            }
        })
    }()
});
//# sourceMappingURL=hmac.min.js.map
!function(e, o, r) {
    "object" == typeof exports ? module.exports = exports = o(require("./core.min"), require("./cipher-core.min")) : "function" == typeof define && define.amd ? define(["./core.min", "./cipher-core.min"], o) : o(e.CryptoJS)
}(this, function(e) {
    return e.mode.ECB = function() {
        var o = e.lib.BlockCipherMode.extend();
        return o.Encryptor = o.extend({
            processBlock: function(e, o) {
                this._cipher.encryptBlock(e, o)
            }
        }),
        o.Decryptor = o.extend({
            processBlock: function(e, o) {
                this._cipher.decryptBlock(e, o)
            }
        }),
        o
    }(),
    e.mode.ECB
});
//# sourceMappingURL=mode-ecb.min.js.map
!function(e, r, i) {
    "object" == typeof exports ? module.exports = exports = r(require("./core.min"), require("./cipher-core.min")) : "function" == typeof define && define.amd ? define(["./core.min", "./cipher-core.min"], r) : r(e.CryptoJS)
}(this, function(e) {
    return e.pad.Pkcs7
});
//# sourceMappingURL=pad-pkcs7.min.js.map
!function(e, r, i) {
    "object" == typeof exports ? module.exports = exports = r(require("./core.min"), require("./enc-base64.min"), require("./md5.min"), require("./evpkdf.min"), require("./cipher-core.min")) : "function" == typeof define && define.amd ? define(["./core.min", "./enc-base64.min", "./md5.min", "./evpkdf.min", "./cipher-core.min"], r) : r(e.CryptoJS)
}(this, function(e) {
    return function() {
        var r = e
          , i = r.lib
          , n = i.BlockCipher
          , o = r.algo
          , t = []
          , c = []
          , s = []
          , f = []
          , a = []
          , d = []
          , u = []
          , v = []
          , h = []
          , y = [];
        !function() {
            for (var e = [], r = 0; r < 256; r++)
                r < 128 ? e[r] = r << 1 : e[r] = r << 1 ^ 283;
            for (var i = 0, n = 0, r = 0; r < 256; r++) {
                var o = n ^ n << 1 ^ n << 2 ^ n << 3 ^ n << 4;
                o = o >>> 8 ^ 255 & o ^ 99,
                t[i] = o,
                c[o] = i;
                var p = e[i]
                  , l = e[p]
                  , _ = e[l]
                  , k = 257 * e[o] ^ 16843008 * o;
                s[i] = k << 24 | k >>> 8,
                f[i] = k << 16 | k >>> 16,
                a[i] = k << 8 | k >>> 24,
                d[i] = k;
                var k = 16843009 * _ ^ 65537 * l ^ 257 * p ^ 16843008 * i;
                u[o] = k << 24 | k >>> 8,
                v[o] = k << 16 | k >>> 16,
                h[o] = k << 8 | k >>> 24,
                y[o] = k,
                i ? (i = p ^ e[e[e[_ ^ p]]],
                n ^= e[e[n]]) : i = n = 1
            }
        }();
        var p = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
          , l = o.AES = n.extend({
            _doReset: function() {
                if (!this._nRounds || this._keyPriorReset !== this._key) {
                    for (var e = this._keyPriorReset = this._key, r = e.words, i = e.sigBytes / 4, n = this._nRounds = i + 6, o = 4 * (n + 1), c = this._keySchedule = [], s = 0; s < o; s++)
                        if (s < i)
                            c[s] = r[s];
                        else {
                            var f = c[s - 1];
                            s % i ? i > 6 && s % i == 4 && (f = t[f >>> 24] << 24 | t[f >>> 16 & 255] << 16 | t[f >>> 8 & 255] << 8 | t[255 & f]) : (f = f << 8 | f >>> 24,
                            f = t[f >>> 24] << 24 | t[f >>> 16 & 255] << 16 | t[f >>> 8 & 255] << 8 | t[255 & f],
                            f ^= p[s / i | 0] << 24),
                            c[s] = c[s - i] ^ f
                        }
                    for (var a = this._invKeySchedule = [], d = 0; d < o; d++) {
                        var s = o - d;
                        if (d % 4)
                            var f = c[s];
                        else
                            var f = c[s - 4];
                        d < 4 || s <= 4 ? a[d] = f : a[d] = u[t[f >>> 24]] ^ v[t[f >>> 16 & 255]] ^ h[t[f >>> 8 & 255]] ^ y[t[255 & f]]
                    }
                }
            },
            encryptBlock: function(e, r) {
                this._doCryptBlock(e, r, this._keySchedule, s, f, a, d, t)
            },
            decryptBlock: function(e, r) {
                var i = e[r + 1];
                e[r + 1] = e[r + 3],
                e[r + 3] = i,
                this._doCryptBlock(e, r, this._invKeySchedule, u, v, h, y, c);
                var i = e[r + 1];
                e[r + 1] = e[r + 3],
                e[r + 3] = i
            },
            _doCryptBlock: function(e, r, i, n, o, t, c, s) {
                for (var f = this._nRounds, a = e[r] ^ i[0], d = e[r + 1] ^ i[1], u = e[r + 2] ^ i[2], v = e[r + 3] ^ i[3], h = 4, y = 1; y < f; y++) {
                    var p = n[a >>> 24] ^ o[d >>> 16 & 255] ^ t[u >>> 8 & 255] ^ c[255 & v] ^ i[h++]
                      , l = n[d >>> 24] ^ o[u >>> 16 & 255] ^ t[v >>> 8 & 255] ^ c[255 & a] ^ i[h++]
                      , _ = n[u >>> 24] ^ o[v >>> 16 & 255] ^ t[a >>> 8 & 255] ^ c[255 & d] ^ i[h++]
                      , k = n[v >>> 24] ^ o[a >>> 16 & 255] ^ t[d >>> 8 & 255] ^ c[255 & u] ^ i[h++];
                    a = p,
                    d = l,
                    u = _,
                    v = k
                }
                var p = (s[a >>> 24] << 24 | s[d >>> 16 & 255] << 16 | s[u >>> 8 & 255] << 8 | s[255 & v]) ^ i[h++]
                  , l = (s[d >>> 24] << 24 | s[u >>> 16 & 255] << 16 | s[v >>> 8 & 255] << 8 | s[255 & a]) ^ i[h++]
                  , _ = (s[u >>> 24] << 24 | s[v >>> 16 & 255] << 16 | s[a >>> 8 & 255] << 8 | s[255 & d]) ^ i[h++]
                  , k = (s[v >>> 24] << 24 | s[a >>> 16 & 255] << 16 | s[d >>> 8 & 255] << 8 | s[255 & u]) ^ i[h++];
                e[r] = p,
                e[r + 1] = l,
                e[r + 2] = _,
                e[r + 3] = k
            },
            keySize: 8
        });
        r.AES = n._createHelper(l)
    }(),
    e.AES
});
//# sourceMappingURL=aes.min.js.map
!function(e, n) {
    "object" == typeof exports ? module.exports = exports = n(require("./core.min")) : "function" == typeof define && define.amd ? define(["./core.min"], n) : n(e.CryptoJS)
}(this, function(e) {
    return e.enc.Utf8
});
//# sourceMappingURL=enc-utf8.min.js.map

var hexcase = 0;
var b64pad = "";
var chrsz = 8;
function hex_md5(r) {
    return binl2hex(core_md5(str2binl(r), r.length * chrsz))
}
function b64_md5(r) {
    return binl2b64(core_md5(str2binl(r), r.length * chrsz))
}
function hex_hmac_md5(r, e) {
    return binl2hex(core_hmac_md5(r, e))
}
function b64_hmac_md5(r, e) {
    return binl2b64(core_hmac_md5(r, e))
}
function calcMD5(r) {
    return binl2hex(core_md5(str2binl(r), r.length * chrsz))
}
function md5_vm_test() {
    return hex_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
}
function core_md5(r, e) {
    r[e >> 5] |= 128 << e % 32;
    r[(e + 64 >>> 9 << 4) + 14] = e;
    var n = 1732584193;
    var a = -271733879;
    var t = -1732584194;
    var d = 271733878;
    for (var c = 0; c < r.length; c += 16) {
        var s = n;
        var m = a;
        var i = t;
        var o = d;
        n = md5_ff(n, a, t, d, r[c + 0], 7, -680876936);
        d = md5_ff(d, n, a, t, r[c + 1], 12, -389564586);
        t = md5_ff(t, d, n, a, r[c + 2], 17, 606105819);
        a = md5_ff(a, t, d, n, r[c + 3], 22, -1044525330);
        n = md5_ff(n, a, t, d, r[c + 4], 7, -176418897);
        d = md5_ff(d, n, a, t, r[c + 5], 12, 1200080426);
        t = md5_ff(t, d, n, a, r[c + 6], 17, -1473231341);
        a = md5_ff(a, t, d, n, r[c + 7], 22, -45705983);
        n = md5_ff(n, a, t, d, r[c + 8], 7, 1770035416);
        d = md5_ff(d, n, a, t, r[c + 9], 12, -1958414417);
        t = md5_ff(t, d, n, a, r[c + 10], 17, -42063);
        a = md5_ff(a, t, d, n, r[c + 11], 22, -1990404162);
        n = md5_ff(n, a, t, d, r[c + 12], 7, 1804603682);
        d = md5_ff(d, n, a, t, r[c + 13], 12, -40341101);
        t = md5_ff(t, d, n, a, r[c + 14], 17, -1502002290);
        a = md5_ff(a, t, d, n, r[c + 15], 22, 1236535329);
        n = md5_gg(n, a, t, d, r[c + 1], 5, -165796510);
        d = md5_gg(d, n, a, t, r[c + 6], 9, -1069501632);
        t = md5_gg(t, d, n, a, r[c + 11], 14, 643717713);
        a = md5_gg(a, t, d, n, r[c + 0], 20, -373897302);
        n = md5_gg(n, a, t, d, r[c + 5], 5, -701558691);
        d = md5_gg(d, n, a, t, r[c + 10], 9, 38016083);
        t = md5_gg(t, d, n, a, r[c + 15], 14, -660478335);
        a = md5_gg(a, t, d, n, r[c + 4], 20, -405537848);
        n = md5_gg(n, a, t, d, r[c + 9], 5, 568446438);
        d = md5_gg(d, n, a, t, r[c + 14], 9, -1019803690);
        t = md5_gg(t, d, n, a, r[c + 3], 14, -187363961);
        a = md5_gg(a, t, d, n, r[c + 8], 20, 1163531501);
        n = md5_gg(n, a, t, d, r[c + 13], 5, -1444681467);
        d = md5_gg(d, n, a, t, r[c + 2], 9, -51403784);
        t = md5_gg(t, d, n, a, r[c + 7], 14, 1735328473);
        a = md5_gg(a, t, d, n, r[c + 12], 20, -1926607734);
        n = md5_hh(n, a, t, d, r[c + 5], 4, -378558);
        d = md5_hh(d, n, a, t, r[c + 8], 11, -2022574463);
        t = md5_hh(t, d, n, a, r[c + 11], 16, 1839030562);
        a = md5_hh(a, t, d, n, r[c + 14], 23, -35309556);
        n = md5_hh(n, a, t, d, r[c + 1], 4, -1530992060);
        d = md5_hh(d, n, a, t, r[c + 4], 11, 1272893353);
        t = md5_hh(t, d, n, a, r[c + 7], 16, -155497632);
        a = md5_hh(a, t, d, n, r[c + 10], 23, -1094730640);
        n = md5_hh(n, a, t, d, r[c + 13], 4, 681279174);
        d = md5_hh(d, n, a, t, r[c + 0], 11, -358537222);
        t = md5_hh(t, d, n, a, r[c + 3], 16, -722521979);
        a = md5_hh(a, t, d, n, r[c + 6], 23, 76029189);
        n = md5_hh(n, a, t, d, r[c + 9], 4, -640364487);
        d = md5_hh(d, n, a, t, r[c + 12], 11, -421815835);
        t = md5_hh(t, d, n, a, r[c + 15], 16, 530742520);
        a = md5_hh(a, t, d, n, r[c + 2], 23, -995338651);
        n = md5_ii(n, a, t, d, r[c + 0], 6, -198630844);
        d = md5_ii(d, n, a, t, r[c + 7], 10, 1126891415);
        t = md5_ii(t, d, n, a, r[c + 14], 15, -1416354905);
        a = md5_ii(a, t, d, n, r[c + 5], 21, -57434055);
        n = md5_ii(n, a, t, d, r[c + 12], 6, 1700485571);
        d = md5_ii(d, n, a, t, r[c + 3], 10, -1894986606);
        t = md5_ii(t, d, n, a, r[c + 10], 15, -1051523);
        a = md5_ii(a, t, d, n, r[c + 1], 21, -2054922799);
        n = md5_ii(n, a, t, d, r[c + 8], 6, 1873313359);
        d = md5_ii(d, n, a, t, r[c + 15], 10, -30611744);
        t = md5_ii(t, d, n, a, r[c + 6], 15, -1560198380);
        a = md5_ii(a, t, d, n, r[c + 13], 21, 1309151649);
        n = md5_ii(n, a, t, d, r[c + 4], 6, -145523070);
        d = md5_ii(d, n, a, t, r[c + 11], 10, -1120210379);
        t = md5_ii(t, d, n, a, r[c + 2], 15, 718787259);
        a = md5_ii(a, t, d, n, r[c + 9], 21, -343485551);
        n = safe_add(n, s);
        a = safe_add(a, m);
        t = safe_add(t, i);
        d = safe_add(d, o)
    }
    return Array(n, a, t, d)
}
function md5_cmn(r, e, n, a, t, d) {
    return safe_add(bit_rol(safe_add(safe_add(e, r), safe_add(a, d)), t), n)
}
function md5_ff(r, e, n, a, t, d, c) {
    return md5_cmn(e & n | ~e & a, r, e, t, d, c)
}
function md5_gg(r, e, n, a, t, d, c) {
    return md5_cmn(e & a | n & ~a, r, e, t, d, c)
}
function md5_hh(r, e, n, a, t, d, c) {
    return md5_cmn(e ^ n ^ a, r, e, t, d, c)
}
function md5_ii(r, e, n, a, t, d, c) {
    return md5_cmn(n ^ (e | ~a), r, e, t, d, c)
}
function core_hmac_md5(r, e) {
    var n = str2binl(r);
    if (n.length > 16)
        n = core_md5(n, r.length * chrsz);
    var a = Array(16)
      , t = Array(16);
    for (var d = 0; d < 16; d++) {
        a[d] = n[d] ^ 909522486;
        t[d] = n[d] ^ 1549556828
    }
    var c = core_md5(a.concat(str2binl(e)), 512 + e.length * chrsz);
    return core_md5(t.concat(c), 512 + 128)
}
var ivkey = "CB3ECYYPT7C95561";
function safe_add(r, e) {
    var n = (r & 65535) + (e & 65535);
    var a = (r >> 16) + (e >> 16) + (n >> 16);
    return a << 16 | n & 65535
}
function bit_rol(r, e) {
    return r << e | r >>> 32 - e
}
function str2binl(r) {
    var e = Array();
    var n = (1 << chrsz) - 1;
    for (var a = 0; a < r.length * chrsz; a += chrsz)
        e[a >> 5] |= (r.charCodeAt(a / chrsz) & n) << a % 32;
    return e
}
function binl2hex(r) {
    var e = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
    var n = "";
    for (var a = 0; a < r.length * 4; a++) {
        n += e.charAt(r[a >> 2] >> a % 4 * 8 + 4 & 15) + e.charAt(r[a >> 2] >> a % 4 * 8 & 15)
    }
    return n
}
function binl2b64(r) {
    var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var n = "";
    for (var a = 0; a < r.length * 4; a += 3) {
        var t = (r[a >> 2] >> 8 * (a % 4) & 255) << 16 | (r[a + 1 >> 2] >> 8 * ((a + 1) % 4) & 255) << 8 | r[a + 2 >> 2] >> 8 * ((a + 2) % 4) & 255;
        for (var d = 0; d < 4; d++) {
            if (a * 8 + d * 6 > r.length * 32)
                n += b64pad;
            else
                n += e.charAt(t >> 6 * (3 - d) & 63)
        }
    }
    return n
}
function ajaxPost(r) {
    var e = r.encType;
    var n = r.url;
    var a = stringIsBlank(r.datatype) ? "json" : r.datatype;
    var t = stringIsBlank(r.type) ? "post" : r.type;
    var d = stringIsBlank(r.data) ? "" : r.data;
    var c = stringIsBlank(r.error) ? errorCommonFunction : r.error;
    var s = stringIsBlank(r.success) ? errorCommonFunction : r.success;
    async = r.async != false ? true : false;
    if ("1" == e) {
        var m = changeTypeABC(d);
        var i = hex_md5(m);
        var o = ePraser(m, n);
        $.ajax({
            url: n,
            type: t,
            datatype: a,
            data: {
                url: n,
                enurl: n,
                strmd: i,
                enstr: o
            },
            async: async,
            success: function(r) {
                s(r)
            },
            error: function(r) {
                c(r)
            }
        })
    } else {
        $.ajax({
            url: n,
            type: t,
            datatype: a,
            data: d,
            async: async,
            success: function(r) {
                s(r)
            },
            error: function(r) {
                c(r)
            }
        })
    }
}
function ajaxPost2(r) {
    var e = r.url;
    var n = stringIsBlank(r.error) ? errorCommonFunction : r.error;
    var a = stringIsBlank(r.success) ? errorCommonFunction : r.success;
    var t = stringIsBlank(r.datatype) ? "json" : r.datatype;
    var d = stringIsBlank(r.type) ? "post" : r.type;
    var c = stringIsBlank(r.data) ? "" : r.data;
    var s = changeTypeABC(c);
    var m = hex_md5(s);
    var i = ePraser(s, e);
    async = r.async != false ? true : false;
    $.ajax({
        url: e,
        type: d,
        datatype: t,
        data: {
            url: e,
            enurl: e,
            strmd: m,
            enstr: i
        },
        async: async,
        success: function(r) {
            a(r)
        },
        error: function(r) {
            n(r)
        }
    })
}
function errorCommonFunction() {
    showMsg("系统异常请重新再试。")
}
function changeTypeABC(r) {
    var e = new Date;
    var n = "datetime=" + e.getTime() + "&";
    for (var a in r) {
        var t = r[a] + "";
        n = n + a.replace(/^\s\s*/, "").replace(/\s\s*$/, "") + "=" + t.replace(/^\s\s*/, "").replace(/\s\s*$/, "") + "" + "&"
    }
    return encodeURIComponent(n)
}
function ePraser(r, e) {
    var n = genPUrl(e);
    var a = CryptoJS.enc.Utf8.parse(n);
    var t = CryptoJS.enc.Utf8.parse(ivkey);
    var d = CryptoJS.AES.encrypt(r, a, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    d = d.ciphertext.toString();
    var c = CryptoJS.enc.Hex.parse(d).toString();
    return c + ""
}
function ePraser2(r, e) {
    var n = CryptoJS.enc.Utf8.parse(e);
    var a = CryptoJS.enc.Utf8.parse(ivkey);
    var t = CryptoJS.AES.encrypt(r, n, {
        iv: a,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    t = t.ciphertext.toString();
    var d = CryptoJS.enc.Hex.parse(t).toString();
    return d + ""
}
function genPUrl(r) {
    var e = CryptoJS.enc.Utf8.parse(ivkey);
    var n = CryptoJS.AES.encrypt(r, e, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    n = n.ciphertext.toString();
    var a = CryptoJS.enc.Hex.parse(n);
    a = a + "";
    if (a == null || a == "") {
        return "qdzg001002003006"
    } else {
        var t = a.substr(0, 16);
        return t
    }
}
function genParam(r, e) {
    var n = r.url;
    var a = changeTypeABC(r);
    var t = hex_md5(a);
    var d = ePraser(a, n);
    var r = {
        url: r.url,
        enurl: r.url,
        strmd: t,
        enstr: d,
        pwd: e
    };
    return r
}
function genParam2(r, e) {
    var n = new Date;
    var a = "datetime=" + n.getTime() + "&" + r;
    var t = encodeURIComponent(a);
    var d = hex_md5(t);
    var c = ePraser(t, e);
    var s = {
        url: e,
        enurl: e,
        strmd: d,
        enstr: c
    };
    return s
}
function getParams(r) {
    var e = new Date;
    var r = "datetime=" + e.getTime() + "&" + r;
    var n = ePraser2(r, "CIBECYYPT7C95561");
    return n
}
function stringIsBlank(r) {
    if (typeof r == "undefined" || r == null || r == "") {
        return true
    }
    return false
}
function stringIsNotBlank(r) {
    return !stringIsBlank(r)
}

// var pk = "E596FAFE186796CF5C5042F35DD3B60B6C3888C2A08E74CB94383B160520804AE9F9AD96022AC3522B993A570C8D15FCA0615CC32AD544351E1149701ABD3BC8DEDEB09F1CB2C37CAA96364A1E62E150C436AD734EE111940E6711550C63DDAC83BE77A9A3F81B64AE093BA7F3434A93299B902884A6BD5CD35EA81D63FED4BD";
var pk = 'E596FAFE186796CF5C5042F35DD3B60B6C3888C2A08E74CB94383B160520804AE9F9AD96022AC3522B993A570C8D15FCA0615CC32AD544351E1149701ABD3BC8DEDEB09F1CB2C37CAA96364A1E62E150C436AD734EE111940E6711550C63DDAC83BE77A9A3F81B64AE093BA7F3434A93299B902884A6BD5CD35EA81D63FED4BD';
bpe = 0;
mask = 0;
radix = mask + 1;
digitsStr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_=!@#$%^&*()[]{}|;:,.<>/?`~ \\'\"+-";
for (bpe = 0; 1 << bpe + 1 > 1 << bpe; bpe++)
    ;
bpe >>= 1;
mask = (1 << bpe) - 1;
radix = mask + 1;
one = int2bigInt(1, 1, 1);
t = new Array(0);
ss = t;
s0 = t;
s1 = t;
s2 = t;
s3 = t;
s4 = t;
s5 = t;
s6 = t;
s7 = t;
T = t;
sa = t;
mr_x1 = t;
mr_r = t;
mr_a = t;
eg_v = t;
eg_u = t;
eg_A = t;
eg_B = t;
eg_C = t;
eg_D = t;
md_q1 = t;
md_q2 = t;
md_q3 = t;
md_r = t;
md_r1 = t;
md_r2 = t;
md_tt = t;
primes = t;
pows = t;
s_i = t;
s_i2 = t;
s_R = t;
s_rm = t;
s_q = t;
s_n1 = t;
s_a = t;
s_r2 = t;
s_n = t;
s_b = t;
s_d = t;
s_x1 = t;
s_x2 = t,
s_aa = t;
rpprb = t;
function findPrimes(n) {
    var i, s, p, ans;
    s = new Array(n);
    for (i = 0; i < n; i++)
        s[i] = 0;
    s[0] = 2;
    p = 0;
    for (; s[p] < n; ) {
        for (i = s[p] * s[p]; i < n; i += s[p])
            s[i] = 1;
        p++;
        s[p] = s[p - 1] + 1;
        for (; s[p] < n && s[s[p]]; s[p]++)
            ;
    }
    ans = new Array(p);
    for (i = 0; i < p; i++)
        ans[i] = s[i];
    return ans
}
function millerRabinInt(x, b) {
    if (mr_x1.length != x.length) {
        mr_x1 = dup(x);
        mr_r = dup(x);
        mr_a = dup(x)
    }
    copyInt_(mr_a, b);
    return millerRabin(x, mr_a)
}
function millerRabin(x, b) {
    var i, j, k, s;
    if (mr_x1.length != x.length) {
        mr_x1 = dup(x);
        mr_r = dup(x);
        mr_a = dup(x)
    }
    copy_(mr_a, b);
    copy_(mr_r, x);
    copy_(mr_x1, x);
    addInt_(mr_r, -1);
    addInt_(mr_x1, -1);
    k = 0;
    for (i = 0; i < mr_r.length; i++)
        for (j = 1; j < mask; j <<= 1)
            if (x[i] & j) {
                s = k < mr_r.length + bpe ? k : 0;
                i = mr_r.length;
                j = mask
            } else
                k++;
    if (s)
        rightShift_(mr_r, s);
    powMod_(mr_a, mr_r, x);
    if (!equalsInt(mr_a, 1) && !equals(mr_a, mr_x1)) {
        j = 1;
        while (j <= s - 1 && !equals(mr_a, mr_x1)) {
            squareMod_(mr_a, x);
            if (equalsInt(mr_a, 1))
                return 0;
            j++
        }
        if (!equals(mr_a, mr_x1))
            return 0
    }
    return 1
}
function bitSize(x) {
    var j, z, w;
    for (j = x.length - 1; x[j] == 0 && j > 0; j--)
        ;
    for (z = 0,
    w = x[j]; w; w >>= 1,
    z++)
        ;
    z += bpe * j;
    return z
}
function expand(x, n) {
    var ans = int2bigInt(0, (x.length > n ? x.length : n) * bpe, 0);
    copy_(ans, x);
    return ans
}
function randTruePrime(k) {
    var ans = int2bigInt(0, k, 0);
    randTruePrime_(ans, k);
    return trim(ans, 1)
}
function randProbPrime(k) {
    if (k >= 600)
        return randProbPrimeRounds(k, 2);
    if (k >= 550)
        return randProbPrimeRounds(k, 4);
    if (k >= 500)
        return randProbPrimeRounds(k, 5);
    if (k >= 400)
        return randProbPrimeRounds(k, 6);
    if (k >= 350)
        return randProbPrimeRounds(k, 7);
    if (k >= 300)
        return randProbPrimeRounds(k, 9);
    if (k >= 250)
        return randProbPrimeRounds(k, 12);
    if (k >= 200)
        return randProbPrimeRounds(k, 15);
    if (k >= 150)
        return randProbPrimeRounds(k, 18);
    if (k >= 100)
        return randProbPrimeRounds(k, 27);
    return randProbPrimeRounds(k, 40)
}
function randProbPrimeRounds(k, n) {
    var ans, i, divisible, B;
    B = 3E4;
    ans = int2bigInt(0, k, 0);
    if (primes.length == 0)
        primes = findPrimes(3E4);
    if (rpprb.length != ans.length)
        rpprb = dup(ans);
    for (; ; ) {
        randBigInt_(ans, k, 0);
        ans[0] |= 1;
        divisible = 0;
        for (i = 0; i < primes.length && primes[i] <= B; i++)
            if (modInt(ans, primes[i]) == 0 && !equalsInt(ans, primes[i])) {
                divisible = 1;
                break
            }
        for (i = 0; i < n && !divisible; i++) {
            randBigInt_(rpprb, k, 0);
            while (!greater(ans, rpprb))
                randBigInt_(rpprb, k, 0);
            if (!millerRabin(ans, rpprb))
                divisible = 1
        }
        if (!divisible)
            return ans
    }
}
function mod(x, n) {
    var ans = dup(x);
    mod_(ans, n);
    return trim(ans, 1)
}
function addInt(x, n) {
    var ans = expand(x, x.length + 1);
    addInt_(ans, n);
    return trim(ans, 1)
}
function mult(x, y) {
    var ans = expand(x, x.length + y.length);
    mult_(ans, y);
    return trim(ans, 1)
}
function powMod(x, y, n) {
    var ans = expand(x, n.length);
    powMod_(ans, trim(y, 2), trim(n, 2), 0);
    return trim(ans, 1)
}
function sub(x, y) {
    var ans = expand(x, x.length > y.length ? x.length + 1 : y.length + 1);
    sub_(ans, y);
    return trim(ans, 1)
}
function add(x, y) {
    var ans = expand(x, x.length > y.length ? x.length + 1 : y.length + 1);
    add_(ans, y);
    return trim(ans, 1)
}
function inverseMod(x, n) {
    var ans = expand(x, n.length);
    var s;
    s = inverseMod_(ans, n);
    return s ? trim(ans, 1) : null
}
function multMod(x, y, n) {
    var ans = expand(x, n.length);
    multMod_(ans, y, n);
    return trim(ans, 1)
}
function randTruePrime_(ans, k) {
    var c, m, pm, dd, j, r, B, divisible, z, zz, recSize;
    if (primes.length == 0)
        primes = findPrimes(3E4);
    if (pows.length == 0) {
        pows = new Array(512);
        for (j = 0; j < 512; j++)
            pows[j] = Math.pow(2, j / 511 - 1)
    }
    c = 0.1;
    m = 20;
    recLimit = 20;
    if (s_i2.length != ans.length) {
        s_i2 = dup(ans);
        s_R = dup(ans);
        s_n1 = dup(ans);
        s_r2 = dup(ans);
        s_d = dup(ans);
        s_x1 = dup(ans);
        s_x2 = dup(ans);
        s_b = dup(ans);
        s_n = dup(ans);
        s_i = dup(ans);
        s_rm = dup(ans);
        s_q = dup(ans);
        s_a = dup(ans);
        s_aa = dup(ans)
    }
    if (k <= recLimit) {
        pm = (1 << (k + 2 >> 1)) - 1;
        copyInt_(ans, 0);
        for (dd = 1; dd; ) {
            dd = 0;
            ans[0] = 1 | 1 << k - 1 | Math.floor(Math.random() * (1 << k));
            for (j = 1; j < primes.length && (primes[j] & pm) == primes[j]; j++)
                if (0 == ans[0] % primes[j]) {
                    dd = 1;
                    break
                }
        }
        carry_(ans);
        return
    }
    B = c * k * k;
    if (k > 2 * m)
        for (r = 1; k - k * r <= m; )
            r = pows[Math.floor(Math.random() * 512)];
    else
        r = 0.5;
    recSize = Math.floor(r * k) + 1;
    randTruePrime_(s_q, recSize);
    copyInt_(s_i2, 0);
    s_i2[Math.floor((k - 2) / bpe)] |= 1 << (k - 2) % bpe;
    divide_(s_i2, s_q, s_i, s_rm);
    z = bitSize(s_i);
    for (; ; ) {
        for (; ; ) {
            randBigInt_(s_R, z, 0);
            if (greater(s_i, s_R))
                break
        }
        addInt_(s_R, 1);
        add_(s_R, s_i);
        copy_(s_n, s_q);
        mult_(s_n, s_R);
        multInt_(s_n, 2);
        addInt_(s_n, 1);
        copy_(s_r2, s_R);
        multInt_(s_r2, 2);
        for (divisible = 0,
        j = 0; j < primes.length && primes[j] < B; j++)
            if (modInt(s_n, primes[j]) == 0 && !equalsInt(s_n, primes[j])) {
                divisible = 1;
                break
            }
        if (!divisible)
            if (!millerRabinInt(s_n, 2))
                divisible = 1;
        if (!divisible) {
            addInt_(s_n, -3);
            for (j = s_n.length - 1; s_n[j] == 0 && j > 0; j--)
                ;
            for (zz = 0,
            w = s_n[j]; w; w >>= 1,
            zz++)
                ;
            zz += bpe * j;
            for (; ; ) {
                randBigInt_(s_a, zz, 0);
                if (greater(s_n, s_a))
                    break
            }
            addInt_(s_n, 3);
            addInt_(s_a, 2);
            copy_(s_b, s_a);
            copy_(s_n1, s_n);
            addInt_(s_n1, -1);
            powMod_(s_b, s_n1, s_n);
            addInt_(s_b, -1);
            if (isZero(s_b)) {
                copy_(s_b, s_a);
                powMod_(s_b, s_r2, s_n);
                addInt_(s_b, -1);
                copy_(s_aa, s_n);
                copy_(s_d, s_b);
                GCD_(s_d, s_n);
                if (equalsInt(s_d, 1)) {
                    copy_(ans, s_aa);
                    return
                }
            }
        }
    }
}
function randBigInt(n, s) {
    var a, b;
    a = Math.floor((n - 1) / bpe) + 2;
    b = int2bigInt(0, 0, a);
    randBigInt_(b, n, s);
    return b
}
function randBigInt_(b, n, s) {
    var i, a;
    for (i = 0; i < b.length; i++)
        b[i] = 0;
    a = Math.floor((n - 1) / bpe) + 1;
    for (i = 0; i < a; i++)
        b[i] = Math.floor(Math.random() * (1 << bpe - 1));
    b[a - 1] &= (2 << (n - 1) % bpe) - 1;
    if (s == 1)
        b[a - 1] |= 1 << (n - 1) % bpe
}
function GCD(x, y) {
    var xc, yc;
    xc = dup(x);
    yc = dup(y);
    GCD_(xc, yc);
    return xc
}
function GCD_(x, y) {
    var i, xp, yp, A, B, C, D, q, sing;
    if (T.length != x.length)
        T = dup(x);
    sing = 1;
    while (sing) {
        sing = 0;
        for (i = 1; i < y.length; i++)
            if (y[i]) {
                sing = 1;
                break
            }
        if (!sing)
            break;
        for (i = x.length; !x[i] && i >= 0; i--)
            ;
        xp = x[i];
        yp = y[i];
        A = 1;
        B = 0;
        C = 0;
        D = 1;
        while (yp + C && yp + D) {
            q = Math.floor((xp + A) / (yp + C));
            qp = Math.floor((xp + B) / (yp + D));
            if (q != qp)
                break;
            t = A - q * C;
            A = C;
            C = t;
            t = B - q * D;
            B = D;
            D = t;
            t = xp - q * yp;
            xp = yp;
            yp = t
        }
        if (B) {
            copy_(T, x);
            linComb_(x, y, A, B);
            linComb_(y, T, D, C)
        } else {
            mod_(x, y);
            copy_(T, x);
            copy_(x, y);
            copy_(y, T)
        }
    }
    if (y[0] == 0)
        return;
    t = modInt(x, y[0]);
    copyInt_(x, y[0]);
    y[0] = t;
    while (y[0]) {
        x[0] %= y[0];
        t = x[0];
        x[0] = y[0];
        y[0] = t
    }
}
function inverseMod_(x, n) {
    var k = 1 + 2 * Math.max(x.length, n.length);
    if (!(x[0] & 1) && !(n[0] & 1)) {
        copyInt_(x, 0);
        return 0
    }
    if (eg_u.length != k) {
        eg_u = new Array(k);
        eg_v = new Array(k);
        eg_A = new Array(k);
        eg_B = new Array(k);
        eg_C = new Array(k);
        eg_D = new Array(k)
    }
    copy_(eg_u, x);
    copy_(eg_v, n);
    copyInt_(eg_A, 1);
    copyInt_(eg_B, 0);
    copyInt_(eg_C, 0);
    copyInt_(eg_D, 1);
    for (; ; ) {
        while (!(eg_u[0] & 1)) {
            halve_(eg_u);
            if (!(eg_A[0] & 1) && !(eg_B[0] & 1)) {
                halve_(eg_A);
                halve_(eg_B)
            } else {
                add_(eg_A, n);
                halve_(eg_A);
                sub_(eg_B, x);
                halve_(eg_B)
            }
        }
        while (!(eg_v[0] & 1)) {
            halve_(eg_v);
            if (!(eg_C[0] & 1) && !(eg_D[0] & 1)) {
                halve_(eg_C);
                halve_(eg_D)
            } else {
                add_(eg_C, n);
                halve_(eg_C);
                sub_(eg_D, x);
                halve_(eg_D)
            }
        }
        if (!greater(eg_v, eg_u)) {
            sub_(eg_u, eg_v);
            sub_(eg_A, eg_C);
            sub_(eg_B, eg_D)
        } else {
            sub_(eg_v, eg_u);
            sub_(eg_C, eg_A);
            sub_(eg_D, eg_B)
        }
        if (equalsInt(eg_u, 0)) {
            if (negative(eg_C))
                add_(eg_C, n);
            copy_(x, eg_C);
            if (!equalsInt(eg_v, 1)) {
                copyInt_(x, 0);
                return 0
            }
            return 1
        }
    }
}
function inverseModInt(x, n) {
    var a = 1, b = 0, t;
    for (; ; ) {
        if (x == 1)
            return a;
        if (x == 0)
            return 0;
        b -= a * Math.floor(n / x);
        n %= x;
        if (n == 1)
            return b;
        if (n == 0)
            return 0;
        a -= b * Math.floor(x / n);
        x %= n
    }
}
function inverseModInt_(x, n) {
    return inverseModInt(x, n)
}
function eGCD_(x, y, v, a, b) {
    var g = 0;
    var k = Math.max(x.length, y.length);
    if (eg_u.length != k) {
        eg_u = new Array(k);
        eg_A = new Array(k);
        eg_B = new Array(k);
        eg_C = new Array(k);
        eg_D = new Array(k)
    }
    while (!(x[0] & 1) && !(y[0] & 1)) {
        halve_(x);
        halve_(y);
        g++
    }
    copy_(eg_u, x);
    copy_(v, y);
    copyInt_(eg_A, 1);
    copyInt_(eg_B, 0);
    copyInt_(eg_C, 0);
    copyInt_(eg_D, 1);
    for (; ; ) {
        while (!(eg_u[0] & 1)) {
            halve_(eg_u);
            if (!(eg_A[0] & 1) && !(eg_B[0] & 1)) {
                halve_(eg_A);
                halve_(eg_B)
            } else {
                add_(eg_A, y);
                halve_(eg_A);
                sub_(eg_B, x);
                halve_(eg_B)
            }
        }
        while (!(v[0] & 1)) {
            halve_(v);
            if (!(eg_C[0] & 1) && !(eg_D[0] & 1)) {
                halve_(eg_C);
                halve_(eg_D)
            } else {
                add_(eg_C, y);
                halve_(eg_C);
                sub_(eg_D, x);
                halve_(eg_D)
            }
        }
        if (!greater(v, eg_u)) {
            sub_(eg_u, v);
            sub_(eg_A, eg_C);
            sub_(eg_B, eg_D)
        } else {
            sub_(v, eg_u);
            sub_(eg_C, eg_A);
            sub_(eg_D, eg_B)
        }
        if (equalsInt(eg_u, 0)) {
            if (negative(eg_C)) {
                add_(eg_C, y);
                sub_(eg_D, x)
            }
            multInt_(eg_D, -1);
            copy_(a, eg_C);
            copy_(b, eg_D);
            leftShift_(v, g);
            return
        }
    }
}
function negative(x) {
    return x[x.length - 1] >> bpe - 1 & 1
}
function greaterShift(x, y, shift) {
    var i, kx = x.length, ky = y.length;
    k = kx + shift < ky ? kx + shift : ky;
    for (i = ky - 1 - shift; i < kx && i >= 0; i++)
        if (x[i] > 0)
            return 1;
    for (i = kx - 1 + shift; i < ky; i++)
        if (y[i] > 0)
            return 0;
    for (i = k - 1; i >= shift; i--)
        if (x[i - shift] > y[i])
            return 1;
        else if (x[i - shift] < y[i])
            return 0;
    return 0
}
function greater(x, y) {
    var i;
    var k = x.length < y.length ? x.length : y.length;
    for (i = x.length; i < y.length; i++)
        if (y[i])
            return 0;
    for (i = y.length; i < x.length; i++)
        if (x[i])
            return 1;
    for (i = k - 1; i >= 0; i--)
        if (x[i] > y[i])
            return 1;
        else if (x[i] < y[i])
            return 0;
    return 0
}
function divide_(x, y, q, r) {
    var kx, ky;
    var i, j, y1, y2, c, a, b;
    copy_(r, x);
    for (ky = y.length; y[ky - 1] == 0; ky--)
        ;
    b = y[ky - 1];
    for (a = 0; b; a++)
        b >>= 1;
    a = bpe - a;
    leftShift_(y, a);
    leftShift_(r, a);
    for (kx = r.length; r[kx - 1] == 0 && kx > ky; kx--)
        ;
    copyInt_(q, 0);
    while (!greaterShift(y, r, kx - ky)) {
        subShift_(r, y, kx - ky);
        q[kx - ky]++
    }
    for (i = kx - 1; i >= ky; i--) {
        if (r[i] == y[ky - 1])
            q[i - ky] = mask;
        else
            q[i - ky] = Math.floor((r[i] * radix + r[i - 1]) / y[ky - 1]);
        for (; ; ) {
            y2 = (ky > 1 ? y[ky - 2] : 0) * q[i - ky];
            c = y2 >> bpe;
            y2 = y2 & mask;
            y1 = c + q[i - ky] * y[ky - 1];
            c = y1 >> bpe;
            y1 = y1 & mask;
            if (c == r[i] ? y1 == r[i - 1] ? y2 > (i > 1 ? r[i - 2] : 0) : y1 > r[i - 1] : c > r[i])
                q[i - ky]--;
            else
                break
        }
        linCombShift_(r, y, -q[i - ky], i - ky);
        if (negative(r)) {
            addShift_(r, y, i - ky);
            q[i - ky]--
        }
    }
    rightShift_(y, a);
    rightShift_(r, a)
}
function carry_(x) {
    var i, k, c, b;
    k = x.length;
    c = 0;
    for (i = 0; i < k; i++) {
        c += x[i];
        b = 0;
        if (c < 0) {
            b = -(c >> bpe);
            c += b * radix
        }
        x[i] = c & mask;
        c = (c >> bpe) - b
    }
}
function modInt(x, n) {
    var i, c = 0;
    for (i = x.length - 1; i >= 0; i--)
        c = (c * radix + x[i]) % n;
    return c
}
function int2bigInt(t, bits, minSize) {
    var i, k;
    k = Math.ceil(bits / bpe) + 1;
    k = minSize > k ? minSize : k;
    buff = new Array(k);
    copyInt_(buff, t);
    return buff
}
function str2bigInt(s, base, minSize) {
    var d, i, j, x, y, kk;
    var k = s.length;
    if (base == -1) {
        x = new Array(0);
        for (; ; ) {
            y = new Array(x.length + 1);
            for (i = 0; i < x.length; i++)
                y[i + 1] = x[i];
            y[0] = parseInt(s, 10);
            x = y;
            d = s.indexOf(",", 0);
            if (d < 1)
                break;
            s = s.substring(d + 1);
            if (s.length == 0)
                break
        }
        if (x.length < minSize) {
            y = new Array(minSize);
            copy_(y, x);
            return y
        }
        return x
    }
    x = int2bigInt(0, base * k, 0);
    for (i = 0; i < k; i++) {
        d = digitsStr.indexOf(s.substring(i, i + 1), 0);
        if (base <= 36 && d >= 36)
            d -= 26;
        if (d >= base || d < 0)
            break;
        multInt_(x, base);
        addInt_(x, d)
    }
    for (k = x.length; k > 0 && !x[k - 1]; k--)
        ;
    k = minSize > k + 1 ? minSize : k + 1;
    y = new Array(k);
    kk = k < x.length ? k : x.length;
    for (i = 0; i < kk; i++)
        y[i] = x[i];
    for (; i < k; i++)
        y[i] = 0;
    return y
}
function equalsInt(x, y) {
    var i;
    if (x[0] != y)
        return 0;
    for (i = 1; i < x.length; i++)
        if (x[i])
            return 0;
    return 1
}
function equals(x, y) {
    var i;
    var k = x.length < y.length ? x.length : y.length;
    for (i = 0; i < k; i++)
        if (x[i] != y[i])
            return 0;
    if (x.length > y.length)
        for (; i < x.length; i++) {
            if (x[i])
                return 0
        }
    else
        for (; i < y.length; i++)
            if (y[i])
                return 0;
    return 1
}
function isZero(x) {
    var i;
    for (i = 0; i < x.length; i++)
        if (x[i])
            return 0;
    return 1
}
function bigInt2str(x, base) {
    var i, t, s = "";
    if (s6.length != x.length)
        s6 = dup(x);
    else
        copy_(s6, x);
    if (base == -1) {
        for (i = x.length - 1; i > 0; i--)
            s += x[i] + ",";
        s += x[0]
    } else
        while (!isZero(s6)) {
            t = divInt_(s6, base);
            s = digitsStr.substring(t, t + 1) + s
        }
    if (s.length == 0)
        s = "0";
    return s
}
function dup(x) {
    var i;
    buff = new Array(x.length);
    copy_(buff, x);
    return buff
}
function copy_(x, y) {
    var i;
    var k = x.length < y.length ? x.length : y.length;
    for (i = 0; i < k; i++)
        x[i] = y[i];
    for (i = k; i < x.length; i++)
        x[i] = 0
}
function copyInt_(x, n) {
    var i, c;
    for (c = n,
    i = 0; i < x.length; i++) {
        x[i] = c & mask;
        c >>= bpe
    }
}
function addInt_(x, n) {
    var i, k, c, b;
    x[0] += n;
    k = x.length;
    c = 0;
    for (i = 0; i < k; i++) {
        c += x[i];
        b = 0;
        if (c < 0) {
            b = -(c >> bpe);
            c += b * radix
        }
        x[i] = c & mask;
        c = (c >> bpe) - b;
        if (!c)
            return
    }
}
function rightShift_(x, n) {
    var i;
    var k = Math.floor(n / bpe);
    if (k) {
        for (i = 0; i < x.length - k; i++)
            x[i] = x[i + k];
        for (; i < x.length; i++)
            x[i] = 0;
        n %= bpe
    }
    for (i = 0; i < x.length - 1; i++)
        x[i] = mask & (x[i + 1] << bpe - n | x[i] >> n);
    x[i] >>= n
}
function halve_(x) {
    var i;
    for (i = 0; i < x.length - 1; i++)
        x[i] = mask & (x[i + 1] << bpe - 1 | x[i] >> 1);
    x[i] = x[i] >> 1 | x[i] & radix >> 1
}
function leftShift_(x, n) {
    var i;
    var k = Math.floor(n / bpe);
    if (k) {
        for (i = x.length; i >= k; i--)
            x[i] = x[i - k];
        for (; i >= 0; i--)
            x[i] = 0;
        n %= bpe
    }
    if (!n)
        return;
    for (i = x.length - 1; i > 0; i--)
        x[i] = mask & (x[i] << n | x[i - 1] >> bpe - n);
    x[i] = mask & x[i] << n
}
function multInt_(x, n) {
    var i, k, c, b;
    if (!n)
        return;
    k = x.length;
    c = 0;
    for (i = 0; i < k; i++) {
        c += x[i] * n;
        b = 0;
        if (c < 0) {
            b = -(c >> bpe);
            c += b * radix
        }
        x[i] = c & mask;
        c = (c >> bpe) - b
    }
}
function divInt_(x, n) {
    var i, r = 0, s;
    for (i = x.length - 1; i >= 0; i--) {
        s = r * radix + x[i];
        x[i] = Math.floor(s / n);
        r = s % n
    }
    return r
}
function linComb_(x, y, a, b) {
    var i, c, k, kk;
    k = x.length < y.length ? x.length : y.length;
    kk = x.length;
    for (c = 0,
    i = 0; i < k; i++) {
        c += a * x[i] + b * y[i];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; i < kk; i++) {
        c += a * x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function linCombShift_(x, y, b, ys) {
    var i, c, k, kk;
    k = x.length < ys + y.length ? x.length : ys + y.length;
    kk = x.length;
    for (c = 0,
    i = ys; i < k; i++) {
        c += x[i] + b * y[i - ys];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; c && i < kk; i++) {
        c += x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function addShift_(x, y, ys) {
    var i, c, k, kk;
    k = x.length < ys + y.length ? x.length : ys + y.length;
    kk = x.length;
    for (c = 0,
    i = ys; i < k; i++) {
        c += x[i] + y[i - ys];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; c && i < kk; i++) {
        c += x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function subShift_(x, y, ys) {
    var i, c, k, kk;
    k = x.length < ys + y.length ? x.length : ys + y.length;
    kk = x.length;
    for (c = 0,
    i = ys; i < k; i++) {
        c += x[i] - y[i - ys];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; c && i < kk; i++) {
        c += x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function sub_(x, y) {
    var i, c, k, kk;
    k = x.length < y.length ? x.length : y.length;
    for (c = 0,
    i = 0; i < k; i++) {
        c += x[i] - y[i];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; c && i < x.length; i++) {
        c += x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function add_(x, y) {
    var i, c, k, kk;
    k = x.length < y.length ? x.length : y.length;
    for (c = 0,
    i = 0; i < k; i++) {
        c += x[i] + y[i];
        x[i] = c & mask;
        c >>= bpe
    }
    for (i = k; c && i < x.length; i++) {
        c += x[i];
        x[i] = c & mask;
        c >>= bpe
    }
}
function mult_(x, y) {
    var i;
    if (ss.length != 2 * x.length)
        ss = new Array(2 * x.length);
    copyInt_(ss, 0);
    for (i = 0; i < y.length; i++)
        if (y[i])
            linCombShift_(ss, x, y[i], i);
    copy_(x, ss)
}
function mod_(x, n) {
    if (s4.length != x.length)
        s4 = dup(x);
    else
        copy_(s4, x);
    if (s5.length != x.length)
        s5 = dup(x);
    divide_(s4, n, s5, x)
}
function multMod_(x, y, n) {
    var i;
    if (s0.length != 2 * x.length)
        s0 = new Array(2 * x.length);
    copyInt_(s0, 0);
    for (i = 0; i < y.length; i++)
        if (y[i])
            linCombShift_(s0, x, y[i], i);
    mod_(s0, n);
    copy_(x, s0)
}
function squareMod_(x, n) {
    var i, j, d, c, kx, kn, k;
    for (kx = x.length; kx > 0 && !x[kx - 1]; kx--)
        ;
    k = kx > n.length ? 2 * kx : 2 * n.length;
    if (s0.length != k)
        s0 = new Array(k);
    copyInt_(s0, 0);
    for (i = 0; i < kx; i++) {
        c = s0[2 * i] + x[i] * x[i];
        s0[2 * i] = c & mask;
        c >>= bpe;
        for (j = i + 1; j < kx; j++) {
            c = s0[i + j] + 2 * x[i] * x[j] + c;
            s0[i + j] = c & mask;
            c >>= bpe
        }
        s0[i + kx] = c
    }
    mod_(s0, n);
    copy_(x, s0)
}
function trim(x, k) {
    var i, y;
    for (i = x.length; i > 0 && !x[i - 1]; i--)
        ;
    y = new Array(i + k);
    copy_(y, x);
    return y
}
function powMod_(x, y, n) {
    var k1, k2, kn, np;
    if (s7.length != n.length)
        s7 = dup(n);
    if ((n[0] & 1) == 0) {
        copy_(s7, x);
        copyInt_(x, 1);
        while (!equalsInt(y, 0)) {
            if (y[0] & 1)
                multMod_(x, s7, n);
            divInt_(y, 2);
            squareMod_(s7, n)
        }
        return
    }
    copyInt_(s7, 0);
    for (kn = n.length; kn > 0 && !n[kn - 1]; kn--)
        ;
    np = radix - inverseModInt(modInt(n, radix), radix);
    s7[kn] = 1;
    multMod_(x, s7, n);
    if (s3.length != x.length)
        s3 = dup(x);
    else
        copy_(s3, x);
    for (k1 = y.length - 1; k1 > 0 & !y[k1]; k1--)
        ;
    if (y[k1] == 0) {
        copyInt_(x, 1);
        return
    }
    for (k2 = 1 << bpe - 1; k2 && !(y[k1] & k2); k2 >>= 1)
        ;
    for (; ; ) {
        if (!(k2 >>= 1)) {
            k1--;
            if (k1 < 0) {
                mont_(x, one, n, np);
                return
            }
            k2 = 1 << bpe - 1
        }
        mont_(x, x, n, np);
        if (k2 & y[k1])
            mont_(x, s3, n, np)
    }
}
function mont_(x, y, n, np) {
    var i, j, c, ui, t, ks;
    var kn = n.length;
    var ky = y.length;
    if (sa.length != kn)
        sa = new Array(kn);
    copyInt_(sa, 0);
    for (; kn > 0 && n[kn - 1] == 0; kn--)
        ;
    for (; ky > 0 && y[ky - 1] == 0; ky--)
        ;
    ks = sa.length - 1;
    for (i = 0; i < kn; i++) {
        t = sa[0] + x[i] * y[0];
        ui = (t & mask) * np & mask;
        c = t + ui * n[0] >> bpe;
        t = x[i];
        j = 1;
        for (; j < ky - 4; ) {
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++
        }
        for (; j < ky; ) {
            c += sa[j] + ui * n[j] + t * y[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++
        }
        for (; j < kn - 4; ) {
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++;
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++
        }
        for (; j < kn; ) {
            c += sa[j] + ui * n[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++
        }
        for (; j < ks; ) {
            c += sa[j];
            sa[j - 1] = c & mask;
            c >>= bpe;
            j++
        }
        sa[j - 1] = c & mask
    }
    if (!greater(n, sa))
        sub_(sa, n);
    copy_(x, sa)
}
function genByteValue(paramStr) {
    var bInt = parseInt(paramStr, 10) & 255;
    if (bInt > 127)
        bInt = -(bInt & 127 ^ 127) - 1;
    return bInt
}
function getBytes(str1) {
    var binStr = "";
    var charBin;
    var i, j;
    for (i = 0; i < str1.length; i++) {
        charBin = str1.charAt(i).charCodeAt().toString(2);
        for (j = charBin.length; j < 8; j++)
            charBin = "0" + charBin;
        binStr += charBin
    }
    return binStr
}
function genRandom(paramInt) {
    var rs = "";
    for (k = 0; k < paramInt; k++)
        rs = "v" + rs;
    return rs
}
var pinMaxLen = 128;
var ee;
ee = str2bigInt("65537", 10, 0);
function EncryptAPin(paramString2) {
    if (paramString2.length < 6) {
        var i = paramString2.length;
        for (j = 0; j < 6 - i; ++j)
            paramString2 = paramString2 + " "
    }
    var i = paramString2.length;
    if (i >= pinMaxLen - 2)
        return "";
    var localInteger1;
    localInteger1 = Math.floor(i / 10 + 48);
    var localInteger2;
    localInteger2 = Math.floor(i % 10 + 48);
    var str1;
    str1 = String.fromCharCode(genByteValue(localInteger1)) + "" + String.fromCharCode(genByteValue(localInteger2)) + "" + paramString2 + "" + genRandom(pinMaxLen - i - 2);
    var inx;
    inx = str2bigInt(getBytes(str1), 2, 0);
    var localBigInteger;
    localBigInteger = str2bigInt(pk, 16, 0);
    var str2;
    str2 = bigInt2str(powMod(inx, ee, localBigInteger), 16);
    for (k = str2.length; k < 256; k++)
        str2 = "0" + str2;
    return str2
}
function EncryptEPin(input, acctId) {
    var password = input + "";
    var customerID = acctId + "";
    var i = 2 + password.length + 2 + customerID.length;
    if (i >= pinMaxLen - 2)
        return "";
    var localInteger1;
    localInteger1 = Math.floor(i / 256);
    var localInteger2;
    localInteger2 = Math.floor(i % 256);
    var j = password.length;
    var localInteger3;
    localInteger3 = Math.floor(j / 10 + 48);
    var localInteger4;
    localInteger4 = Math.floor(j % 10 + 48);
    var k = customerID.length;
    var localInteger5;
    localInteger5 = Math.floor(k / 10 + 48);
    var localInteger6;
    localInteger6 = Math.floor(k % 10 + 48);
    var str1;
    str1 = String.fromCharCode(genByteValue(localInteger1)) + "" + String.fromCharCode(genByteValue(localInteger2));
    str1 += String.fromCharCode(genByteValue(localInteger3)) + "" + String.fromCharCode(genByteValue(localInteger4)) + "" + password;
    str1 += String.fromCharCode(genByteValue(localInteger5)) + "" + String.fromCharCode(genByteValue(localInteger6)) + "" + customerID + "" + genRandom(pinMaxLen - i - 2);
    var inx;
    inx = str2bigInt(getBytes(str1), 2, 0);
    var localBigInteger;
    localBigInteger = str2bigInt(pk, 16, 0);
    var str2;
    str2 = bigInt2str(powMod(inx, ee, localBigInteger), 16);
    for (k = str2.length; k < 256; k++)
        str2 = "0" + str2;
    return str2
}
function encrypt(pwds) {
    for (var i = 0; i < pwds.length; i++) {
        var pwd = document.getElementById(pwds[i] + "1");
        var hidPwd = document.getElementById(pwds[i]);
        try {
            hidPwd.value = EncryptAPin(pwd.value);
            pwd.value = ""
        } catch (e) {
            return false
        }
    }
    return true
}
function encryptEPin(pwds, acctId) {
    for (var i = 0; i < pwds.length; i++) {
        var pwd = document.getElementById(pwds[i] + "1");
        var hidPwd = document.getElementById(pwds[i]);
        try {
            hidPwd.value = EncryptEPin(pwd.value, acctId)
        } catch (e) {
            return false
        }
    }
    return true
}
function encryptEPinTwice(pwd, acctId) {
         return  EncryptEPin(pwd, "") + EncryptEPin(pwd, acctId)

};
function get_pwd(user,pwd,captch){

    var new_pwd =  encryptEPinTwice(pwd, user);
    var param = "ncid=&captchafield="+captch+"&loginType=-1&custType=&j_username="+user+"&j_password="+new_pwd+"&encodeType=&loginSim=";
    return getParams(param);
    // return new_pwd;
}

function get_pwd_no_cap(user,pwd) {
    var new_pwd =  encryptEPinTwice(pwd, user);
    var param = "ncid=&loginType=-1&custType=&j_username="+user+"&j_password="+new_pwd+"&encodeType=&loginSim=";
    return getParams(param);

}
