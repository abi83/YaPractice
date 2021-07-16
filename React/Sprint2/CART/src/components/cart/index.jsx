import React from 'react';
import { Tabs } from './tabs';
import { ProductsContainer } from './products-container';
import { PostponedContainer } from './postponed-container';
import { useSelector } from 'react-redux';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { DndProvider } from 'react-dnd';

export const Cart = () => {
  const currentTab = useSelector(state => state.cart.currentTab);
  return (
    <section>
      <DndProvider backend={HTML5Backend}>
        <Tabs />
        {currentTab === 'items' ? <ProductsContainer /> : <PostponedContainer />}
      </DndProvider>
    </section>
  );
};
