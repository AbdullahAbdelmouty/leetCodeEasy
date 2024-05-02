// let twoSum =function (nums,target){
//     let result = []
//     //you must traverse on array and sum each element with the next one and equal it with target number.
//     nums.forEach((element,index,arr) => {
//         for(let i=index+1;i<arr.length;i++){
//             if((element+arr[i])==target){
//                 result.push(index);
//                 result.push(i)
//             }
//         }
//     });
//     return result
    
// }
// const nums = [1,2,3,4,5]
// const target = 6
// console.log(twoSum(nums,target));

// add two numbers
// const l1 = [2,4,3];
// const l2 = [5,6,4];

// const addTwoNumbers = (l1,l2)=>{
//     let reverseL1 = [];
//     let reverseL2 = [];
//     for(let index=0;index<l1.length;index++){
//         reverseL1[index] = l1[l1.length - index - 1];
//     }
//     reverseL1 = reverseL1.join("")
//     const result1 = parseInt(reverseL1,10);
//     for(let index=0;index<l2.length;index++){
//         reverseL2[index] = l2[l2.length - index - 1];
//     }
//     reverseL2 = reverseL2.join("")
//     const result2 = parseInt(reverseL2,10);
//     let result = result1 + result2;
//     result = String(result).split("").map(element=>{
//         return Number(element)
//     })
//     let lastResult = []
//     for(let index=0;index<result.length;index++){
//         lastResult[index] = result[result.length - index - 1];
//     }
//     console.log(typeof lastResult);
//     return lastResult
// }

//9. Palindrome Number
// let x = 11311;
// var isPalindrome = function(x) {
//     //first step convert number to array
//     //third step compare the first section of array with the secound section
//     let result = true
//     let arr = String(x).split("").map(element=>{
//         if(element==="-"){
//             return element
//         }else{
//             return Number(element)
//         }
//     })
//     for(let e=0;e<(arr.length -1)/2;e++ ){
//         if(arr[e]!=arr[arr.length - 1 -e]){
//             result = false
//         }
//     }
//     return result
// };
// 13.Roman to Integer
const input = "III"
var romanToInt = function(s) {
    // console.log(s);
    let arr = s.split("")
    
    console.log(arr);
};

romanToInt(input)