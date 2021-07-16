import React from 'react';
import styles from './tab.module.css';
import { useDispatch, useSelector } from 'react-redux';
import {
  ADD_ITEM,
  ADD_POSTPONED_ITEM,
  TAB_SWITCH,
  DELETE_ITEM,
  DELETE_POSTPONED_ITEM
} from '../../services/actions/cart';
import { useDrop } from 'react-dnd';

export const Tab = ({ text, tabName }) => {
  const dispatch = useDispatch();
  const currentTab = useSelector(state => state.cart.currentTab);

  const switchTab = () => {
    dispatch({ type: TAB_SWITCH });
  };

  const className = `${styles.tab} ${currentTab === tabName ? styles.tab_type_current : ''}`;
  return (
    <div className={className} onClick={switchTab}>
      {text}
    </div>
  );
};
