## About

This script looks up Mazii dict on a Japanese word and generate an iOS Anki url scheme to create a simple Anki card for that word in this format:

Front:
```
{Japanese word}
```

Back:

```
{hiragana reading}

{Sino Vietnamese reading}

{Vietnamese meaning}

{example sentences with Vietnamese translations}
```

## Dependencies on iOS
- iOS AnkiMobile
- Pythonista

## Install env to run script in this project

Run following in terminal:

```
source myenv/bin/activate
pip install -r requirements.txt
```

## Examples

### Create url scheme from a word

To create a card for the word "勉強" in deck N1 in iOS Anki mobile app, run following in terminal:

```
python make_url_scheme_main.py 勉強 N1
```

The output will be

```
anki%3A//x-callback-url/addnote%3Fprofile%3DUser%25201%26type%3DBasic%26deck%3DN1%26fldFront%3D%E5%8B%89%E5%BC%B7%26fldBack%3D%E3%81%B9%E3%82%93%E3%81%8D%E3%82%87%E3%81%86%0A%0A%20%20%20%20%5BC%C6%AF%E1%BB%9CNG%2C%20C%C6%AF%E1%BB%A0NG%5D%0A%0A%20%20%20%20vi%E1%BB%87c%20h%E1%BB%8Dc%20h%C3%A0nh%3B%20s%E1%BB%B1%20h%E1%BB%8Dc%20h%C3%A0nh%0A%20%20%20%20%0A%20%20%20%20%E9%95%B7%E6%99%82%E9%96%93%E3%81%AE%E5%8B%89%E5%BC%B7%0AH%E1%BB%8Dc%20trong%20th%E1%BB%9Di%20gian%20d%C3%A0i%0A%0A%E6%9A%97%E8%A8%98%E3%81%A0%E3%81%91%E3%81%AE%E5%8B%89%E5%BC%B7%0ACh%E1%BB%89%20h%E1%BB%8Dc%20v%E1%BA%B9t
```

If user opens this url on an iPhone or iPad, a new card will be created in deck N1 inside iOS Anki mobile app.

#### Pythonista URL Scheme

This is an example Pythonista URL Scheme to run this script from Pythonista

```
pythonista3://icloud/iosAnkiCreateJaViCard/make_url_scheme_main?action=run&args=勉強%20N1
```

### Create url scheme from a mazii url

To create a card for the word "勉強" (found from this mazii dict url "https://mazii.net/vi-VN/search/word/javi/勉強") to deck N1 in iOS Anki mobile app, run following in terminal:

```
python main.py https://mazii.net/vi-VN/search/word/javi/勉強 N1
```

The output will be

```
anki%3A//x-callback-url/addnote%3Fprofile%3DUser%25201%26type%3DBasic%26deck%3DN1%26fldFront%3D%E5%8B%89%E5%BC%B7%26fldBack%3D%E3%81%B9%E3%82%93%E3%81%8D%E3%82%87%E3%81%86%0A%0A%20%20%20%20%5BC%C6%AF%E1%BB%9CNG%2C%20C%C6%AF%E1%BB%A0NG%5D%0A%0A%20%20%20%20vi%E1%BB%87c%20h%E1%BB%8Dc%20h%C3%A0nh%3B%20s%E1%BB%B1%20h%E1%BB%8Dc%20h%C3%A0nh%0A%20%20%20%20%0A%20%20%20%20%E9%95%B7%E6%99%82%E9%96%93%E3%81%AE%E5%8B%89%E5%BC%B7%0AH%E1%BB%8Dc%20trong%20th%E1%BB%9Di%20gian%20d%C3%A0i%0A%0A%E6%9A%97%E8%A8%98%E3%81%A0%E3%81%91%E3%81%AE%E5%8B%89%E5%BC%B7%0ACh%E1%BB%89%20h%E1%BB%8Dc%20v%E1%BA%B9t
```

If user opens this url on an iPhone or iPad, a new card will be created in deck N1 inside iOS Anki mobile app.

#### Pythonista URL Scheme

This is an example Pythonista URL Scheme to run this script from Pythonista

```
pythonista3://icloud/iosAnkiCreateJaViCard/main?action=run&args=勉強%20N1
```

## iOS Shortcuts Example
https://www.icloud.com/shortcuts/f55a3b3d2e0344a09509dc862188fc8c