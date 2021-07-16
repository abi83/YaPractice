import React from "react";

export default function DragList(props) {
  const { puzzleElement, handleDrag } = props;

  return (
    <li key={puzzleElement.id} className="listItem">
      {puzzleElement && (
        <img
          src={`./${puzzleElement.elementSrc}`}
          draggable
          onDrag={(e) => handleDrag(e, puzzleElement)}
        />
      )}
    </li>
  );
}
