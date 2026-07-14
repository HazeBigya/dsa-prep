export {};

function isAnagram(s:string, t:string): boolean{
    if(s.length !== t.length) return false;
    const count_s = new Map<string, number>();
    const count_t = new Map<string, number>();

    for (const char of s) {
        count_s.set(char, (count_s.get(char) || 0) + 1);
    }

    for (const char of t) {
        count_t.set(char, (count_t.get(char) || 0) + 1);
    }

    for(const char of count_s.keys()){
        if(count_s.get(char) !== count_t.get(char)){
            return false;
        }
    }
    return true;
}   

function isAnagramOptimized(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const count = new Map<string, number>();

    for (const char of s) {
        count.set(char, (count.get(char) || 0) + 1);
    }

    for (const char of t) {
        if (!count.has(char)) return false;
        count.set(char, count.get(char)! - 1);
        if (count.get(char) === 0) {
            count.delete(char);
        }
    }

    return count.size === 0;
}   

const s = "anagram";
const t = "nagaram";

console.log("The string S and T are anagrams: ", isAnagram(s, t));
console.log("The string S and T are anagrams (optimized): ", isAnagramOptimized(s, t));