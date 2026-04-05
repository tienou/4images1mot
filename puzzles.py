"""
Base de données des puzzles pour 4 Images 1 Mot.
Chaque puzzle contient :
  - word: le mot à deviner
  - images: 4 descriptions + couleur de fond pour les cartes visuelles
  - difficulty: 1 (facile) à 3 (difficile)
"""

PUZZLES = [
    {
        "word": "SOLEIL",
        "images": [
            {"desc": "Lever du jour\nsur la mer", "color": "#FF6B35", "icon": "☀️"},
            {"desc": "Lunettes\nde soleil", "color": "#F7C948", "icon": "🕶️"},
            {"desc": "Crème\nsolaire", "color": "#FFA62B", "icon": "🧴"},
            {"desc": "Tournesol\nen fleur", "color": "#FFD166", "icon": "🌻"},
        ],
        "difficulty": 1,
    },
    {
        "word": "CHAT",
        "images": [
            {"desc": "Boule\nde poils", "color": "#A8DADC", "icon": "🐱"},
            {"desc": "Pelote\nde laine", "color": "#457B9D", "icon": "🧶"},
            {"desc": "Griffes\nacérées", "color": "#1D3557", "icon": "🐾"},
            {"desc": "Souris\nqui court", "color": "#E63946", "icon": "🐭"},
        ],
        "difficulty": 1,
    },
    {
        "word": "FROID",
        "images": [
            {"desc": "Flocons\nde neige", "color": "#CAF0F8", "icon": "❄️"},
            {"desc": "Bonhomme\nde neige", "color": "#90E0EF", "icon": "⛄"},
            {"desc": "Glaçons\ntransparents", "color": "#48CAE4", "icon": "🧊"},
            {"desc": "Écharpe\nen laine", "color": "#023E8A", "icon": "🧣"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MUSIQUE",
        "images": [
            {"desc": "Notes sur\nune portée", "color": "#7B2CBF", "icon": "🎵"},
            {"desc": "Guitare\nacoustique", "color": "#9D4EDD", "icon": "🎸"},
            {"desc": "Casque\naudio", "color": "#C77DFF", "icon": "🎧"},
            {"desc": "Piano\nà queue", "color": "#E0AAFF", "icon": "🎹"},
        ],
        "difficulty": 1,
    },
    {
        "word": "PLAGE",
        "images": [
            {"desc": "Sable\nfin doré", "color": "#FFD166", "icon": "🏖️"},
            {"desc": "Vagues\nbleues", "color": "#118AB2", "icon": "🌊"},
            {"desc": "Parasol\ncoloré", "color": "#EF476F", "icon": "⛱️"},
            {"desc": "Coquillage\nrare", "color": "#06D6A0", "icon": "🐚"},
        ],
        "difficulty": 1,
    },
    {
        "word": "ROUGE",
        "images": [
            {"desc": "Rose\nécarlate", "color": "#E63946", "icon": "🌹"},
            {"desc": "Camion de\npompier", "color": "#D62828", "icon": "🚒"},
            {"desc": "Fraise\njuteuse", "color": "#C1121F", "icon": "🍓"},
            {"desc": "Feu de\nsignalisation", "color": "#780000", "icon": "🚦"},
        ],
        "difficulty": 1,
    },
    {
        "word": "VOITURE",
        "images": [
            {"desc": "Volant\nen cuir", "color": "#264653", "icon": "🚗"},
            {"desc": "Route\nasphaltée", "color": "#2A9D8F", "icon": "🛣️"},
            {"desc": "Pneu\nnoir", "color": "#E9C46A", "icon": "🔧"},
            {"desc": "Clé de\ncontact", "color": "#F4A261", "icon": "🔑"},
        ],
        "difficulty": 2,
    },
    {
        "word": "NUIT",
        "images": [
            {"desc": "Étoiles\nscintillantes", "color": "#10002B", "icon": "⭐"},
            {"desc": "Lune\ncroissante", "color": "#240046", "icon": "🌙"},
            {"desc": "Hibou\nperché", "color": "#3C096C", "icon": "🦉"},
            {"desc": "Lampe de\nchevet", "color": "#5A189A", "icon": "🔦"},
        ],
        "difficulty": 1,
    },
    {
        "word": "LIVRE",
        "images": [
            {"desc": "Bibliothèque\nremplie", "color": "#606C38", "icon": "📚"},
            {"desc": "Lunettes\nde lecture", "color": "#283618", "icon": "👓"},
            {"desc": "Page\ntournée", "color": "#FEFAE0", "icon": "📖"},
            {"desc": "Marque-\npage", "color": "#DDA15E", "icon": "🔖"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MONTAGNE",
        "images": [
            {"desc": "Sommet\nenneigé", "color": "#457B9D", "icon": "🏔️"},
            {"desc": "Randonneur\nsur sentier", "color": "#1D3557", "icon": "🥾"},
            {"desc": "Chalet en\nbois", "color": "#A8DADC", "icon": "🏠"},
            {"desc": "Aigle\nmajestueux", "color": "#F1FAEE", "icon": "🦅"},
        ],
        "difficulty": 2,
    },
    {
        "word": "FEU",
        "images": [
            {"desc": "Flammes\nvives", "color": "#FF4800", "icon": "🔥"},
            {"desc": "Cheminée\nallumée", "color": "#FF6000", "icon": "🏠"},
            {"desc": "Allumettes\nen bois", "color": "#FF8800", "icon": "🔥"},
            {"desc": "Marshmallow\ngrillé", "color": "#FFB700", "icon": "🍡"},
        ],
        "difficulty": 1,
    },
    {
        "word": "ÉCOLE",
        "images": [
            {"desc": "Tableau\nnoir craie", "color": "#264653", "icon": "📝"},
            {"desc": "Cartable\ncoloré", "color": "#2A9D8F", "icon": "🎒"},
            {"desc": "Cour de\nrécréation", "color": "#E9C46A", "icon": "🏫"},
            {"desc": "Cahier et\ncrayon", "color": "#F4A261", "icon": "✏️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "VENT",
        "images": [
            {"desc": "Éolienne\ntournante", "color": "#48CAE4", "icon": "🌬️"},
            {"desc": "Cerf-volant\nen l'air", "color": "#0096C7", "icon": "🪁"},
            {"desc": "Feuilles\nqui volent", "color": "#0077B6", "icon": "🍂"},
            {"desc": "Drapeau\nqui flotte", "color": "#023E8A", "icon": "🏳️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "TEMPS",
        "images": [
            {"desc": "Horloge\nancienne", "color": "#774936", "icon": "⏰"},
            {"desc": "Sablier\nqui coule", "color": "#9B8816", "icon": "⏳"},
            {"desc": "Calendrier\nmural", "color": "#6B705C", "icon": "📅"},
            {"desc": "Rides\ndu visage", "color": "#A5A58D", "icon": "👴"},
        ],
        "difficulty": 3,
    },
    {
        "word": "DANSE",
        "images": [
            {"desc": "Chaussons\nde ballet", "color": "#FFCAD4", "icon": "🩰"},
            {"desc": "Piste de\ndanse", "color": "#F4ACB7", "icon": "💃"},
            {"desc": "Tango\npassionné", "color": "#9D8189", "icon": "🕺"},
            {"desc": "Rythme\net musique", "color": "#D8E2DC", "icon": "🎶"},
        ],
        "difficulty": 2,
    },
    {
        "word": "JARDIN",
        "images": [
            {"desc": "Arrosoir\nvert", "color": "#606C38", "icon": "🌱"},
            {"desc": "Fleurs\nmulticolores", "color": "#283618", "icon": "🌸"},
            {"desc": "Tondeuse\nà gazon", "color": "#FEFAE0", "icon": "🌿"},
            {"desc": "Papillon\nposé", "color": "#DDA15E", "icon": "🦋"},
        ],
        "difficulty": 2,
    },
    {
        "word": "CLEF",
        "images": [
            {"desc": "Serrure\nancienne", "color": "#FFB703", "icon": "🔐"},
            {"desc": "Trousseau\nde clés", "color": "#FB8500", "icon": "🔑"},
            {"desc": "Porte\nfermée", "color": "#023047", "icon": "🚪"},
            {"desc": "Clé de sol\nmusicale", "color": "#219EBC", "icon": "🎼"},
        ],
        "difficulty": 3,
    },
    {
        "word": "TRAIN",
        "images": [
            {"desc": "Rails\nparallèles", "color": "#6C757D", "icon": "🛤️"},
            {"desc": "Gare\nanimée", "color": "#495057", "icon": "🚉"},
            {"desc": "Locomotive\nà vapeur", "color": "#343A40", "icon": "🚂"},
            {"desc": "Billet\nde voyage", "color": "#212529", "icon": "🎫"},
        ],
        "difficulty": 2,
    },
    {
        "word": "ESPACE",
        "images": [
            {"desc": "Fusée en\ndécollage", "color": "#03045E", "icon": "🚀"},
            {"desc": "Planète\nSaturne", "color": "#0077B6", "icon": "🪐"},
            {"desc": "Astronaute\nen vol", "color": "#00B4D8", "icon": "👨‍🚀"},
            {"desc": "Galaxie\nspirales", "color": "#90E0EF", "icon": "🌌"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PAIN",
        "images": [
            {"desc": "Baguette\ncroustillante", "color": "#D4A373", "icon": "🥖"},
            {"desc": "Four du\nboulanger", "color": "#CCD5AE", "icon": "👨‍🍳"},
            {"desc": "Farine\nblanche", "color": "#E9EDC9", "icon": "🌾"},
            {"desc": "Sandwich\ngarni", "color": "#FEFAE0", "icon": "🥪"},
        ],
        "difficulty": 1,
    },
    {
        "word": "PHOTO",
        "images": [
            {"desc": "Appareil\nreflex", "color": "#264653", "icon": "📷"},
            {"desc": "Album de\nfamille", "color": "#2A9D8F", "icon": "📸"},
            {"desc": "Flash\nlumineux", "color": "#E9C46A", "icon": "💡"},
            {"desc": "Cadre\naccroché", "color": "#F4A261", "icon": "🖼️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "OCEAN",
        "images": [
            {"desc": "Baleine\nbleue", "color": "#03045E", "icon": "🐋"},
            {"desc": "Vagues\ngéantes", "color": "#0077B6", "icon": "🌊"},
            {"desc": "Phare\ncôtier", "color": "#00B4D8", "icon": "🗼"},
            {"desc": "Dauphin\njoueur", "color": "#90E0EF", "icon": "🐬"},
        ],
        "difficulty": 2,
    },
    {
        "word": "CIRQUE",
        "images": [
            {"desc": "Clown\ncoloré", "color": "#E63946", "icon": "🤡"},
            {"desc": "Chapiteau\nrayé", "color": "#F1FAEE", "icon": "🎪"},
            {"desc": "Acrobate\nen l'air", "color": "#A8DADC", "icon": "🤸"},
            {"desc": "Lion\ndompteur", "color": "#457B9D", "icon": "🦁"},
        ],
        "difficulty": 2,
    },
    {
        "word": "ARBRE",
        "images": [
            {"desc": "Feuilles\nvertes", "color": "#2D6A4F", "icon": "🌳"},
            {"desc": "Racines\nprofondes", "color": "#40916C", "icon": "🪵"},
            {"desc": "Pomme\nrouge", "color": "#52B788", "icon": "🍎"},
            {"desc": "Nid\nd'oiseau", "color": "#74C69D", "icon": "🪺"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MAGIE",
        "images": [
            {"desc": "Chapeau\nhaut-de-forme", "color": "#7B2CBF", "icon": "🎩"},
            {"desc": "Baguette\nétoilée", "color": "#9D4EDD", "icon": "🪄"},
            {"desc": "Lapin\nblanc", "color": "#C77DFF", "icon": "🐇"},
            {"desc": "Cartes à\njouer", "color": "#E0AAFF", "icon": "🃏"},
        ],
        "difficulty": 2,
    },
    {
        "word": "SPORT",
        "images": [
            {"desc": "Ballon de\nfoot", "color": "#06D6A0", "icon": "⚽"},
            {"desc": "Médaille\nd'or", "color": "#FFD166", "icon": "🏅"},
            {"desc": "Baskets\nde course", "color": "#EF476F", "icon": "👟"},
            {"desc": "Stade\nolympique", "color": "#118AB2", "icon": "🏟️"},
        ],
        "difficulty": 1,
    },
    {
        "word": "FILM",
        "images": [
            {"desc": "Pellicule\ncinéma", "color": "#212529", "icon": "🎬"},
            {"desc": "Pop-corn\nbeurré", "color": "#343A40", "icon": "🍿"},
            {"desc": "Siège de\ncinéma", "color": "#495057", "icon": "💺"},
            {"desc": "Oscar\ndoré", "color": "#6C757D", "icon": "🏆"},
        ],
        "difficulty": 2,
    },
    {
        "word": "BÉBÉ",
        "images": [
            {"desc": "Biberon\nde lait", "color": "#FFCAD4", "icon": "🍼"},
            {"desc": "Hochet\ncoloré", "color": "#F4ACB7", "icon": "🧸"},
            {"desc": "Couches\nblanches", "color": "#FFE5D9", "icon": "👶"},
            {"desc": "Poussette\npliable", "color": "#D8E2DC", "icon": "🧒"},
        ],
        "difficulty": 1,
    },
    {
        "word": "PIRATE",
        "images": [
            {"desc": "Trésor et\ncoffre", "color": "#774936", "icon": "💰"},
            {"desc": "Perroquet\ncoloré", "color": "#E76F51", "icon": "🦜"},
            {"desc": "Bateau à\nvoiles", "color": "#264653", "icon": "🏴‍☠️"},
            {"desc": "Carte au\ntrésor", "color": "#DDA15E", "icon": "🗺️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PLUIE",
        "images": [
            {"desc": "Parapluie\nouvert", "color": "#457B9D", "icon": "☂️"},
            {"desc": "Gouttes\nqui tombent", "color": "#A8DADC", "icon": "🌧️"},
            {"desc": "Flaque\nd'eau", "color": "#1D3557", "icon": "💧"},
            {"desc": "Arc-en-\nciel", "color": "#F1FAEE", "icon": "🌈"},
        ],
        "difficulty": 1,
    },
    # --- Nouveaux puzzles ---
    # FACILE (difficulty 1)
    {
        "word": "EAU",
        "images": [
            {"desc": "Rivière\nlimpide", "color": "#48CAE4", "icon": "🏞️"},
            {"desc": "Verre\nrempli", "color": "#90E0EF", "icon": "🥤"},
            {"desc": "Cascade\npuissante", "color": "#0077B6", "icon": "💧"},
            {"desc": "Robinet\nqui coule", "color": "#023E8A", "icon": "🚿"},
        ],
        "difficulty": 1,
    },
    {
        "word": "FLEUR",
        "images": [
            {"desc": "Bouquet\ncoloré", "color": "#FF69B4", "icon": "💐"},
            {"desc": "Abeille\nbutinant", "color": "#FFD700", "icon": "🐝"},
            {"desc": "Pétales\nde rose", "color": "#E63946", "icon": "🌹"},
            {"desc": "Pot de\nfleurs", "color": "#2D6A4F", "icon": "🌷"},
        ],
        "difficulty": 1,
    },
    {
        "word": "CHIEN",
        "images": [
            {"desc": "Os à\nmâcher", "color": "#D4A373", "icon": "🦴"},
            {"desc": "Laisse de\npromenade", "color": "#606C38", "icon": "🐕"},
            {"desc": "Niche en\nbois", "color": "#8B4513", "icon": "🏠"},
            {"desc": "Balle\nde jeu", "color": "#EF476F", "icon": "🎾"},
        ],
        "difficulty": 1,
    },
    {
        "word": "NEIGE",
        "images": [
            {"desc": "Station\nde ski", "color": "#CAF0F8", "icon": "⛷️"},
            {"desc": "Luge\nrapide", "color": "#90E0EF", "icon": "🛷"},
            {"desc": "Flocons\nblancs", "color": "#48CAE4", "icon": "❄️"},
            {"desc": "Igloo\npolaire", "color": "#0096C7", "icon": "🏔️"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MER",
        "images": [
            {"desc": "Bateau à\nvoiles", "color": "#0077B6", "icon": "⛵"},
            {"desc": "Poisson\ncoloré", "color": "#00B4D8", "icon": "🐟"},
            {"desc": "Ancre\nmarine", "color": "#023E8A", "icon": "⚓"},
            {"desc": "Vagues\nbleues", "color": "#48CAE4", "icon": "🌊"},
        ],
        "difficulty": 1,
    },
    {
        "word": "FRUIT",
        "images": [
            {"desc": "Panier de\nfruits", "color": "#06D6A0", "icon": "🧺"},
            {"desc": "Pomme\nverte", "color": "#52B788", "icon": "🍏"},
            {"desc": "Banane\njaune", "color": "#FFD166", "icon": "🍌"},
            {"desc": "Orange\njuteuse", "color": "#F4A261", "icon": "🍊"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MAISON",
        "images": [
            {"desc": "Toit\nrouge", "color": "#E63946", "icon": "🏠"},
            {"desc": "Fenêtre\nouverte", "color": "#457B9D", "icon": "🪟"},
            {"desc": "Cheminée\nqui fume", "color": "#6C757D", "icon": "🏡"},
            {"desc": "Porte\nd'entrée", "color": "#8B4513", "icon": "🚪"},
        ],
        "difficulty": 1,
    },
    {
        "word": "LUNE",
        "images": [
            {"desc": "Croissant\nargent", "color": "#240046", "icon": "🌙"},
            {"desc": "Loup qui\nhurle", "color": "#3C096C", "icon": "🐺"},
            {"desc": "Cratères\nlunaires", "color": "#6C757D", "icon": "🌕"},
            {"desc": "Marée\nhaute", "color": "#0077B6", "icon": "🌊"},
        ],
        "difficulty": 1,
    },
    {
        "word": "OISEAU",
        "images": [
            {"desc": "Nid avec\ndes œufs", "color": "#606C38", "icon": "🪺"},
            {"desc": "Plumes\ncolorées", "color": "#2A9D8F", "icon": "🪶"},
            {"desc": "Ailes\ndéployées", "color": "#48CAE4", "icon": "🦅"},
            {"desc": "Chant\nmélodieux", "color": "#FFD166", "icon": "🐦"},
        ],
        "difficulty": 1,
    },
    {
        "word": "BONBON",
        "images": [
            {"desc": "Sucette\nronde", "color": "#EF476F", "icon": "🍭"},
            {"desc": "Sachet\ncoloré", "color": "#FFD166", "icon": "🍬"},
            {"desc": "Chocolat\nfondant", "color": "#8B4513", "icon": "🍫"},
            {"desc": "Réglisse\nnoire", "color": "#212529", "icon": "🖤"},
        ],
        "difficulty": 1,
    },
    {
        "word": "ETOILE",
        "images": [
            {"desc": "Ciel de\nnuit", "color": "#10002B", "icon": "✨"},
            {"desc": "Étoile\nfilante", "color": "#240046", "icon": "🌠"},
            {"desc": "Sapin de\nNoël", "color": "#2D6A4F", "icon": "🎄"},
            {"desc": "Étoile de\nmer", "color": "#F4A261", "icon": "⭐"},
        ],
        "difficulty": 1,
    },
    {
        "word": "COEUR",
        "images": [
            {"desc": "Valentin\nrouge", "color": "#E63946", "icon": "❤️"},
            {"desc": "Chocolats\nen boîte", "color": "#8B4513", "icon": "🍫"},
            {"desc": "Stéthoscope\nmédical", "color": "#457B9D", "icon": "🩺"},
            {"desc": "Carte\nd'amour", "color": "#FFCAD4", "icon": "💌"},
        ],
        "difficulty": 1,
    },
    {
        "word": "ROI",
        "images": [
            {"desc": "Couronne\ndorée", "color": "#FFD700", "icon": "👑"},
            {"desc": "Trône\nroyal", "color": "#7B2CBF", "icon": "🪑"},
            {"desc": "Château\nfort", "color": "#6C757D", "icon": "🏰"},
            {"desc": "Cape\nrouge", "color": "#E63946", "icon": "🧥"},
        ],
        "difficulty": 1,
    },
    {
        "word": "GLACE",
        "images": [
            {"desc": "Cornet\nvanille", "color": "#FEFAE0", "icon": "🍦"},
            {"desc": "Patinoire\ngelée", "color": "#48CAE4", "icon": "⛸️"},
            {"desc": "Glaçon\ntransparent", "color": "#90E0EF", "icon": "🧊"},
            {"desc": "Miroir\ngelé", "color": "#CAF0F8", "icon": "🪞"},
        ],
        "difficulty": 1,
    },
    {
        "word": "AVION",
        "images": [
            {"desc": "Aéroport\nanimé", "color": "#264653", "icon": "🛫"},
            {"desc": "Nuages\nblancs", "color": "#CAF0F8", "icon": "☁️"},
            {"desc": "Valise de\nvoyage", "color": "#E9C46A", "icon": "🧳"},
            {"desc": "Hublot\nrond", "color": "#457B9D", "icon": "✈️"},
        ],
        "difficulty": 1,
    },
    {
        "word": "CADEAU",
        "images": [
            {"desc": "Ruban\nrouge", "color": "#E63946", "icon": "🎀"},
            {"desc": "Papier\ndoré", "color": "#FFD700", "icon": "🎁"},
            {"desc": "Sapin de\nNoël", "color": "#2D6A4F", "icon": "🎄"},
            {"desc": "Surprise\njoyeuse", "color": "#7B2CBF", "icon": "🎉"},
        ],
        "difficulty": 1,
    },
    # MOYEN (difficulty 2)
    {
        "word": "VOYAGE",
        "images": [
            {"desc": "Carte du\nmonde", "color": "#264653", "icon": "🗺️"},
            {"desc": "Passeport\ntamponné", "color": "#2A9D8F", "icon": "🛂"},
            {"desc": "Valise\nouverte", "color": "#E9C46A", "icon": "🧳"},
            {"desc": "Avion en\nvol", "color": "#48CAE4", "icon": "✈️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "CUISINE",
        "images": [
            {"desc": "Casserole\nchaude", "color": "#E63946", "icon": "🍳"},
            {"desc": "Tablier de\ncuisinier", "color": "#F1FAEE", "icon": "👨‍🍳"},
            {"desc": "Couteau\naiguisé", "color": "#6C757D", "icon": "🔪"},
            {"desc": "Recette\nécriture", "color": "#DDA15E", "icon": "📋"},
        ],
        "difficulty": 2,
    },
    {
        "word": "ORANGE",
        "images": [
            {"desc": "Agrume\njuteux", "color": "#F4A261", "icon": "🍊"},
            {"desc": "Coucher\nde soleil", "color": "#FF6B35", "icon": "🌅"},
            {"desc": "Citrouille\nronde", "color": "#E76F51", "icon": "🎃"},
            {"desc": "Carotte\ncroquante", "color": "#FB8500", "icon": "🥕"},
        ],
        "difficulty": 2,
    },
    {
        "word": "NATURE",
        "images": [
            {"desc": "Forêt\ndense", "color": "#2D6A4F", "icon": "🌲"},
            {"desc": "Lac\npaisible", "color": "#0077B6", "icon": "🏞️"},
            {"desc": "Papillon\nvolant", "color": "#FFD166", "icon": "🦋"},
            {"desc": "Cerf dans\nla forêt", "color": "#606C38", "icon": "🦌"},
        ],
        "difficulty": 2,
    },
    {
        "word": "DESERT",
        "images": [
            {"desc": "Dunes de\nsable", "color": "#DDA15E", "icon": "🏜️"},
            {"desc": "Cactus\népineux", "color": "#606C38", "icon": "🌵"},
            {"desc": "Chameau\npatient", "color": "#D4A373", "icon": "🐪"},
            {"desc": "Oasis\nverdoyante", "color": "#2A9D8F", "icon": "🏝️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "MUSEE",
        "images": [
            {"desc": "Tableau\ncélèbre", "color": "#7B2CBF", "icon": "🖼️"},
            {"desc": "Statue\nantique", "color": "#6C757D", "icon": "🗿"},
            {"desc": "Gardien\nsilencieux", "color": "#264653", "icon": "🧑‍💼"},
            {"desc": "Audio\nguide", "color": "#457B9D", "icon": "🎧"},
        ],
        "difficulty": 2,
    },
    {
        "word": "ROBOT",
        "images": [
            {"desc": "Bras\nmécanique", "color": "#6C757D", "icon": "🦾"},
            {"desc": "Circuit\nélectronique", "color": "#2A9D8F", "icon": "🔌"},
            {"desc": "Écran\nlumineux", "color": "#48CAE4", "icon": "🖥️"},
            {"desc": "Engrenages\nmétal", "color": "#495057", "icon": "🤖"},
        ],
        "difficulty": 2,
    },
    {
        "word": "FANTOME",
        "images": [
            {"desc": "Drap\nblanc", "color": "#F1FAEE", "icon": "👻"},
            {"desc": "Maison\nhantée", "color": "#3C096C", "icon": "🏚️"},
            {"desc": "Nuit\nsombre", "color": "#10002B", "icon": "🌑"},
            {"desc": "Bougie\ntremblante", "color": "#FFB703", "icon": "🕯️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "MUSEE",
        "images": [
            {"desc": "Tableau\ncélèbre", "color": "#7B2CBF", "icon": "🖼️"},
            {"desc": "Statue\nantique", "color": "#6C757D", "icon": "🗿"},
            {"desc": "Gardien\nsilencieux", "color": "#264653", "icon": "🧑‍💼"},
            {"desc": "Audio\nguide", "color": "#457B9D", "icon": "🎧"},
        ],
        "difficulty": 2,
    },
    {
        "word": "JUNGLE",
        "images": [
            {"desc": "Lianes\népaisses", "color": "#2D6A4F", "icon": "🌿"},
            {"desc": "Singe\nmalin", "color": "#606C38", "icon": "🐒"},
            {"desc": "Perroquet\nvif", "color": "#E63946", "icon": "🦜"},
            {"desc": "Tigre\nrayé", "color": "#F4A261", "icon": "🐯"},
        ],
        "difficulty": 2,
    },
    {
        "word": "CHATEAU",
        "images": [
            {"desc": "Tour\nmédiévale", "color": "#6C757D", "icon": "🏰"},
            {"desc": "Pont-levis\nen bois", "color": "#8B4513", "icon": "🌉"},
            {"desc": "Chevalier\nen armure", "color": "#495057", "icon": "⚔️"},
            {"desc": "Drapeau au\nsommet", "color": "#E63946", "icon": "🏳️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "MEDECIN",
        "images": [
            {"desc": "Blouse\nblanche", "color": "#F1FAEE", "icon": "🥼"},
            {"desc": "Stéthoscope\nmédical", "color": "#457B9D", "icon": "🩺"},
            {"desc": "Seringue\nstérile", "color": "#48CAE4", "icon": "💉"},
            {"desc": "Ambulance\nurgente", "color": "#E63946", "icon": "🚑"},
        ],
        "difficulty": 2,
    },
    {
        "word": "DRAGON",
        "images": [
            {"desc": "Flammes\ncrachées", "color": "#FF4800", "icon": "🔥"},
            {"desc": "Ailes\ngéantes", "color": "#2D6A4F", "icon": "🐉"},
            {"desc": "Grotte\nsombre", "color": "#343A40", "icon": "🕳️"},
            {"desc": "Écailles\nbrillantes", "color": "#7B2CBF", "icon": "✨"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PAPIER",
        "images": [
            {"desc": "Feuille\nblanche", "color": "#F1FAEE", "icon": "📄"},
            {"desc": "Origami\ngrue", "color": "#E63946", "icon": "🦢"},
            {"desc": "Journal\ndu matin", "color": "#6C757D", "icon": "📰"},
            {"desc": "Ciseaux\nqui coupent", "color": "#495057", "icon": "✂️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "POLICE",
        "images": [
            {"desc": "Sirène\nbleue", "color": "#0077B6", "icon": "🚨"},
            {"desc": "Badge\ndoré", "color": "#FFD700", "icon": "🪪"},
            {"desc": "Menottes\nmétal", "color": "#6C757D", "icon": "⛓️"},
            {"desc": "Voiture\npatrouille", "color": "#264653", "icon": "🚔"},
        ],
        "difficulty": 2,
    },
    {
        "word": "FORET",
        "images": [
            {"desc": "Sentier\nombragé", "color": "#2D6A4F", "icon": "🌲"},
            {"desc": "Champignon\nrouge", "color": "#E63946", "icon": "🍄"},
            {"desc": "Écureuil\nmalin", "color": "#D4A373", "icon": "🐿️"},
            {"desc": "Mousse\nverte", "color": "#40916C", "icon": "🌿"},
        ],
        "difficulty": 2,
    },
    {
        "word": "FERME",
        "images": [
            {"desc": "Tracteur\nrouge", "color": "#E63946", "icon": "🚜"},
            {"desc": "Poule et\nses œufs", "color": "#D4A373", "icon": "🐔"},
            {"desc": "Champs de\nblé", "color": "#FFD166", "icon": "🌾"},
            {"desc": "Grange en\nbois", "color": "#8B4513", "icon": "🏚️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PIRATE",
        "images": [
            {"desc": "Trésor et\ncoffre", "color": "#774936", "icon": "💰"},
            {"desc": "Perroquet\ncoloré", "color": "#E76F51", "icon": "🦜"},
            {"desc": "Bateau à\nvoiles", "color": "#264653", "icon": "🏴‍☠️"},
            {"desc": "Carte au\ntrésor", "color": "#DDA15E", "icon": "🗺️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "MUSIQUE",
        "images": [
            {"desc": "Violon\nclassique", "color": "#8B4513", "icon": "🎻"},
            {"desc": "Batterie\nrock", "color": "#343A40", "icon": "🥁"},
            {"desc": "Micro sur\nscène", "color": "#7B2CBF", "icon": "🎤"},
            {"desc": "Partition\nmusicale", "color": "#F1FAEE", "icon": "🎼"},
        ],
        "difficulty": 1,
    },
    {
        "word": "VOLCAN",
        "images": [
            {"desc": "Lave\nincandescente", "color": "#FF4800", "icon": "🌋"},
            {"desc": "Cendres\nvolcaniques", "color": "#6C757D", "icon": "🌫️"},
            {"desc": "Île\ntropicale", "color": "#2D6A4F", "icon": "🏝️"},
            {"desc": "Fumée\népaisse", "color": "#495057", "icon": "💨"},
        ],
        "difficulty": 2,
    },
    {
        "word": "ANNIVERSAIRE",
        "images": [
            {"desc": "Gâteau à\nbougies", "color": "#EF476F", "icon": "🎂"},
            {"desc": "Ballons\ncolorés", "color": "#FFD166", "icon": "🎈"},
            {"desc": "Confettis\nen l'air", "color": "#7B2CBF", "icon": "🎉"},
            {"desc": "Cadeaux\nemballés", "color": "#06D6A0", "icon": "🎁"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PONT",
        "images": [
            {"desc": "Arches de\npierre", "color": "#6C757D", "icon": "🌉"},
            {"desc": "Rivière\nen dessous", "color": "#0077B6", "icon": "🏞️"},
            {"desc": "Câbles\ntendus", "color": "#495057", "icon": "🔗"},
            {"desc": "Bateau\nqui passe", "color": "#264653", "icon": "🚢"},
        ],
        "difficulty": 2,
    },
    {
        "word": "PLUME",
        "images": [
            {"desc": "Oiseau\ncoloré", "color": "#2A9D8F", "icon": "🐦"},
            {"desc": "Encrier\nancien", "color": "#264653", "icon": "🖋️"},
            {"desc": "Oreiller\nmoelleux", "color": "#F1FAEE", "icon": "🛏️"},
            {"desc": "Légèreté\naérienne", "color": "#CAF0F8", "icon": "🪶"},
        ],
        "difficulty": 2,
    },
    # DIFFICILE (difficulty 3)
    {
        "word": "SILENCE",
        "images": [
            {"desc": "Bibliothèque\ncalme", "color": "#264653", "icon": "📚"},
            {"desc": "Doigt sur\nla bouche", "color": "#F4ACB7", "icon": "🤫"},
            {"desc": "Temple\nzen", "color": "#606C38", "icon": "🏯"},
            {"desc": "Nuit\nétoilée", "color": "#10002B", "icon": "🌌"},
        ],
        "difficulty": 3,
    },
    {
        "word": "HASARD",
        "images": [
            {"desc": "Dés qui\nroulent", "color": "#E63946", "icon": "🎲"},
            {"desc": "Tirage au\nsort", "color": "#7B2CBF", "icon": "🎰"},
            {"desc": "Trèfle à\nquatre", "color": "#2D6A4F", "icon": "🍀"},
            {"desc": "Pile ou\nface", "color": "#FFD700", "icon": "🪙"},
        ],
        "difficulty": 3,
    },
    {
        "word": "VITESSE",
        "images": [
            {"desc": "Compteur\nau max", "color": "#E63946", "icon": "🏎️"},
            {"desc": "Guépard\nqui court", "color": "#F4A261", "icon": "🐆"},
            {"desc": "Fusée en\nvol", "color": "#264653", "icon": "🚀"},
            {"desc": "Chrono\nqui tourne", "color": "#FFD166", "icon": "⏱️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "LIBERTE",
        "images": [
            {"desc": "Oiseau en\nvol", "color": "#48CAE4", "icon": "🕊️"},
            {"desc": "Chaînes\nbrisées", "color": "#6C757D", "icon": "⛓️"},
            {"desc": "Statue de\nla liberté", "color": "#06D6A0", "icon": "🗽"},
            {"desc": "Ciel\nimmense", "color": "#90E0EF", "icon": "☁️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "REVE",
        "images": [
            {"desc": "Nuages\ncotonneux", "color": "#CAF0F8", "icon": "☁️"},
            {"desc": "Oreiller\nmoelleux", "color": "#F1FAEE", "icon": "😴"},
            {"desc": "Bulle de\npensée", "color": "#7B2CBF", "icon": "💭"},
            {"desc": "Lune\nbrillante", "color": "#240046", "icon": "🌙"},
        ],
        "difficulty": 3,
    },
    {
        "word": "MEMOIRE",
        "images": [
            {"desc": "Album\nphoto", "color": "#8B4513", "icon": "📸"},
            {"desc": "Cerveau\nhumain", "color": "#EF476F", "icon": "🧠"},
            {"desc": "Journal\nintime", "color": "#7B2CBF", "icon": "📓"},
            {"desc": "Clé USB\nbleue", "color": "#0077B6", "icon": "💾"},
        ],
        "difficulty": 3,
    },
    {
        "word": "COURAGE",
        "images": [
            {"desc": "Lion\nmajestueux", "color": "#F4A261", "icon": "🦁"},
            {"desc": "Pompier\nhéroïque", "color": "#E63946", "icon": "🧑‍🚒"},
            {"desc": "Épée\nmédiévale", "color": "#6C757D", "icon": "⚔️"},
            {"desc": "Montagne\nescaladée", "color": "#264653", "icon": "🧗"},
        ],
        "difficulty": 3,
    },
    {
        "word": "SAISON",
        "images": [
            {"desc": "Feuille\nd'automne", "color": "#F4A261", "icon": "🍂"},
            {"desc": "Flocon\nd'hiver", "color": "#CAF0F8", "icon": "❄️"},
            {"desc": "Fleur de\nprintemps", "color": "#EF476F", "icon": "🌸"},
            {"desc": "Soleil\nd'été", "color": "#FFD166", "icon": "☀️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "ENIGME",
        "images": [
            {"desc": "Point\nd'interrogation", "color": "#7B2CBF", "icon": "❓"},
            {"desc": "Puzzle\nincomplet", "color": "#2A9D8F", "icon": "🧩"},
            {"desc": "Loupe de\ndétective", "color": "#FFD700", "icon": "🔍"},
            {"desc": "Coffre\nfermé", "color": "#8B4513", "icon": "🔐"},
        ],
        "difficulty": 3,
    },
    {
        "word": "HORIZON",
        "images": [
            {"desc": "Coucher de\nsoleil", "color": "#FF6B35", "icon": "🌅"},
            {"desc": "Mer au\nloin", "color": "#0077B6", "icon": "🌊"},
            {"desc": "Route\ninfinie", "color": "#6C757D", "icon": "🛣️"},
            {"desc": "Plaine\nimmense", "color": "#606C38", "icon": "🌾"},
        ],
        "difficulty": 3,
    },
    {
        "word": "OMBRE",
        "images": [
            {"desc": "Silhouette\nnoire", "color": "#212529", "icon": "🕴️"},
            {"desc": "Soleil\nderrière", "color": "#FFD166", "icon": "☀️"},
            {"desc": "Mur avec\nune ombre", "color": "#495057", "icon": "🏗️"},
            {"desc": "Cadran\nsolaire", "color": "#6C757D", "icon": "🕐"},
        ],
        "difficulty": 3,
    },
    {
        "word": "PARFUM",
        "images": [
            {"desc": "Flacon\nélégant", "color": "#7B2CBF", "icon": "🧴"},
            {"desc": "Rose\nparfumée", "color": "#EF476F", "icon": "🌹"},
            {"desc": "Nez qui\nrenifle", "color": "#F4ACB7", "icon": "👃"},
            {"desc": "Lavande\nen champ", "color": "#9D4EDD", "icon": "💜"},
        ],
        "difficulty": 3,
    },
    {
        "word": "MARCHE",
        "images": [
            {"desc": "Étals de\nlégumes", "color": "#2D6A4F", "icon": "🥕"},
            {"desc": "Pas après\npas", "color": "#6C757D", "icon": "🚶"},
            {"desc": "Escalier\nqui monte", "color": "#495057", "icon": "🪜"},
            {"desc": "Foule\nanimée", "color": "#E9C46A", "icon": "👥"},
        ],
        "difficulty": 3,
    },
    {
        "word": "JUSTICE",
        "images": [
            {"desc": "Balance\néquilibrée", "color": "#FFD700", "icon": "⚖️"},
            {"desc": "Marteau du\njuge", "color": "#8B4513", "icon": "🔨"},
            {"desc": "Bandeau\nsur les yeux", "color": "#6C757D", "icon": "🫣"},
            {"desc": "Tribunal\nimposant", "color": "#264653", "icon": "🏛️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "POISSON",
        "images": [
            {"desc": "Aquarium\ncoloré", "color": "#00B4D8", "icon": "🐠"},
            {"desc": "Canne à\npêche", "color": "#606C38", "icon": "🎣"},
            {"desc": "Sushi\nfrais", "color": "#F1FAEE", "icon": "🍣"},
            {"desc": "Récif de\ncorail", "color": "#EF476F", "icon": "🐡"},
        ],
        "difficulty": 1,
    },
    {
        "word": "MONTAGNE",
        "images": [
            {"desc": "Ski\nalpin", "color": "#CAF0F8", "icon": "⛷️"},
            {"desc": "Sommet\nrocheux", "color": "#6C757D", "icon": "🏔️"},
            {"desc": "Marmotte\ncurieuse", "color": "#D4A373", "icon": "🐿️"},
            {"desc": "Cascade\nen hauteur", "color": "#0077B6", "icon": "💧"},
        ],
        "difficulty": 2,
    },
    {
        "word": "LETTRE",
        "images": [
            {"desc": "Enveloppe\ncachetée", "color": "#F4A261", "icon": "✉️"},
            {"desc": "Boîte aux\nlettres", "color": "#E63946", "icon": "📮"},
            {"desc": "Timbre\ncoloré", "color": "#7B2CBF", "icon": "📬"},
            {"desc": "Plume et\nencre", "color": "#264653", "icon": "🖋️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "SABLE",
        "images": [
            {"desc": "Château de\nsable", "color": "#DDA15E", "icon": "🏖️"},
            {"desc": "Sablier\nancien", "color": "#D4A373", "icon": "⏳"},
            {"desc": "Désert\nimmense", "color": "#F4A261", "icon": "🏜️"},
            {"desc": "Dune\ndorée", "color": "#FFD166", "icon": "🌅"},
        ],
        "difficulty": 2,
    },
    {
        "word": "SOURIRE",
        "images": [
            {"desc": "Visage\nheureux", "color": "#FFD166", "icon": "😊"},
            {"desc": "Photo de\ngroupe", "color": "#2A9D8F", "icon": "📸"},
            {"desc": "Clown\namusant", "color": "#EF476F", "icon": "🤡"},
            {"desc": "Soleil\nradieux", "color": "#FF6B35", "icon": "☀️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "TRESOR",
        "images": [
            {"desc": "Coffre\nancien", "color": "#8B4513", "icon": "💰"},
            {"desc": "Pièces\nd'or", "color": "#FFD700", "icon": "🪙"},
            {"desc": "Carte au\ntrésor", "color": "#DDA15E", "icon": "🗺️"},
            {"desc": "Diamant\nbrillant", "color": "#48CAE4", "icon": "💎"},
        ],
        "difficulty": 2,
    },
    {
        "word": "CHAPEAU",
        "images": [
            {"desc": "Haut-de-\nforme noir", "color": "#212529", "icon": "🎩"},
            {"desc": "Casquette\nde sport", "color": "#E63946", "icon": "🧢"},
            {"desc": "Sombrero\nmexicain", "color": "#F4A261", "icon": "👒"},
            {"desc": "Bonnet\nd'hiver", "color": "#0077B6", "icon": "🧶"},
        ],
        "difficulty": 2,
    },
    {
        "word": "MIROIR",
        "images": [
            {"desc": "Reflet\nparfait", "color": "#CAF0F8", "icon": "🪞"},
            {"desc": "Salle de\nbain", "color": "#F1FAEE", "icon": "🚿"},
            {"desc": "Lac\ntranquille", "color": "#0077B6", "icon": "🏞️"},
            {"desc": "Kaléido\nscope", "color": "#7B2CBF", "icon": "🔮"},
        ],
        "difficulty": 3,
    },
    {
        "word": "CIEL",
        "images": [
            {"desc": "Nuages\nblancs", "color": "#90E0EF", "icon": "☁️"},
            {"desc": "Arc-en-\nciel", "color": "#FFD166", "icon": "🌈"},
            {"desc": "Avion\nen vol", "color": "#48CAE4", "icon": "✈️"},
            {"desc": "Étoiles\nla nuit", "color": "#10002B", "icon": "⭐"},
        ],
        "difficulty": 1,
    },
    {
        "word": "HERBE",
        "images": [
            {"desc": "Pelouse\nverte", "color": "#52B788", "icon": "🌿"},
            {"desc": "Tondeuse\nqui coupe", "color": "#40916C", "icon": "🌱"},
            {"desc": "Sauterelle\nverte", "color": "#2D6A4F", "icon": "🦗"},
            {"desc": "Rosée du\nmatin", "color": "#74C69D", "icon": "💧"},
        ],
        "difficulty": 1,
    },
    {
        "word": "CAMION",
        "images": [
            {"desc": "Remorque\nénorme", "color": "#264653", "icon": "🚛"},
            {"desc": "Route\nautoroutière", "color": "#6C757D", "icon": "🛣️"},
            {"desc": "Klaxon\npuissant", "color": "#E63946", "icon": "📢"},
            {"desc": "Chargement\nlourd", "color": "#495057", "icon": "📦"},
        ],
        "difficulty": 1,
    },
    {
        "word": "TIGRE",
        "images": [
            {"desc": "Rayures\norangées", "color": "#F4A261", "icon": "🐯"},
            {"desc": "Jungle\népaisse", "color": "#2D6A4F", "icon": "🌿"},
            {"desc": "Griffes\nacérées", "color": "#E63946", "icon": "🐾"},
            {"desc": "Regard\nperçant", "color": "#FFD700", "icon": "👁️"},
        ],
        "difficulty": 1,
    },
    {
        "word": "PIRATE",
        "images": [
            {"desc": "Bandeau\nsur l'œil", "color": "#212529", "icon": "🏴‍☠️"},
            {"desc": "Trésor\nenfoui", "color": "#FFD700", "icon": "💰"},
            {"desc": "Île\ndéserte", "color": "#2D6A4F", "icon": "🏝️"},
            {"desc": "Sabre\nd'abordage", "color": "#6C757D", "icon": "⚔️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "VOIX",
        "images": [
            {"desc": "Micro\nsur scène", "color": "#7B2CBF", "icon": "🎤"},
            {"desc": "Ondes\nsonores", "color": "#48CAE4", "icon": "🔊"},
            {"desc": "Chorale\nqui chante", "color": "#E9C46A", "icon": "🎶"},
            {"desc": "Gorge\nhumaine", "color": "#F4ACB7", "icon": "🗣️"},
        ],
        "difficulty": 3,
    },
    {
        "word": "DANGER",
        "images": [
            {"desc": "Panneau\ntriangulaire", "color": "#E63946", "icon": "⚠️"},
            {"desc": "Crâne et\nos croisés", "color": "#212529", "icon": "☠️"},
            {"desc": "Éclair\nélectrique", "color": "#FFD700", "icon": "⚡"},
            {"desc": "Falaise\nabrupte", "color": "#6C757D", "icon": "🏔️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "DRAPEAU",
        "images": [
            {"desc": "Mât\nmétallique", "color": "#6C757D", "icon": "🏳️"},
            {"desc": "Pays du\nmonde", "color": "#264653", "icon": "🌍"},
            {"desc": "Course\nautomobile", "color": "#212529", "icon": "🏁"},
            {"desc": "Vent qui\nsouffle", "color": "#48CAE4", "icon": "🌬️"},
        ],
        "difficulty": 2,
    },
    {
        "word": "NOIR",
        "images": [
            {"desc": "Nuit sans\nlune", "color": "#10002B", "icon": "🌑"},
            {"desc": "Chat\nnoir", "color": "#212529", "icon": "🐈‍⬛"},
            {"desc": "Café\nsans lait", "color": "#3C096C", "icon": "☕"},
            {"desc": "Costume\nélégant", "color": "#343A40", "icon": "🤵"},
        ],
        "difficulty": 1,
    },
    {
        "word": "PORTE",
        "images": [
            {"desc": "Poignée\ndorée", "color": "#FFD700", "icon": "🚪"},
            {"desc": "Serrure à\nclé", "color": "#6C757D", "icon": "🔐"},
            {"desc": "Sonnette\nqui sonne", "color": "#E63946", "icon": "🔔"},
            {"desc": "Paillasson\nd'entrée", "color": "#8B4513", "icon": "🏠"},
        ],
        "difficulty": 1,
    },
    {
        "word": "NUAGE",
        "images": [
            {"desc": "Ciel\ncotonneux", "color": "#CAF0F8", "icon": "☁️"},
            {"desc": "Avion au\ndessus", "color": "#48CAE4", "icon": "✈️"},
            {"desc": "Pluie qui\ntombe", "color": "#457B9D", "icon": "🌧️"},
            {"desc": "Forme\namusante", "color": "#90E0EF", "icon": "🤔"},
        ],
        "difficulty": 1,
    },
    {
        "word": "METAL",
        "images": [
            {"desc": "Engrenages\nen acier", "color": "#6C757D", "icon": "⚙️"},
            {"desc": "Guitare\nélectrique", "color": "#212529", "icon": "🎸"},
            {"desc": "Armure\nmédiévale", "color": "#495057", "icon": "🛡️"},
            {"desc": "Lingot\nd'or", "color": "#FFD700", "icon": "🏅"},
        ],
        "difficulty": 3,
    },
    {
        "word": "MUSIQUE",
        "images": [
            {"desc": "Trompette\ndorée", "color": "#FFD700", "icon": "🎺"},
            {"desc": "Disque\nvinyle", "color": "#212529", "icon": "💿"},
            {"desc": "Danseurs\nen rythme", "color": "#EF476F", "icon": "💃"},
            {"desc": "Concert\nen plein air", "color": "#7B2CBF", "icon": "🎵"},
        ],
        "difficulty": 1,
    },
]
