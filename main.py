from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def yumetype():
    return render_template('hello.html', qr_code_url='/static/qrcode.png')

@app.route('/terms-of-use')
def terms_of_use():
    return 'Terms of Use'

@app.route('/privacy-policy')
def privacy_policy():
    return '''
    プライバシーポリシー<br>
    ユーザーの入力に関する方針<br>
    ユメタイプは、ユーザーのプライバシーを深く尊重しています。当アプリは、ユーザーが入力するテキストやその他のデータを一切収集しません。これには、キーボードを通じて入力されるあらゆる情報が含まれます。<br>
    データ収集の不在<br>
    当アプリの使用中、ユーザーがキーボードを通じて入力する全ての情報は、完全にプライベートなものとして扱われ、当アプリまたは第三者によって収集、保存、または使用されることはありません。私たちは、ユーザーのプライバシーを保護するために、最大限の注意を払っており、入力データのプライバシーを確保することをお約束します。<br>
    プライバシー保護の保証<br>
    ユーザーのプライバシーとセキュリティは当社の最優先事項です。ユーザーが安心して当アプリを使用できるように、最高水準のプライバシー保護を実施しています。当アプリは、ユーザーの入力内容を監視、記録、または解析することは一切ありません。<br>
    連絡先<br>
    もしご不明な点やご質問がございましたら、以下の連絡先までお気軽にお問い合わせください。<br>
    info@tokyo.engineer<br><br>

    Privacy Policy<br>
    Policy on User Inputs<br>
    YumeType deeply respects user privacy. Our app does not collect any text or other data entered by users. This includes any information entered through the keyboard.<br>
    Absence of Data Collection<br>
    During the use of our app, all information entered by the user through the keyboard is treated as completely private and is not collected, saved, or used by our app or any third parties. We pay the utmost attention to protect user privacy and ensure the privacy of input data.<br>
    Guarantee of Privacy Protection<br>
    User privacy and security is our top priority. To ensure users can use our app with confidence, we implement the highest standard of privacy protection. Our app does not monitor, record, or analyze any user input.<br>
    Contact Information<br>
    If you have any questions or concerns, please feel free to contact us at:<br>
    info@tokyo.engineer
    '''

# The below lines are not used for production in App Engine
if __name__ == '__main__':
     app.run(host='127.0.0.1', port=8080, debug=True)
