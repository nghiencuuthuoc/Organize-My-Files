#install.packages("RISmed")
# First, automagically install needed libraries:
list.of.packages <- c("RISmed")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='https://cran.rstudio.com/', dependencies = TRUE)
library(RISmed)

# setwd("Z:/BioMedSyn/R/project/PubMed and RISmed/")
# search_topic <- 'copd'
# Where do you save data search
getwd()
search_topic <- readline(prompt="Enter an key search: ") # for example Nexium
#search_query <- EUtilsSummary(search_topic, retmax=1000, mindate=2012,maxdate=2012)
search_query <- EUtilsSummary(search_topic)
summary(search_query)

# see the ids of our returned query
QueryId(search_query)

# get actual data from PubMed
records<- EUtilsGet(search_query)
class(records)

# store it
pubmed_data <- data.frame('Title'=ArticleTitle(records),'Abstract'=AbstractText(records))
head(pubmed_data,1)
# Write txt in R
write.table(pubmed_data, file='pubmed_drug_delivery.txt')
# Write CSV in R
write.csv(pubmed_data, file = "pubmed_drug_delivery.csv")

# First, automagically install needed library xlsx for save file to xlsx:
# list.of.packages <- c("rJava", "xlsx")
# new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
# if(length(new.packages)) install.packages(new.packages, repos='https://cran.rstudio.com/', dependencies = TRUE)
# install.packages("xlsx", dependencies = TRUE)
# library(xlsx)
# write.xlsx(pubmed_data, "pubmed_data_nexium.xlsx")

pubmed_data 
pubmed_data$Abstract <- as.character(pubmed_data$Abstract)
pubmed_data$Abstract <- gsub(",", " ", pubmed_data$Abstract, fixed = TRUE)

# see what we have
str(pubmed_data)

# Write txt in R
write.table(pubmed_data, file='pubmed_drug_delivery_1.txt')
# Write CSV in R
write.csv(pubmed_data, file='pubmed_drug_delivery_1.csv')
