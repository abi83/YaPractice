import React from "react";

export default function DropTarget(props) {
  const { puzzleElement, handleDrop, dropTargetIndex } = props;
  return (
    <li
      onDragOver={(e) => e.preventDefault()}
      onDrop={(e) => handleDrop(e, dropTargetIndex)}
      className="listItem"
    >
      {puzzleElement.elementSrc && (
        <img
          src={`./${puzzleElement.elementSrc}`}
        />
      )}
    </li>
  );
}
