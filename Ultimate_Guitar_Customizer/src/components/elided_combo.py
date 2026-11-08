from PySide6.QtWidgets import (
    QComboBox, QSizePolicy, QStyle, QStyleOptionComboBox, QStylePainter
)
from PySide6.QtCore import Qt


class ElidedComboBox(QComboBox):
    """ComboBox de largeur indépendante du contenu, texte tronqué avec « … »,
    texte complet en infobulle."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.setMinimumContentsLength(12)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # infobulle = valeur courante
        self.setToolTip(self.currentText())
        self.currentTextChanged.connect(self.setToolTip)

    def set_items(self, items):
        """Remplit le combo, avec une infobulle par entrée et un menu assez large."""
        self.clear()
        self.addItems(items)

        for i, text in enumerate(items):
            self.setItemData(i, text, Qt.ToolTipRole)

        # le menu déroulant s'élargit pour afficher les textes longs en entier
        widest = max((self.fontMetrics().horizontalAdvance(t) for t in items), default=0)
        self.view().setMinimumWidth(widest + 40)

        self.setToolTip(self.currentText())

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionComboBox()
        self.initStyleOption(option)

        # dessine le cadre et la flèche
        painter.drawComplexControl(QStyle.CC_ComboBox, option)

        # zone réellement disponible pour le texte
        text_rect = self.style().subControlRect(
            QStyle.CC_ComboBox, option, QStyle.SC_ComboBoxEditField, self
        )
        option.currentText = self.fontMetrics().elidedText(
            self.currentText(), Qt.ElideRight, text_rect.width() - 8
        )

        # dessine le texte tronqué
        painter.drawControl(QStyle.CE_ComboBoxLabel, option)