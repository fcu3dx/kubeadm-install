# 任务说明

## 设置计算机名

在`hosts`列表中添加 `hostname`项(变量)，且值不为空，则计算机名命名为该值
如果该变量不存在则跳过该任务执行.

```yml
when: hostname is defined and hostname != ""
```
