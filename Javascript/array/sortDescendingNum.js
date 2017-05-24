function sortFunc(a, b){
	return b - a;
}

window.onload = function () {
    array = [2, 5, 3, 1, 4]
    array.sort(sortFunc);
    alert(array); // 5, 4, 3, 2, 1
}
