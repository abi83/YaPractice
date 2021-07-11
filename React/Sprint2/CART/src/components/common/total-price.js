import React, { useContext } from 'react';
import styles from './total-price.module.css';

import { DiscountContext, TotalPriceContext } from '../../services/appContext';

export const TotalPrice = ({ extraClass }) => {
  const { totalPrice } = useContext(TotalPriceContext);
  const { discountState } = useContext(DiscountContext);

  return (
    <div className={`${styles.container} ${extraClass}`}>
      <p className={styles.text}>Итого:</p>
      <p className={styles.cost}>
        {`${(totalPrice - totalPrice * (discountState.discount / 100)).toFixed(0)} руб.`}
      </p>
    </div>
  );
};
