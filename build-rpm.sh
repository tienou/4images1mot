#!/bin/bash
# ============================================================
# Build .rpm package pour Fedora/RHEL/openSUSE
# Usage: ./build-rpm.sh
# Prérequis: rpmbuild (rpm-build)
# ============================================================
set -e

APP_NAME="4images1mot"
VERSION="1.0.0"
RELEASE="1"

echo "📦 Construction du paquet .rpm..."

# --- Préparer l'arborescence rpmbuild ---
TOPDIR="$(pwd)/rpmbuild"
rm -rf "${TOPDIR}"
mkdir -p "${TOPDIR}"/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# --- Créer l'archive source ---
SRCDIR="${APP_NAME}-${VERSION}"
mkdir -p "${SRCDIR}"
cp main.py puzzles.py icon.svg 4images1mot.desktop "${SRCDIR}/"
tar czf "${TOPDIR}/SOURCES/${APP_NAME}-${VERSION}.tar.gz" "${SRCDIR}"
rm -rf "${SRCDIR}"

# --- Fichier .spec ---
cat > "${TOPDIR}/SPECS/${APP_NAME}.spec" << EOF
Name:           ${APP_NAME}
Version:        ${VERSION}
Release:        ${RELEASE}%{?dist}
Summary:        4 Images 1 Mot - Jeu de devinettes
License:        MIT
URL:            https://github.com/tienou/4images1mot
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3 >= 3.8
Requires:       python3-tkinter

%description
Trouve le mot commun aux 4 images !
Un jeu de réflexion amusant inspiré du célèbre jeu mobile.
30 niveaux de difficulté croissante, système de score et indices.

%prep
%setup -q

%install
mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps

install -m 644 main.py %{buildroot}/opt/%{name}/
install -m 644 puzzles.py %{buildroot}/opt/%{name}/
install -m 644 icon.svg %{buildroot}/opt/%{name}/

# Lanceur
cat > %{buildroot}/%{_bindir}/%{name} << 'LAUNCHER'
#!/bin/bash
exec python3 /opt/4images1mot/main.py "\$@"
LAUNCHER
chmod 755 %{buildroot}/%{_bindir}/%{name}

# Desktop
install -m 644 %{name}.desktop %{buildroot}/%{_datadir}/applications/
install -m 644 icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
/opt/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%post
update-desktop-database %{_datadir}/applications/ 2>/dev/null || true
gtk-update-icon-cache %{_datadir}/icons/hicolor/ 2>/dev/null || true

%postun
update-desktop-database %{_datadir}/applications/ 2>/dev/null || true
gtk-update-icon-cache %{_datadir}/icons/hicolor/ 2>/dev/null || true

%changelog
* $(date "+%a %b %d %Y") tienou - ${VERSION}-${RELEASE}
- Version initiale
EOF

# --- Build ---
rpmbuild --define "_topdir ${TOPDIR}" -bb "${TOPDIR}/SPECS/${APP_NAME}.spec"

# --- Copier le résultat ---
find "${TOPDIR}/RPMS" -name "*.rpm" -exec cp {} . \;

echo ""
echo "✅ Paquet .rpm créé !"
ls -la *.rpm 2>/dev/null
echo ""
echo "Installation :"
echo "  sudo dnf install ./${APP_NAME}-${VERSION}-${RELEASE}*.rpm   # Fedora"
echo "  sudo zypper install ./${APP_NAME}-${VERSION}-${RELEASE}*.rpm # openSUSE"
echo ""
echo "Désinstallation :"
echo "  sudo dnf remove ${APP_NAME}"
