import React from 'react';
import { Tabs } from './tabs';
import { ProductsContainer } from './products-container';

export const Cart = ({totalPrice, discount, setTotalPrice, setDiscount}) => {
  return (
    <section>
      <Tabs />
      <ProductsContainer totalPrice={totalPrice} discount={discount} setTotalPrice={setTotalPrice} setDiscount={setDiscount}/>
    </section>
  );
};
