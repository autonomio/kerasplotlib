# kerasplotlib
A visualization library for Keras users with plots particularly useful for training and evaluating deep learning models. 


### TrainingLog

A live updated plot where each epoch is shown in a line graph. Adapted from [livelossplot](https://github.com/stared/livelossplot).

#### Usage

First import the package:

    from kerasplotlib import TrainingLog
    
If you're in a Notebook:
    
    %matplotlib inline
        
Then make sure that your model.fit includes the following: 

    callbacks=[TrainingLog()]
  
