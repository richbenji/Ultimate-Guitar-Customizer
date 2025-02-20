# Étapes de développement du projet

## Introduction

1. Initialisation du projet :
   - Crée la structure de fichier proposée.
   - Initialise ton environnement virtuel et installe les dépendances.
2. Développement de l'interface graphique :
   - Commence par implémenter les composants visuels de base (panneaux, menus déroulants).
   - Ajoute progressivement la logique de modification de l'image de la guitare en fonction des options sélectionnées.
3. Gestion des assets :
   - Prépare les images et couleurs nécessaires pour l'aperçu dynamique.

## GitHub & GitKraken

### Création du dépôt local

Pour mettre ton projet GuitarBuilder sur GitHub en utilisant GitKraken, suis ces étapes :

1. **Créer un nouveau dépôt sur GitHub** :
   - Connecte-toi à ton compte GitHub.
   - Clique sur le bouton "+" en haut à droite et sélectionne "New repository".
   - Donne un nom à ton dépôt (par exemple, `GuitarBuilder`).
   - Choisis si tu veux le rendre public ou privé, puis clique sur "Create repository".
2. **Dans GitKraken** :
   - Dans l'onglet "Repository Management", sélectionne "Clone a repo" ou "Initialize a new repo" selon si tu veux cloner un dépôt existant ou créer un nouveau dépôt pour ton projet.
   - Si tu choisis "Initialize a new repo", sélectionne le dossier de ton projet `GuitarBuilder`.
3. **Ajouter des fichiers à ton dépôt** :
   - Une fois le dépôt créé ou initialisé, fais glisser les fichiers de ton projet dans la fenêtre de GitKraken ou utilise le bouton "+" pour les ajouter au suivi.
4. **Faire un commit** :
   - Dans la section "Unstaged Files", sélectionne les fichiers que tu veux ajouter.
   - Écris un message de commit (par exemple, "Initial commit") et clique sur le bouton "Commit changes".
5. **Pousser les modifications vers GitHub** :
   - Clique sur le bouton "Push" pour envoyer tes commits vers le dépôt GitHub que tu viens de créer.
   - Si tu as créé le dépôt sur GitHub, assure-toi de le lier à ton dépôt local en utilisant l'URL du dépôt (tu peux le faire dans les paramètres de ton dépôt dans GitKraken).

![GitKraken1](/media/richard/PROGRAMMATION/Projets/guitarBuilder/UltimateGuitarCustomizer/dev-notebook/GitKraken1.png)

![GitKraken2](/media/richard/PROGRAMMATION/Projets/guitarBuilder/UltimateGuitarCustomizer/dev-notebook/GitKraken2.png)

> Note : si le projet existe déjà, il faut pointer vers le dossier parent dans "Initialize in" et spécifier le nom du dossier dans "Name". GitKraken créera alors un dossier `.git`dans le répertoire déjà existant.

### Étapes pour lier ton dépôt local à GitHub

1. **Obtenir l'URL de ton dépôt GitHub** :
   - Accède à ton dépôt sur GitHub.
   - Copie l'URL du dépôt. Elle devrait ressembler à quelque chose comme `https://github.com/ton-utilisateur/GuitarBuilder.git`.
2. **Configurer le dépôt local avec l'URL de GitHub** :
   - Ouvre GitKraken et navigue vers ton dépôt local.
   - Si tu es dans GitKraken, il te suffit de cliquer sur le bouton de configuration du dépôt (l'icône en forme de crayon ou d'engrenage en haut à droite).
   - Dans les paramètres du dépôt, cherche la section "Remote" ou "Remotes".
   - Ajoute une nouvelle remote en cliquant sur le bouton "Add Remote" et entre les détails suivants :
     - **Nom** : par convention, on l'appelle `origin`.
     - **URL** : colle l'URL de ton dépôt GitHub que tu as copiée précédemment.
3. **Vérifier que la liaison a fonctionné** :
   - Dans GitKraken, tu devrais voir maintenant la remote `origin` listée dans les paramètres de ton dépôt.
4. **Pousser tes modifications vers GitHub** :
   - Une fois que tu as ajouté tes fichiers, fait des commits, et que tu es prêt à envoyer ton code vers GitHub, clique sur le bouton "Push".
   - Choisis la branche (généralement `main` ou `master`) et confirme que tu souhaites envoyer tes modifications.

![GitKraken3](/media/richard/PROGRAMMATION/Projets/guitarBuilder/UltimateGuitarCustomizer/dev-notebook/GitKraken3.png)

Résumé :

- Tu as un dépôt local pour travailler sur ton code.
- Tu as créé un dépôt sur GitHub pour stocker ton code en ligne.
- En ajoutant l'URL de GitHub comme remote dans ton dépôt local, tu peux facilement synchroniser les modifications entre les deux.

### Le fichier .gitignore

Lorsque tu choisis un template pour ton fichier `.gitignore`, cela dépend du type de projet que tu développes et des fichiers que tu souhaites ignorer. Voici quelques suggestions en fonction de ton projet `GuitarBuilder` :

- **Python** : Puisque ton projet est en Python, tu devrais inclure les règles spécifiques à Python. Par exemple :
  - Ignorer les fichiers `.pyc` (fichiers de bytecode).
  - Ignorer le dossier `__pycache__`.
  - Ignorer les fichiers de l'environnement virtuel (souvent nommé `venv` ou `env`).

- **Environnements Virtuels** : Si tu utilises un environnement virtuel (comme c'est le cas avec ton dossier `venv`), tu devrais également ignorer ce dossier pour éviter d'inclure les dépendances de l'environnement virtuel dans ton dépôt.
- **Fichiers Temporaire ou Cache** : Si tu as des fichiers temporaires ou des caches (comme ceux dans le dossier `scratches` que tu souhaites ignorer), il serait utile de les ajouter.
- Exemples de contenu pour `.gitignore` :

Voici un exemple de contenu pour ton fichier `.gitignore` :

```bash
# Ignorer l'environnement virtuel
venv/

# Ignorer les fichiers compilés Python
*.pyc
__pycache__/

# Ignorer les fichiers de configuration IDE (comme PyCharm)
.idea/
*.sublime-workspace
*.sublime-project

# Ignorer d'autres fichiers temporaires
scratches/
```

### Les licences

Le choix d'une licence pour ton projet dépend de la manière dont tu souhaites que les autres interagissent avec ton code. Voici quelques options courantes avec leurs caractéristiques :

1. **MIT License** :
   - **Simplicité et permissivité** : Permet à quiconque d'utiliser, modifier et distribuer le code, tant qu'ils incluent la licence d'origine.
   - **Idéal pour** : Les projets que tu veux rendre largement accessibles.
2. **GNU General Public License (GPL)** :
   - **Copyleft** : Permet d'utiliser, modifier et distribuer le code, mais exige que toute œuvre dérivée soit également sous la même licence.
   - **Idéal pour** : Projets où tu souhaites que les modifications restent libres.
3. **Apache License 2.0** :
   - **Permissive avec protections** : Permet d'utiliser, modifier et distribuer le code, tout en offrant une protection contre les brevets.
   - **Idéal pour** : Projets qui peuvent être utilisés dans des contextes commerciaux.
4. **Creative Commons** (pour des projets non logiciels) :
   - Il existe plusieurs types de licences Creative Commons, qui permettent de contrôler comment ton contenu peut être partagé et utilisé.
5. **Propriétaire** :
   - Si tu veux garder le contrôle total sur ton code sans permettre à d'autres de l'utiliser ou de le modifier.

## Initialisation du projet

### Création de la structure du projet

Voici une commande Bash qui te permettra de créer toute la structure de fichiers et dossiers de ton projet :

```bash
mkdir -p guitar_customizer/{assets/{guitars,logos,colors},src/{components,controllers,views}} && \
touch guitar_customizer/{guitar_customizer.py,requirements.txt,README.md,src/models.py,src/components/dropdowns.py,src/controllers/{general_options_controller.py,body_controller.py,preview_controller.py},src/views/{main_view.py,preview_view.py}}
```

Cette commande fait les actions suivantes :
1. **`mkdir -p`** : Crée les dossiers nécessaires (avec l'option `-p` pour créer les sous-dossiers en une fois).
2. **`touch`** : Crée les fichiers vides dans chaque dossier.

Après avoir exécuté cette commande, tu obtiendras l'arborescence suivante :

```
guitar_customizer/
│
├── assets/                 # Dossier pour les images de guitares et autres assets visuels
│   ├── guitars/            # Images de la guitare à charger selon les options
│   ├── logos/              # Logos pour la prévisualisation
│   └── colors/             # Aperçu des couleurs
│
├── src/
│   ├── components/         # Composants Tkinter (menus déroulants, widgets customisés)
│   │   └── dropdown.py     # Gestion des menus déroulants
│   ├── controllers/        # Contrôleurs pour gérer la logique de chaque section
│   │   ├── general_options_controller.py
│   │   ├── body_controller.py
│   │   └── preview_controller.py
│   ├── views/              # Vues (interfaces graphiques)
│   │   ├── main_view.py    # L'interface principale avec les trois panneaux
│   │   └── preview_view.py  # Interface pour l'aperçu
│   └── models.py           # Modèle de données représentant l'état actuel des options de la guitare
│
├── guitar_customizer.py    # Fichier principal qui lance l'application
├── requirements.txt        # Dépendances du projet
└── README.md               # Instructions pour lancer le projet
```

**Détails des composants :**

- **assets/** : Ce dossier contiendra toutes les ressources visuelles de ton application, comme les images des différentes options de guitare, les couleurs, et les logos.
- **src/components/** : Ce répertoire regroupera les composants Tkinter que nous allons réutiliser dans plusieurs parties de l'application, comme les menus déroulants (comboboxes), pour assurer une meilleure modularité et réutilisabilité du code.
- **src/controllers/** : Cette partie contiendra la logique pour chaque section de l'application (General Options, Body, etc.). Chaque contrôleur sera responsable de la gestion des données pour une partie spécifique des options de la guitare.
- **src/views/** : Les vues contiendront la logique d'affichage de l'interface graphique. Le fichier principal sera `main_view.py`, qui construira l'interface principale avec les trois panneaux (gauche : options, centre : aperçu de la guitare, droite : preview des logos/couleurs).
- **models.py** : Ce fichier contiendra les classes représentant les différentes options et paramètres pour la guitare, et servira de modèle de données pour stocker l'état courant de la configuration de la guitare.
- **guitar_customizer.py** : C'est le point d'entrée de l'application, qui initialise Tkinter et lance la fenêtre principale.

**Fichiers spécifiques :**

1. **guitar_customizer.py** :
   - C'est le fichier principal qui contient la logique pour démarrer l'application Tkinter.
   - Il importera les vues et contrôleurs, et initialisera l'interface graphique.
2. **controllers/general_options_controller.py** :
   - Ce fichier contrôlera la logique pour les options générales de la guitare, comme la dextérité (gauche/droite) et le nombre de cordes (6 ou 7).
3. **views/main_view.py** :
   - Ce fichier gérera la disposition des trois panneaux (options, guitare, et aperçu des options) et inclura les menus déroulants pour les différentes catégories d'options.
4. **views/preview_view.py** :
   - **vue dédiée à la prévisualisation** des options ou des éléments graphiques choisis dans l'application. Son rôle est de permettre à l'utilisateur de **voir en temps réel** les modifications apportées à la guitare ou à certains aspects de celle-ci (comme la couleur, les matériaux, etc.). Afficher les éléments visuels de la guitare dans la zone de prévisualisation (c'est-à-dire la partie droite ou centrale de l'interface).
5. **requirements.txt** :
   - Ce fichier listera toutes les dépendances Python nécessaires pour le projet. Pour le moment, cela inclura `tkinter` et `tkinter-designer`.
6. **components/`dropdown.py`**:
  - **`dropdown.py`** contient une **classe générique** qui encapsule la création d'un menu déroulant (`CTkComboBox` de `CustomTkinter`). Ce composant peut être utilisé partout dans l'application pour créer facilement un menu déroulant, et chaque instance aura des options (valeurs) différentes en fonction du contexte dans lequel elle est utilisée.

### Création de l'environnement virtuel Python

```bash
# Créer un environnement virtuel dans un dossier appelé 'venv'
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate  # Sur Linux/Mac

# Installer les dépendances
pip install -r requirements.txt
```

## Développement de l'interface utilisateur avec `Tkinter` et `customtkinter`

### Installation de Tkinter

Installer `tkinter`:

```bash
sudo apt install python3-tk
```

Sur Manjaro, il faut chercher le package `tk`dans Pamac.

### Installation de `customtkinter`

Dans ce projet, `tkinter` et `customtkinter`seront utilisés pour gérer l'interface graphique. Voici un aperçu de comment nous allons structurer la fenêtre avec les trois panneaux.

1. Le panneau de gauche contiendra les menus déroulants (General Options, Body, etc.).
2. Le panneau central affichera l'image de la guitare, qui changera en fonction des paramètres sélectionnés.
3. Le panneau de droite proposera un aperçu des couleurs et logos, sans affecter l'image principale.

```bash
# Installer customtkinter
pip install customtkinter

# Actualiser le fichier requirements.txt
pip freeze > requirements.txt
```

### Explication avec `CustomTkinter`

1. **Apparence Moderne :**
   - CustomTkinter ajoute une apparence plus moderne avec des widgets comme `CTkFrame`, `CTkButton`, et `CTkComboBox`, qui remplacent les widgets standards de Tkinter.
   - Le mode d'apparence peut être défini sur "dark" ou "light", et un thème de couleur (comme "blue", "green", ou "dark-blue") peut être choisi pour les composants.
2. **Panneaux déroulants :**
   - Chaque section ("General Options" et "Body") utilise des boutons pour déclencher les actions de **déroulement** et **réduction**. Ces boutons sont définis par `CTkButton`.
   - Le contenu des sections est encapsulé dans un `CTkFrame` et masqué ou affiché avec les méthodes `pack_forget()` et `pack()` pour simuler le déroulement.
3. **Widgets CustomTkinter :**
   - **`CTkButton`** : Utilisé pour les boutons de réduction/déroulement.
   - **`CTkComboBox`** : Remplace les menus déroulants standard (`ttk.Combobox`) par une version plus moderne.
   - **`CTkFrame`** : Remplace `tk.Frame` pour structurer l'interface.
   - **`CTkLabel`** : Remplace `tk.Label` pour afficher les labels dans l'interface.

### Résultat

L'interface aura maintenant un aspect plus moderne, avec les fonctionnalités suivantes :

- **Sections déroulantes (General Options et Body)** : Cliquer sur les boutons "General Options" ou "Body Options" permet de dérouler/réduire chaque section.
- **Menus déroulants stylisés** : Les options de sélection (dextérité, nombre de cordes, type de bois, couleurs) sont stylisées grâce à `CustomTkinter`.

### Améliorations possibles

- Tu peux facilement changer les couleurs ou thèmes en ajustant les paramètres `ctk.set_appearance_mode` et `ctk.set_default_color_theme`.
- Ajouter plus de logique pour mettre à jour le panneau central lorsque l'utilisateur sélectionne des options.

## Les `components`

### `dropdown.py`

Le fichier **`dropdown.py`** peut être utilisé pour encapsuler la logique et la création des **menus déroulants** (les **dropdowns**), afin de centraliser la création de ces composants qui sont utilisés à plusieurs endroits dans l'interface. Cela permet de :

- **Réutiliser le code** pour créer des menus déroulants, au lieu de réécrire plusieurs fois les mêmes éléments.
- **Modulariser** l'interface, en isolant les composants visuels dans des fichiers dédiés, ce qui rend le code plus facile à maintenir.

Le fichier **`dropdown.py`** servira à :

1. Créer des **widgets personnalisés** pour les menus déroulants (comme ceux pour le choix de la dextérité, des cordes, des bois, des couleurs, etc.).
2. Gérer les options communes, les styles, et potentiellement des comportements spécifiques liés aux menus déroulants.

Ce que contient `dropdown.py` :

1. **Classe `Dropdown`** : Une classe qui hérite de `CTkComboBox`, un widget de **CustomTkinter** utilisé pour créer des menus déroulants.
2. Paramètres de la classe :
   - **`parent`** : Le widget parent dans lequel le menu déroulant sera placé.
   - **`values`** : La liste des options à afficher dans le menu déroulant (ceci sera défini dans les vues comme `main_view.py`).
   - **`placeholder`** : Un texte qui apparaît dans le menu déroulant avant que l'utilisateur ne sélectionne une option.
   - **`kwargs`** : Des options supplémentaires que tu peux passer pour personnaliser le comportement (comme la largeur, la couleur, etc.).
3. Méthodes :
   - **`get_selected_value()`** : Retourne la valeur actuellement sélectionnée dans le menu déroulant.
   - **`reset()`** : Réinitialise le menu déroulant pour remettre le placeholder (texte par défaut).

### `switch.py`