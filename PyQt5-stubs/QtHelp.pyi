# The PEP 484 type hints stub file for the QtHelp module.
#
# Generated by SIP 5.2.0
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QCompressedHelpInfo(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QCompressedHelpInfo') -> None: ...

    @staticmethod
    def fromCompressedHelpFile(documentationFileName: str) -> 'QCompressedHelpInfo': ...
    def version(self) -> QtCore.QVersionNumber: ...
    def component(self) -> str: ...
    def namespaceName(self) -> str: ...
    def swap(self, other: 'QCompressedHelpInfo') -> None: ...


class QHelpContentItem(sip.simplewrapper):

    def childPosition(self, child: 'QHelpContentItem') -> int: ...
    def parent(self) -> 'QHelpContentItem': ...
    def row(self) -> int: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...
    def childCount(self) -> int: ...
    def child(self, row: int) -> 'QHelpContentItem': ...


class QHelpContentModel(QtCore.QAbstractItemModel):

    def contentsCreated(self) -> None: ...
    def contentsCreationStarted(self) -> None: ...
    def isCreatingContents(self) -> bool: ...
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...
    def contentItemAt(self, index: QtCore.QModelIndex) -> QHelpContentItem: ...
    def createContents(self, customFilterName: str) -> None: ...


class QHelpContentWidget(QtWidgets.QTreeView):

    def linkActivated(self, link: QtCore.QUrl) -> None: ...
    def indexOf(self, link: QtCore.QUrl) -> QtCore.QModelIndex: ...


class QHelpEngineCore(QtCore.QObject):

    def __init__(self, collectionFile: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def usesFilterEngine(self) -> bool: ...
    def setUsesFilterEngine(self, uses: bool) -> None: ...
    def filterEngine(self) -> 'QHelpFilterEngine': ...
    def readersAboutToBeInvalidated(self) -> None: ...
    def warning(self, msg: str) -> None: ...
    def currentFilterChanged(self, newFilter: str) -> None: ...
    def setupFinished(self) -> None: ...
    def setupStarted(self) -> None: ...
    def setAutoSaveFilter(self, save: bool) -> None: ...
    def autoSaveFilter(self) -> bool: ...
    def error(self) -> str: ...
    @staticmethod
    def metaData(documentationFileName: str, name: str) -> typing.Any: ...
    def setCustomValue(self, key: str, value: typing.Any) -> bool: ...
    def customValue(self, key: str, defaultValue: typing.Any = ...) -> typing.Any: ...
    def removeCustomValue(self, key: str) -> bool: ...
    def linksForKeyword(self, keyword: str) -> typing.Dict[str, QtCore.QUrl]: ...
    def linksForIdentifier(self, id: str) -> typing.Dict[str, QtCore.QUrl]: ...
    def fileData(self, url: QtCore.QUrl) -> QtCore.QByteArray: ...
    def findFile(self, url: QtCore.QUrl) -> QtCore.QUrl: ...
    @typing.overload
    def files(self, namespaceName: str, filterAttributes: typing.Iterable[str], extensionFilter: str = ...) -> typing.List[QtCore.QUrl]: ...
    @typing.overload
    def files(self, namespaceName: str, filterName: str, extensionFilter: str = ...) -> typing.List[QtCore.QUrl]: ...
    def filterAttributeSets(self, namespaceName: str) -> typing.List[typing.List[str]]: ...
    def registeredDocumentations(self) -> typing.List[str]: ...
    def setCurrentFilter(self, filterName: str) -> None: ...
    def currentFilter(self) -> str: ...
    @typing.overload
    def filterAttributes(self) -> typing.List[str]: ...
    @typing.overload
    def filterAttributes(self, filterName: str) -> typing.List[str]: ...
    def addCustomFilter(self, filterName: str, attributes: typing.Iterable[str]) -> bool: ...
    def removeCustomFilter(self, filterName: str) -> bool: ...
    def customFilters(self) -> typing.List[str]: ...
    def documentationFileName(self, namespaceName: str) -> str: ...
    def unregisterDocumentation(self, namespaceName: str) -> bool: ...
    def registerDocumentation(self, documentationFileName: str) -> bool: ...
    @staticmethod
    def namespaceName(documentationFileName: str) -> str: ...
    def copyCollectionFile(self, fileName: str) -> bool: ...
    def setCollectionFile(self, fileName: str) -> None: ...
    def collectionFile(self) -> str: ...
    def setupData(self) -> bool: ...


class QHelpEngine(QHelpEngineCore):

    def __init__(self, collectionFile: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def searchEngine(self) -> 'QHelpSearchEngine': ...
    def indexWidget(self) -> 'QHelpIndexWidget': ...
    def contentWidget(self) -> QHelpContentWidget: ...
    def indexModel(self) -> 'QHelpIndexModel': ...
    def contentModel(self) -> QHelpContentModel: ...


class QHelpFilterData(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QHelpFilterData') -> None: ...

    def versions(self) -> typing.List[QtCore.QVersionNumber]: ...
    def components(self) -> typing.List[str]: ...
    def setVersions(self, versions: typing.Iterable[QtCore.QVersionNumber]) -> None: ...
    def setComponents(self, components: typing.Iterable[str]) -> None: ...
    def swap(self, other: 'QHelpFilterData') -> None: ...


class QHelpFilterEngine(QtCore.QObject):

    def filterActivated(self, newFilter: str) -> None: ...
    def namespacesForFilter(self, filterName: str) -> typing.List[str]: ...
    def removeFilter(self, filterName: str) -> bool: ...
    def setFilterData(self, filterName: str, filterData: QHelpFilterData) -> bool: ...
    def filterData(self, filterName: str) -> QHelpFilterData: ...
    def availableComponents(self) -> typing.List[str]: ...
    def setActiveFilter(self, filterName: str) -> bool: ...
    def activeFilter(self) -> str: ...
    def filters(self) -> typing.List[str]: ...
    def namespaceToVersion(self) -> typing.Dict[str, QtCore.QVersionNumber]: ...
    def namespaceToComponent(self) -> typing.Dict[str, str]: ...


class QHelpIndexModel(QtCore.QStringListModel):

    def indexCreated(self) -> None: ...
    def indexCreationStarted(self) -> None: ...
    def isCreatingIndex(self) -> bool: ...
    def linksForKeyword(self, keyword: str) -> typing.Dict[str, QtCore.QUrl]: ...
    def filter(self, filter: str, wildcard: str = ...) -> QtCore.QModelIndex: ...
    def createIndex(self, customFilterName: str) -> None: ...


class QHelpIndexWidget(QtWidgets.QListView):

    def activateCurrentItem(self) -> None: ...
    def filterIndices(self, filter: str, wildcard: str = ...) -> None: ...
    def linksActivated(self, links: typing.Dict[str, QtCore.QUrl], keyword: str) -> None: ...
    def linkActivated(self, link: QtCore.QUrl, keyword: str) -> None: ...


class QHelpSearchQuery(sip.simplewrapper):

    class FieldName(int): ...
    DEFAULT = ... # type: 'QHelpSearchQuery.FieldName'
    FUZZY = ... # type: 'QHelpSearchQuery.FieldName'
    WITHOUT = ... # type: 'QHelpSearchQuery.FieldName'
    PHRASE = ... # type: 'QHelpSearchQuery.FieldName'
    ALL = ... # type: 'QHelpSearchQuery.FieldName'
    ATLEAST = ... # type: 'QHelpSearchQuery.FieldName'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, field: 'QHelpSearchQuery.FieldName', wordList: typing.Iterable[str]) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QHelpSearchQuery') -> None: ...


class QHelpSearchEngine(QtCore.QObject):

    def __init__(self, helpEngine: QHelpEngineCore, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def searchInput(self) -> str: ...
    def searchResults(self, start: int, end: int) -> typing.List['QHelpSearchResult']: ...
    def searchResultCount(self) -> int: ...
    def searchingFinished(self, hits: int) -> None: ...
    def searchingStarted(self) -> None: ...
    def indexingFinished(self) -> None: ...
    def indexingStarted(self) -> None: ...
    def cancelSearching(self) -> None: ...
    @typing.overload
    def search(self, queryList: typing.Iterable[QHelpSearchQuery]) -> None: ...
    @typing.overload
    def search(self, searchInput: str) -> None: ...
    def cancelIndexing(self) -> None: ...
    def reindexDocumentation(self) -> None: ...
    def hits(self, start: int, end: int) -> typing.List[typing.Tuple[str, str]]: ...
    def hitCount(self) -> int: ...
    def resultWidget(self) -> 'QHelpSearchResultWidget': ...
    def queryWidget(self) -> 'QHelpSearchQueryWidget': ...
    def query(self) -> typing.List[QHelpSearchQuery]: ...


class QHelpSearchResult(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QHelpSearchResult') -> None: ...
    @typing.overload
    def __init__(self, url: QtCore.QUrl, title: str, snippet: str) -> None: ...

    def snippet(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...


class QHelpSearchQueryWidget(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def setSearchInput(self, searchInput: str) -> None: ...
    def searchInput(self) -> str: ...
    def setCompactMode(self, on: bool) -> None: ...
    def isCompactMode(self) -> bool: ...
    def search(self) -> None: ...
    def collapseExtendedSearch(self) -> None: ...
    def expandExtendedSearch(self) -> None: ...
    def setQuery(self, queryList: typing.Iterable[QHelpSearchQuery]) -> None: ...
    def query(self) -> typing.List[QHelpSearchQuery]: ...


class QHelpSearchResultWidget(QtWidgets.QWidget):

    def requestShowLink(self, url: QtCore.QUrl) -> None: ...
    def linkAt(self, point: QtCore.QPoint) -> QtCore.QUrl: ...