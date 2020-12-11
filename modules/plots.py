import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools as tools
# TODO: You can use other packages if you want, e.g., Numpy, Scikit-learn, etc.


def plot_learning_curves(train_losses, valid_losses, train_accuracies, valid_accuracies):
	# TODO: Make plots for loss curves and accuracy curves.
	# TODO: You do not have to return the plots.
	# TODO: You can save plots as files by codes here or an interactive way according to your preference.
	graph, labels = plt.subplots(1, 2, figsize = (20, 10))
	labels[0].set_title('Loss Curves')
	labels[0].plot(np.arange(len(train_losses)), train_losses, label='Train Loss')
	labels[0].plot(np.arange(len(valid_losses)), valid_losses, label='Validation Loss')
	labels[0].legend(loc="best")
	labels[0].set_xlabel("Epoch")
	labels[0].set_ylabel("Loss")
	labels[1].set_title('Accuracy Curves')
	labels[1].plot(np.arange(len(train_accuracies)), train_accuracies, label='Training Accuracy')
	labels[1].plot(np.arange(len(valid_accuracies)), valid_accuracies, label='Validation Accuracy')
	labels[1].legend(loc="best")
	labels[1].set_xlabel("Epoch")
	labels[1].set_ylabel("Accuracy")
	graph.savefig('Learning_Curve.png')



def plot_confusion_matrix(results, class_names):
	# TODO: Make a confusion matrix plot.
	# TODO: You do not have to return the plots.
	# TODO: You can save plots as files by codes here or an interactive way according to your preference.
	y_true, y_pred = zip(*results)

	# Compute confusion matrix
	cnf_matrix = confusion_matrix(y_true, y_pred)
	np.set_printoptions(precision=2)

	# Normalize
	plt.figure(figsize=(10, 10))
	cm = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
	plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
	plt.colorbar()
	tick_marks = np.arange(len(class_names))
	plt.xticks(tick_marks, class_names, rotation=45)
	plt.yticks(tick_marks, class_names)
	thresh = cm.max() / 2
	for x, y in tools.product(range(cm.shape[0]), range(cm.shape[1])):
		plt.text(y, x, format(cm[x, y], '.2f'), fontsize=12, horizontalalignment="center",
				color="white" if cm[x, y] > thresh else "black")
	plt.ylabel('True')
	plt.xlabel('Predicted')
	plt.title('Normalized Confusion Matrix')
	plt.savefig('Confusion_matrix.png')

