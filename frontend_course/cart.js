var discountApplied = false;

function getDomNodesBySelector(selector) {
  return Array.from(document.querySelectorAll(selector));
}

function applyDiscount() {
  let prices = getDomNodesBySelector('.price-value');
  let total = getDomNodesBySelector('.total-price-value');
//  console.log(prices);
  if (!discountApplied){
    total[0].innerText *= 0.85;
    prices.map(e => e.innerText *= 0.85)
    // total[0].innerText = prices
    //   .reduce((previousValue, currenItem) => previousValue + currenItem.innerText, 0)
    discountApplied = true;
  }
  //console.log(total);
}
// console.log(getDomNodesBySelector('.price-value'));
