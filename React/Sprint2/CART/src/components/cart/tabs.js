import React from 'react';
import styles from './tabs.module.css';
import { Tab } from './tab';
import { useDispatch, useSelector } from 'react-redux';


export const Tabs = () => {
  const currentTab = useSelector(state => state.cart.currentTab)

  return (
    <div className={`${styles.tabs}`}>
      <Tab text="Товары в корзине" value="items" active={currentTab === 'items'} />
      <Tab text="Отложенные товары" active={currentTab === 'postponed'} />
    </div>
  );
};
