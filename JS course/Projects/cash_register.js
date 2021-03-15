/*
Design a cash register drawer function checkCashRegister() that accepts purchase
price as the first argument (price), payment as the second argument (cash),
and cash-in-drawer (cid) as the third argument.

cid is a 2D array listing available currency.
The checkCashRegister() function should always return an object with a status
key and a change key.

Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less
than the change due, or if you cannot return the exact change.

Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for
the key change if it is equal to the change due.

Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins
and bills, sorted in highest to lowest order, as the value of the change key.
 */

function checkCashRegister(price, cash, cid) {
  let cidRate = {
    'PENNY'       : 0.01,
    'NICKEL'      : 0.05,
    'DIME'        : 0.10,
    'QUARTER'     : 0.25,
    'ONE'         : 1,
    'FIVE'        : 5,
    'TEN'         : 10,
    'TWENTY'      : 20,
    'ONE HUNDRED' : 100,
  }
 
  let cidObject = Array.from(cid
      .map((element) => {
        return {
          'name': element[0],
          'rate': cidRate[element[0]],
          'quantity': Math.round(element[1]/cidRate[element[0]]),
          'value': element[1]
        }
      })
      .sort((a,b) => b.rate - a.rate)
  )
  let changeRemains = parseFloat((cash - price).toFixed(2))
  let cidRemains = cidObject.reduce((acc,item)=>acc+item.value,0)
  // console.log('Start: cidRemains', cidRemains)
  // console.log('Start: changeRemains', changeRemains)
  let changeObj = Array.from(cidObject
    .map((element) => {
      let quantity = Math.min(Math.floor(changeRemains/element.rate), element.quantity)
      changeRemains = parseFloat((changeRemains - element.rate * quantity).toFixed(2))
      cidRemains = parseFloat((cidRemains - element.rate*quantity).toFixed(2))
      return {
        'name': element.name,
        'quantity': quantity,
        'value': parseFloat((quantity*cidRate[element.name]).toFixed(2)),
        'changeRemains': changeRemains
      }
    })
    .filter((element) => element.quantity)
  );
  // console.log('End: cidRemains', cidRemains)//.toFixed(2))
  // console.log('End: changeRemains', changeRemains)//.toFixed(2))
  if (changeRemains > 0) {
    return {status: "INSUFFICIENT_FUNDS", change: []}
  }
  let changeArr = [];
  for (let element of changeObj) {
      changeArr.push([element.name, element.value]);
  }
  if (cidRemains.toFixed(2) === '0.00'){
    return {status: "CLOSED", change: changeArr};
  }
  return {status: "OPEN", change: cid}
;
}
console.log(
  checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
);