import React from "react";

export default function DragList(props) {
  const { puzzleElement } = props;

  return (
    <li key={puzzleElement.id} className="listItem">
      {puzzleElement && (
        <img
          src={`./${puzzleElement.elementSrc}`}
        />
      )}
    </li>
  );
}
