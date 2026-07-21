export {}

function isAlphanumeric(char: string): boolean{
    const code = RegExp('^[a-zA-Z0-9]$');
    return code.test(char);
}

function isPalindrome(str: string): boolean{
    const length = str.length;
    let l: number = 0;
    let r: number = length - 1;

    while ( l < r ){
        while ( l < r && !isAlphanumeric(str[l])) l ++;
        while ( l < r && !isAlphanumeric(str[r])) r --;
        if(str[l].toLowerCase() !== str[r].toLocaleLowerCase()){
            return false;
        }
        l ++;
        r --;
    }
    return true;
}

const string: string = "A man, a plan, a canal: Panama";
console.log(isPalindrome(string));