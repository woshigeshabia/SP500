# EdgeSP500

基于边缘计算的工业级时序信号实时预测与异常分析系统

## 项目简介

本项目以标普500 ETF（SPY）分钟级数据为研究对象，
构建工业级时序预测系统。

系统实现：

- RNN
- GRU
- LSTM

三种神经网络对比实验。

重点分析：

- 梯度消散问题
- 收敛速度
- 推理延迟
- 模型大小
- 边缘部署性能

并构建异常波动检测模块与实时工业监控面板。

---

## 项目结构

（项目树）

---

## 环境配置

```bash
pip install -r requirements.txt
```

## 数据下载

```bash
python download_data.py
```

## 训练模型

```bash
python train/train_gru.py
```

## 启动工业面板

```bash
streamlit run frontend/app.py
```

---

## 实验结果

| Model | RMSE | Latency |
|--------|--------|--------|
| RNN | - | - |
| GRU | - | - |
| LSTM | - | - |

---

## 作者

XXX

浙江大学城市学院
