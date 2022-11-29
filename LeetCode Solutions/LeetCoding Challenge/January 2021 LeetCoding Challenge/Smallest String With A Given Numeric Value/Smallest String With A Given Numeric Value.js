/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function(n, k) {
    k -= n
    let numericValue ='_bcdefghijklmnopqrstuvwxy_',
        lexicographicallySmallestString = 'z'.repeat(~~(k / 25))
    if (k % 25)
        lexicographicallySmallestString = numericValue[k % 25] + lexicographicallySmallestString
    return lexicographicallySmallestString.padStart(n, 'a')
};