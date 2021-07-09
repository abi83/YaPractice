import React from 'react';
import { Tabs } from './tabs';
import { ProductsContainer } from './products-container';

export const Cart = ({ setTotalPrice, totalPrice, setDiscount, discount }) => {
  return (
    <section>
      <Tabs />
      <ProductsContainer
        setTotalPrice={setTotalPrice}
        totalPrice={totalPrice}
        setDiscount={setDiscount}
        discount={discount}
      />
    </section>
  );
};
