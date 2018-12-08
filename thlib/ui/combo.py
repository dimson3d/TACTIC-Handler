from PySide import QtCore
from PySide import QtGui 


class AdvComboBox(QtGui.QComboBox):
    def __init__(self, parent=None):
        super(AdvComboBox, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QtGui.QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer
        self.completer = QtGui.QCompleter(self)
        #Set the model that the QCompleter uses
        # - in PySide doing this as a separate step worked better
        self.completer.setModel(self.pFilterModel)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)

        self.setCompleter(self.completer)

        # connect signals

        def filter(text):
            print "Edited: ", text, "type: ", type(text)
            self.pFilterModel.setFilterFixedString(str(text))

        self.lineEdit().textEdited[unicode].connect(filter)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        print "activated"
        if text:
            print "text: ", text
            index = self.findText(str(text))
            print "index: ", index
            self.setCurrentIndex(index)


    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(AdvComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(AdvComboBox, self).setModelColumn(column)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    combo = AdvComboBox()

    names = ['bob', 'fred', 'bobby', 'frederick', 'charles', 'charlie', 'rob']

    # fill the standard model of the combobox
    combo.addItems(names)
    combo.setModelColumn(0)
    combo.resize(300, 40)
    combo.show()

    sys.exit(app.exec_())