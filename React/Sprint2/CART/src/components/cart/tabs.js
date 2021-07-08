import React from 'react';
import styles from './tabs.module.css';
import { Tab } from './tab';

export const Tabs = () => {
  return (
    <div className={`${styles.tabs}`}>
      <Tab text="Товары в корзине" value="items" active />
    </div>
  );
};
