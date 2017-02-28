// 年齢算出（生年月日）
function calcAge(year, month, day) {
	var birthdate = year * 10000 + month * 100 + day;
	var today = new Date();
	var targetdate = today.getFullYear() * 10000 + (today.getMonth() + 1) * 100 + today.getDate();
	return (Math.floor((targetdate - birthdate) / 10000));
}

function main()
{
    // 生年月日を変数に格納
    var year = 1994; 
	var month = 4;
	var day = 16;
   // 生年月日から現在の年齢を計算
    age = calcAge(year, month, day)
    // 結果表示
    alert("現在年齢：" + age);
}
