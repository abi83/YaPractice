import React from 'react';
import { DeleteButton } from '../../ui/delete-button/delete-button';
import styles from './postponed.module.css';
import { useDispatch, useSelector } from 'react-redux';
import { DELETE_POSTPONED_ITEM } from '../../services/actions/cart';
import { priceFormat } from '../common/utils';
import { useDrag } from 'react-dnd';

export const Postponed = ({ src, id, text, qty, price }) => {
  const dispatch = useDispatch();
  const discount = useSelector(state => state.cart.promoDiscount);
  const discountedPrice = ((price - price * (discount / 100)) * qty).toFixed(0);
  const onDelete = () => {
    dispatch({
      type: DELETE_POSTPONED_ITEM,
      id
    });
  };

  const [{ opacity }, ref] = useDrag({
    type: 'postponed',
    item: { id },
    collect: monitor => ({
      opacity: monitor.isDragging() ? 0.5 : 1
    })
  });

  return (
    <div className={styles.postponed} style={{ opacity }}>
      <div ref={ref} className={styles.postponedBox}>
        <img className={styles.img} src={src} alt="фото товара." />
        <p className={styles.text}>{text}</p>
      </div>
      <div className={styles.price}>
        <p className={`${styles.price} ${discount && styles.exPrice}`}>
          {priceFormat(price * qty)}
        </p>
        {discount && <p className={styles.price}>{priceFormat(discountedPrice)}</p>}
      </div>
      <DeleteButton onDelete={onDelete} />
    </div>
  );
};
