import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2

BLOCK_SIZE = 16


def pad(s):
    """
    对输入字符串进行填充，使其长度成为BLOCK_SIZE的整数倍
    这是常用的PKCS7填充方案实现
    @params s: 需要填充的字符串
    @return 填充后的字符串，在原始字符串末尾添加特定长度的填充字节
    """
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(  # 计算需要填充的长度并添加相应字符
        BLOCK_SIZE - len(s) % BLOCK_SIZE  # 计算填充字符的ASCII值
    )


def unpad(s):
    """
    移除字符串末尾的填充字符
    该函数假设字符串是根据PKCS#7标准进行填充的
    @params s: 需要移除填充的字符串
    @return 移除填充后的字符串
    """
    # 获取字符串最后一个字符的ASCII值，这个值表示填充的长度
    padding_length = ord(s[len(s) - 1:])
    # 返回从字符串开始到去掉填充长度的部分
    return s[: -ord(s[len(s) - 1:])]


def get_private_key(password):
    """
    根据密码生成私钥，使用PBKDF2算法通过密码和固定盐值生成私钥
    @params password: 用户密码，用于生成私钥的输入
    @return key: 生成的32字节私钥
    """
    salt = b"this is a salt"  # 固定盐值，用于增加密码的安全性
    kdf = PBKDF2(password, salt, 64, 1000)  # 使用PBKDF2算法派生密钥，64是生成的密钥长度，1000是迭代次数
    key = kdf[:32]  # 取派生密钥的前32字节作为最终的私钥
    return key  # 返回生成的私钥


def encrypt(raw, password):
    """
    使用AES加密算法对原始数据进行加密
    @params raw: 需要加密的原始数据
    @params password: 加密时使用的密码
    @return 返回Base64编码的加密结果
    """
    # 根据密码生成私钥
    private_key = get_private_key(password)
    # 对原始数据进行填充，使其符合AES块大小的要求
    raw = pad(raw)
    # 生成一个初始化向量(IV)，用于加密过程
    iv = Random.new().read(AES.block_size)
    # 创建AES加密器，使用CBC模式
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    # 执行加密操作，并将IV与加密结果拼接
    cipher = iv + cipher.encrypt(raw.encode("utf-8"))
    # 将加密结果进行Base64编码并返回
    return base64.b64encode(cipher)


def decrypt(enc, password):
    """
    使用给定的密码解密数据
    @params enc: 加密后的数据(Base64编码)
    @params password: 用于解密的密码
    @return 解密后的原始数据
    """
    # 从密码生成私钥
    private_key = get_private_key(password)
    # 将Base64编码的加密数据解码为字节
    enc = base64.b64decode(enc)
    # 提取初始化向量(IV)，它位于加密数据的前16个字节
    iv = enc[:16]
    # 创建AES解密器，使用CBC模式
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    # 解密数据(跳过前16字节的IV)，并移除填充
    return unpad(cipher.decrypt(enc[16:]))


if __name__ == "__main__":
    password = input("Enter encryption password: ")
    # First let us encrypt secret message
    encrypted = encrypt("This is a secret message", password)
    print(encrypted)

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)
    print(bytes.decode(decrypted))
