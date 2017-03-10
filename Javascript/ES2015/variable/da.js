function main() {
    // 分割代入1
    [x, y, z] = [1, 2]
    console.log(a) // 1
    console.log(b) // 2
	
    // 分割代入2
	[a, b, ...rest] = [1, 2, 3, 4, 5]
    console.log(a) // 1
    console.log(b) // 2
    console.log(rest) // [3, 4, 5]
	
    // 分割代入3
    ({a, b} = {a:1, b:2})
    console.log(a) // 1
    console.log(b) // 2
}
