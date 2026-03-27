#!/usr/bin/env python3
"""
4 Images 1 Mot - Jeu de devinettes
Application desktop pour Linux et Windows
Multilingue : fr, en, es, de, it, pt
"""

import locale
import os
import sys
import tkinter as tk
from tkinter import font as tkfont
import random
import string
import unicodedata

from puzzles import PUZZLES
from puzzles_i18n import TRANSLATIONS
from i18n import t, LANGUAGES

# --- Constantes ---
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 820
BG_COLOR = "#1A1A2E"
BG_SECONDARY = "#16213E"
ACCENT_COLOR = "#0F3460"
HIGHLIGHT_COLOR = "#E94560"
SUCCESS_COLOR = "#06D6A0"
TEXT_COLOR = "#EAEAEA"
TEXT_DARK = "#1A1A2E"
CARD_SIZE = 170


def _get_font_family():
    """Retourne une police disponible sur le système."""
    try:
        root = tk._default_root
        available = tkfont.families(root)
        for candidate in ("Ubuntu", "Segoe UI", "Helvetica Neue", "Helvetica", "Arial"):
            if candidate in available:
                return candidate
    except Exception:
        pass
    return "TkDefaultFont"


def _get_emoji_font():
    """Retourne une police emoji disponible."""
    try:
        root = tk._default_root
        available = tkfont.families(root)
        for candidate in ("Segoe UI Emoji", "Noto Color Emoji", "Apple Color Emoji", "Symbola"):
            if candidate in available:
                return candidate
    except Exception:
        pass
    return "TkDefaultFont"


def _text_color_for_bg(hex_color):
    """Retourne 'white' ou '#1A1A2E' selon la luminosité du fond."""
    try:
        c = hex_color.lstrip("#")
        r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        return TEXT_DARK if luminance > 160 else "white"
    except Exception:
        return "white"


def detect_language():
    """Détecte la langue du système."""
    # Linux: LANG, LC_ALL, LANGUAGE
    for var in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        val = os.environ.get(var, "")
        if val:
            code = val.split("_")[0].split(".")[0].split(":")[0].lower()
            if code in LANGUAGES:
                return code
    # Fallback via locale (compatible Python 3.11+)
    try:
        loc = locale.getlocale()[0] or ""
        code = loc.split("_")[0].lower()
        if code in LANGUAGES:
            return code
    except Exception:
        pass
    # Windows: kernel32 API
    if sys.platform == "win32":
        try:
            import ctypes
            lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            lang_code = {
                0x040C: "fr", 0x0409: "en", 0x0C0A: "es",
                0x0407: "de", 0x0410: "it", 0x0416: "pt",
            }.get(lang_id & 0xFFFF)
            if lang_code:
                return lang_code
        except Exception:
            pass
    return "fr"


def normalize(text):
    """Retire les accents pour la comparaison."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).upper()


def get_puzzle_for_lang(puzzle, lang):
    """Retourne le puzzle adapté à la langue."""
    if lang == "fr":
        return puzzle["word"], [img["desc"] for img in puzzle["images"]]

    fr_word = puzzle["word"]
    tr = TRANSLATIONS.get(fr_word, {}).get(lang)
    if tr:
        return tr["word"], tr["descs"]
    # Fallback français
    return puzzle["word"], [img["desc"] for img in puzzle["images"]]


class ImageCard(tk.Canvas):
    """Carte visuelle représentant une image du puzzle."""

    def __init__(self, parent, desc, color, icon, size=CARD_SIZE):
        super().__init__(
            parent,
            width=size,
            height=size,
            bg=color,
            highlightthickness=2,
            highlightbackground="#B0B0B0",
            relief="flat",
        )
        text_color = _text_color_for_bg(color)
        emoji_font = _get_emoji_font()
        ui_font = _get_font_family()

        self._round_rect(2, 2, size - 2, size - 2, 15, color)
        self.create_text(
            size // 2,
            size // 2 - 15,
            text=icon,
            font=(emoji_font, 42),
            fill=text_color,
        )
        self.create_text(
            size // 2,
            size - 30,
            text=desc,
            font=(ui_font, 11, "bold"),
            fill=text_color,
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

        # Langue auto-détectée
        self.lang = detect_language()

        # Polices adaptées au système
        ui_font = _get_font_family()

        self.title(f"🎮 {t(self.lang, 'title')}")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # État du jeu
        self.puzzles = list(PUZZLES)
        random.shuffle(self.puzzles)
        self.current_index = 0
        self.score = 0
        self.hints_used = 0
        self.current_answer = []
        self.pool_buttons = []
        self.answer_slots = []
        self.locked = False  # Verrouille les interactions pendant les transitions
        self._pending_after = None  # ID du timer en cours

        # Polices
        self.font_title = tkfont.Font(family=ui_font, size=24, weight="bold")
        self.font_score = tkfont.Font(family=ui_font, size=14)
        self.font_letter = tkfont.Font(family=ui_font, size=18, weight="bold")
        self.font_btn = tkfont.Font(family=ui_font, size=12, weight="bold")
        self.font_small = tkfont.Font(family=ui_font, size=11)

        self._build_ui()
        self._load_puzzle()

    def _schedule_next(self, delay, callback):
        """Planifie un callback avec annulation de l'ancien."""
        if self._pending_after is not None:
            self.after_cancel(self._pending_after)
        self._pending_after = self.after(delay, callback)

    def _set_locked(self, locked):
        """Verrouille ou déverrouille les interactions."""
        self.locked = locked
        state = "disabled" if locked else "normal"
        self.btn_hint.config(state=state)
        self.btn_skip.config(state=state)
        self.btn_clear.config(state=state)

    def _build_ui(self):
        """Construit l'interface utilisateur."""
        # --- Header ---
        header = tk.Frame(self, bg=BG_SECONDARY, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text=f"🎮  {t(self.lang, 'title')}",
            font=self.font_title,
            bg=BG_SECONDARY,
            fg=TEXT_COLOR,
        ).pack(side="left", padx=20, pady=10)

        self.lbl_score = tk.Label(
            header,
            text=f"⭐ {t(self.lang, 'score')}: 0",
            font=self.font_score,
            bg=BG_SECONDARY,
            fg="#FFD166",
        )
        self.lbl_score.pack(side="right", padx=20)

        self.lbl_level = tk.Label(
            header,
            text=f"{t(self.lang, 'level')} 1/30",
            font=self.font_score,
            bg=BG_SECONDARY,
            fg=TEXT_COLOR,
        )
        self.lbl_level.pack(side="right", padx=10)

        # Sélecteur de langue (discret, dans le header)
        lang_frame = tk.Frame(header, bg=BG_SECONDARY)
        lang_frame.pack(side="right", padx=10)

        self.lang_var = tk.StringVar(value=self.lang)
        lang_menu = tk.OptionMenu(
            lang_frame, self.lang_var, *LANGUAGES.keys(),
            command=self._change_language,
        )
        lang_menu.config(
            bg=ACCENT_COLOR, fg=TEXT_COLOR, font=self.font_small,
            activebackground="#1A4080", activeforeground=TEXT_COLOR,
            highlightthickness=0, relief="flat", width=3,
        )
        lang_menu["menu"].config(bg=ACCENT_COLOR, fg=TEXT_COLOR, font=self.font_small)
        lang_menu.pack()

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

        # --- Boutons d'action ---
        actions = tk.Frame(self, bg=BG_COLOR)
        actions.pack(pady=10)

        # --- Pool de lettres ---
        self.pool_frame = tk.Frame(self, bg=BG_COLOR)
        self.pool_frame.pack(pady=10)

        self.btn_hint = tk.Button(
            actions,
            text=f"💡 {t(self.lang, 'hint')}",
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
            text=f"⏭️ {t(self.lang, 'skip')}",
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
            text=f"🗑️ {t(self.lang, 'clear')}",
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

    def _change_language(self, new_lang):
        """Change la langue et recharge l'interface."""
        if self._pending_after is not None:
            self.after_cancel(self._pending_after)
            self._pending_after = None
        self.locked = False
        self.lang = new_lang
        self.title(f"🎮 {t(self.lang, 'title')}")
        self.btn_hint.config(text=f"💡 {t(self.lang, 'hint')}")
        self.btn_skip.config(text=f"⏭️ {t(self.lang, 'skip')}")
        self.btn_clear.config(text=f"🗑️ {t(self.lang, 'clear')}")
        self._load_puzzle()

    def _load_puzzle(self):
        """Charge le puzzle courant."""
        self._pending_after = None
        self._set_locked(False)

        if self.current_index >= len(self.puzzles):
            self._show_end_screen()
            return

        puzzle = self.puzzles[self.current_index]
        word, descs = get_puzzle_for_lang(puzzle, self.lang)
        self.current_word = normalize(word)
        self.current_answer = []
        self.lbl_feedback.config(text="")

        # Mise à jour header
        self.lbl_level.config(
            text=f"{t(self.lang, 'level')} {self.current_index + 1}/{len(self.puzzles)}"
        )
        self.lbl_score.config(text=f"⭐ {t(self.lang, 'score')}: {self.score}")

        # --- Images ---
        for w in self.images_frame.winfo_children():
            w.destroy()

        for i, img in enumerate(puzzle["images"]):
            desc = descs[i] if i < len(descs) else img["desc"]
            card = ImageCard(
                self.images_frame, desc, img["color"], img["icon"]
            )
            card.grid(row=i // 2, column=i % 2, padx=8, pady=8)

        # --- Slots réponse ---
        for w in self.answer_frame.winfo_children():
            w.destroy()
        self.answer_slots = []

        # Adapter la taille de police pour les longs mots
        letter_font = self.font_letter
        if len(self.current_word) > 8:
            letter_font = tkfont.Font(family=_get_font_family(), size=15, weight="bold")

        for i in range(len(self.current_word)):
            slot = tk.Label(
                self.answer_frame,
                text="",
                width=3,
                height=1,
                font=letter_font,
                bg=ACCENT_COLOR,
                fg=TEXT_COLOR,
                relief="flat",
                cursor="hand2",
            )
            slot.grid(row=0, column=i, padx=2, pady=5)
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
        pool_size = max(14, len(word_letters) + 4)
        extra = pool_size - len(word_letters)
        freq_map = {
            "fr": "AEIOURSTNLCDPMG",
            "en": "ETAOINSRHLDCUMF",
            "es": "EAOSRNIDLCTUMPB",
            "de": "ENISRATDHULCGMO",
            "it": "EAIONLRTSCDUPMG",
            "pt": "EAOSRIDMNTUCLPG",
        }
        freq_letters = freq_map.get(self.lang, freq_map["fr"])
        extras = [random.choice(freq_letters) for _ in range(extra)]
        all_letters = word_letters + extras
        random.shuffle(all_letters)

        self.pool_letters = all_letters
        self.pool_used = [False] * len(all_letters)

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
        if self.locked:
            return
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

        if len(self.current_answer) == len(self.current_word):
            self._check_answer()

    def _remove_letter_at(self, slot_idx):
        """Retire une lettre à une position donnée."""
        if self.locked:
            return
        if slot_idx >= len(self.current_answer):
            return

        pool_idx, letter = self.current_answer[slot_idx]

        self.pool_used[pool_idx] = False
        self.pool_buttons[pool_idx].config(
            bg="#2A4A7F", fg=TEXT_COLOR, state="normal"
        )

        self.current_answer.pop(slot_idx)

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
        if self.locked:
            return
        if self.current_answer:
            self._remove_letter_at(len(self.current_answer) - 1)

    def _on_key_press(self, event):
        """Gère la saisie clavier."""
        if self.locked:
            return
        key = event.char.upper()
        if key and key in string.ascii_uppercase:
            for i, letter in enumerate(self.pool_letters):
                if letter == key and not self.pool_used[i]:
                    self._place_letter(i)
                    break

    def _clear_answer(self):
        """Efface toute la réponse."""
        if self.locked:
            return
        while self.current_answer:
            self._remove_letter_at(len(self.current_answer) - 1)

    def _check_answer(self):
        """Vérifie si la réponse est correcte."""
        answer = "".join(letter for _, letter in self.current_answer)
        if answer == self.current_word:
            points = max(100, 200 - self.hints_used * 50)
            self.score += points
            self.lbl_score.config(text=f"⭐ {t(self.lang, 'score')}: {self.score}")
            self.lbl_feedback.config(
                text=f"✅ {t(self.lang, 'bravo', pts=points)}", fg=SUCCESS_COLOR
            )

            for slot in self.answer_slots:
                slot.config(bg=SUCCESS_COLOR, fg=TEXT_DARK)

            self.hints_used = 0
            self.current_index += 1
            self._set_locked(True)
            self._schedule_next(1500, self._load_puzzle)
        else:
            self.lbl_feedback.config(
                text=f"❌ {t(self.lang, 'wrong')}", fg=HIGHLIGHT_COLOR
            )
            self._shake_animation()

    def _shake_animation(self, count=0):
        """Animation de secousse en cas d'erreur."""
        if count >= 6:
            self.answer_frame.pack_configure(padx=0)
            return
        offset = 8 if count % 2 == 0 else -8
        self.answer_frame.pack_configure(padx=offset)
        self.after(60, self._shake_animation, count + 1)

    def _use_hint(self):
        """Révèle une lettre correcte."""
        if self.locked:
            return
        if self.current_index >= len(self.puzzles):
            return
        placed = len(self.current_answer)
        if placed >= len(self.current_word):
            return

        needed_letter = self.current_word[placed]
        self.hints_used += 1

        for i, letter in enumerate(self.pool_letters):
            if letter == needed_letter and not self.pool_used[i]:
                self._place_letter(i)
                # Colorer en jaune seulement si on n'a pas changé de puzzle
                if placed < len(self.answer_slots) and not self.locked:
                    self.answer_slots[placed].config(bg="#E9C46A", fg=TEXT_DARK)
                break

    def _skip_puzzle(self):
        """Passe au puzzle suivant."""
        if self.locked:
            return
        if self.current_index >= len(self.puzzles):
            return

        self.hints_used = 0
        puzzle = self.puzzles[self.current_index]
        word, _ = get_puzzle_for_lang(puzzle, self.lang)
        self.current_index += 1

        self.lbl_feedback.config(
            text=f"{t(self.lang, 'answer_was', word=word)}",
            fg="#FFD166",
        )
        self._set_locked(True)
        self._schedule_next(1500, self._load_puzzle)

    def _show_end_screen(self):
        """Affiche l'écran de fin de jeu."""
        for w in self.images_frame.winfo_children():
            w.destroy()
        for w in self.answer_frame.winfo_children():
            w.destroy()
        for w in self.pool_frame.winfo_children():
            w.destroy()
        self.lbl_feedback.config(text="")

        # Désactiver les boutons
        self.btn_hint.config(state="disabled")
        self.btn_skip.config(state="disabled")
        self.btn_clear.config(state="disabled")

        emoji_font = _get_emoji_font()
        ui_font = _get_font_family()

        end_frame = tk.Frame(self.images_frame, bg=BG_COLOR)
        end_frame.pack(pady=40)

        tk.Label(
            end_frame,
            text="🎉",
            font=(emoji_font, 64),
            bg=BG_COLOR,
        ).pack()

        tk.Label(
            end_frame,
            text=t(self.lang, "congrats"),
            font=tkfont.Font(family=ui_font, size=32, weight="bold"),
            bg=BG_COLOR,
            fg=SUCCESS_COLOR,
        ).pack(pady=10)

        tk.Label(
            end_frame,
            text=t(self.lang, "final_score", score=self.score),
            font=tkfont.Font(family=ui_font, size=20),
            bg=BG_COLOR,
            fg="#FFD166",
        ).pack(pady=5)

        total = len(self.puzzles)
        tk.Label(
            end_frame,
            text=t(self.lang, "completed", total=total),
            font=self.font_score,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        ).pack(pady=5)

        tk.Button(
            end_frame,
            text=f"🔄 {t(self.lang, 'replay')}",
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
        self.btn_hint.config(state="normal")
        self.btn_skip.config(state="normal")
        self.btn_clear.config(state="normal")
        self._load_puzzle()


if __name__ == "__main__":
    app = Game()
    app.mainloop()
