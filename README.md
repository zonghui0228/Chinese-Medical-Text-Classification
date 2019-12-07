# Chinese Medical Short Text Classification #

## 数据介绍：
* 10000条临床试验筛选标准，8000条训练数据(含label)，2000条测试数据。
* 自由文本格式，短文本，非结构化，中文，医学相关。   
* 44类语义类别，样本数据中包含15类。  

|#|group topic|semantic categories|
|---|---|----
|1|`Health Status`|`Disease` `Symptom` `Sign` `Pregnancy-related Activity` `Neoplasm Status` `Non-Neoplasm Disease Stage` `Allergy Intolerance` `Organ or Tissue Status` `Life Expectancy` `Oral related`
|2|`Treatment or Health Care`|`Pharmaceutical Substance or Drug` `Therapy or Surgery` `Device` `Nursing`
|3|`Diagnostic or Lab Test`|`Diagnostic` `Laboratory Examinations` `Risk Assessment` `Receptor Status`
|4|`Demographic Characteristics`|`Age` `Special Patient Characteristic` `Literacy` `Gender` `Education` `Address` `Ethnicity`
|5|`Ethical Consideration`|`Consent` `Enrollment in other studies` `Researcher Decision` `Capacity` `Ethical Audit` `Compliance with Protocol`
|6|`Lifestyle Choice`|`Addictive Behavior` `Bedtime` `Exercise` `Diet` `Alcohol Consumer` `Sexual related` `Smoking Status` `Blood Donation`
|7|`Data or Patient Source`|`Encounter` `Disabilities` `Healthy` `Data Accessible`
|8|`Other`|`Multiple`

## 实验平台：
Anaconda3 版本的Jupyter Notebook, Python3

## 分类方法：
* 逻辑回归, [logistic regression](https://github.com/zonghui0228/cn_med_text_class/blob/master/notebooks/logistic_regression.ipynb)
* 支持向量机, [support vector machine](https://github.com/zonghui0228/cn_med_text_class/blob/master/notebooks/support_vector_machine.ipynb)
* K近邻算法, [k nearest neighbors](https://github.com/zonghui0228/cn_med_text_class/blob/master/notebooks/k_nearest_neighbors.ipynb)
* 朴素贝叶斯, [naive bayes](https://github.com/zonghui0228/cn_med_text_class/blob/master/notebooks/naive_bayes.ipynb)
* 神经网络, [Neural network](https://github.com/zonghui0228/cn_med_text_class/blob/master/notebooks/neural_network.ipynb)，部分代码来源于《neural networks and deep learning》

## 所需python包：
* [pandas](https://pypi.org/project/pandas/)
* [numpy](https://pypi.org/project/numpy/)
* [codecs](https://docs.python.org/3/library/codecs.html)
* [scikit-learn](https://pypi.org/project/scikit-learn/)
* [jieba](https://pypi.org/project/jieba/)
* [wordcloud](https://pypi.org/project/wordcloud/)

## PPT介绍：
[Chinese_Medical_Text_Classification.pptx](https://github.com/zonghui0228/cn_med_text_class/blob/master/Chinese_Medical_Text_Classification.pptx)

## Docker安装：
```Bash
docker pull zonghui0228/cn_med_text_class:latest
```
```Bash
docker run -t -i -d -p 6543:6543 zonghui0228/cn_med_text_class
```
