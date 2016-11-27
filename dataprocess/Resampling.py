
from random import seed
from random import randrange
# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# test train/test split
seed(1)
dataset = [[1,1], [2,1], [3,1], [4,4], [5,5], [6,5], [7,7], [8,8], [9,8], [10]]
train, test = train_test_split(dataset)
print(train)
print(test)
print(randrange(50))
##k-fold Cross Validation Split
