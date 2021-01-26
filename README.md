# 中文医学短文本分类实验 #

随着医院信息化的发展，医学临床数据呈现出指数级的增长和积累，其中大多数为非结构化的自由文本数据。基于自然语言处理技术（NLP）将非结构化的医疗文本转化为结构化的信息，挖掘知识，并开发相关工具应用于临床上，在智慧医疗英语具有巨大的价值和潜力。

一般来说，医学自然语言处理包括命名实体识别、实体标准化、关系抽取、文本分类、决策支持系统构建等。此实验内容为医学短文本分类。

## 1. 实验数据

> 数据来源于第五届中国健康信息处理会议（CHIP2019）评测三。为中国临床试验注册网站公开的临床试验受试者筛选标准文本。数据特点未自由文本格式，短文本，非结构化，中文，医学相关。
>

我们筛选了其中的10000条数据，其中训练数据8000条，测试数据2000条。

类别包括15种，分别为： `成瘾行为（addictive behavior）`、`年龄（age）`、`过敏耐受（allergy intolerance）`、 `依存性（compliance with protocol）`、`知情同意（consent）`、`诊断（diagnostic）`、`疾病（disease）`、`参与其它试验（enrollment in other studies）`、`实验室检查（laboratory examinations）`、`预期寿命（life expectancy）`、`器官组织状态（organ or tissue status）`、`药物（pharmaceutical substance or drug）`、`风险评估（risk assessment）`、`吸烟状况（smoking status）`、`治疗或手术（therapy or surgery）`。

## 2. 实验流程
详细流程见文件 [Chinese_Medical_Text_Classification.pptx](https://github.com/zonghui0228/cn_med_text_class/blob/master/Chinese_Medical_Text_Classification.pptx)

## 3. 实验环境
* 软件工具
  * Anaconda3
  * Python3
  * Jupyter Notebook
  * Pyramid
  * Docker
* Python3 依赖包
  * [pandas](https://pypi.org/project/pandas/)
  * [numpy](https://pypi.org/project/numpy/)
  * [scikit-learn](https://pypi.org/project/scikit-learn/)
  * [jieba](https://pypi.org/project/jieba/)
  * [wordcloud](https://pypi.org/project/wordcloud/)
  * [matplotlib](https://pypi.org/project/matplotlib/)
  * [seaborn](https://pypi.org/project/seaborn/)

```Bash
# python3 packages install
pip install -r requirements.txt
```

## 3. 实验方法
* 逻辑回归, [logistic regression](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/LR/logistic_regression.ipynb)
* 支持向量机, [support vector machine](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/SVM/support_vector_machine.ipynb)
* K近邻算法, [k nearest neighbors](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/kNN/k_nearest_neighbors.ipynb)
* 朴素贝叶斯, [naive bayes](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/NB/naive_bayes.ipynb)
* 随机森林, [ranodm forest](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/RF/random_forest.ipynb)
* ~~神经网络, [Neural network](https://github.com/zonghui0228/cn_med_text_class/blob/master/models/NN/neural_network.ipynb)~~

## 4. Docker安装和网页展示
### 1.下载镜像：
```Bash
docker pull zonghui0228/cn_med_text_class:latest
```
### 2. 运行镜像：
* 选择1：直接运行镜像
```Bash
docker run -it -d -p 6543:6543 zonghui0228/cn_med_text_class
```
* 选择2：训练好自己的模型后，加载到镜像里，运行镜像
```Bash
# 建立文件夹model
mkdir model
cd model
# 将模型文件都移动到此文件夹，然后执行：
docker run -it -d -p 6543:6543 zonghui0228/cn_med_text_class
docker cp ./ CONTAINER_ID:/home/zonghui/mynginx/myproj/myproj/views/model/mymodel
```
### 3. 打开浏览器，输入：
```Bash
http://ip:6543/index
```

![img](https://github.com/zonghui0228/cn_med_text_class/blob/master/img/docker_6543.png)

