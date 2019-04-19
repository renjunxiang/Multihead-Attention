# Multihead-Attention
Multihead Attention for PyTorch

[![](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/torch-1.0.0-brightgreen.svg)](https://pypi.org/project/torch/1.0.0)

## **项目简介**
最近在尝试注意力机制提升模型效果，没有找到PyTorch版本非常合适的Multihead-Attention，就参考部分资料尝试写了一个。<br>

## **模块结构**
Attention里面有两个简单的Self-Attention和Multihead-Attention<br>
Multihead-Attention修改自：<br>
<https://www.github.com/kyubyong/transformer>，<br>
还参考了：<br>
<https://github.com/jadore801120/attention-is-all-you-need-pytorch><br>
<https://blog.csdn.net/stupid_3/article/details/83184691>。<br>
一般来说，Q、K、V三者的通道数(即字/词的向量维度)是一致的，K通常等于V，不过PyTorch的nn.LayerNorm和自己实现的略有出入。
