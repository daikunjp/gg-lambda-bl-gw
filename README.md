# GreengrassでつくるBluetoothゲートウェイ

## アーキテクチャ


Raspberry PIでGreengrassからデプロイされたLambdaがローカルのBLEアダプタにアクセスしてBLEデバイスの情報を取得しAWS IoT Coreに連携する。

![](gg-lambda-bl-gw-arch.dio.svg)

## Raspberry PI のセットアップ

AWS CLIをインストールして自分のAWS環境にアクセスできるようにしておく。
