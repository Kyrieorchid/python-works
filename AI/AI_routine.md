# AI 概念、工作方向与学习路线

本文件整理自前面两部分内容：  
1. **AI 相关概念（LLM、Transformer 等）与行业工作方向**  
2. **从零开始学习 AI 的完整路线图（结合系统级工程师背景）**

内容以结构化 Markdown 形式呈现，便于阅读、保存与扩展。

---

# 1. AI 核心概念

## 1.1 Transformer 是什么
Transformer 是现代大模型的基础架构，核心特点：

- 使用 **自注意力机制（Self-Attention）**
- 能并行处理序列（比 RNN/LSTM 更快）
- 由多层 Encoder/Decoder 堆叠组成
- 所有主流大模型（GPT、LLaMA、Qwen）都基于它

## 1.2 LLM（大语言模型）是什么
LLM = 基于 Transformer 训练出的超大规模语言模型。

能力包括：

- 文本生成
- 推理
- 总结
- 翻译
- 代码生成
- 多模态理解

LLM 是 **应用级产物**，Transformer 是 **底层结构**。

---

# 2. AI 行业主要工作方向

AI 行业的岗位可以按“从底层到应用”分为四大类。

## 2.1 模型本体方向（底层算法）

- **模型架构研究（Transformer/MoE）**
- **预训练（Pre-training）**：大规模训练基础模型
- **微调（Fine-tuning/SFT/RLHF）**：让模型适应特定任务

适合背景：数学、算法、科研导向

---

## 2.2 系统工程方向（AI Infra）

适合系统级工程师（如 Cortex-M/RISC-V 背景）。

包括：

- **推理优化（Inference Optimization）**
  - 量化（INT8/INT4）
  - KV Cache 优化
  - CUDA Kernel
  - TensorRT / TVM
- **AI 芯片软件栈（NPU/GPU）**
  - 算子开发（Operator）
  - 编译器（MLIR/TVM）
  - Runtime/Driver
- **分布式推理与服务化**

这是目前最缺人的方向。

---

## 2.3 应用层方向（LLM 应用）

- **RAG（检索增强生成）**：让模型能“查资料”
- **Agent（智能体）**：让模型能“执行任务”
- **企业级 AI 应用开发**（搜索、客服、办公自动化）

适合全栈、后端、系统工程师。

---

## 2.4 多模态方向

- 图像（Diffusion、ViT）
- 语音（ASR/TTS）
- 视频生成（Sora 等）

---

# 3. 从哪里开始学 AI（适合系统级工程师的路线）

以下路线专为具备 C、汇编、Linux、架构背景的工程师设计。

## 3.1 第一步：Python（1–2 周）

掌握：

- 基础语法
- Numpy
- Matplotlib
- Jupyter Notebook

## 3.2 第二步：机器学习基础（2–4 周）

理解：

- 线性回归 / 逻辑回归
- 训练 / 验证 / 测试
- 过拟合 / 正则化

目标：建立“模型 = 函数 + 参数 + 数据”的直觉。

## 3.3 第三步：深度学习（4–6 周）

重点：

- 神经网络（MLP）
- 反向传播（理解思想即可）
- PyTorch
- CNN

## 3.4 第四步：Transformer（4–8 周）

掌握：

- Self-Attention（Q/K/V）
- Multi-Head Attention
- Positional Encoding
- GPT/BERT 架构

产出：从零实现一个迷你 Transformer。

## 3.5 第五步：LLM 实战（4–8 周）

学习：

- Tokenizer（BPE）
- 预训练流程
- 微调（LoRA）
- 推理（KV Cache、量化）

产出：微调一个小模型（如 Qwen、LLaMA、Phi）。

---

# 4. 进阶方向（结合系统级背景）

## 4.1 推理优化（最适合你）

- CUDA Kernel
- Flash Attention
- KV Cache
- INT8/INT4 量化
- TensorRT / TVM

## 4.2 AI 芯片软件栈

- NPU/GPU 编译器
- 算子开发
- Runtime/Driver
- RISC-V + AI 加速器生态

## 4.3 Agent / RAG 系统工程

- 向量数据库（FAISS/Milvus）
- 检索 + 推理系统
- 多工具 Agent

---

# 5. 推荐的学习顺序（8 周入门 + 6 个月进阶）

## 0–2 周
Python + Numpy

## 2–6 周
机器学习基础

## 6–12 周
深度学习 + PyTorch

## 12–20 周
Transformer 理解与实现

## 20–28 周
LLM 微调与推理

## 28 周以后
进入专业方向：推理优化 / AI 芯片软件栈 / Agent 系统

---

# 6. 总结

- Transformer 是 LLM 的底层结构  
- LLM 是基于 Transformer 训练出的超大模型  
- AI 行业方向分为：模型、系统、应用、多模态  
- 系统级工程师最适合：推理优化、AI 芯片软件栈、Agent 系统  
- 学习路线：Python → ML → DL → Transformer → LLM → 专业方向  
