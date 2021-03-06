library(ggplot2)
nflData=read.csv(file="c:/users/Mitch/projects/PyCharmProjects/newProj/NFL Stats.csv", header=TRUE, sep=",")
y = nflData$Score
x = nflData$Total.Yards
df = data.frame(x,y)

png(file = "scoreX Total Yards.png")
ggplot(df,aes(x=x,y=y)) + geom_point(alpha = 0.3)
# plot(x,y, xlab="Total Yards", ylab="Score", main="Score as a Function of Total Yards")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$First.Downs
png(file = "scoreX First Downs.png")
plot(x,y, xlab="First Downs", ylab="Score", main="Score as a Function of First Downs")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Passing.Yards
png(file = "scoreX Passing Yards.png")
plot(x,y, xlab="Passing Yards", ylab="Score", main="Score as a Function of Passing Yards")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Rushing.Yards
png(file = "scoreX Rushing Yards.png")
plot(x,y, xlab="Rushing Yards", ylab="Score", main="Score as a Function of Rushing Yards")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Penalty.Yards
png(file = "scoreX Penalty Yards.png")
plot(x,y, xlab="Penalty Yards", ylab="Score", main="Score as a Function of Penalty Yards")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Penalty.Count
png(file = "scoreX Penalty Count.png")
plot(x,y, xlab="Penalty Count", ylab="Score", main="Score as a Function of Penalty Count")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Turnovers
png(file = "scoreX Turnovers.png")
plot(x,y, xlab="Turnovers", ylab="Score", main="Score as a Function of Turnovers")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Punt.Count
png(file = "scoreX Punt Count.png")
plot(x,y, xlab="Punt Count", ylab="Score", main="Score as a Function of Punt Count")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Punt.Yards
png(file = "scoreX Punt Yards.png")
plot(x,y, xlab="Punt Yards", ylab="Score", main="Score as a Function of Punt Yards")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
x = nflData$Punt.Average
png(file = "scoreX Punt Average.png")
plot(x,y, xlab="Punt Average", ylab="Score", main="Score as a Function of Punt Average")
abline(lm(y~x), col="red") # regression line (y~x)
lines(lowess(x,y), col="blue") # lowess line (x,y)
dev.off()
