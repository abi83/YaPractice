import React from 'react';
import { Tabs } from './tabs';
import { ProductsContainer } from './products-container';
import { Postponed } from './postponed';

export const Cart = () => {
  return (
    <section>
      <Tabs />
      <ProductsContainer />
    </section>
  );
};
