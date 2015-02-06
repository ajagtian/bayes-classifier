HW1, Naive Bayes, CSCI 544

--------------------------------

*** Please consider the files that were reuqired to be submitted, other scripts were developed as helper scripts to do score calculations and other stuff.***

#### PART 1 ####

* nbtrain.py - creates a trainging file from directory of learning examples.
* nblearn.py - learns from a training file to create model file.
* nbclassify.py - classifies files as some class, based on learning.

* all scripts take command line arguments as per the specification document. Other utility scripts print their usage on wrong use.

#### PART 2 ####

* SVMLite implementation

### PART 3 ###
> What are the precision, recall and F-score on the development data for your classifier in part I for each of the two datasets. Report precision, recall and F-score for each label.


--------------------------
PART 1 - Scores on dev set
-------------------------
SPAM:

	precision: 0.9701897018970189
	recall: 0.9701897018970189
	f_score: 0.9701897018970189

HAM:
	
	precision: 0.9949698189134809
	recall: 0.9949698189134809
	f_score: 0.9949698189134809

> What are the precision, recall and F-score for your classifier in part II for each of the two datasets. Report precision, recall and F-score for each label.


--------------------------
PART 2 - Scores on dev set
-------------------------
SPAM:

	precision: 0.9789156626506024
	recall: 0.9789156626506024
	f_score: 0.9789156626506024


HAM:
	
	precision: 0.9631425800193987
	recall: 0.9631425800193987
	f_score: 0.9631425800193987


> What happens exactly to precision, recall and F-score in each of the two tasks (on the development data) when only 10% of the training data is used to train the classifiers in part I and part II? Why do you think that is?

* When the training data will be reduced, most of the files would be classifed as SPAM. The precision recall and f_score would decrease (tend towads zero ) for SPAM and tend towards 1 for HAM.

* Why? As the training data is reduced, we have less knowledge of what is SPAM and what is not, because of which smoothing effect kicks in, as result of which most of the files would be classifies as SPAMS. This is how Naive Bayes works.

* As the number of files guessed as spam are way more than actual, f_score decreases for spams.

* This is what normal behavior should be, when in some doubt mark as spam.

Here are the results under less (10%) training...


Naive Bayes:

SPAM:
	precision: 0.26424870466321243
	recall: 0.26424870466321243
	f_score: 0.26424870466321243
HAM:
	precision: 0.7328556806550666
	recall: 0.7328556806550666
	f_score: 0.7328556806550666


SVM Lite:

SPAM:

	precision: 0.28530670470756064
	recall: 0.28530670470756064
	f_score: 0.28530670470756064
HAM: 
	precision: 0.7537764350453172
	recall: 0.7537764350453172
	f_score: 0.7537764350453171


