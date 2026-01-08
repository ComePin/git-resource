import time
import datetime
import simpleaudio

t = int()


def snooze(t):

    """
    该函数用于在当前设置的时间上增加指定的分钟数

    参数:
        t (int): 需要增加的分钟数

    返回:
        无返回值，直接修改全局变量 set_time 的值
    """
    global set_time  # 声明使用全局变量 set_time
    HH_MM = set_time.split(':')  # 将时间字符串按冒号分割成小时和分钟
    HH_MM[1] = str(int(HH_MM[1]) + t)  # 将分钟部分转换为整数并增加 t 分钟，再转回字符串
    set_time = ':'.join(HH_MM)  # 将修改后的小时和分钟重新组合成时间字符串


set_time = input("please enter the time in HH:MM format to set an alarm : ")
label = input("Alarm label: ")


def alarm(set_time):
    """
    闹钟函数，用于在指定时间播放闹钟声音
    参数:
        set_time (str): 设置的闹钟时间，格式为"HH:MM"
    """
    while True:
        time.sleep(1)  # 每秒检查一次时间
        # 创建音频对象，从alarm.wav文件加载
        obj = simpleaudio.WaveObject.from_wave_file("./alarm.wav")
        # 获取当前时间并格式化为"HH:MM"字符串
        current_time = datetime.datetime.now().time().strftime("%H:%M")
        # 将当前时间字符串分割并转换为整数列表
        curr_l = current_time.split(":")
        curr_l = [int(i) for i in curr_l]
        # 将设置的时间字符串分割并转换为整数列表
        set_l = set_time.split(":")
        set_l = [int(i) for i in set_l]
        # 检查当前时间是否与设置时间相等（小时和分钟）
        if curr_l[0] == set_l[0] and curr_l[1] == set_l[1]:
            print(label)  # 打印标签信息
            obj.play()  # 播放闹钟声音
            break  # 退出循环


while True:
    alarm(set_time)
    x = input("Press y if you want the alarm to snooze: ")
    if x == 'y':
        t = int(input("Snooze time: "))
        snooze(t)
        print(f"The alarm will ring again in {t} min")
    else:
        break
