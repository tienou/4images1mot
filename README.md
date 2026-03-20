# 🎮 4 Images 1 Mot / 4 Pics 1 Word

> **[Français](#fr)** | **[English](#en)**

![Screenshot](assets/screenshot.png)

---

<a id="fr"></a>

## 🇫🇷 Français

Jeu de devinettes pour Linux et Windows — Trouve le mot commun aux 4 images !

### Fonctionnalités

- 🖼️ **30 puzzles** avec 3 niveaux de difficulté
- ⌨️ Sélection de lettres par **clic ou clavier**
- ⭐ Système de **score** (+200pts par mot, -50pts par indice)
- 💡 **Indices** pour révéler une lettre
- ⏭️ Possibilité de **passer** un puzzle
- 🎨 Interface sombre moderne

### 🌍 Langues supportées

La langue est **détectée automatiquement** depuis le système.
Un sélecteur dans le header permet de changer manuellement.

| Langue | Code |
|--------|------|
| 🇫🇷 Français | `fr` |
| 🇬🇧 English | `en` |
| 🇪🇸 Español | `es` |
| 🇩🇪 Deutsch | `de` |
| 🇮🇹 Italiano | `it` |
| 🇧🇷 Português | `pt` |

### Installation

#### 🪟 Windows

| Type | Fichier | Description |
|------|---------|-------------|
| **Installeur** | `4images1mot-x.x.x-setup.exe` | Installe le jeu, crée un raccourci bureau et menu Démarrer |
| **Portable** | `4images1mot-x.x.x-portable.exe` | Fichier unique, aucune installation requise |

Télécharger depuis la [page Releases](https://github.com/tienou/4images1mot/releases/latest).

#### 🐧 Linux — Depuis les sources
```bash
sudo apt install python3-tk
git clone https://github.com/tienou/4images1mot.git
cd 4images1mot
python3 main.py
```

#### 🐧 Linux — Paquets pré-compilés
```bash
# .deb (Debian/Ubuntu/Mint)
sudo dpkg -i 4images1mot_1.0.0_all.deb

# .rpm (Fedora/RHEL/openSUSE)
sudo dnf install 4images1mot-1.0.0-1.noarch.rpm

# AppImage (universel)
chmod +x 4images1mot-1.0.0-x86_64.AppImage
./4images1mot-1.0.0-x86_64.AppImage
```

### 📦 Tous les packages

| Format | Plateforme | Distribution |
|--------|-----------|-------------|
| **Installeur .exe** | Windows | Windows 10/11 |
| **Portable .exe** | Windows | Windows 10/11 (aucune installation) |
| **.deb** | Linux | Debian, Ubuntu, Mint |
| **.rpm** | Linux | Fedora, RHEL, openSUSE |
| **AppImage** | Linux | Toutes (portable) |
| **Flatpak** | Linux | Toutes (sandboxé) |
| **Snap** | Linux | Ubuntu, Manjaro |

#### Build depuis les sources (Linux)

| Commande | Résultat |
|----------|----------|
| `make deb` | Paquet .deb |
| `make rpm` | Paquet .rpm |
| `make appimage` | AppImage |
| `make flatpak` | Flatpak |
| `make snap` | Snap |
| `make all` | Tous les formats |

### 🎮 Contrôles

| Action | Contrôle |
|--------|----------|
| Placer une lettre | Clic sur la lettre ou touche clavier |
| Retirer une lettre | Clic sur la lettre placée |
| Retirer la dernière | `Backspace` |
| Effacer tout | Bouton Effacer |

---

<a id="en"></a>

## 🇬🇧 English

A word guessing game for Linux and Windows — Find the word that connects the 4 images!

### Features

- 🖼️ **30 puzzles** with 3 difficulty levels
- ⌨️ Letter selection by **click or keyboard**
- ⭐ **Scoring system** (+200pts per word, -50pts per hint)
- 💡 **Hints** to reveal a letter
- ⏭️ Option to **skip** a puzzle
- 🎨 Modern dark UI

### 🌍 Supported languages

The language is **auto-detected** from the system.
A selector in the header allows manual switching.

| Language | Code |
|----------|------|
| 🇫🇷 Français | `fr` |
| 🇬🇧 English | `en` |
| 🇪🇸 Español | `es` |
| 🇩🇪 Deutsch | `de` |
| 🇮🇹 Italiano | `it` |
| 🇧🇷 Português | `pt` |

### Installation

#### 🪟 Windows

| Type | File | Description |
|------|------|-------------|
| **Installer** | `4images1mot-x.x.x-setup.exe` | Installs the game, creates desktop and Start menu shortcuts |
| **Portable** | `4images1mot-x.x.x-portable.exe` | Single file, no installation required |

Download from the [Releases page](https://github.com/tienou/4images1mot/releases/latest).

#### 🐧 Linux — From source
```bash
sudo apt install python3-tk
git clone https://github.com/tienou/4images1mot.git
cd 4images1mot
python3 main.py
```

#### 🐧 Linux — Pre-built packages
```bash
# .deb (Debian/Ubuntu/Mint)
sudo dpkg -i 4images1mot_1.0.0_all.deb

# .rpm (Fedora/RHEL/openSUSE)
sudo dnf install 4images1mot-1.0.0-1.noarch.rpm

# AppImage (universal)
chmod +x 4images1mot-1.0.0-x86_64.AppImage
./4images1mot-1.0.0-x86_64.AppImage
```

### 📦 All packages

| Format | Platform | Distribution |
|--------|----------|-------------|
| **Installer .exe** | Windows | Windows 10/11 |
| **Portable .exe** | Windows | Windows 10/11 (no installation) |
| **.deb** | Linux | Debian, Ubuntu, Mint |
| **.rpm** | Linux | Fedora, RHEL, openSUSE |
| **AppImage** | Linux | All (portable) |
| **Flatpak** | Linux | All (sandboxed) |
| **Snap** | Linux | Ubuntu, Manjaro |

#### Build from source (Linux)

| Command | Output |
|---------|--------|
| `make deb` | .deb package |
| `make rpm` | .rpm package |
| `make appimage` | AppImage |
| `make flatpak` | Flatpak |
| `make snap` | Snap |
| `make all` | All formats |

### 🎮 Controls

| Action | Control |
|--------|---------|
| Place a letter | Click on the letter or press the key |
| Remove a letter | Click on the placed letter |
| Remove last | `Backspace` |
| Clear all | Clear button |

---

## Licence / License

MIT
