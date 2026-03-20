#!/bin/bash
# Désinstallation de 4 Images 1 Mot
set -e
echo "🗑️  Désinstallation de 4 Images 1 Mot..."
rm -rf /opt/4images1mot
rm -f /usr/local/bin/4images1mot
rm -f /usr/share/applications/4images1mot.desktop
rm -f /usr/share/icons/hicolor/scalable/apps/4images1mot.svg
update-desktop-database /usr/share/applications/ 2>/dev/null || true
echo "✅ Désinstallation terminée."
