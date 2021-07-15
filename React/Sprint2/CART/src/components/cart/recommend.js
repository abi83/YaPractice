import React, { useMemo } from 'react';
import styles from './recommend.module.css';
import { Title } from '../../ui/title/title';
import { RecommendItem } from './recommend-item';
import { useSelector } from 'react-redux';
import { Loader } from '../../ui/loader/loader';

export const Recommend = ({ extraClass }) => {
  const { recommendedItems, recommendedItemsRequest } = useSelector(state => state.cart);

  const content = useMemo(
    () => (
        <Loader size="large" />
    ),
    [recommendedItemsRequest, recommendedItems]
  );

  return (
    <section className={`${styles.container} ${extraClass}`}>
      <Title
        text="Обычно с этим покупают"
        amount={(recommendedItems && recommendedItems.length) || ''}
      />
      <div className={styles.items}>{content}</div>
    </section>
  );
};
