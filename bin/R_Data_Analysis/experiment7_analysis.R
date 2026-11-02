# EXPERIMENT 7: DATA ANALYSIS AND VISUALIZATION USING R
# Dataset and 15 records reproduced from the BDA practical manual.

data <- data.frame(
  Student_ID = 1:15,
  Gender = c("Male", "Female", "Male", "Female", "Male",
             "Female", "Male", "Female", "Male", "Female",
             "Male", "Female", "Male", "Female", "Male"),
  Study_Hours = c(2, 4, 3, 5, 1, 3, 4, 2, 5, 4, 3, 5, 2, 3, 4),
  Attendance = c(72, 85, 80, 92, 65, 78, 88, 70, 95, 86, 76, 94, 68, 82, 89),
  Assignment_Score = c(65, 78, 72, 88, 55, 75, 82, 68, 91, 85, 70, 90, 60, 77, 84),
  Internal_Marks = c(60, 82, 70, 90, 52, 73, 80, 64, 92, 84, 68, 91, 58, 75, 81),
  Final_Marks = c(62, 84, 73, 91, 50, 76, 83, 65, 94, 86, 71, 93, 59, 78, 85)
)

cat("\n1. DATASET\n")
print(data)

cat("\n2. STRUCTURE\n")
str(data)

cat("\n3. SUMMARY\n")
print(summary(data))

cat("\n4. MEAN, MEDIAN AND STANDARD DEVIATION\n")
cat("Mean Final Marks:", mean(data$Final_Marks, na.rm = TRUE), "\n")
cat("Median Final Marks:", median(data$Final_Marks, na.rm = TRUE), "\n")
cat("SD Final Marks:", sd(data$Final_Marks, na.rm = TRUE), "\n")

cat("\n5. MINIMUM AND MAXIMUM\n")
cat("Minimum Final Marks:", min(data$Final_Marks, na.rm = TRUE), "\n")
cat("Maximum Final Marks:", max(data$Final_Marks, na.rm = TRUE), "\n")

cat("\n6. GENDER COUNT\n")
print(table(data$Gender))

# 7. BAR CHART
barplot(table(data$Gender),
        main = "Gender Count",
        xlab = "Gender",
        ylab = "Number of Students")

# 8. HISTOGRAM
hist(data$Final_Marks,
     main = "Distribution of Final Marks",
     xlab = "Final Marks",
     ylab = "Frequency")

# 9. SCATTER PLOT
plot(data$Study_Hours, data$Final_Marks,
     main = "Study Hours vs Final Marks",
     xlab = "Study Hours",
     ylab = "Final Marks",
     pch = 19)

# 10. PIE CHART
pie(table(data$Gender),
    main = "Gender Distribution")
