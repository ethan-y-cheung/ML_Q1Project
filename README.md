# Predicting the Productivity of Garment Workers

## Project Overview
This project focuses on predicting the productivity of garment workers using machine learning models. The dataset contains attributes related to worker performance, such as incentives, overtime, and idle time. The goal is to analyze these factors and determine their impact on productivity.

## Tools Used
This project was conducted using **Weka**, a machine learning software suite that provides various data preprocessing, attribute selection, and classification techniques.

## Methodology
1. **Data Preprocessing**
   - Removal of missing values
   - Discretization of numerical attributes using Weka’s discretization function
   - Attribute selection using Weka’s built-in evaluators
   
2. **Attribute Selection Techniques**
   - CorrelationAttributeEval
   - InfoGainAttributeEval
   - ReliefFAttributeEval
   - WrapperSubsetEval (with J48 Decision Tree)
   - Intuition-based attribute selection

3. **Machine Learning Models**
   - OneR
   - J48 Decision Tree
   - Random Forest
   - Decision Table

4. **Performance Evaluation**
   - Accuracy comparison across different attribute selection techniques and classifiers
   - Use of confusion matrices to assess classification errors

## Best Performing Model
The best-performing model was **Random Forest with InfoGainAttributeEval**, achieving an accuracy of **81.62%**.

## Steps to Reproduce
1. Open Weka and load the dataset.
2. Remove irrelevant attributes (e.g., WIP and Date).
3. Apply discretization using Weka’s discretization filter.
4. Select attributes using **InfoGainAttributeEval**.
5. Train a **Random Forest classifier** with 10-fold cross-validation.
6. Evaluate performance using Weka’s built-in metrics.

## Files Included
- **Garment_worker_productivity_classification.csv** - Original dataset
- **Garment_worker_productivity_classification_preprocessed.csv** - Preprocessed dataset
- **Nominalize_class.py** - Python script for converting the target variable
- **Train_test_val_split.py** - Python script for dataset splitting

## Conclusion
This project successfully demonstrates how machine learning can be leveraged to analyze worker productivity. The results indicate that **financial incentives and standard minute value (SMV) play a crucial role in productivity levels**. Future work could explore deep learning techniques for improved accuracy.
