import pyttsx3

# 创建语音引擎
engine = pyttsx3.init()

# 设置语速和音量
engine.setProperty('rate', 200)  # 语速
engine.setProperty('volume', 2.0)  # 音量

# 设置要转换的文本
text = "你好，欢迎使用pyttsx3库进行语音合成"

# 使用语音引擎将文本转换成语音
engine.say(text)

# 等待语音播放完毕
engine.runAndWait()
