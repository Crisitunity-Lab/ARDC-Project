from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics  import classification_report,confusion_matrix, \
    accuracy_score, precision_score, recall_score, f1_score
from sklearn.utils.multiclass import unique_labels


def format_barplot(ax, title, xlabel):
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('', fontsize=12)
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.set_xlim([0, 1])


def class_metrics (actual_values, predicted_values, class_label_drop=[]):

    # Generate classification report
    report = classification_report(actual_values, predicted_values, output_dict=True)
    
    # Convert report to pandas dataframe and format it
    df = pd.DataFrame(report).transpose()
    df = df.drop(class_label_drop,errors='ignore')
    df = df.sort_values(by=['f1-score'], ascending=False)
    df = pd.concat([df[df.index.isin([ 'weighted avg'])], df[~df.index.isin(['accuracy', 'macro avg', 'weighted avg'])]])
    
    # Set color palette for plots
    colors = sns.color_palette('pastel')
   
    # Create subplots for precision, recall, and f1-score
    fig, axes = plt.subplots(ncols=3, sharey=True, figsize=(10, 6))
    
    # Plot precision
    ax = sns.barplot(x=df['precision'], y=df.index, color=colors[0], ax=axes[0])
    format_barplot(ax, 'Precision by Class', 'Precision')
    ax.axvline(x=df['precision'][0], color='grey', linestyle='--', alpha=0.5)

    # Plot recall
    ax = sns.barplot(x=df['recall'], y=df.index, color=colors[1], ax=axes[1])
    format_barplot(ax, 'Recall by Class', 'Recall')
    ax.axvline(x=df['recall'][0], color='grey', linestyle='--', alpha=0.5)

    # Plot f1-score
    ax = sns.barplot(x=df['f1-score'], y=df.index, color=colors[2], ax=axes[2])
    format_barplot(ax, 'F1-score by Class', 'F1-score')
    ax.axvline(x=df['f1-score'][0], color='grey', linestyle='--', alpha=0.5)
    
    # Display the plots
    plt.tight_layout()
    plt.show()
    
    # Return the classification report dataframe
    print(df)


def plt_confusion_matrix(actual_values, predicted_values):
      # Create the unique labels
      labels = unique_labels(actual_values, predicted_values)
      ylabel = np.unique(actual_values)
      print(ylabel)
      # Get the indices of labels that appear in ylabels
      indices = np.where(np.isin(labels, ylabel))

      # Delete the labels that appear in ylabels and append them to the end of labels
      labels = np.delete(labels, indices)
      labels = np.append(labels, ylabel)
      print(labels)
      # Change the label order for Not labeled, Other, Unknown
      indices = np.where((labels == 'Not labeled') | (labels == 'Other') | (labels == 'Unknown'))
      labels = np.delete(labels, indices)
      labels = np.append(labels, ['Other', 'Not labeled', 'Unknown'])
      print(labels)
      # Compute the confusion matrix.
      cm = confusion_matrix(actual_values, predicted_values, labels=labels)
      num_labels = len(ylabel)
      cm = cm[-num_labels-3:]
      ylabel = labels[-num_labels-3:]
      print(ylabel)
      # print cm shape
      print("Confusion Matrix Shape: ", cm.shape)
      # Create a mask that selects the diagonal elements
      diag = np.eye(len(ylabel), dtype=bool)
      difference = diag.shape[-1] - cm.shape[-1] 

      # make diag and array2 the same size by padding diag with zeros in the front columns
      mask = np.pad(diag, ((0, 0), (abs(difference), 0)), 'constant')
      print(mask.shape)

      # Create a color map with blue off-diagonal elements and green diagonal elements
      cmap = sns.diverging_palette(220, 20, as_cmap=True)
      cmap.set_bad("green")

      # Plot the confusion matrix.
      fig, ax = plt.subplots(figsize=(10, 8))
      sns.heatmap(cm,
                        annot=True,
                        fmt='g',
                        xticklabels=labels,
                        yticklabels=ylabel,
                        cbar=False,
                        annot_kws={"fontsize": 7})
      sns.heatmap(cm,
                        xticklabels=labels,
                        yticklabels=ylabel,
                        mask=mask,
                        cmap=cmap, cbar=False, square=True, linewidths=1, linecolor='white')

      plt.ylabel('Actual', fontsize=13)
      plt.xlabel('Prediction', fontsize=13)
      plt.title('Confusion Matrix', fontsize=17)
      plt.show()
      plt.clf()

      # Calculate metrics
      accuracy = accuracy_score(actual_values, predicted_values)
      precision = precision_score(actual_values, predicted_values, average='weighted')
      recall = recall_score(actual_values, predicted_values, average='weighted')
      f1 = f1_score(actual_values, predicted_values, average='weighted')

      # Print metrics
      print(f'Accuracy: {accuracy}')
      print(f'Precision: {precision}')
      print(f'Recall: {recall}')
      print(f'F1-score: {f1}')
      print('Unique Predict Labels: ', list(np.unique(predicted_values)))
      print('Unique Actual Labels: ', list(np.unique(actual_values)))
      print('Number of rows: ', len(actual_values))
      print(predicted_values.value_counts())
      class_label_drop = labels[~np.in1d(labels, np.unique(actual_values))]

      # Print class metrics
      class_metrics(actual_values, predicted_values,class_label_drop)