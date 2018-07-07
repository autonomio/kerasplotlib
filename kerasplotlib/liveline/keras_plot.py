from __future__ import division

from keras.callbacks import Callback
from .core import draw_plot, not_inline_warning

metric2printable = {
    "acc": "Accuracy",
    "mean_squared_error": "Mean squared error",
    "mean_absolute_error": "Mean absolute error",
    "mean_absolute_percentage_error": "Mean absolute percentage error",
    "categorical_crossentropy": "Loss",
    "sparse_categorical_crossentropy": "Loss",
    "binary_crossentropy": "Loss",
    "logcosh": "Loss",
    "kullback_leibler_divergence": "Loss",
    "fmeasure": "f1 score"
}

def loss2name(loss):
    if hasattr(loss, '__call__'):
        # if passed as a function
        return loss.__name__
    else:
        # if passed as a string
        return loss

class PlotLossesKeras(Callback):
    def __init__(self, figsize=None, cell_size=(6, 4), dynamic_x_axis=False, max_cols=2):
        self.figsize = figsize
        self.cell_size = cell_size
        self.dynamic_x_axis = dynamic_x_axis
        self.max_cols = max_cols
        self.metric2printable = metric2printable.copy()

        not_inline_warning()

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

        loss_name = loss2name(losses[0])
        self.metric2printable['loss'] = "{}".format(self.metric2printable.get(loss_name, loss_name))
        if len(losses) > 1:
            for output_name, loss in zip(self.model.output_names, losses):
               loss_name = loss2name(loss)
               self.metric2printable['{}_loss'.format(output_name)] = "{} ({})".format(self.metric2printable.get(loss_name, loss_name), output_name)
        else:
            for output_name in self.model.output_names:
               self.metric2printable['{}_loss'.format(output_name)] = "{} ({})".format(self.metric2printable.get(loss_name, loss_name), output_name)

        self.max_epoch = self.params['epochs'] if not self.dynamic_x_axis else None

        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        self.logs.append(logs.copy())

        draw_plot(self.logs, self.base_metrics,
                  figsize=self.figsize, max_epoch=self.max_epoch,
                  max_cols=self.max_cols,
                  validation_fmt="val_{}",
                  metric2title=self.metric2printable)
