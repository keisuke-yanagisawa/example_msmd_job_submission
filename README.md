## このコードで何ができるか
複数のタンパク質 × 複数のプローブ × 20 runs のMSMDを自動実行する

## このコードの前提

- TSUBAME3.0上で実行
- ディレクトリ：`$HOME/workspace/0010_invmsmd_alignment/20230719_inverseMSMD_xiap2`
- タンパク質リスト：2WEA, 2CYB, 1ZUA, 1YMS, 1WBI, 1W4P, 1TU6, 1TT1, 1JZF, 1H60, 1H4G, 1E0X, 1CXV, 1BK9, 1HEE
  - リストを変える場合は3種類のpythonファイルそれぞれについて書き換える必要あり
- プローブリスト：A17, E14, E15, E16, E17, E18, E19
  - リストを変える場合は3種類のpythonファイルそれぞれについて書き換える必要あり
- タンパク質データの存在位置： `$HOME/workspace/9998_share/msmd/protein/{PROTEIN}/{PROTEIN}.pdb`
  - 例： `$HOME/workspace/9998_share/msmd/protein/2WEA/2WEA.pdb`
  - ファイルの位置を変える場合は `config_files/template.yaml` を修正する
- プローブデータの存在位置：`$HOME/workspace/9998_share/msmd/probe/{PROBE}/{PROBE}.mol2` および `$HOME/workspace/9998_share/msmd/probe/{PROBE}/{PROBE}.pdb`
  - 例：`$HOME/workspace/9998_share/msmd/probe/A17/A17.mol2` および `$HOME/workspace/9998_share/msmd/probe/A17/A17.pdb`
  - ファイルの位置を変える場合は `config_files/template.yaml` を修正する
- `exprorer_msmd`のバージョン：`v1.1.5.4`

 
## このコードの実行手順

```
cd config_files
python config_file_generator.py

cd ../job_files
python job_file_generator.py
python job_submitter.py
```
