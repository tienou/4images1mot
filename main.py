#!/usr/bin/env python3
"""
4 Images 1 Mot - Jeu de devinettes
Application desktop pour Linux (Ubuntu)
"""

import tkinter as tk
from tkinter import font as tkfont
import random
import string
import unicodedata

from puzzles import PUZZLES

# --- Constantes ---
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 720
BG_COLOR = "#1A1A2E"
BG_SECONDARY = "#16213E"
ACCENT_COLOR = "#0F3460"
HIGHLIGHT_COLOR = "#E94560"
SUCCESS_COLOR = "#06D6A0"
TEXT_COLOR = "#EAEAEA"
TEXT_DARK = "#1A1A2E"
CARD_SIZE = 170
LETTER_BTN_SIZE = 48
ANSWER_SLOT_SIZE = 44


def normalize(text):
    """Retire les accents pour la comparaison."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).upper()


class ImageCard(tk.Canvas):
    """Carte visuelle représentant une image du puzzle."""

    def __init__(self, parent, desc, color, icon, size=CARD_SIZE):
        super().__init__(
            parent,
            width=size,
            height=size,
            bg=color,
            highlightthickness=2,
            highlightbackground="#FFFFFF30",
            relief="flat",
        )
        self.create_text(
            size // 2,
            size // 2 - 15,
            text=icon,
            font=("Segoe UI Emoji", 42),
            fill="white",
        )
        self.create_text(
            size // 2,
            size - 30,
            text=desc,
            font=("Ubuntu", 11, "bold"),
            fill="white",
            justify="center",
            width=size - 20,
        )
        # Arrondir les coins visuellement
        self._round_rect(2, 2, size - 2, size - 2, 15, color)
        self.create_text(
            size // 2,
            size // 2 - 15,
            text=icon,
            font=("Segoe UI Emoji", 42),
            fill="white",
        )
        self.create_text(
            size // 2,
            size - 30,
            text=desc,
            font=("Ubuntu", 11, "bold"),
            fill="white",
            justify="center",
            width=size - 20,
        )

    def _round_rect(self, x1, y1, x2, y2, r, fill):
        self.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, fill=fill, outline=fill)
        self.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, fill=fill, outline=fill)
        self.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, fill=fill, outline=fill)
        self.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, fill=fill, outline=fill)
        self.create_rectangle(x1 + r, y1, x2 - r, y2, fill=fill, outline=fill)
        self.create_rectangle(x1, y1 + r, x2, y2 - r, fill=fill, outline=fill)


class Game(tk.Tk):
    """Application principale du jeu."""

    def __init__(self):
        super().__init__()
        self.title("4 Images 1 Mot")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # État du jeu
        self.puzzles = list(PUZZLES)
        random.shuffle(self.puzzles)
        self.current_index = 0
        self.score = 0
        self.hints_used = 0
        self.current_answer = []  # Lettres placées [(index_pool, lettre), ...]
        self.pool_buttons = []
        self.answer_slots = []

        # Polices
        self.font_title = tkfont.Font(family="Ubuntu", size=24, weight="bold")
        self.font_score = tkfont.Font(family="Ubuntu", size=14)
        self.font_letter = tkfont.Font(family="Ubuntu", size=18, weight="bold")
        self.font_btn = tkfont.Font(family="Ubuntu", size=12, weight="bold")
        self.font_small = tkfont.Font(family="Ubuntu", size=11)

        self._build_ui()
        self._load_puzzle()

    def _build_ui(self):
        """Construit l'interface utilisateur."""
        # --- Header ---
        header = tk.Frame(self, bg=BG_SECONDARY, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🎮  4 Images 1 Mot",
            font=self.font_title,
            bg=BG_SECONDARY,
            fg=TEXT_COLOR,
        ).pack(side="left", padx=20, pady=10)

        self.lbl_score = tk.Label(
            header,
            text="⭐ Score: 0",
            font=self.font_score,
            bg=BG_SECONDARY,
            fg="#FFD166",
        )
        self.lbl_score.pack(side="right", padx=20)

        self.lbl_level = tk.Label(
            header,
            text="Niveau 1/30",
            font=self.font_score,
            bg=BG_SECONDARY,
            fg=TEXT_COLOR,
        )
        self.lbl_level.pack(side="right", padx=10)

        # --- Zone images ---
        self.images_frame = tk.Frame(self, bg=BG_COLOR)
        self.images_frame.pack(pady=20)

        # --- Zone réponse ---
        self.answer_frame = tk.Frame(self, bg=BG_COLOR)
        self.answer_frame.pack(pady=10)

        # --- Message feedback ---
        self.lbl_feedback = tk.Label(
            self, text="", font=self.font_btn, bg=BG_COLOR, fg=SUCCESS_COLOR
        )
        self.lbl_feedback.pack(pady=5)

        # --- Pool de lettres ---
        self.pool_frame = tk.Frame(self, bg=BG_COLOR)
        self.pool_frame.pack(pady=10)

        # --- Boutons d'action ---
        actions = tk.Frame(self, bg=BG_COLOR)
        actions.pack(pady=15)

        self.btn_hint = tk.Button(
            actions,
            text="💡 Indice (-50pts)",
            font=self.font_btn,
            bg="#E9C46A",
            fg=TEXT_DARK,
            activebackground="#F4A261",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self._use_hint,
        )
        self.btn_hint.pack(side="left", padx=10)

        self.btn_skip = tk.Button(
            actions,
            text="⏭️ Passer",
            font=self.font_btn,
            bg=ACCENT_COLOR,
            fg=TEXT_COLOR,
            activebackground="#1A4080",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self._skip_puzzle,
        )
        self.btn_skip.pack(side="left", padx=10)

        self.btn_clear = tk.Button(
            actions,
            text="🗑️ Effacer",
            font=self.font_btn,
            bg="#6C757D",
            fg=TEXT_COLOR,
            activebackground="#495057",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self._clear_answer,
        )
        self.btn_clear.pack(side="left", padx=10)

        # Raccourcis clavier
        self.bind("<BackSpace>", lambda e: self._remove_last_letter())
        self.bind("<Key>", self._on_key_press)

    def _load_puzzle(self):
        """Charge le puzzle courant."""
        if self.current_index >= len(self.puzzles):
            self._show_end_screen()
            return

        puzzle = self.puzzles[self.current_index]
        self.current_word = normalize(puzzle["word"])
        self.current_answer = []
        self.lbl_feedback.config(text="")

        # Mise à jour header
        self.lbl_level.config(
            text=f"Niveau {self.current_index + 1}/{len(self.puzzles)}"
        )
        self.lbl_score.config(text=f"⭐ Score: {self.score}")

        # --- Images ---
        for w in self.images_frame.winfo_children():
            w.destroy()

        for i, img in enumerate(puzzle["images"]):
            card = ImageCard(
                self.images_frame, img["desc"], img["color"], img["icon"]
            )
            card.grid(row=i // 2, column=i % 2, padx=8, pady=8)

        # --- Slots réponse ---
        for w in self.answer_frame.winfo_children():
            w.destroy()
        self.answer_slots = []

        for i in range(len(self.current_word)):
            slot = tk.Label(
                self.answer_frame,
                text="",
                width=3,
                height=1,
                font=self.font_letter,
                bg=ACCENT_COLOR,
                fg=TEXT_COLOR,
                relief="flat",
                cursor="hand2",
            )
            slot.grid(row=0, column=i, padx=3, pady=5)
            slot.bind("<Button-1>", lambda e, idx=i: self._remove_letter_at(idx))
            self.answer_slots.append(slot)

        # --- Pool de lettres ---
        self._generate_pool()

    def _generate_pool(self):
        """Génère le pool de lettres (mot + lettres aléatoires)."""
        for w in self.pool_frame.winfo_children():
            w.destroy()
        self.pool_buttons = []

        word_letters = list(self.current_word)
        # Ajouter des lettres aléatoires pour remplir à 14 lettres
        pool_size = max(14, len(word_letters) + 4)
        extra = pool_size - len(word_letters)
        # Lettres fréquentes en français
        freq_letters = "AEIOURSTNLCDPMG"
        extras = [random.choice(freq_letters) for _ in range(extra)]
        all_letters = word_letters + extras
        random.shuffle(all_letters)

        self.pool_letters = all_letters
        self.pool_used = [False] * len(all_letters)

        # Afficher en 2 lignes
        cols = 7
        for i, letter in enumerate(all_letters):
            btn = tk.Button(
                self.pool_frame,
                text=letter,
                width=3,
                height=1,
                font=self.font_letter,
                bg="#2A4A7F",
                fg=TEXT_COLOR,
                activebackground="#3A5A9F",
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self._place_letter(idx),
            )
            btn.grid(row=i // cols, column=i % cols, padx=3, pady=3)
            self.pool_buttons.append(btn)

    def _place_letter(self, pool_idx):
        """Place une lettre du pool dans la réponse."""
        if self.pool_used[pool_idx]:
            return
        if len(self.current_answer) >= len(self.current_word):
            return

        letter = self.pool_letters[pool_idx]
        self.pool_used[pool_idx] = True
        self.pool_buttons[pool_idx].config(bg=BG_COLOR, fg=BG_COLOR, state="disabled")

        pos = len(self.current_answer)
        self.current_answer.append((pool_idx, letter))
        self.answer_slots[pos].config(text=letter, bg="#3A5A9F")

        # Vérifier si réponse complète
        if len(self.current_answer) == len(self.current_word):
            self._check_answer()

    def _remove_letter_at(self, slot_idx):
        """Retire une lettre à une position donnée."""
        if slot_idx >= len(self.current_answer):
            return

        pool_idx, letter = self.current_answer[slot_idx]

        # Remettre dans le pool
        self.pool_used[pool_idx] = False
        self.pool_buttons[pool_idx].config(
            bg="#2A4A7F", fg=TEXT_COLOR, state="normal"
        )

        # Retirer de la réponse et décaler
        self.current_answer.pop(slot_idx)

        # Reconstruire l'affichage des slots
        for i in range(len(self.current_word)):
            if i < len(self.current_answer):
                self.answer_slots[i].config(
                    text=self.current_answer[i][1], bg="#3A5A9F"
                )
            else:
                self.answer_slots[i].config(text="", bg=ACCENT_COLOR)

        self.lbl_feedback.config(text="")

    def _remove_last_letter(self):
        """Retire la dernière lettre placée."""
        if self.current_answer:
            self._remove_letter_at(len(self.current_answer) - 1)

    def _on_key_press(self, event):
        """Gère la saisie clavier."""
        key = event.char.upper()
        if key and key in string.ascii_uppercase:
            # Trouver la première lettre correspondante non utilisée dans le pool
            for i, letter in enumerate(self.pool_letters):
                if letter == key and not self.pool_used[i]:
                    self._place_letter(i)
                    break

    def _clear_answer(self):
        """Efface toute la réponse."""
        while self.current_answer:
            self._remove_letter_at(len(self.current_answer) - 1)

    def _check_answer(self):
        """Vérifie si la réponse est correcte."""
        answer = "".join(letter for _, letter in self.current_answer)
        if answer == self.current_word:
            # Succès !
            points = max(50, 200 - self.hints_used * 50)
            self.score += points
            self.lbl_score.config(text=f"⭐ Score: {self.score}")
            self.lbl_feedback.config(
                text=f"✅ Bravo ! +{points} points", fg=SUCCESS_COLOR
            )

            # Colorer les slots en vert
            for slot in self.answer_slots:
                slot.config(bg=SUCCESS_COLOR, fg=TEXT_DARK)

            # Passer au puzzle suivant après un délai
            self.hints_used = 0
            self.current_index += 1
            self.after(1500, self._load_puzzle)
        else:
            self.lbl_feedback.config(text="❌ Essaie encore !", fg=HIGHLIGHT_COLOR)
            # Secouer les slots (animation simple)
            self._shake_animation()

    def _shake_animation(self, count=0):
        """Animation de secousse en cas d'erreur."""
        if count >= 6:
            self.answer_frame.place_forget()
            self.answer_frame.pack(pady=10)
            return
        offset = 8 if count % 2 == 0 else -8
        self.answer_frame.pack_configure(padx=offset)
        self.after(60, self._shake_animation, count + 1)

    def _use_hint(self):
        """Révèle une lettre correcte."""
        placed = len(self.current_answer)
        if placed >= len(self.current_word):
            return

        # Trouver la lettre nécessaire à la position suivante
        needed_letter = self.current_word[placed]
        self.hints_used += 1
        self.score = max(0, self.score - 50)
        self.lbl_score.config(text=f"⭐ Score: {self.score}")

        # Trouver cette lettre dans le pool
        for i, letter in enumerate(self.pool_letters):
            if letter == needed_letter and not self.pool_used[i]:
                self._place_letter(i)
                # Colorer en jaune pour montrer que c'est un indice
                self.answer_slots[placed].config(bg="#E9C46A", fg=TEXT_DARK)
                break

    def _skip_puzzle(self):
        """Passe au puzzle suivant."""
        self.hints_used = 0
        self.current_index += 1

        # Afficher la réponse avant de passer
        self.lbl_feedback.config(
            text=f"La réponse était : {self.puzzles[self.current_index - 1]['word']}",
            fg="#FFD166",
        )
        self.after(1500, self._load_puzzle)

    def _show_end_screen(self):
        """Affiche l'écran de fin de jeu."""
        for w in self.images_frame.winfo_children():
            w.destroy()
        for w in self.answer_frame.winfo_children():
            w.destroy()
        for w in self.pool_frame.winfo_children():
            w.destroy()
        self.lbl_feedback.config(text="")

        end_frame = tk.Frame(self.images_frame, bg=BG_COLOR)
        end_frame.pack(pady=40)

        tk.Label(
            end_frame,
            text="🎉",
            font=("Segoe UI Emoji", 64),
            bg=BG_COLOR,
        ).pack()

        tk.Label(
            end_frame,
            text="Félicitations !",
            font=tkfont.Font(family="Ubuntu", size=32, weight="bold"),
            bg=BG_COLOR,
            fg=SUCCESS_COLOR,
        ).pack(pady=10)

        tk.Label(
            end_frame,
            text=f"Score final : {self.score} points",
            font=tkfont.Font(family="Ubuntu", size=20),
            bg=BG_COLOR,
            fg="#FFD166",
        ).pack(pady=5)

        total = len(self.puzzles)
        tk.Label(
            end_frame,
            text=f"Tu as complété les {total} niveaux !",
            font=self.font_score,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        ).pack(pady=5)

        tk.Button(
            end_frame,
            text="🔄 Rejouer",
            font=self.font_btn,
            bg=HIGHLIGHT_COLOR,
            fg=TEXT_COLOR,
            activebackground="#FF6680",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self._restart_game,
        ).pack(pady=20)

    def _restart_game(self):
        """Relance le jeu depuis le début."""
        random.shuffle(self.puzzles)
        self.current_index = 0
        self.score = 0
        self.hints_used = 0
        self._load_puzzle()


if __name__ == "__main__":
    app = Game()
    app.mainloop()
