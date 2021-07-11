import React, { useState } from 'react';
import styles from './app.module.css';
import { Title } from '../../ui/title/title';
import { Cart } from '../cart';
import { TotalPrice } from '../common/total-price';

import { TotalPriceContext, DiscountContext } from '../../services/appContext';

function App() {
  const [totalPrice, setTotalPrice] = useState(0);
  const [discount, setDiscount] = useState(null);

  return (
    <div className={styles.app}>
      <TotalPriceContext.Provider value={{ totalPrice, setTotalPrice }}>
        <DiscountContext.Provider value={{ discount, setDiscount }}>
          <Title text={'Корзина'} />
          <Cart />
          <TotalPrice />
        </DiscountContext.Provider>
      </TotalPriceContext.Provider>
    </div>
  );
}

export default App;
