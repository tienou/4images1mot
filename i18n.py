"""
Système d'internationalisation pour 4 Images 1 Mot.
"""

LANGUAGES = {
    "fr": "Français",
    "en": "English",
    "es": "Español",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
}

UI_STRINGS = {
    "fr": {
        "title": "4 Images 1 Mot",
        "score": "Score",
        "level": "Niveau",
        "hint": "Indice (-50pts)",
        "skip": "Passer",
        "clear": "Effacer",
        "bravo": "Bravo ! +{pts} points",
        "wrong": "Essaie encore !",
        "answer_was": "La réponse était : {word}",
        "congrats": "Félicitations !",
        "final_score": "Score final : {score} points",
        "completed": "Tu as complété les {total} niveaux !",
        "replay": "Rejouer",
        "select_lang": "Langue",
    },
    "en": {
        "title": "4 Pics 1 Word",
        "score": "Score",
        "level": "Level",
        "hint": "Hint (-50pts)",
        "skip": "Skip",
        "clear": "Clear",
        "bravo": "Well done! +{pts} points",
        "wrong": "Try again!",
        "answer_was": "The answer was: {word}",
        "congrats": "Congratulations!",
        "final_score": "Final score: {score} points",
        "completed": "You completed all {total} levels!",
        "replay": "Play again",
        "select_lang": "Language",
    },
    "es": {
        "title": "4 Fotos 1 Palabra",
        "score": "Puntos",
        "level": "Nivel",
        "hint": "Pista (-50pts)",
        "skip": "Saltar",
        "clear": "Borrar",
        "bravo": "¡Bravo! +{pts} puntos",
        "wrong": "¡Inténtalo de nuevo!",
        "answer_was": "La respuesta era: {word}",
        "congrats": "¡Felicidades!",
        "final_score": "Puntuación final: {score} puntos",
        "completed": "¡Has completado los {total} niveles!",
        "replay": "Jugar de nuevo",
        "select_lang": "Idioma",
    },
    "de": {
        "title": "4 Bilder 1 Wort",
        "score": "Punkte",
        "level": "Level",
        "hint": "Hinweis (-50Pkt)",
        "skip": "Überspringen",
        "clear": "Löschen",
        "bravo": "Super! +{pts} Punkte",
        "wrong": "Versuch es nochmal!",
        "answer_was": "Die Antwort war: {word}",
        "congrats": "Herzlichen Glückwunsch!",
        "final_score": "Endpunktzahl: {score} Punkte",
        "completed": "Du hast alle {total} Level geschafft!",
        "replay": "Nochmal spielen",
        "select_lang": "Sprache",
    },
    "it": {
        "title": "4 Immagini 1 Parola",
        "score": "Punteggio",
        "level": "Livello",
        "hint": "Indizio (-50pti)",
        "skip": "Salta",
        "clear": "Cancella",
        "bravo": "Bravo! +{pts} punti",
        "wrong": "Riprova!",
        "answer_was": "La risposta era: {word}",
        "congrats": "Congratulazioni!",
        "final_score": "Punteggio finale: {score} punti",
        "completed": "Hai completato tutti i {total} livelli!",
        "replay": "Gioca ancora",
        "select_lang": "Lingua",
    },
    "pt": {
        "title": "4 Fotos 1 Palavra",
        "score": "Pontos",
        "level": "Nível",
        "hint": "Dica (-50pts)",
        "skip": "Pular",
        "clear": "Limpar",
        "bravo": "Parabéns! +{pts} pontos",
        "wrong": "Tente novamente!",
        "answer_was": "A resposta era: {word}",
        "congrats": "Parabéns!",
        "final_score": "Pontuação final: {score} pontos",
        "completed": "Você completou todos os {total} níveis!",
        "replay": "Jogar novamente",
        "select_lang": "Idioma",
    },
}


def t(lang, key, **kwargs):
    """Retourne la traduction pour la clé donnée."""
    s = UI_STRINGS.get(lang, UI_STRINGS["fr"]).get(key, key)
    if kwargs:
        s = s.format(**kwargs)
    return s
