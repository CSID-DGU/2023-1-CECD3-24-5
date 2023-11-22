import React from "react";
import '../styles/BinaryTree.css';


class TreeNode {
    constructor(value) { //js의 생성자 함수
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

//일반 이진 트리
function insertTree(root, value) {
    if (root === null) {
        return new TreeNode(value);
    }

    if (value < root.value) {
        root.left = insertTree(root.left, value);
    } else {
        root.right = insertTree(root.right, value);
    }

    return root;
}

//최소 힙 트리
function insertMinHeap(root, value) {
    if (root === null) {
        return new TreeNode(value);
    }

    if (value < root.value) {
        // 새 값이 현재 노드의 값보다 작으면, 현재 노드와 새 노드의 위치를 바꾸고
        // 원래 노드를 하위 트리에 재삽입합니다.
        let temp = root.value;
        root.value = value;
        insertMinHeap(root, temp);
    } else {
        // 새 노드가 현재 노드보다 크거나 같으면, 왼쪽 또는 오른쪽 자식으로 삽입합니다.
        // 먼저 왼쪽 자식이 비어 있는지 확인합니다.
        if (root.left === null) {
            root.left = new TreeNode(value);
        } else if (root.right === null) {
            root.right = new TreeNode(value);
        } else {
            // 두 자식이 모두 존재하는 경우, 재귀적으로 왼쪽 또는 오른쪽 서브트리에 삽입합니다.
            // 이는 트리가 균형 잡힌 상태를 유지하도록 도와줍니다.
            if (Math.random() < 0.5) {
                insertMinHeap(root.left, value);
            } else {
                insertMinHeap(root.right, value);
            }
        }
    }

    return root;
}


const TreeNodeComponent = ({node}) => {
    if (!node) {
        return <div className="emptyNode"></div>;
    }

    return (
        <div className="treeNode">
            <div className="nodeValue">{node.value}</div>
            <div className="children">
                {node.left && <div className="child">
                                    <TreeNodeComponent node={node.left} />
                                </div>}
                {node.right && <div className="child">
                                    <TreeNodeComponent node={node.right} />
                                </div>}
            </div>
        </div>
    );
};

function BinaryTree ({values}) {
    let root = null;
    values.forEach(value => {
        root = insertMinHeap(root, value);
     });

    return <TreeNodeComponent node={root} />;
}

export default BinaryTree;