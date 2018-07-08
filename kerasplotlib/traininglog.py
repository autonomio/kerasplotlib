from __future__ import division
import warnings

import matplotlib
import matplotlib.pyplot as plt
from IPython.display import clear_output

from keras.callbacks import Callback

def loss2name(loss):
    if hasattr(loss, '__call__'):
        # if passed as a function
        return loss.__name__
    else:
        # if passed as a string
        return loss

class TrainingLog(Callback):
    def __init__(self, figsize=None, cell_size=(6, 4), dynamic_x_axis=False, max_cols=2):
        self.figsize = figsize
        self.cell_size = cell_size
        self.dynamic_x_axis = dynamic_x_axis
        self.max_cols = max_cols

    def on_train_begin(self, logs={}):
        self.base_metrics = [metric for metric in self.params['metrics'] if not metric.startswith('val_')]
        if self.figsize is None:
            self.figsize = (
                self.max_cols * self.cell_size[0],
                ((len(self.base_metrics) + 1) // self.max_cols + 1) * self.cell_size[1]
            )

        if isinstance(self.model.loss, list):
            losses = self.model.loss
        elif isinstance(self.model.loss, dict):
            losses = self.model.loss.values()
        else:
            losses = [self.model.loss]

        self.max_epoch = self.params['epochs'] if not self.dynamic_x_axis else None

        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        
        self.logs.append(logs.copy())

        draw_plot(self.logs, 
                  self.base_metrics,
                  figsize=self.figsize, 
                  max_epoch=self.max_epoch,
                  max_cols=self.max_cols,
                  validation_fmt="val_{}")

def draw_plot(logs,
              metrics,
              figsize=None,
              max_epoch=None,
              max_cols=2,
              validation_fmt="val_{}",
              metric2title={}):
    
    plt.figure(figsize=figsize)
    clear_output(wait=True)

    for metric_id, metric in enumerate(metrics):
        plt.subplot((len(metrics) + 1) // max_cols + 1, max_cols, metric_id + 1)

        if max_epoch is not None:
            plt.xlim(0, max_epoch)

        plt.plot(range(1, len(logs) + 1),
                 [log[metric] for log in logs],
                 label="training", color='#1B2F33', linestyle='dashed')
        plt.ylim(0, 1)
        if validation_fmt.format(metric) in logs[0]:
            plt.plot(range(1, len(logs) + 1),
                     [log[validation_fmt.format(metric)] for log in logs],
                     label="validation", color='#A72608')
        plt.ylim(0, 1)
        plt.title(metric2title.get(metric, metric), pad=15)
        plt.xlabel('epoch', color='grey')
    plt.legend(loc=1, ncol=1, bbox_to_anchor=(1.35, 1.0))

    plt.tight_layout()
    plt.show()
