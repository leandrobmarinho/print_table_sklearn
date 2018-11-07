import pandas as pd, glob


def create_table(file, classifiers, metrics, num_test, type='mean_metrics', without_name=False):
    # METRICS: test_f1_macro test_f1_micro test_f1_weighted test_matthews_corrcoef test_precision_macro test_precision_micro test_precision_weighted test_recall_macro test_recall_micro test_recall_weighted

    # creating table
    df = pd.read_csv(file)

    # Select classifiers
    df = df.loc[df['classifier'].isin(classifiers)]

    # # Select metrics
    # temp_metrics = list(metrics)
    # temp_metrics.append(df.columns[0])
    # temp_metrics.append(df.columns[1])
    # temp_metrics.append(df.columns[2])
    # df = df[temp_metrics]

    # Select the output print
    if type is "mean_std_metrics":
        output = "print('{:.PRECISION}\t{:.PRECISION}\t'.format(mean, std), end='')"

    elif type is "mean_metrics":
        output = "print('{:.PRECISION}\t'.format(mean), end='')"

    elif type is "test_acc":
        metrics = ['test_accuracy']
        output = "print('{:.PRECISION}\t'.format(mean), end='')"

    elif type is "mean_std_metrics_pm":

        output = "print('{:.PRECISION}$\pm${:.PRECISION}\t'.format(mean, std), end='')"

    for i in range(0, int(len(df.index) / 2)):

        for metric in metrics:
            mean = float(df[metric].values[i * 2])
            std = float(df[metric].values[i * 2 + 1])

            if metric is 'score_time':
                mean = mean / num_test
                std = std / num_test

            elif metric is not 'fit_time':
                mean = mean * 100
                std = std * 100

            name = df["classifier"].values[i * 2]
            model = df["model"].values[i * 2]

            if metric is 'score_time' or metric is 'fit_time':
                output_prec = output.replace('PRECISION', '3f')
            else:
                output_prec = output.replace('PRECISION', '2f')

            eval(output_prec)

        if not without_name:
            print('{:<18}\t{}'.format(name, model))
        else:
            print('')


if __name__ == '__main__':
    # parameters
    classifiers = ['Bayes', 'MLP', 'Nearest_Neighbors', 'Random_Forest',
                   'SVM_Linear', 'SVM_Polynomial', 'SVM_RBF']

    metrics = ['test_accuracy', 'test_f1_weighted', 'test_recall_weighted',
               'fit_time', 'score_time']

    type = 'mean_std_metrics_pm'  # mean_std_metrics mean_metrics test_acc mean_std_metrics_pm

    num_test = 120
    for file in glob.glob('examples/*.csv'):
        create_table(file, classifiers, metrics, num_test, type)
