#!/bin/bash
# ============================================================
# Script d'installation locale pour Ubuntu
# Usage: sudo ./install.sh
# ============================================================
set -e

APP_NAME="4images1mot"
INSTALL_DIR="/opt/${APP_NAME}"
BIN_LINK="/usr/local/bin/${APP_NAME}"
DESKTOP_FILE="/usr/share/applications/${APP_NAME}.desktop"
ICON_FILE="/usr/share/icons/hicolor/scalable/apps/${APP_NAME}.svg"

echo "🎮 Installation de 4 Images 1 Mot..."

# Vérifier les dépendances
echo "📋 Vérification des dépendances..."
if ! command -v python3 &> /dev/null; then
    echo "❌ python3 non trouvé. Installation..."
    apt-get update && apt-get install -y python3
fi

if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "📦 Installation de python3-tk..."
    apt-get update && apt-get install -y python3-tk
fi

# Installer les fichiers
echo "📁 Copie des fichiers vers ${INSTALL_DIR}..."
mkdir -p "${INSTALL_DIR}"
cp main.py "${INSTALL_DIR}/"
cp puzzles.py "${INSTALL_DIR}/"
cp icon.svg "${INSTALL_DIR}/"

# Créer le lanceur
cat > "${INSTALL_DIR}/launch.sh" << 'EOF'
#!/bin/bash
exec python3 /opt/4images1mot/main.py "$@"
EOF
chmod +x "${INSTALL_DIR}/launch.sh"

# Lien symbolique
ln -sf "${INSTALL_DIR}/launch.sh" "${BIN_LINK}"

# Fichier .desktop
cat > "${DESKTOP_FILE}" << EOF
[Desktop Entry]
Name=4 Images 1 Mot
Comment=Jeu de devinettes - Trouve le mot commun aux 4 images
Exec=${APP_NAME}
Icon=${APP_NAME}
Type=Application
Categories=Game;
Terminal=false
StartupWMClass=4images1mot
EOF

# Icône
mkdir -p "$(dirname "${ICON_FILE}")"
cp icon.svg "${ICON_FILE}"

# Mettre à jour le cache
update-desktop-database /usr/share/applications/ 2>/dev/null || true
gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true

echo ""
echo "✅ Installation terminée !"
echo ""
echo "Lancer le jeu :"
echo "  • Depuis le menu Applications → Jeux → 4 Images 1 Mot"
echo "  • Ou en terminal : ${APP_NAME}"
echo ""
echo "Désinstaller : sudo ./uninstall.sh"
