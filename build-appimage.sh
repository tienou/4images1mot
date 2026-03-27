#!/bin/bash
# ============================================================
# Build script - Crée un AppImage de "4 Images 1 Mot"
# Usage: ./build-appimage.sh
# Prérequis: python3, pip, wget
# ============================================================
set -e

APP_NAME="4images1mot"
APP_VERSION="1.0.0"
ARCH=$(uname -m)

echo "🔨 Construction de ${APP_NAME} v${APP_VERSION} AppImage..."

# --- Nettoyage ---
rm -rf AppDir build dist "${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"

# --- Créer la structure AppDir ---
echo "📁 Création de la structure AppDir..."
mkdir -p AppDir/usr/bin
mkdir -p AppDir/usr/share/applications
mkdir -p AppDir/usr/share/icons/hicolor/scalable/apps
mkdir -p AppDir/usr/share/${APP_NAME}

# --- Copier les fichiers de l'application ---
echo "📦 Copie des fichiers..."
cp main.py AppDir/usr/share/${APP_NAME}/
cp puzzles.py AppDir/usr/share/${APP_NAME}/
cp puzzles_i18n.py AppDir/usr/share/${APP_NAME}/
cp i18n.py AppDir/usr/share/${APP_NAME}/
cp icon.svg AppDir/usr/share/icons/hicolor/scalable/apps/${APP_NAME}.svg
cp ${APP_NAME}.desktop AppDir/usr/share/applications/
cp ${APP_NAME}.desktop AppDir/

# --- Créer le script de lancement ---
cat > AppDir/usr/bin/${APP_NAME} << 'LAUNCHER'
#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
APP_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")/usr/share/4images1mot"
exec python3 "$APP_DIR/main.py" "$@"
LAUNCHER
chmod +x AppDir/usr/bin/${APP_NAME}

# --- AppRun ---
cat > AppDir/AppRun << 'APPRUN'
#!/bin/bash
HERE="$(dirname "$(readlink -f "$0")")"
exec python3 "$HERE/usr/share/4images1mot/main.py" "$@"
APPRUN
chmod +x AppDir/AppRun

# --- Icône à la racine ---
cp icon.svg AppDir/${APP_NAME}.svg
cp icon.svg AppDir/.DirIcon

# --- Télécharger appimagetool si nécessaire ---
if [ ! -f appimagetool ]; then
    echo "⬇️  Téléchargement de appimagetool..."
    wget -q "https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-${ARCH}.AppImage" -O appimagetool
    chmod +x appimagetool
fi

# --- Construire l'AppImage ---
echo "🏗️  Construction de l'AppImage..."
ARCH=${ARCH} ./appimagetool AppDir "${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"

echo ""
echo "✅ AppImage créé avec succès !"
echo "   → ./${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"
echo ""
echo "Pour lancer le jeu :"
echo "   chmod +x ${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"
echo "   ./${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"
