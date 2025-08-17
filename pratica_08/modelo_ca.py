from sklearn.datasets import load_breast_cancer #Conjunto de dados câncer de mama
from sklearn.ensemble import RandomForestClassifier #Algoritmo Random Forest
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score  #Métricas de avaliação do modelo
from sklearn.model_selection import train_test_split #Divisão do conjunto de dados em treino e teste

data = load_breast_cancer() #Carrega o conjunto de dados

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42) #Divide os dados em treino e teste

modelo = RandomForestClassifier(n_estimators=100, random_state=42) #Cria o modelo Random Forest
modelo.fit(x_train, y_train) #Treina o modelo com os dados de treino

y_pred = modelo.predict(x_test) #Faz previsões com os dados de teste
y_prep_proba = modelo.predict_proba(x_test)[:, 1] #Probabilidades de previsão
precisao = precision_score(y_test, y_pred) #Calcula a precisão = TP / (TP + FP)
recall_score = recall_score(y_test, y_pred) #Calcula o recall = TP / (TP + FN)
f1 = f1_score(y_test, y_pred) #Calcula o F1 Score = 2 * (precisao * recall) / (precisao + recall)
auc = roc_auc_score(y_test, y_prep_proba) #Calcula a AUC-ROC = Área sob a curva ROC

print(f'Precisão: {precisao:.2f}')
print(f'Recall: {recall_score:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'AUC-ROC: {auc:.2f}') #Exibe as métricas de avaliação do modelo