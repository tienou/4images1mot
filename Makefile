.PHONY: run install uninstall appimage snap clean

# Lancer directement
run:
	python3 main.py

# Installation locale (nécessite sudo)
install:
	sudo bash install.sh

uninstall:
	sudo bash uninstall.sh

# Construire un AppImage
appimage:
	bash build-appimage.sh

# Construire un Snap
snap:
	snapcraft

# Nettoyage
clean:
	rm -rf AppDir build dist *.AppImage appimagetool __pycache__
	rm -rf parts prime stage snap/.snapcraft *.snap
