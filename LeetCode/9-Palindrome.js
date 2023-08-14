
let x = 123;
let y = 121;

isPalindrome(x);
isPalindrome(y);

function isPalindrome(x){
    //In case of STRING
    // name = name.toUpperCase();
    // nameArr = Array.from(name);
    // let reversedName = nameArr.reverse().toString().replaceAll(',',"");
    //
    // return name === reversedName;

    //In case of INTEGER
    let stringX = x.toString();
    let stringXReversed = Array.from(stringX).reverse().toString().replaceAll(',','');

    return (stringX === stringXReversed);
}