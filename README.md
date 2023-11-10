# 在线学籍验证报告翻译器

帮助中国宝宝翻译教育部在线学籍验证报告, 生成英文版验证报告, 可用于 github 学生认证等需要学生证明的地方。

> 注意：这只是个翻译器, 官方中文版在线学籍验证报告请在官方平台进行生成！！


### 快速开始

1. 使用 python3.9 安装依赖
    ```shell
      pip install -r requirements.txt
    ```
   
2. 打开中文版在线学籍验证报告, 将个人照片, 认证二维码保存放至 data 目录下
3. 在配置文件输入相关参数的中文
    ```shell
      vim configuration.yaml
   ```
   
4. 执行 main.py
    ```shell
      python main.py
   ```
   
5. 在 soutput 目录下查看生成的文件
    