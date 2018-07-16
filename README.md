# 魔镜后端服务器

```
|____app.py     运行服务器
|____config.ini 配置文件
|____core       核心功能文件夹
| |______init__.py
| |____login.py 登录 / 人脸识别
| |____register.py 注册 / 人脸模型训练
|____dataset    数据集
| |____haarcascade_frontalface_default.xml 数据集
| |____train    人脸图片
|____extensions 扩展功能
| |____humidity.py      获取湿度
| |____temperature.py   获取温度
|____route      服务器路由文件夹
| |____auth_route.py    身份认证路由 / 登录注册
| |____extension_route.py   扩展功能路由 / 温度湿度
|____utils      一些可能会用到的功能性函数
| |______init__.py
```


- Todo
    - [ ] 多线程优化人脸识别
    - [ ] API文档
    - [ ] 增加规范注释