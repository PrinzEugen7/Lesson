function year2wareki(year)
{
    if (year > 1988) 
    {
        return "平成" + (year - 1988);
    }
    else if (year > 1925) 
    {
        return "昭和" + (year - 1925);
    }
    else if (year > 1911) 
    {
        return "大正" + (year - 1911);
    }
    else if (year > 1988)
    {
        return "明治" + (year - 1867);
    }
    else{}
}

function main()
{
    // 西暦
    var year = 1993;
    // 西暦を和暦に変換
    var wareki = year2wareki(year);
    // 結果表示
    alert("西暦" + year + "年→" + wareki + "年");
}
