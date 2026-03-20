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
]
