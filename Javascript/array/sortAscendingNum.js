function sortFunc(a, b){
	return a - b;
}

window.onload = function () {
    array = [2, 5, 3, 1, 4]
    array.sort(sortFunc);
    alert(array); // 1, 2, 3, 4, 5
}

