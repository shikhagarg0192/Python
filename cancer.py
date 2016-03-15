from DecisionTree import DecisionTree
from DecisionTree import EvalTrainingData
from DecisionTree import DTIntrospection
from DecisionTree import TrainingDataGeneratorNumeric
from DecisionTree import TrainingDataGeneratorSymbolic
from DecisionTree import TestDataGeneratorSymbolic
from DecisionTree import __version__
from DecisionTree import __author__
from DecisionTree import __date__
from DecisionTree import __url__
from DecisionTree import __copyright__

training_datafile = "train.csv"
dt = DecisionTree(
                training_datafile = training_datafile,
                csv_class_column_index = 1,
                csv_columns_for_features = [2,4,5,6,7,9,11],
                entropy_threshold = 0.01,
                max_depth_desired = 15,
                symbolic_to_numeric_cardinality_threshold = 10,
     )

dt.get_training_data()
dt.calculate_first_order_probabilities()
dt.calculate_class_priors()
dt.show_training_data()
root_node = dt.construct_decision_tree_classifier()
root_node.display_decision_tree("   ")

test_sample  = ['Pclass = 3',
                'Sex = male',
                'Age = 22',
                'SibSp = 1',
                'Parch = 0',
                'Fare = 7.25',
                'Embarked = S']
classification = dt.classify(root_node, test_sample)
print "Classification: ", classification

