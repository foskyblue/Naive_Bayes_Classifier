# Naive_Bayes_Classifier

The project consists of four (4) classes:
 <li>CountVectorizer : Responsible for computing the vector of frequency for each document</li>
 <li>Main : Contains the main method, where program execution begin.</li>
 <li>NaiveBayes : Responsible for training and prediction</li>
 <li>PreProcess : Responsible for processing the texts. Folds all characters to lowercase, then tokenize them using 
 regular expression and uses the set of resulting words as the vocabulary.</li>
 
 ### How to run:
 This program was written using Python 3.7
 <li>Dependencies: Numpy, re</li>
 <br>
 After cloning/downloading, be sure that the training and test samples are available in ../datasets/train/ and 
 ../datasets/test folders respectively.
 
 Start execution from the Main class. After completion the following files are generated:
 <li>model.txt file is generated and saved in the output folder.</li>
 <li>result.txt file is also generated and saved in the output folder.</li>
 
 Accuracy, precision, recall and f1-measure is also computed for spam and ham classes.