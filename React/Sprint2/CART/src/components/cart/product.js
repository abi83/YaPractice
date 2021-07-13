import React, { useContext, useMemo } from 'react';
import { AmountButton } from '../../ui/amount-button/amount-button';
import { DeleteButton } from '../../ui/delete-button/delete-button';
import styles from './product.module.css';

import { DiscountContext, TotalCostContext } from '../../services/appContext';
import { DataContext } from '../../services/productsContext';

export const Product = ({ src, id, text, qty, price }) => {
  const { totalPrice, setTotalPrice } = useContext(TotalCostContext);
  const { discount } = useContext(DiscountContext);
  const { data, setData } = useContext(DataContext);

  const discountedPrice = useMemo(() => ((price - price * (discount / 100)) * qty).toFixed(0), [
    discount,
    price,
    qty
  ]);

  const onDelete = () => {
    setData(data.filter(item => item.id !== id));
  };

  const decrease = () => {
    if (qty === 1) {
      onDelete();
    } else {
      setTotalPrice(totalPrice - price);
      const newData = data.map(item => {
        if (item.id === id) {
          item.qty -= 1;
          return item;
        }
        return item;
      });
      setData(newData);
    }
  };

  const increase = () => {
    setTotalPrice(totalPrice + price);
    const newData = data.map(item => {
      if (item.id === id) {
        item.qty += 1;
        return item;
      }
      return item;
    });
    setData(newData);
  };

  return (
    <div className={`${styles.product}`}>
      <img className={styles.img} src={src} alt="фото товара." />
      <p className={styles.text}>{text}</p>
      <div className={styles.amountbox}>
        <AmountButton onClick={decrease}>-</AmountButton>
        <p className={styles.amount}>{qty}</p>
        <AmountButton onClick={increase}>+</AmountButton>
      </div>
      <div className={styles.price}>
        <p className={`${styles.price} ${discount && styles.exPrice}`}>{price * qty} руб.</p>
        {discount && <p className={styles.price}>{discountedPrice} руб.</p>}
      </div>
      <DeleteButton onDelete={onDelete} />
    </div>
  );
};
