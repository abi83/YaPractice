import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { applyPromoCodeRequest, getItemsRequest } from '../../services/fakeApi';
import styles from './products-container.module.css';
import { Product } from './product';
import { Input } from '../../ui/input/input';
import { MainButton } from '../../ui/main-button/main-button';
import { PromoButton } from '../../ui/promo-button/promo-button';
import { Loader } from '../../ui/loader/loader';

import {applyPromo, getItems} from '../../services/actions/cart'

import { useDispatch, useSelector } from 'react-redux';

export const ProductsContainer = () => {
  const {items, promoCode, promoDiscount, promoRequest, promoFailed, itemsRequest} = useSelector(store => store);
  // const promoCode = useSelector(state => state.cart.promoCode);

  // const [itemsRequest, setItemsRequest] = useState(false);
  // const [promoFailed, setPromoFailed] = useState(false);
  // const [promoRequest, setPromoRequest] = useState(false);
  //
  const dispatch = useDispatch();
  const inputRef = useRef(null);
  useEffect(()=>{
    dispatch(getItems());
  }, [dispatch])
  
  const applyPromoCode = useCallback(() => {
    dispatch(applyPromo(inputRef.current.value));
  }, [inputRef])
  
  //
  // useEffect(() => {
  //   setItemsRequest(true);
  //   getItemsRequest()
  //     .then(res => {
  //       if (res && res.success) {
  //         setItemsRequest(false);
  //       }
  //     })
  //     .catch(err => {
  //       console.log(err);
  //       setItemsRequest(false);
  //     });
  // }, []);
  //
  // const applyPromoCode = useCallback(() => {
  //   const inputValue = inputRef.current.value;
  //   setPromoRequest(true);
  //   applyPromoCodeRequest(inputValue)
  //     .then(res => {
  //       if (res && res.success) {
  //         setPromoRequest(false);
  //         setPromoFailed(false);
  //       } else {
  //         setPromoFailed(true);
  //         setPromoRequest(false);
  //       }
  //     })
  //     .catch(err => {
  //       console.log(err);
  //       setPromoRequest(false);
  //     });
  // }, []);

  const content = useMemo(
    () => {
      return itemsRequest ? (
        <Loader size="large" />
      ) : (
        items.map((item, index) => {
          return <Product key={index} {...item} />;
        })
      );
    },
    [itemsRequest, items]
  );

  const promoCodeStatus = useMemo(
    () => {
      return promoFailed ? (
        <p className={styles.text}>Произошла ошибка! Проверьте корректность введенного промокода</p>
      ) : promoRequest ? (
        ''
      ) : promoCode ? (
        <p className={styles.text}>Промокод успешно применён!</p>
      ) : (
        ''
      );
    },
    [promoRequest, promoCode, promoFailed]
  );

  return (
    <div className={`${styles.container}`}>
      {content}
      <div className={styles.promo}>
        <div className={styles.inputWithBtn}>
          <Input
            type="text"
            placeholder="Введите промокод"
            extraClass={styles.input}
            inputWithBtn={true}
            inputRef={inputRef}
          />
          <MainButton
            type="button"
            extraClass={styles.promo_button}
            inputButton={true}
            onClick={applyPromoCode}
          >
            {promoRequest ? <Loader size="small" inverse={true} /> : 'Применить'}
          </MainButton>
        </div>
        {!promoCode && !promoDiscount && <PromoButton extraClass={styles.promocode}>{promoCode}</PromoButton>}
      </div>
      {promoCodeStatus}
    </div>
  );
};
