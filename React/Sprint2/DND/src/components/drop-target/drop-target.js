import React from "react";

export default function DropTarget(props) {
  const { puzzleElement, handleDrop, dropTargetIndex, handleDrag } = props;
  return (
    <li
      onDragOver={(e) => e.preventDefault()}
      {...(!puzzleElement.id && {
        onDrop: (e) => handleDrop(e, dropTargetIndex)
      })}
      className="listItem"
    >
      {puzzleElement.elementSrc && (
        <img
          src={`./${puzzleElement.elementSrc}`}
          onDrag={(e) => handleDrag(e, puzzleElement)}
          draggable
        />
      )}
    </li>
  );
}