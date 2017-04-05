// ワークブックの読み込み
var wb = new ClosedXML.Excel.XLWorkbook(@"test.xlsx");

// シートを1つずつ取り出して処理
foreach (var ws in wb.Worksheets)
{
    // ワークシート名の表示
    Console.WriteLine(ws.Name);
    
    // シートのセル毎に処理
    foreach (var cell in ws.CellsUsed())
    {
        // セルにアドレス，値，数式があれば表示
        Console.WriteLine("{0} : {1} : {2}", cell.Address, cell.Value, cell.FormulaA1);
    }
}
