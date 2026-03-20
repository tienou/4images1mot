.PHONY: run install uninstall deb rpm appimage flatpak snap all clean

# Lancer directement
run:
	python3 main.py

# Installation locale (nécessite sudo)
install:
	sudo bash install.sh

uninstall:
	sudo bash uninstall.sh

# --- Packages individuels ---

deb:
	bash build-deb.sh

rpm:
	bash build-rpm.sh

appimage:
	bash build-appimage.sh

flatpak:
	bash build-flatpak.sh

snap:
	snapcraft

# --- Tous les packages ---
all:
	bash build-all.sh

# Nettoyage
clean:
	rm -rf AppDir build dist *.AppImage appimagetool __pycache__
	rm -rf parts prime stage snap/.snapcraft *.snap
	rm -rf 4images1mot_*_all 4images1mot_*.deb
	rm -rf rpmbuild *.rpm
	rm -rf build-flatpak .flatpak-builder *.flatpak
