import React from 'react';
import styles from './tab.module.css';

export const Tab = ({ text, active, onClick: handleClick, value }) => {
  const onClick = React.useCallback(
    () => {
      if (typeof handleClick === 'function') {
        handleClick(value);
      }
    },
    [handleClick, value]
  );

  const className = `${styles.tab} ${active ? styles.tab_type_current : ''}`;
  return (
    <div className={`${className}`} onClick={onClick}>
      {text}
    </div>
  );
};
