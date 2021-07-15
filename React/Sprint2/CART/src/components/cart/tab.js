// import React from 'react';
import styles from './tab.module.css';
import { useDispatch, useSelector } from 'react-redux';
import {TAB_SWITCH} from '../../services/actions/cart'


export const Tab = ({ text, active, onClick: handleClick, value }) => {
  const dispatch = useDispatch();
  
  // const onClick = React.useCallback(
  //   () => {
  //     if (typeof handleClick === 'function') {
  //       handleClick(value);
  //     }
  //   },
  //   [handleClick, value]
  // );
  
  const switchTab = () => {
    dispatch({type: TAB_SWITCH })
  }

  const className = `${styles.tab} ${active ? styles.tab_type_current : ''}`;
  return (
    <div className={`${className}`} onClick={switchTab}>
      {text}
    </div>
  );
};
