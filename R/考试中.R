1、	Setwd(“ \\ ”)  ## 设立工作路径
2、	A=read.table(“  .csv”, sep=",",header = T,)  ##导入文件
head (A)  ##查看数据集前六行
dim(A)  ##查看数据行列数
3、	Table(A$字段)
Length(A$字段[A$字段==”某字段1”)  ##计算某列中某类字段的个数
4、	Sort(A$列名,T)[1:5]  ##对某列降序排序，并取出排序后前五个价钱信息
5、	A$new[A$列名==”某字段2”]=”new”  
A$new[！（A$列名==”某字段2”）]=”其他”
Head(A$new)  ##新生一列数据，将列名中的”某字段2”记为”new”，其余记为”其他”
6、	nai$奶源产地[grep("澳洲/新西兰　",nai$奶源产地)]=gsub("澳洲/新西兰　","澳洲/新西兰",nai$奶源产地[grep("澳洲/新西兰　",nai$奶源产地)])
gsub("/","",nai$奶源产地[nai$奶源产地=="澳洲/新西兰"])         ##去掉 “列名”中“某字段2  ”和“其它　”的空格
7、	hist(nai$团购价.元.,xlab="团购价格",main="团购价直方图",col="lightblue")  ##绘制价格的直方图，设置横纵坐标，图名和颜色
8、	par(mfrow=c(1,2))
boxplot(log(nai$评价量)~nai$国产或进口,col="yellow")
boxplot(log(nai$评价量)~nai$new,col="blue")
9、	t <- nai$评价量[nai$包装单位=="桶装"]
   sum(t)

   h <- nai$评价量[nai$包装单位=="盒装"]
   sum(h)
！！！
han<-function(x)
{
  p=0
  p1=0
  for(i in 1:length(x$包装单位))
  {
    if(x$包装单位[i]=="桶装")
      p=p+x$评价量[i]
    if((x$包装单位[i]=="盒装"))
      p1=p1+x$评价量[i]
  }
  return(c(p,p1))
}
han(nai)
！！！
fun2=function(x)
{
q=c(0,0)
q[1]=mean(x[x$包装单位=="盒装",]$评价量)
q[2]=mean(x[x$包装单位=="桶装",]$评价量)
return(q)
}
fun2(nai)
10、nai$商品名称[grep("H",nai$商品名称)]   ##查找商品名称中含有“H”的奶粉名称
11、library(plyr)
y <- ddply(nai,.(配方),function(x){mean(x$评价量)})
y             ##计算不同配方的评价量的均值
12、利用现有数据，探究其他因素对评价量的影响

###商品毛重;团购价（散点图）
par(mfrow=c(1,2))
plot(log(nai$评价量)~nai$商品毛重,pch=1,cex=0.5,xlab="kg",ylab="评价量")
plot(log(nai$评价量)~nai$团购价,pch=1,col="yellow",cex=0.5,xlab="元",ylab="评价量")

###适用年龄.岁.
boxplot(log(nai$评价量)~nai$适用年龄.岁.,col="yellow")

###段位
n1 <- table(nai$段位)
v1 <- head(sort(n1,decreasing=TRUE))
v1=v1[order(v1,decreasing = T)]
boxplot(log(nai$评价量)~nai$段位,nai,col="yellow",alpha=0.4,xlab="段位",ylab="评价量")

###商品名称
n <- table(nai$商品名称)
v <- head(sort(n,decreasing=TRUE))
v=v[order(v,decreasing = T)]
l=prop.table(v)
barplot(l,names.arg = names(l)[1:6],col = rainbow(8,alpha = 0.4),xlab="商品名称",ylab="评价量")

小说
###1导入novels1.csv数据，并计算其维度（行列数），显示其数据集的前6行数据
setwd("F:\\异类语言\\R\\R实践\\1802班\\网路小说排行榜分析")
data=read.csv("novels1.csv")
head(data)
dim(data)

###2查看每种小说类型对应的频数
table(data$小说类型)

###3对评分这一列进行排序，并取出排序后前5个评分是多少
m=sort(data$评分)
m[1:5]
###4新生成一列，将评分大于7的记为高分，其余的为低分
#method1
data$分类=" score"
data$分类[data$评分>7]="高分"
data$分类[data$评分<=7]="低分"
table(data$分类)
data$分类2=rep(1,dim(data)[1])

#method2
data$分类3[data$评分>7]="高分"
data$分类3[data$评分<=7]="低分"

#method3
data$分类4=ifelse(data$评分>7,"高分","低分")

###5找出总点击数最大的那个小说的全部信息
data[which.max(data$总点击数),]
data[data$总点击数==max(data$总点击数),]
data[data$总点击数==1248708,]

###6绘制总点击数的直方图，设置横纵坐标，图名，颜色。
hist(log((data$总点击数/10000)),xlab="总点击数",ylab="频数",main="直方图",col="lightblue")

###7在1*2的画布上绘制写作进程对总点击数、授权状态对总点击数的分组箱线图
par(mfrow=c(1,2))
boxplot(log(data$总点击数)~data$写作进程,col="yellow")
boxplot(log(data$总点击数)~data$授权状态,col="red")

###8编写函数，其功能是计算不同性质小说的个数各是多少
fun1=function(x)
{
k=table(x$小说性质)
return(k)
}

fun1(data)

##拓展
fun2=function(x)
{
q=c(0,0)
q[1]=mean(x[x$小说性质=="VIP作品",]$总点击数)
q[2]=mean(x[x$小说性质=="公众作品",]$总点击数)
return(q)
}
fun2(data)

###9查找小说名称中含有汉字“玄”的小说
s=data$小说名称[grep("玄",data$小说名称)]
s

###10计算不同写作进程小说的平均点击量
library(plyr)
df=ddply(data,.(写作进程),function(x){mean(x$总点击数)})
df

面膜
setwd("C:\\Users\\Administrator\\Desktop\\面膜销售")
##1
data=read.csv("面膜销售数据.csv")
head(data)
dim(data)
data[1:4,]

##2
table(data$产地)

##3
table(data$控油祛痘)

##4
p=sort(data$价格,T)
p[1:5]

##5
data[which.max(data$评价数),]
data[data$评价数==max(data$评价数),]

##6
fun2=function(x)
{
a=table(x$适合肤质)
return(a)
}
fun2(data)

##7
hist(data$价格)

m=data$名称[grep("雀",data$名称)]
m

d=ddply(data,.(提拉紧致),function(x){mean(x$价格)})
d

##4
方法1
data$hux=rep(1,dim(data)[1])
data$hux[data$area>=100]="大户型"
data$hux[data$area<100]="小户型"

方法2
data$hux1[data$area>=100]="大户型"
data$hux1[data$area<100]="小户型"

方法3
data$hux2=ifelse(data$area>=100,"大户型","小户型")

##5
data[which.max(data$totalprice),]

data[data$totalprice==max(data$totalprice),]

##6
hist(log((data$totalprice/10000)),xlab="总价",ylab="频数",main="总价直方图",col="lightblue")
##7
par(mfrow=c(1,2))
boxplot(log(data$totalprice)~data$subway)
boxplot(log(data$totalprice)~data$road)

##8
fun1=function(x)
{
p=c(0,0)
p[1]=mean(x[x$subway==1,]$unitprice)
p[2]=mean(x[x$subway==0,]$unitprice)
return(p)
}
fun1(data)

install.packages("plyr")
library(plyr)

df=ddply(data,.(subway),function(x){mean(x$unitprice)})
df


##9
nam=names(data)
nam[grep("o",nam)]


##10
ddply(data,.(type),function(x){mean(x$totalprice)})

商铺
setwd("C:\\Users\\Administrator\\Desktop\\西安商铺")
##1
data=read.csv("shop_xian.csv")
head(data)
dim(data)
data[1:4,]

##2
table(data$subway)
table(data$type)

##3
a=sort(data$area)
a[1:5]

##4
方法1
data$hux=rep(1,dim(data)[1])
data$hux[data$area>=100]="大户型"
data$hux[data$area<100]="小户型"

方法2
data$hux1[data$area>=100]="大户型"
data$hux1[data$area<100]="小户型"

方法3
data$hux2=ifelse(data$area>=100,"大户型","小户型")

##5
data[which.max(data$totalprice),]
data[data$totalprice==max(data$totalprice),]

##6
hist(log((data$totalprice/10000)),xlab="总价",ylab="频数",main="总价直方图",col="lightblue")

##7
par(mfrow=c(1,2))
boxplot(log(data$totalprice)~data$subway)
boxplot(log(data$totalprice)~data$road)

##8
fun1=function(x)
{
p=c(0,0)
p[1]=mean(x[x$subway==1,]$unitprice)
p[2]=mean(x[x$subway==0,]$unitprice)
return(p)
}
fun1(data)

install.packages("plyr")
library(plyr)

df=ddply(data,.(subway),function(x){mean(x$unitprice)})
df

##9
nam=names(data)
nam[grep("o",nam)]

##10
ddply(data,.(type),function(x){mean(x$totalprice)})
