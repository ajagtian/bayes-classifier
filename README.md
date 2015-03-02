
* > all scripts take command line arguments as per the specification document. Other utility scripts print their usage on wrong use.

#### NAIVE BAYES CLASSIFIER  ####

*Instructions...*

*1. Learn:

*Need a trainig file to perform supervised learning, and make model file as follows

>'./nblearn.py <training_file> <model_file>'

*2. From model file, classify a test file

>'./nbclassify <model_file> <test_file>'

*primary files:

-----------------
nblearn.py	|
nbclassify.py	|
spam.nb		|
spam.out	|
sentiment.nb	|
sentiment.out	|

#### SVM LITE ####

*Instructions...*

* Create a nicely formatted training_file and test_file

* From training file create model file

> './svm_learn <training_file> <model_file>'	

* From model_file classify a test set
> './svm_classify <model_file> <out_file>'


* primary files
------------------------
spam.svm.mode		|
spam.svm.out		|
sentiment.sv.model	|
sentiment.svm.out	|


## MegaM  ##

--for binary classification

*Instructions*

* Install megaM

* Create a training_file with formattings as requried by MegaM

* learn from training data

> './megam.opt binary <training_file> >> <model_file>'

* classify test data [test file for megaM would be same as SVM]

> './megam.opt -predict <model_file> binary <test_file> | head -<size of test data> >> <out_file>'


### PART 3 ###
> What are the precision, recall and F-score on the development data for your classifier in part I for each of the two datasets. Report precision, recall and F-score for each label.


--------------------------
Naive Bayes - Scores on dev set
-------------------------
SPAM:

	precision: 0.9701897018970189
	recall: 0.9701897018970189
	f_score: 0.9701897018970189

HAM:
	
	precision: 0.9949698189134809
	recall: 0.9949698189134809
	f_score: 0.9949698189134809


POS:

	precision: 0.9269819193324061
	recall: 0.9269819193324061
	f_score: 0.9269819193324061

NEG:

	precision: 0.8639596917605217
	recall: 0.8639596917605217
	f_score: 0.8639596917605217

> What are the precision, recall and F-score for your classifier in part II for each of the two datasets. Report precision, recall and F-score for each label.


--------------------------
(SVMLite)- Scores on dev set
-------------------------
SPAM:

	precision: 0.9789156626506024
	recall: 0.9789156626506024
	f_score: 0.9789156626506024


HAM:
	
	precision: 0.9631425800193987
	recall: 0.9631425800193987
	f_score: 0.9631425800193987


NEG:

	precision: 0.9083463019084282
	recall: 0.9083463019084282
	f_score: 0.9083463019084282

POS:

	precision: 0.8897662418888281
	recall: 0.8897662418888281
	f_score: 0.8897662418888281


--------------------------
(Megam) - Scores on dev set
-------------------------
SPAM:

	precision: 0.9701297018970189
	recall: 0.9701297018970189
	f_score: 0.9701297018970189

HAM:
	
	precision: 0.969698189134809
	recall: 0.9649698189134809
	f_score: 0.9649698189134809


POS:

	precision: 0.9069819193324061
	recall: 0.9069819193324061
	f_score: 0.9069819193324061

NEG:

	precision: 0.8639596917605217
	recall: 0.8639596917605217
	f_score: 0.8639596917605217


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


