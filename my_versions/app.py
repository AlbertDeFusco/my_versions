import sys
from PyQt4 import QtGui

import osgeo.gdal
import pandas
import numpy
import matplotlib
import sys

def get_versions():
    versions = {}
    versions['gdal'] = osgeo.gdal.__version__
    versions['pandas'] = pandas.__version__
    versions['numpy'] = numpy.__version__
    versions['matplotlib'] = matplotlib.__version__
    versions['python'] = sys.version.split()[0]

    return '\n'.join('{} version {}'.format(k,v) for k,v in versions.items())

def window(versions):
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hi, there!\n"+versions)
    w.setGeometry(100,100,200,100)
    b.move(50,20)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())

def main():
    window(get_versions())

if __name__ == '__main__':
    main()
