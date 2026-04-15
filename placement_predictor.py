"""
PROJECT: University Placement Predictor (Random Forest Optimization)
GOAL: Compare GridSearchCV vs. RandomizedSearchCV on Imbalanced Data
"""

import time
import numpy as np
import pandas as pd
from scipy.stats import randint
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix

# ==========================================
# 1. DATA PREPARATION
# ==========================================
print("--- Step 1: Generating Imbalanced Placement Data ---")

# 1000 students, 20 features, 10% unplaced
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    weights=[0.9, 0.1],
    random_state=42
)

# Split (Stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scaling (NO DATA LEAKAGE)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 2. BASELINE MODEL
# ==========================================
print("\n--- Step 2: Baseline Model ---")

baseline = RandomForestClassifier(
    random_state=42,
    class_weight='balanced'
)

baseline.fit(X_train_scaled, y_train)
y_pred = baseline.predict(X_test_scaled)

print(f"Baseline Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Baseline F1-Score: {f1_score(y_test, y_pred):.4f}")

# ==========================================
# 3. GRID SEARCH (F1 OPTIMIZATION)
# ==========================================
print("\n--- Step 3: Grid Search (F1) ---")

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42, class_weight='balanced'),
    param_grid=param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

start_grid = time.time()
grid_search.fit(X_train_scaled, y_train)
end_grid = time.time()

grid_time = end_grid - start_grid

print(f"Grid Search Time: {grid_time:.2f} seconds")
print(f"Best Params (Grid): {grid_search.best_params_}")

# ==========================================
# 4. RANDOMIZED SEARCH
# ==========================================
print("\n--- Step 4: Randomized Search ---")

param_dist = {
    'n_estimators': randint(10, 500),
    'max_depth': [None, 10, 20, 30, 40, 50],
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42, class_weight='balanced'),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='f1',
    random_state=42,
    n_jobs=-1
)

start_rand = time.time()
random_search.fit(X_train_scaled, y_train)
end_rand = time.time()

rand_time = end_rand - start_rand

print(f"Random Search Time: {rand_time:.2f} seconds")
print(f"Best Params (Random): {random_search.best_params_}")

# ==========================================
# 5. FINAL COMPARISON
# ==========================================
print("\n" + "="*50)
print("FINAL PERFORMANCE COMPARISON")
print("="*50)

# Predictions
grid_pred = grid_search.predict(X_test_scaled)
rand_pred = random_search.predict(X_test_scaled)

# Scores
print(f"Grid Search F1:   {f1_score(y_test, grid_pred):.4f} | Time: {grid_time:.2f}s")
print(f"Random Search F1: {f1_score(y_test, rand_pred):.4f} | Time: {rand_time:.2f}s")

print("\nAccuracy Comparison:")
print(f"Grid Accuracy:   {accuracy_score(y_test, grid_pred):.4f}")
print(f"Random Accuracy: {accuracy_score(y_test, rand_pred):.4f}")

# ==========================================
# 6. DETAILED REPORTS
# ==========================================
print("\n--- Grid Search Classification Report ---")
print(classification_report(y_test, grid_pred))

print("\n--- Random Search Classification Report ---")
print(classification_report(y_test, rand_pred))

# ==========================================
# 7. CONFUSION MATRIX (BONUS)
# ==========================================
print("\n--- Confusion Matrix (Grid) ---")
print(confusion_matrix(y_test, grid_pred))

print("\n--- Confusion Matrix (Random) ---")
print(confusion_matrix(y_test, rand_pred))

# ==========================================
# FINAL NOTE
# ==========================================
print("\nMENTOR'S NOTE:")
print("> Accuracy can be misleading in imbalanced datasets.")
print("> F1-score ensures we correctly identify at-risk students.")
print("> GridSearch is slower but thorough; RandomizedSearch is faster and efficient.")