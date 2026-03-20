#!/bin/bash
# ============================================================
# Build Flatpak
# Usage: ./build-flatpak.sh
# Prérequis: flatpak, flatpak-builder
#   flatpak install flathub org.freedesktop.Platform//23.08
#   flatpak install flathub org.freedesktop.Sdk//23.08
# ============================================================
set -e

APP_ID="com.github.tienou.4images1mot"

echo "📦 Construction du Flatpak..."

# Nettoyage
rm -rf build-flatpak .flatpak-builder

# Build et install local
flatpak-builder --user --install --force-clean build-flatpak "${APP_ID}.yml"

echo ""
echo "✅ Flatpak installé !"
echo ""
echo "Lancer :"
echo "  flatpak run ${APP_ID}"
echo ""
echo "Exporter en .flatpak :"
echo "  flatpak build-bundle ~/.local/share/flatpak/repo ${APP_ID}.flatpak ${APP_ID}"
echo ""
echo "Désinstaller :"
echo "  flatpak uninstall ${APP_ID}"
