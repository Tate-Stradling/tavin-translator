# What is Tavin code?
The technical definition of Tavin code is that it's a form of substitution cipher that operates by translating text to and from pairs of vowels.
What does this mean? It means that each letter and number has a corresponding pair of vowels that are used to either encrypt or decrypt.
For example, the word `testing` encrypts to `aeaaeeaeaueaoe`, and `Eoaaeueuao, Oiaoeieuia!` decrypts to `Hello, World!`.
## Tavin code chart
|a |b |c |d |e |f |g |h |i |g |k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|ai|ou|ie|ia|aa|iu|oe|eo|au|oe|ue|eu|io|ea|ao|oa|uu|ei|ee|ae|ii|ua|oi|ui|oo|yy|ya|ay|oy|yu|yi|iy|yo|ye|ey|uy|
## Looping
You can also loop over the translator multiple times, for example `dog` encrypts to `iaaooe`, and `iaaooe` can be re-encrypted to `auaiaiaoaoaa`!
You can then re-decrypt over the encrypted text until it outputs the decrypted value.
Each time you loop over the translator, the translated text will change exponentially.
## Double translating
Besides looping, you can also do something called 'double encrypting' or 'double decrypting'. Double encrypting is where you encrypt a word, move the first letter of the encrypted word to the end of the word, and decrypt it. For example, `cat` encrypts to `ieaiae`, and the first letter, `i`, is moved to the back to make `eaiaei`. When `eaiaei` is decrypted, it outputs `ndr`. While `ndr` is a seemingly random combination of letters, you can retrieve the decrypted value, `cat`, by double decrypting it. You can double decrypt `ndr` by encrypting it to `eaiaei`, moving the last letter, `i`, to the front to make `ieaiae`. You can then decrypt `ieaiae`, to get `cat`.
