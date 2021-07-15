import React from 'react';
import styles from './total-price.module.css';
import { useSelector } from 'react-redux';

export const TotalPrice = ({ extraClass }) => {
  const totalPrice = useSelector(store =>
    store.cart.items.reduce((acc, item) => acc + item.price * item.qty, 0)
  );
  const discount = useSelector(state => state.cart.promoDiscount);
  const price = discount ? totalPrice - totalPrice * (discount / 100) : totalPrice;
  return (
    <div className={`${styles.container} ${extraClass}`}>
      <p className={styles.text}>Итого:</p>
      <p className={styles.cost}>{`${price.toFixed(0)} руб.`}</p>
    </div>
  );
};
