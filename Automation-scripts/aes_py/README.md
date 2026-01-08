# aes_py
This script will be able to encrypt and decrypt text using AES256 using password based key. -

该脚本能够使用基于密码的密钥，通过 AES256 算法对文本进行加密和解密。

## Usage
`
$ python3 main.py --text "this is a secret message" -op 0  
Enter password : 
b'8jeJABqjpdK0aVExWZars2Uzd+vBZIWQFRvdIqt5DJz3X/bSuHBnX4YW7MjYCrSg'  
$ python3 main.py --text "8jeJABqjpdK0aVExWZars2Uzd+vBZIWQFRvdIqt5DJz3X/bSuHBnX4YW7MjYCrSg" -op 1
Enter password : 
b'this is a secret message'
`