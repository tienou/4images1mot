#!/bin/bash
# ============================================================
# Build .deb package pour Debian/Ubuntu
# Usage: ./build-deb.sh
# Prérequis: dpkg-deb
# ============================================================
set -e

APP_NAME="4images1mot"
VERSION="1.0.0"
ARCH="all"  # Python = architecture indépendante
PKG_DIR="${APP_NAME}_${VERSION}_${ARCH}"

echo "📦 Construction du paquet .deb..."

# --- Nettoyage ---
rm -rf "${PKG_DIR}" "${PKG_DIR}.deb"

# --- Structure Debian ---
mkdir -p "${PKG_DIR}/DEBIAN"
mkdir -p "${PKG_DIR}/opt/${APP_NAME}"
mkdir -p "${PKG_DIR}/usr/local/bin"
mkdir -p "${PKG_DIR}/usr/share/applications"
mkdir -p "${PKG_DIR}/usr/share/icons/hicolor/scalable/apps"

# --- Fichier control ---
cat > "${PKG_DIR}/DEBIAN/control" << EOF
Package: ${APP_NAME}
Version: ${VERSION}
Section: games
Priority: optional
Architecture: ${ARCH}
Depends: python3 (>= 3.8), python3-tk
Maintainer: tienou <tienou@github.com>
Description: 4 Images 1 Mot - Jeu de devinettes
 Trouve le mot commun aux 4 images !
 Un jeu de réflexion amusant inspiré du célèbre jeu mobile.
 30 niveaux de difficulté croissante, système de score et indices.
Homepage: https://github.com/tienou/4images1mot
EOF

# --- Scripts post-install / post-remove ---
cat > "${PKG_DIR}/DEBIAN/postinst" << 'EOF'
#!/bin/bash
update-desktop-database /usr/share/applications/ 2>/dev/null || true
gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true
EOF
chmod 755 "${PKG_DIR}/DEBIAN/postinst"

cat > "${PKG_DIR}/DEBIAN/postrm" << 'EOF'
#!/bin/bash
update-desktop-database /usr/share/applications/ 2>/dev/null || true
gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true
EOF
chmod 755 "${PKG_DIR}/DEBIAN/postrm"

# --- Copier les fichiers ---
cp main.py "${PKG_DIR}/opt/${APP_NAME}/"
cp puzzles.py "${PKG_DIR}/opt/${APP_NAME}/"
cp puzzles_i18n.py "${PKG_DIR}/opt/${APP_NAME}/"
cp i18n.py "${PKG_DIR}/opt/${APP_NAME}/"
cp icon.svg "${PKG_DIR}/opt/${APP_NAME}/"

# --- Lanceur ---
cat > "${PKG_DIR}/usr/local/bin/${APP_NAME}" << 'EOF'
#!/bin/bash
exec python3 /opt/4images1mot/main.py "$@"
EOF
chmod 755 "${PKG_DIR}/usr/local/bin/${APP_NAME}"

# --- Desktop file ---
cat > "${PKG_DIR}/usr/share/applications/${APP_NAME}.desktop" << EOF
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

# --- Icône ---
cp icon.svg "${PKG_DIR}/usr/share/icons/hicolor/scalable/apps/${APP_NAME}.svg"

# --- Permissions ---
find "${PKG_DIR}/opt" -type f -name "*.py" -exec chmod 644 {} \;
find "${PKG_DIR}/opt" -type f -name "*.svg" -exec chmod 644 {} \;
chmod 755 "${PKG_DIR}/opt/${APP_NAME}"

# --- Build ---
dpkg-deb --build --root-owner-group "${PKG_DIR}"

echo ""
echo "✅ Paquet .deb créé : ${PKG_DIR}.deb"
echo ""
echo "Installation :"
echo "  sudo dpkg -i ${PKG_DIR}.deb"
echo "  sudo apt-get install -f   # résoudre les dépendances si besoin"
echo ""
echo "Désinstallation :"
echo "  sudo apt remove ${APP_NAME}"
