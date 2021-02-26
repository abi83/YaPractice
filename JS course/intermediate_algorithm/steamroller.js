/*
Flatten a nested array. You must account for varying levels of nesting.
steamrollArray([1, [], [3, [[4]]]]) should return [1, 3, 4].
steamrollArray([1, {}, [3, [[4]]]]) should return [1, {}, 3, 4].
 */

function steamrollArray(arr) {
  try {
    console.log('Удачная попытка - a[0]:', arr[0]);
    if (arr[0] === undefined) {
      console.log('Returning', arr, typeof(arr))
      return arr
    }
    else
      steamrollArray(arr[0])
  }
  catch (TypeError){
    console.log('Ошибка', arr);
    return arr
  }
}
console.log('answer: ',
  steamrollArray([[[1,1],2], [2], [3, [[4]]]])
);

