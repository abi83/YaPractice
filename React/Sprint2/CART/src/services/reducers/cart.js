import {
  DELETE_ITEM,
  CANCEL_PROMO,
  DECREASE_ITEM,
  INCREASE_ITEM,
  GET_ITEMS_FAILED,
  GET_ITEMS_REQUEST,
  GET_ITEMS_SUCCESS,
  GET_RECOMMENDED_ITEMS_REQUEST,
  GET_RECOMMENDED_ITEMS_FAILED,
  GET_RECOMMENDED_ITEMS_SUCCESS,
  APPLY_PROMO_FAILED,
  APPLY_PROMO_REQUEST,
  APPLY_PROMO_SUCCESS,
  TAB_SWITCH
} from '../actions/cart';
import { recommendedItems } from '../initialData';

const initialState = {
  items: [],
  itemsRequest: false,
  itemsFailed: false,

  recommendedItems: [],
  recommendedItemsRequest: false,
  recommendedItemsFailed: false,
  
  promoRequest: false,
  promoFailed: false,

  promoCode: 'PROMOCODE',
  promoDiscount: 50,

  currentTab: 'items'
};

export const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ITEMS_REQUEST: {
      return {
        ...state,
        itemsRequest: true
      };
    }
    case GET_ITEMS_SUCCESS: {
      return { ...state, itemsFailed: false, items: action.items, itemsRequest: false };
    }
    case GET_ITEMS_FAILED: {
      return { ...state, itemsFailed: true, itemsRequest: false };
    }
    case GET_RECOMMENDED_ITEMS_REQUEST: {
      return {
        ...state,
        recommendedItemsRequest: true
      };
    }
    case GET_RECOMMENDED_ITEMS_SUCCESS: {
      return { ...state, recommendedItemsFailed: false, recommendedItems: action.items, recommendedItemsRequest: false };
    }
    case GET_RECOMMENDED_ITEMS_FAILED: {
      return { ...state, recommendedItemsFailed: true, recommendedItemsRequest: false };
    }
    case APPLY_PROMO_REQUEST: {
      return {
        ...state,
        promoRequest: true
      };
    }
    case APPLY_PROMO_SUCCESS: {
      return { ...state, promoFailed: false, promoRequest: false, promoCode: action.value.code, promoDiscount: action.value.discount };
    }
    case APPLY_PROMO_FAILED: {
      return { ...state, promoFailed: true, promoRequest: false, promoDiscount: null, promoCode: '' };
    }
    
    
    case TAB_SWITCH: {
      return {
        ...state,
        currentTab: state.currentTab === 'items' ? 'postponed' : 'items'
      };
    }
    case INCREASE_ITEM: {
      return {
        ...state,
        items: [...state.items].map(item =>
          item.id === action.id ? { ...item, qty: ++item.qty } : item
        )
      };
    }
    case DECREASE_ITEM: {
      return {
        ...state,
        items: [...state.items].map(item =>
          item.id === action.id ? { ...item, qty: --item.qty } : item
        )
      };
    }
    case DELETE_ITEM: {
      return { ...state, items: [...state.items].filter(item => item.id !== action.id) };
    }
    case CANCEL_PROMO: {
      return {
        ...state,
        promoCode: '',
        promoDiscount: null
      };
    }
    default: {
      return state;
    }
  }
};
