# BTC 5分钟预测系统

## 项目简介

这是一个基于Python的BTC 5分钟价格预测系统，使用机器学习模型进行预测，并提供自动交易功能。

## 功能特点

- 实时BTC价格监控
- 基于机器学习的价格预测
- 自动交易功能
- 胜率统计
- 语音播报
- 多平台支持（Windows、Android）

## 如何构建APK

### 方法：使用GitHub Actions

1. **创建GitHub仓库**
   - 在GitHub上创建一个新的仓库
   - 将本项目的所有文件上传到仓库中

2. **触发构建**
   - 推送代码到`main`分支
   - GitHub Actions会自动开始构建APK

3. **下载APK**
   - 构建完成后，在GitHub仓库的`Actions`标签页中找到构建任务
   - 点击`Artifacts`下载APK文件

### 构建配置

构建配置文件位于`.github/workflows/build.yml`，包含了所有必要的构建步骤。

## 依赖项

- Python 3.10+
- Kivy 2.0.0+
- requests
- pandas
- numpy
- scikit-learn

## 使用说明

1. **Windows版本**：直接运行`五分钟自动下单.py`
2. **Android版本**：安装构建生成的APK文件

## 注意事项

- Android版本需要网络权限来获取BTC价格数据
- 首次运行可能需要较长时间加载模型
- 自动交易功能需要配置坐标信息

## 许可证

MIT License
