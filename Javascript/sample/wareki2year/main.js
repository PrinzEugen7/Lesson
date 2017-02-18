function wareki2year(nengo, wareki)
{
    if ((nengo == "平成") && (wareki > 0)) 
    {
        return (wareki+1988)+"年";
    }
    else if ((nengo == "昭和") && (wareki > 0) && (wareki <= 64)) 
    {
        return (wareki+1925)+"年";
    }
    else if ((nengo == "大正") && (wareki > 0) && (wareki <= 15)) 
    {
        return (wareki+1911)+"年";
    }
    else if ((nengo == "明治") && (wareki > 0) && (wareki <= 45))
    {
        return (wareki+1867)+"年";
    }
    else{}
}

function main()
{
    // 和暦
    var nengo = "平成";
    var num = 5;
    // 和暦を西暦に変換
    year = wareki2year(nengo, num);
    // 結果表示
    alert(nengo + num + "→西暦" + year);
}
