# 🎮 4 Images 1 Mot

Jeu de devinettes pour Linux — Trouve le mot commun aux 4 images !

![Screenshot](assets/screenshot.png)

## Fonctionnalités

- 🖼️ **30 puzzles** en français avec 3 niveaux de difficulté
- ⌨️ Sélection de lettres par **clic ou clavier**
- ⭐ Système de **score** (+200pts par mot, -50pts par indice)
- 💡 **Indices** pour révéler une lettre
- ⏭️ Possibilité de **passer** un puzzle
- 🎨 Interface sombre moderne
- 🌍 **Multilingue** : Français, English, Español, Deutsch, Italiano, Português

## Installation

### Depuis les sources
```bash
sudo apt install python3-tk
git clone https://github.com/tienou/4images1mot.git
cd 4images1mot
python3 main.py
```

### Paquet .deb (Debian/Ubuntu/Mint)
```bash
# Télécharger depuis les releases GitHub
sudo dpkg -i 4images1mot_1.0.0_all.deb
```

### Paquet .rpm (Fedora/RHEL/openSUSE)
```bash
sudo dnf install 4images1mot-1.0.0-1.noarch.rpm
```

### AppImage (universel)
```bash
chmod +x 4images1mot-1.0.0-x86_64.AppImage
./4images1mot-1.0.0-x86_64.AppImage
```

## Packages disponibles

| Format | Commande | Distribution |
|--------|----------|-------------|
| **.deb** | `make deb` | Debian, Ubuntu, Mint |
| **.rpm** | `make rpm` | Fedora, RHEL, openSUSE |
| **AppImage** | `make appimage` | Toutes (portable) |
| **Flatpak** | `make flatpak` | Toutes (sandboxé) |
| **Snap** | `make snap` | Ubuntu, Manjaro |
| **Tous** | `make all` | Build tout d'un coup |

## Prérequis pour le build

| Package | Outil requis |
|---------|-------------|
| .deb | `dpkg-dev` |
| .rpm | `rpm-build` |
| AppImage | `wget` (télécharge appimagetool) |
| Flatpak | `flatpak-builder` + runtime freedesktop 23.08 |
| Snap | `snapcraft` |

## Contrôles

| Action | Contrôle |
|--------|----------|
| Placer une lettre | Clic sur la lettre ou touche clavier |
| Retirer une lettre | Clic sur la lettre placée |
| Retirer la dernière | `Backspace` |
| Effacer tout | Bouton Effacer |

## Licence

MIT
