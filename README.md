# 魔镜后端服务器

```
├── app.py 
├── cache   缓存一些数据
├── config.ini  配置文件
├── dataset 数据集文件夹
│   ├── haarcascade_frontalface_default.xml 人脸识别数据集
│   ├── model   保存训练好的人脸模型
│   ├── train   保存训练时候的临时图片
├── README.md   就是你现在看到的这个
└── server      app的主要代码
    ├── auth    用户认证的blueprint
    │   ├── __init__.py
    │   └── views.py 
    ├── bluetooth   蓝牙相关功能的blueprint
    │   ├── __init__.py
    │   └── views.py
    ├── controller  控制器，主要功能的实现逻辑
    │   ├── heartrate.py    获取心率
    │   ├── heart_utils 获取心率相关的文件（Python2）
    │   │   ├── base.py
    │   │   ├── constants.py
    │   │   └── get_heart_rate.py
    │   ├── humidity.py 获取湿度
    │   ├── __init__.py 
    │   ├── login.py    登录
    │   ├── news.py 获取新闻
    │   ├── pm25.py 获取pm2.5
    │   ├── register.py 注册
    │   ├── temperature.py  获取温度
    │   ├── traveladvice.py 获取出行建议
    │   ├── weather.py  获取天气
    │   ├── weather_utils   获取天气相关的代码
    │   │   ├── fetch.py
    │   │   ├── __init__.py
    │   │   ├── match.py
    │   │   └── save.py
    │   ├── weight.py   获取重量
    │   ├── weight_utils    获取重量相关的文件
    │   │   ├── blescan.py
    │   │   └── main.py
    │   └── wind.py 获取风力
    ├── database.sqlite3    数据
    ├── extensions  扩展功能的blueprint
    │   ├── __init__.py
    │   └── views.py
    ├── __init__.py 使用工厂模式构建app的文件
    ├── models.py   数据模型
    └── util    一些实用性的函数
        ├── cache.py    缓存装饰器
        ├── config.py   读取配置的代码
        ├── __init__.py
        └── resp.py 生成response的代码
```