#Object: Manhattan & QQ Plot for genome-wide association study
#Output: Single figure with PDF/PNG format
#Authors: Yingwei Guo; Zhuangbiao Zhang
#Date: 8th, Jan, 2021
#Usage: Rscript commandArgs()[4] pvalue.txt sites_number traits_name outfmt

# 如果报没有qqman这个包的错误，在shell环境运行下面一行命令：
#export R_LIBS_USER="/stor9000/apps/users/NWSUAF/2015010726/R/x86_64-conda_cos6-linux-gnu-library/3.5/"

args <- commandArgs(trailingOnly = TRUE)

script_name <- (sub(".*/", "", commandArgs()[4]))

# If the number of arguments are not 4, print usuage.
if(length(args) < 4){
cat(paste("\n\tError! Please check your command according to the usuage below:\n\n\tUsage: Rscript", script_name, "pvalue.txt sites_number traits_name png/pdf\n\n"))
quit('no')
} 

library(qqman)
data <- read.table(args[1],header = T) #读取数去存到data变量里面
colorset <- c("#4C72B0", "#DD8452") # 创建一个颜色集合
x <- "png"
if(args[4] == x) {
   png(file = paste0(args[3], ".", args[4]), width=1500, height=350)
} else {
   pdf(file = paste0(args[3], ".", args[4]), width = 18,height=4.5)
}
layout(matrix(c(1,2), 1, 2, byrow = TRUE),widths=c(3,1), heights=c(1,1))
par(mar = (c(3,4,2,2)+ 0.5), mgp=c(1.6,1,0))
par(bty="l", lwd=1.5)  ## bty=l  the plot is coordinate instead of box
manhattan(data, CHR = "CHR", BP = "BP", SNP="SNP", p = "P", suggestiveline = F, genomewideline = F, cex = 0.8)  # 画曼哈顿图，默认是黑色和灰色，加color=colorset可自定义
sites_number <- as.numeric(args[2])
abline(h=-log10(0.05/sites_number), lty=5, col="grey40") # 自定义阈值线，h=-log10(0.05/sites_number)
qq(data$P, cex = 0.8)
dev.off()
