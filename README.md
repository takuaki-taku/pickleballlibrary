# django_ecsite

# ピックルボールパドルライブラリ

このプロジェクトは、ピックルボールパドルをオンラインで販売するためのシンプルなECサイトです。Djangoフレームワークを使用して構築されており、ユーザーは商品の閲覧、検索、購入を行うことができます。

## ER図

以下は、データベースのER図です。

![ER Diagram](static/images/ER_Diagram.png)

## 機能

*   **商品一覧:** カテゴリごとに商品を一覧表示します。
*   **商品詳細:** 各商品の詳細情報（画像、価格、説明）を表示します。
*   **カート機能:** ログインユーザーは、商品を購入カートに追加できます。
*   **検索機能:** カテゴリで商品を絞り込んで検索できます。
*   **ユーザー認証:** ユーザー登録、ログイン、ログアウト機能を提供します。
*   **管理サイト:** Django管理サイトから、商品の追加、編集、削除が可能です。

## 技術スタック

*   **Python:** 3.8.18
*   **Django:** 4.2.19
*   **SQLite:** データベース
*   **HTML:** テンプレート
*   **CSS:** Bootstrap 5 (スタイル)
*   **JavaScript:** (必要に応じて)

## 開発環境の構築

1.  **リポジトリのクローン:**
    ```bash
    git clone https://github.com/takuaki-taku/pickleballlibrary.git
    cd mysite
    ```

2.  **仮想環境の作成:**
    ```bash
    python -m venv .venv
    ```

3.  **仮想環境のアクティベート:**
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows:**
        ```bash
        .venv\Scripts\activate
        ```

4.  **依存関係のインストール:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **マイグレーションの実行:**
    ```bash
    python manage.py migrate
    ```

6.  **スーパーユーザーの作成:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **開発サーバーの起動:**
    ```bash
    python manage.py runserver
    ```

8.  **ブラウザでアクセス:**
    *   `http://127.0.0.1:8000/` にアクセスして、サイトを表示します。
    *   `http://127.0.0.1:8000/admin/` にアクセスして、管理サイトを表示します。

## ファイル構成
mysite/
├── core/
│ ├── migrations/
│ ├── models.py
│ ├── admin.py
│ ├── forms.py
│ ├── views.py
│ └── urls.py
├── accounts/
│ ├── migrations/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ └── urls.py
├── static/
│ └── css/
│ └── style.css
├── templates/
│ ├── core/
│ │ ├── home.html
│ │ ├── item.html
│ │ └── ...
│ ├── accounts/
│ │ └── ...
│ ├── header.html
│ └── base.html
├── mysite/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt


*   `core/`: 商品、カテゴリなどのコア機能に関するファイル
*   `accounts/`: ユーザー認証に関するファイル
*   `static/`: CSSなどの静的ファイル
*   `templates/`: HTMLテンプレートファイル
*   `mysite/`: プロジェクトの設定ファイル
*   `db.sqlite3`: データベースファイル
*   `manage.py`: Djangoの管理コマンドを実行するためのファイル
*   `requirements.txt`: プロジェクトの依存関係を記述したファイル

## カスタマイズ

*   `mysite/settings.py`: データベース設定、静的ファイル設定などを変更できます。
*   `core/models.py`: 商品モデル、カテゴリモデルなどを変更できます。
*   `templates/`: HTMLテンプレートを編集して、サイトのデザインを変更できます。
*   `static/css/style.css`: CSSを編集して、サイトのスタイルを変更できます。

## 今後の開発

*   カート機能の完成
*   決済機能の追加
*   ユーザープロフィールの作成
*   検索機能の改善
*   レスポンシブデザインの改善

## ライセンス

このプロジェクトは、MITライセンスの下で公開されています。

## 貢献

バグ報告や機能追加の提案など、貢献を歓迎します。