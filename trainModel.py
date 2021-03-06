from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from prepDataforTraining import *
from sklearn import svm
from sklearn.model_selection import cross_val_score



model = svm.SVC()
model.fit(X_train, y_train)


print cross_val_score(model, X_test, y_test, scoring='roc_auc')















# # Fit regression model
# model = ensemble.GradientBoostingRegressor(
#     n_estimators=1000,
#     learning_rate=0.1,
#     max_depth=6,
#     min_samples_leaf=9,
#     max_features=0.1,
#     loss='huber'
# )
# model.fit(X_train, y_train)

# # Save the trained model to a file so we can use it in other programs
# joblib.dump(model, 'trained_house_classifier_model.pkl')
#
# # Find the error rate on the training set
# mse = mean_absolute_error(y_train, model.predict(X_train))
# print("Training Set Mean Absolute Error: %.4f" % mse)
#
# # Find the error rate on the test set
# mse = mean_absolute_error(y_test, model.predict(X_test))
# print("Test Set Mean Absolute Error: %.4f" % mse)

