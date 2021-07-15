import React, { useMemo } from 'react';
import { AmountButton } from '../../ui/amount-button/amount-button';
import { DeleteButton } from '../../ui/delete-button/delete-button';
import styles from './product.module.css';
import { useDispatch, useSelector } from 'react-redux';
import { DECREASE_ITEM, DELETE_ITEM, INCREASE_ITEM } from '../../services/actions/cart';

export const Product = ({ src, id, text, qty, price }) => {
  const dispatch = useDispatch();

  const discount = useSelector(store => store.cart.promoDiscount);

  const discountedPrice = useMemo(() => ((price - price * (discount / 100)) * qty).toFixed(0), [
    discount,
    price,
    qty
  ]);

  const onDelete = () => {
    dispatch({
      type: DELETE_ITEM,
      id
    });
  };

  const decrease = () => {
    if (qty === 1) {
      onDelete();
    } else {
      dispatch({
        type: DECREASE_ITEM,
        id
      });
    }
  };
  const increase = () => {
    dispatch({
      type: INCREASE_ITEM,
      id
    });
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
