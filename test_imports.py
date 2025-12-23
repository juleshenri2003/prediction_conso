"""
Script de vérification des imports
Exécutez ce script pour vérifier que toutes les bibliothèques sont correctement installées.
"""

import sys

print("=" * 60)
print("VÉRIFICATION DES IMPORTS")
print("=" * 60)
print(f"\nPython version: {sys.version}\n")

errors = []
success = []

# Test NumPy
try:
    import numpy as np
    print(f"✓ NumPy {np.__version__}")
    success.append("NumPy")
except ImportError as e:
    print(f"✗ NumPy non installé : {e}")
    errors.append("NumPy")

# Test Matplotlib
try:
    import matplotlib
    print(f"✓ Matplotlib {matplotlib.__version__}")
    success.append("Matplotlib")
except ImportError as e:
    print(f"✗ Matplotlib non installé : {e}")
    errors.append("Matplotlib")

# Test Seaborn
try:
    import seaborn as sns
    print(f"✓ Seaborn {sns.__version__}")
    success.append("Seaborn")
except ImportError as e:
    print(f"✗ Seaborn non installé : {e}")
    errors.append("Seaborn")

# Test Scikit-learn
try:
    import sklearn
    print(f"✓ Scikit-learn {sklearn.__version__}")
    success.append("Scikit-learn")
except ImportError as e:
    print(f"✗ Scikit-learn non installé : {e}")
    errors.append("Scikit-learn")

# Test Jupyter
try:
    import jupyter
    print(f"✓ Jupyter installé")
    success.append("Jupyter")
except ImportError as e:
    print(f"✗ Jupyter non installé : {e}")
    errors.append("Jupyter")

# Test IPython Kernel
try:
    import ipykernel
    print(f"✓ IPython Kernel {ipykernel.__version__}")
    success.append("IPython Kernel")
except ImportError as e:
    print(f"✗ IPython Kernel non installé : {e}")
    errors.append("IPython Kernel")

# Test des imports spécifiques utilisés dans le notebook
print("\n" + "=" * 60)
print("VÉRIFICATION DES IMPORTS SPÉCIFIQUES")
print("=" * 60 + "\n")

try:
    from sklearn.neural_network import MLPRegressor
    print("✓ MLPRegressor (scikit-learn)")
except ImportError as e:
    print(f"✗ MLPRegressor non disponible : {e}")
    errors.append("MLPRegressor")

try:
    from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
    print("✓ Métriques sklearn (MSE, MAE, MAPE)")
except ImportError as e:
    print(f"✗ Métriques sklearn non disponibles : {e}")
    errors.append("Métriques sklearn")

try:
    from sklearn.preprocessing import StandardScaler
    print("✓ StandardScaler (scikit-learn)")
except ImportError as e:
    print(f"✗ StandardScaler non disponible : {e}")
    errors.append("StandardScaler")

# Résumé
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print(f"\n✓ Bibliothèques installées : {len(success)}/{len(success) + len(errors)}")

if errors:
    print(f"\n✗ Bibliothèques manquantes ({len(errors)}) :")
    for err in errors:
        print(f"  - {err}")
    print("\n💡 Solution : Exécutez 'pip install -r requirements.txt'")
else:
    print("\n🎉 Toutes les bibliothèques sont installées correctement !")
    print("   Vous pouvez maintenant exécuter le notebook.")

print("\n" + "=" * 60)

