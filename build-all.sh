#!/bin/bash
# ============================================================
# Build tous les packages disponibles
# Usage: ./build-all.sh
# ============================================================
set -e

echo "=========================================="
echo "  4 Images 1 Mot - Build tous les packages"
echo "=========================================="
echo ""

BUILT=()
SKIPPED=()

# --- .deb ---
if command -v dpkg-deb &> /dev/null; then
    echo "📦 [1/4] Construction .deb..."
    bash build-deb.sh
    BUILT+=("deb")
    echo ""
else
    echo "⏭️  [1/4] dpkg-deb non trouvé, .deb ignoré"
    SKIPPED+=("deb (installer dpkg-dev)")
fi

# --- .rpm ---
if command -v rpmbuild &> /dev/null; then
    echo "📦 [2/4] Construction .rpm..."
    bash build-rpm.sh
    BUILT+=("rpm")
    echo ""
else
    echo "⏭️  [2/4] rpmbuild non trouvé, .rpm ignoré"
    SKIPPED+=("rpm (installer rpm-build)")
fi

# --- AppImage ---
echo "📦 [3/4] Construction AppImage..."
bash build-appimage.sh
BUILT+=("AppImage")
echo ""

# --- Flatpak ---
if command -v flatpak-builder &> /dev/null; then
    echo "📦 [4/4] Construction Flatpak..."
    bash build-flatpak.sh
    BUILT+=("Flatpak")
    echo ""
else
    echo "⏭️  [4/4] flatpak-builder non trouvé, Flatpak ignoré"
    SKIPPED+=("Flatpak (installer flatpak-builder)")
fi

# --- Résumé ---
echo ""
echo "=========================================="
echo "  Résumé"
echo "=========================================="
echo ""
if [ ${#BUILT[@]} -gt 0 ]; then
    echo "✅ Packages créés : ${BUILT[*]}"
fi
if [ ${#SKIPPED[@]} -gt 0 ]; then
    echo "⏭️  Packages ignorés : ${SKIPPED[*]}"
fi
echo ""
ls -lh *.deb *.rpm *.AppImage 2>/dev/null || true
