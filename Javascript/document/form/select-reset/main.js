window.onload = function () {

        // 名前用のリスト
        var nameList = new Array(
                new Array('青葉', 'ひふみ'),
                new Array('ゆん', 'はじめ'),
                new Array('コウ', 'リン', 'アハゴン')
        );

        // 選択項目のリセット
        var initSelectBox = function () {
                var groupNum;
                // 選択したグループ番号を取得
                for (var i = 0; i < document.getElementById('group').options.length; i++) {
                        if (document.getElementById('group').options[i].selected) {
                                groupNum = i;
                        }
                }
                // 名前の選択項目を初期化
                for (var i = 0; i < document.getElementById('list').options.length; i++) {
                        document.getElementById('list').options[i] = null;
                }

                // グループに所属している名前を選択項目にセット
                for (var i = 0; i < nameList[groupNum].length; i++) {
                        document.getElementById('list').options[i] = new Option(nameList[groupNum][i]);
                }
                document.getElementById('list').options[0].selected = true;
        }

        // 選択したグループが変更されたら名前の選択項目をリセット
        document.getElementById('group').onchange = function () {
                initSelectBox();
        }

        // ページを読み込んだ時に選択項目をリセット
        initSelectBox();
}
