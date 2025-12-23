# Guide d'installation - Environnement Python pour le projet de prédiction de consommation

Ce guide vous explique comment configurer votre environnement Python pour exécuter le notebook `notebook.ipynb`.

## Prérequis

- Python 3.8 ou supérieur (recommandé : Python 3.10 ou 3.11)
- pip (gestionnaire de paquets Python, généralement inclus avec Python)

Pour vérifier votre version de Python :
```bash
python --version
```

## Option A : Environnement virtuel Python (venv) - RECOMMANDÉ

Cette méthode crée un environnement isolé pour votre projet, évitant les conflits avec d'autres projets.

### Étape 1 : Créer l'environnement virtuel

Ouvrez un terminal dans le répertoire du projet (`prediction_conso`) et exécutez :

```bash
python -m venv venv
```

Cela crée un dossier `venv` contenant l'environnement virtuel.

### Étape 2 : Activer l'environnement virtuel

**Sur Windows (PowerShell) :**
```powershell
venv\Scripts\Activate.ps1
```

Si vous obtenez une erreur de politique d'exécution, exécutez d'abord :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Sur Windows (Invite de commandes) :**
```cmd
venv\Scripts\activate.bat
```

**Sur Linux/Mac :**
```bash
source venv/bin/activate
```

Une fois activé, vous verrez `(venv)` au début de votre ligne de commande.

### Étape 3 : Installer les dépendances

Avec l'environnement activé, installez toutes les bibliothèques nécessaires :

```bash
pip install -r requirements.txt
```

### Étape 4 : Installer le kernel Jupyter (pour utiliser le notebook)

Pour que Jupyter puisse utiliser votre environnement virtuel :

```bash
python -m ipykernel install --user --name=prediction_conso --display-name "Python (prediction_conso)"
```

### Étape 5 : Lancer Jupyter

```bash
jupyter notebook
```

Ou si vous préférez JupyterLab :

```bash
jupyter lab
```

### Étape 6 : Désactiver l'environnement (quand vous avez terminé)

```bash
deactivate
```

---

## Option B : Conda (Alternative)

Si vous utilisez Anaconda ou Miniconda, vous pouvez créer un environnement conda.

### Étape 1 : Créer l'environnement conda

```bash
conda create -n prediction_conso python=3.10
```

### Étape 2 : Activer l'environnement

```bash
conda activate prediction_conso
```

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou installez certaines bibliothèques via conda :

```bash
conda install numpy matplotlib scikit-learn jupyter seaborn
```

### Étape 4 : Installer le kernel Jupyter

```bash
python -m ipykernel install --user --name=prediction_conso --display-name "Python (prediction_conso)"
```

### Étape 5 : Lancer Jupyter

```bash
jupyter notebook
```

---

## Vérification de l'installation

Pour vérifier que toutes les bibliothèques sont correctement installées, vous pouvez exécuter ce script Python :

```python
import sys
print(f"Python version: {sys.version}")

try:
    import numpy as np
    print(f"✓ NumPy {np.__version__}")
except ImportError:
    print("✗ NumPy non installé")

try:
    import matplotlib
    print(f"✓ Matplotlib {matplotlib.__version__}")
except ImportError:
    print("✗ Matplotlib non installé")

try:
    import seaborn as sns
    print(f"✓ Seaborn {sns.__version__}")
except ImportError:
    print("✗ Seaborn non installé")

try:
    import sklearn
    print(f"✓ Scikit-learn {sklearn.__version__}")
except ImportError:
    print("✗ Scikit-learn non installé")

try:
    import jupyter
    print(f"✓ Jupyter installé")
except ImportError:
    print("✗ Jupyter non installé")
```

Ou créez un fichier `test_imports.py` avec ce contenu et exécutez-le :

```bash
python test_imports.py
```

---

## Bibliothèques installées

Le fichier `requirements.txt` installe les bibliothèques suivantes :

- **numpy** (>=1.24.0) : Calculs numériques et manipulation de tableaux
- **matplotlib** (>=3.7.0) : Visualisations graphiques
- **seaborn** (>=0.12.0) : Visualisations statistiques avancées
- **scikit-learn** (>=1.3.0) : Machine learning (MLPRegressor, métriques, preprocessing)
- **jupyter** (>=1.0.0) : Interface pour exécuter les notebooks
- **ipykernel** (>=6.25.0) : Kernel Python pour Jupyter

---

## Dépannage

### Problème : "pip n'est pas reconnu"
- Assurez-vous que Python est installé et ajouté au PATH
- Sur Windows, réinstallez Python en cochant "Add Python to PATH"

### Problème : Erreur lors de l'activation de l'environnement virtuel
- Vérifiez que vous êtes dans le bon répertoire
- Sur Windows PowerShell, vous devrez peut-être changer la politique d'exécution (voir Option A, Étape 2)

### Problème : "ModuleNotFoundError" dans le notebook
- Vérifiez que l'environnement virtuel est activé
- Vérifiez que vous avez sélectionné le bon kernel dans Jupyter (menu Kernel > Change Kernel)
- Réinstallez les dépendances : `pip install -r requirements.txt`

### Problème : Le notebook ne trouve pas le fichier CSV
- Assurez-vous que le fichier `conso_campus_aix.csv` est dans le même répertoire que le notebook
- Vérifiez le répertoire de travail dans Jupyter (menu File > Open)

---

## Mise à jour des dépendances

Si vous modifiez `requirements.txt`, réinstallez les dépendances :

```bash
pip install --upgrade -r requirements.txt
```

---

## Support

Si vous rencontrez des problèmes, vérifiez :
1. Que Python 3.8+ est installé
2. Que l'environnement virtuel est activé
3. Que toutes les dépendances sont installées (`pip list`)
4. Que le bon kernel est sélectionné dans Jupyter


