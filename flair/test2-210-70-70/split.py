from sklearn.model_selection import train_test_split

with open('train2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
mystring = ' '
for i in lines:
    mystring += i
tests = mystring.split("\n\n")

X_train, X_test1 =train_test_split(tests, test_size=0.4)
X_test, X_dev = train_test_split(X_test1, test_size=0.5)

print(len(X_train))
print(len(X_test))
print(len(X_dev))

train= '\n\n'.join(X_train)
test= '\n\n'.join(X_test)
dev= '\n\n'.join(X_dev)


with open('test.txt', 'w',encoding='utf-8') as f:
    f.write(test)

with open('train.txt', 'w',encoding='utf-8') as f:
    f.write(train)

with open('dev.txt', 'w',encoding='utf-8') as f:
    f.write(dev)

#import pandas as pd

# read text file into pandas DataFrame
#df = pd.read_csv("train1.txt", sep=" ", error_bad_lines=False)

# display DataFrame
#print(df)