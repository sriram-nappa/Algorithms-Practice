isUnique = (str) => {
    if(str.length < 0) {
        return false
    }
    let strSet = new Set([...str])
    if(strSet.size !== str.length) {
        return false
    }
    return true
}

console.log(isUnique("super"))

// Approach 2
// Use 128 bits boolean array if the string only contains lower case characters
