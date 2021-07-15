import React from 'react';
import styles from './app.module.css';
import { Title } from '../../ui/title/title';
import { Cart } from '../cart';
import { TotalPrice } from '../common/total-price';
import { Recommend } from '../cart/recommend';

function App() {
  return (
    <div className={styles.app}>
      <Title text={'Корзина'} />
      <Cart />
      <TotalPrice />
      <Recommend extraClass={styles.recommend} />
    </div>
  );
}

export default App;
