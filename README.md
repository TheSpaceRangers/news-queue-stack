# 📰 NewsFlow - Agrégateur d'Actualités avec Stack et Queue

Un projet Python interactif pour gérer un flux d'actualités en utilisant les structures de données **Queue (File)** et **Stack (Pile)**.

---

## 🚀 Fonctionnalités

- 🔄 Récupère en temps réel les dernières actualités via l'API **[Currents API](https://currentsapi.services/en)**.
- 📥 Stocke les **articles non lus** dans une **file d’attente (Queue)**.
- 📚 Archive les **articles lus** dans une **pile (Stack)**.
- 📟 Interface en ligne de commande simple et intuitive.
- ✅ Code modulaire et bien structuré (chaque fonctionnalité dans un fichier séparé).

---

## 🧠 Structures de Données Utilisées

| Structure | Implémentation | Rôle |
|----------|----------------|------|
| Queue    | `collections.deque` | Stocke les articles non lus (FIFO) |
| Stack    | `list` native Python | Historique des articles lus (LIFO) |

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/newsflow.git
cd newsflow
```

2. Installer les dépendances

```bash
pip install -r requirements.txt
```
> 📌 Note : Le projet ne dépend que de requests, et de collections (natif).

3. Ajouter votre clé API

Dans le fichier config.py, ajoutez votre clé :

```python
API_KEY = "votre_clé_API"
```

---

## ▶️ Lancer l'application

```bash
python main.py
```

---

## 📸 Aperçu

```text
===== MENU =====
1. 📖 Lire un article
2. 🔙 Voir le dernier article lu
3. 🚪 Quitter
```

---

## 📄 Licence

Projet réalisé à des fins pédagogiques. Libre d’utilisation, modification et partage.