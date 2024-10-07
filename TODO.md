# Your Dream Guitar / Guitar Builder / Universal Guitar Customizer

==*Il faut trouver un nom qui lorsqu’on le tape sur Google on le trouve, un nom avec des mots courant qui sont très susceptibles d’êtres cherchés (ex. built your dream custom guitar)*==

Guitar Builder - *Give birth to your dream guitar*

## Brainstorming

- Récupérer les formes de guitare de chaque marque, avec les têtes
    
- Récupérer les images de différents bois
    
- ex. de programmes :
    
    - https://www.kieselguitars.com/builder/guitar
    - https://virtual-guitar-builder.co.uk/v1/
    - https://leftyfretz.com/virtual-guitar-builder/
    - https://tctwp.com/kisekae/
- Implémenter l’ajout des couleurs (mode produit ? satin, matte, brillant, verni, sparkle…) avec un sélecteur de couleurs
    
    - [Add A Color Chooser To Treeview - Python Tkinter GUI Tutorial 181](https://www.youtube.com/watch?v=4j__fwak70g) => Il montre comment assigner une couleur à une variable
    - [Color Picker - Python Tkinter GUI Tutorial #49](https://www.youtube.com/watch?v=NDCirUTTrhg)
    - [Tkinter Color Chooser](https://www.pythontutorial.net/tkinter/tkinter-color-chooser/)
    - [PyQT Color picker widget (avec vidéo YouTube)](https://pythonprogramming.net/color-picker-widget-pyqt-tutorial/)
    - [PyQt5 QColorDialog – Selected Color](https://www.geeksforgeeks.org/pyqt5-qcolordialog-selected-color/) (C’est ce sélecteur de couleurs qui est utilisé dans KDE dans Konsole)
    - [blend modes](https://pypi.org/project/blend-modes/)
    - [layer-is-python](https://github.com/subwaymatch/layer-is-python)
    - [Mari : Manipuler les Couleurs et Images en Python](https://olivierschmitt.fr/mari-manipuler-les-couleurs-et-images-en-python/)
    - [Mari : Liste des modes de fusion du Painting Mode](https://olivierschmitt.fr/mari-liste-des-modes-de-fusion-du-painting-mode/)
    - [Mari : Liste des modes de fusion des Layers](https://olivierschmitt.fr/mari-liste-des-modes-de-fusion-des-layers/)
    - [CSS Blending Modes](https://www.youtube.com/watch?v=-c94pr41jaI)
- Possibilité de faire des dégradés de couleurs

- Possibilité de générer une customization aléatoire
    
- Possibilité d’importer une image pour l’avoir sur sa guitare (ex. créer la Jurassic Park guitare)

- Griser certaines options selon les choix qui sont fait (ex. si micro middle = None, griser les choix de marques)

- Dans le menu, quand on clique sur "Bridge Pickup" et qu'on sélectionne le type, on doit voir apparaitre les logos des marques dans le panneau de droite pour choisir le micro qu'on veut et faire apparaitre la description (scraping)

- menu : option "Pickup Configuration" : tout doit se faire dans le panneau de droite, en sélection bridge/middle/neck pickup

- Mettre un petit son / solo de guitare à l'ouverture du logiciel

- Aspirer la liste des micros disponibles par marque (web-scrapping)
    
- Choisir configuration des micros (H, HS, HSS, HH, HSH, SSS, HHH). Possibilité d’incliner les micros (comme sur certaines guitares des années 80)
    
- Possibilité d’exporter en .pdf une fiche de sa customisation avec la photo et toutes les caractéristiques de la guitare, le nom de l’utilisateur, le nom choisi pour la guitare
    
- Faire une option “random” qui sort une guitare avec tous les paramètres au pif
    
- Interface : PyQt ou TKinter
    
- Utiliser des toggle buttons switch pour activer ou désactiver certaines options
    
- arborescence sur le côté gauche des options (comme un explorateur de fichiers)
    
- Catégories : options générales, body, neck, head, electronics, hardware, export/load
    
- |     |     |
    | --- | --- |
    | Orientation / Dexterity |     |
    | Body shape |     |
    | Body wood |     |
    | Body finish - solid (couleur) | proposer couleurs prédéfinies ou utiliser un nuancier |
    | Body finish - transparent (couleur) |     |
    | Body finish - metallic (couleur) |     |
    | Body finish - fades (couleur) |     |
    | sparkle | oui / non |
    | Body finish - burst (couleur du burst) |     |
    | couleurs de l’arrière |     |
    | additional finish options | California burst, Reverse California burst, Black burst edges, translucent black burst edges |
    | revêtement / top coat | satin, vernis, brut |
    | Body binding |     |
    | Neck wood |     |
    | construction | neck thru, bolt-on |
    | fingerboard wood |     |
    | nombre de frettes |     |
    | fingerboard binding |     |
    | radius |     |
    | neck profile | C, D,  V, soft V |
    | frets | none, nickel, stainless, gold |
    | taille des frettes | small, jumbo, medium |
    | headstock finish (couleur tête) |     |
    | headstock shape |     |
    | headstock reverse | yes / no |
    | headstock binding |     |
    | truss rod cover |     |
    | nut (sillet) |     |
    | inlay shapes |     |
    | inlay material |     |
    | inlay position | standard, juste la case 12, aucun inlay |
    | hardware colour |     |
    | bridge | fixe, tremolo, floyd rose |
    | pickguard |     |
    | couleur des bobines des micros |     |
    | pickup pole pieces |     |
    | pickup bezel color |     |
    | cover pickup | none, black, silver, gold |
    | pickup neck |     |
    | pickup middle |     |
    | pickup bridge |     |
    | switch |     |
    | knobs | volume x1, volume x2, tone neck, tone middle |
    | knobs type | speed knobs, strat type… |
    | knobs couleur |     |
    | sortie jack | devant, sur le côté |
    | brand / marque |     |
    | modèle |     |
    | strings | 6, 7, 8, 9 |
    | multiscale |     |
    | scallopage |     |
    | scale length |     |
    | couleurs des plaques arrières pour l’électronique et le vibrato |     |
    | export image | format png, jpg |
    | export specs | pdf, txt, yaml, json |
    | import specs | import le fichier txt qui aura été exporté |