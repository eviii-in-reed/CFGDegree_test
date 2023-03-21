#subset() practice

student<-read.dta("student.dta")
young<-subset(student,select=c("w2a0801a","w2a0802","w2a10","w2a12","w2c01","w2c02","w2b21","w2d05"))
young<-na.omit(young)

levels(young$w2a0801a)
levels(young$w2a0802)

young2<-subset(young,w2a0801a=="No"|w2a0802=="Yes")
young3<-subset(young2,w2a12=="No, we don't")
young4<-subset(young3,w2b21=="Very confident")

attach(young)
BMI<-w2c02/(w2c01/100)^2
young$BMI<-BMI
detach(young)


levels(young$w2d05)
young5<-subset(young,BMI >22&w2d05=="Yes, I have or I\xa1\xafm in a relationship now")

#recode in {dplyr}
young5$w2d05<-recode(young5$w2d05,"Yes, I have or I\xa1\xafm in a relationship now"="Yes")