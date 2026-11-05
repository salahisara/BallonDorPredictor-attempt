
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
# pip install lightgbm
from lightgbm import LGBMRanker


EXCEL_PATH = "BSO2.xlsx"   # <-- your file path

TRAIN_YEARS = [2018, 2019, 2021, 2022, 2023, 2024, 2025]
TEST_YEARS  = [2026]

TARGET_COL = "Rank"

# Numeric columns — fed in as-is (scaled for Ridge, untouched for RF)
NUMERIC_COLS = [
    "N_1", "Club_1", "UCL_result", "WC_finish", "CC_finish",
    "UEFA_Club_coefficient",  "WC_Goals", "WC_Assists", "CC_goals", "CC_Assists", "WC_year", "CC_year",
    "League_finish", "Goals", "Assists",
    "Is_Club_Cap", "Is_National_Cap", "Won_league", "Won_UCL",
]

#social media effects, public image


# Categorical columns — one-hot encoded
CATEGORICAL_COLS = [
    "Name", "Nationality", "Position", "Club_Country"
]

ALL_FEATURES = NUMERIC_COLS + CATEGORICAL_COLS


df = pd.read_excel(EXCEL_PATH)

missing = [c for c in ALL_FEATURES + [TARGET_COL, "Year"] if c not in df.columns]
if missing:
    raise ValueError(f"These columns weren't found in your spreadsheet: {missing}\n"
                      f"Your actual columns are: {list(df.columns)}")


train_df = df[df["Year"].isin(TRAIN_YEARS)].copy()
test_df  = df[df["Year"].isin(TEST_YEARS)].copy()

print(f"Training rows: {len(train_df)}  (years {TRAIN_YEARS})")
print(f"Test rows:     {len(test_df)}  (years {TEST_YEARS})")

X_train, y_train = train_df[ALL_FEATURES], train_df[TARGET_COL]
X_test,  y_test  = test_df[ALL_FEATURES],  test_df[TARGET_COL]


preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), NUMERIC_COLS),
    ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLS),
])

# Random Forest:
rf_pipeline = Pipeline([
    ("prep", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=300,
        max_depth=5,
        min_samples_leaf=3,
        random_state=42,
    )),
])

# Ridge regression:
ridge_pipeline = Pipeline([
    ("prep", preprocessor),
    ("model", Ridge(alpha=5.0)),
])


for name, pipeline in [("Random Forest", rf_pipeline), ("Ridge", ridge_pipeline)]:
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"\n=== {name} ===")
    print(f"Mean Absolute Error: {mae:.2f} rank positions")
    print(f"R²: {r2:.3f}")

    # Attach predictions back for inspection
    result_col = f"Predicted_rank_{name.replace(' ', '_')}"
    test_df[result_col] = preds


results = test_df[["Name", "Year", TARGET_COL,
                    "Predicted_rank_Random_Forest",
                    "Predicted_rank_Ridge"]].sort_values(
    "Predicted_rank_Random_Forest"
)
print("\n=== Test set predictions (sorted by model's predicted rank) ===")
print(results.to_string(index=False))


rf_model = rf_pipeline.named_steps["model"]
feature_names = rf_pipeline.named_steps["prep"].get_feature_names_out()
importances = pd.Series(rf_model.feature_importances_, index=feature_names)
importances = importances.sort_values(ascending=False)

print("\n=== Top 10 most important features ===")
print(importances.head(10).to_string())

