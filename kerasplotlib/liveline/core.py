from __future__ import division
import warnings

import matplotlib
import matplotlib.pyplot as plt
from IPython.display import clear_output


def not_inline_warning():
    backend = matplotlib.get_backend()
    if "backend_inline" not in backend:
        warnings.warn("livelossplot requires inline plots.\nYour current backend is: {}\nRun in a Jupyter environment and execute '%matplotlib inline'.".format(backend))


def draw_plot(logs,
              metrics,
              figsize=None,
              max_epoch=None,
              max_cols=2,
              validation_fmt="val_{}",
              metric2title={}):

    clear_output(wait=True)
    plt.figure(figsize=figsize)

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
    plt.show();
