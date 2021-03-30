import QtQuick 2.15
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtQml 2.15

Row {
    id: myRow
    width: 1000
    height: 500

    property var currentModelItem

    ListView {
        id: numberList
        focus: true
        height: 300
        width: 200


        Component {
            id: numberListDelegate
            Item {
                width: parent.width
                height: childrenRect.height
                Text {
                    text: model.display 
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: numberList.currentIndex = index
                }
            }
        }

        model: DelegateModel {
            id: numberListDelegateModel
            model: numberListModel
            delegate: numberListDelegate
        }

        onCurrentItemChanged: {
            currentModelItem = numberListDelegateModel.items.get(numberList.currentIndex).model
            console.log('Item changed')
            }

        highlight: Rectangle {
            color: "lightsteelblue"
        }

    }

    Button {
        text: "Přidat prvek"
        onClicked: numberListModel.add_num()

    }

    Button {
        text: "Odebrat prvek"
        onClicked: numberListModel.del_num()
    }


}
