# llm-sec-project

## 项目简介：

基于flask后端模型的一个简单调用千问api的调用实现

## 项目结构：

```
llm-sec-project/
├── llm/                  # LLM 相关业务模块
├── routes/               # 路由模块
├── security/             # 安全相关模块
├── templates/            # 模板文件目录
├── .env                  # 环境变量配置文件
├── .gitignore            # Git 忽略文件配置
├── app.py                # 项目入口/主应用文件
├── config.py             # 项目配置文件
├── README.md             # 项目说明文档
└── requirements.txt      # 项目依赖清单
```

## 项目依赖：

- Flask
- openai GDK
- os
- dotenv


## 项目日志：
2026.4.9 -前端添加回复网页功能，后端调用千文api，实现简单的问答功能，最小web-llm的实现框架
-接下来